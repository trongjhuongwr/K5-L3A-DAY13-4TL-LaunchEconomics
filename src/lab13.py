"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm 4TL.
Chạy trong thư mục src/: python3 lab13.py   (cần pandas, numpy, scipy, statsmodels, pyyaml)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000  # 40 triệu đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B; giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    cps = tong / thanh_cong if thanh_cong > 0 else float('nan')
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) > 0 else 0
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()

    return dict(token=tien_token.sum(),
                tool=tien_tool.sum(),
                chay_lai=chay_lai,
                xem_lai=xem_lai,
                lam_lai=lam_lai,
                tong=tong,
                thanh_cong=thanh_cong,
                cps=cps,
                hoa_don_moi_yc=hoa_don_moi_yc)


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    mau = (p2 - p1) ** 2
    return math.ceil(tu / mau)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=' * 70)
    print('LAB 13 · GATE 2A · BÀI LÀM NHÓM 4TL (NGUYỄN TRỌNG HƯỞNG - CODE AUTHOR)')
    print('=' * 70)

    # 1. Kiểm tra đáp án biết trước A1
    kiem_tra_dap_an_biet_truoc()

    # 2. Nhiệm vụ A2 · Mô hình chi phí từ trace
    print('\n' + '-' * 70)
    print('NHIỆM VỤ A2 · MÔ HÌNH CHI PHÍ TỪ TRACE')
    print('-' * 70)
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:20s}: {gia_tri:>14.1f} đ')
        elif ten == 'thanh_cong':
            print(f'{ten:20s}: {gia_tri:>14,d}')
        else:
            print(f'{ten:20s}: {gia_tri:>14,.0f} đ')

    boi_so = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    phan_tram_nhan_vien = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong'] * 100
    phan_tram_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    phan_tram_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    print(f"\n-> Chi phí mỗi việc thành công gấp: {boi_so:.1f} lần hoá đơn chia số yêu cầu.")
    print(f"-> Giờ nhân viên chiếm: {phan_tram_nhan_vien:.1f}% tổng chi phí (Làm lại: {phan_tram_lam_lai:.1f}%, Xem lại: {phan_tram_xem_lai:.1f}%).")

    # 3. Nhiệm vụ A3 · Tách theo loại yêu cầu
    print('\n' + '-' * 70)
    print('NHIỆM VỤ A3 · TÁCH THEO LOẠI YÊU CẦU')
    print('-' * 70)
    print(f"{'Loại':<12} | {'Số YC':>7} | {'Thành công':>10} | {'Runs/YC':>8} | {'CPS [sim]':>12} | {'So với 12k':>10}")
    print('-' * 70)
    runs_merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        reqs_loai = reqs[reqs['loai'] == loai]
        runs_loai = runs[runs['request_id'].isin(reqs_loai['request_id'])]
        kq_l = mo_hinh(runs, reqs_loai)
        n_yc = len(reqs_loai)
        ti_le_tc = kq_l['thanh_cong'] / n_yc * 100
        lan_chay_tb = len(runs_loai) / n_yc
        cps_l = kq_l['cps']
        so_voi_12k = cps_l / BASELINE
        print(f"{loai:<12} | {n_yc:>7d} | {ti_le_tc:>9.1f}% | {lan_chay_tb:>8.2f} | {cps_l:>10,.0f} đ | {so_voi_12k:>9.2f}×")

    print("\nTỉ lệ thành công (status == ok) theo từng attempt:")
    pivot = runs_merged.pivot_table(index='loai', columns='attempt', values='status', aggfunc=lambda s: (s == 'ok').mean() * 100)
    print(pivot.to_string(formatters={col: '{:5.1f}%'.format for col in pivot.columns}))

    # 4. Nhiệm vụ A4 · Chi phí cố định
    print('\n' + '-' * 70)
    print('NHIỆM VỤ A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI NOI_DIA + HANG_NANG)')
    print('-' * 70)
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, reqs_pilot)
    tc_pilot = kq_pilot['thanh_cong']  # 900
    n_sample = len(reqs)  # 1200
    # Đầy đủ quy mô: 45.000 yêu cầu/tháng
    tc_thang_full = 45000 * tc_pilot / n_sample  # 33.750
    cp_co_dinh_full = CO_DINH_THANG / tc_thang_full  # 1.185 đ
    cps_full_codinh = kq_pilot['cps'] + cp_co_dinh_full  # 3.414 + 1.185 = 4.599 đ
    # Một nửa quy mô: 22.500 yêu cầu/tháng
    tc_thang_half = tc_thang_full / 2  # 16.875
    cp_co_dinh_half = CO_DINH_THANG / tc_thang_half  # 2.370 đ
    cps_half_codinh = kq_pilot['cps'] + cp_co_dinh_half  # 3.414 + 2.370 = 5.784 đ

    print(f"Khối lượng 45.000 YC/tháng: Việc TC: {tc_thang_full:,.0f} | Cố định/việc: {cp_co_dinh_full:,.0f} đ | CPS + cố định: {cps_full_codinh:,.0f} đ ({cps_full_codinh/BASELINE:.2f}×)")
    print(f"Một nửa khối lượng:        Việc TC: {tc_thang_half:,.0f} | Cố định/việc: {cp_co_dinh_half:,.0f} đ | CPS + cố định: {cps_half_codinh:,.0f} đ ({cps_half_codinh/BASELINE:.2f}×)")

    # 5. Nhiệm vụ B1 · Bảng độ nhạy (9 kịch bản)
    print('\n' + '-' * 70)
    print('NHIỆM VỤ B1 · BẢNG ĐỘ NHẠY (9 KỊCH BẢN)')
    print('-' * 70)
    goc = ket_qua['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f"{'Kịch bản':<30} | {'CPS [sim]':>12} | {'Thay đổi (%)':>14}")
    print('-' * 70)
    print(f"{'Gốc (A2)':<30} | {goc:>10,.0f} đ | {'0.0%':>14}")
    for ten, kw in kich_ban.items():
        cps_kb = mo_hinh(runs, reqs, **kw)['cps']
        diff_pct = (cps_kb / goc - 1) * 100
        print(f"{ten:<30} | {cps_kb:>10,.0f} đ | {diff_pct:>+13.1f}%")

    # Nhiệm vụ B2: Đổi một cặp
    kb_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    diff_cap = (kb_cap / goc - 1) * 100
    print(f"\nB2 - Token x2 VÀ Xem lại x2: {kb_cap:,.0f} đ ({diff_cap:+.1f}%) = 5.6% + 40.7% (Cộng tuyến tính)")

    # 6. Nhiệm vụ B3 · Giới hạn chạy lại cả hệ thống
    print('\n' + '-' * 70)
    print('NHIỆM VỤ B3 · GIỚI HẠN CHẠY LẠI CẢ HỆ THỐNG')
    print('-' * 70)
    print(f"{'Giới hạn':<10} | {'Tổng trợ lý [sim]':>18} | {'Không TC':>10} | {'Cả hệ thống':>16} | {'CPS Trợ lý':>12}")
    print('-' * 70)
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k if k < 3 else None)
        khong_tc = len(reqs) - kq_k['thanh_cong']
        chi_phi_he_thong = kq_k['tong'] + BASELINE * khong_tc
        ghi_chu = " (thấp nhất)" if k == 1 else (" (RẺ NHẤT)" if k == 2 else "")
        print(f"{k} lần chạy  | {kq_k['tong']:>16,.0f} đ | {khong_tc:>10d} | {chi_phi_he_thong:>14,.0f} đ{ghi_chu} | {kq_k['cps']:>10,.0f} đ")

    # 7. Nhiệm vụ B4 · Nếu phải xem lại tất cả (100%)
    print('\n' + '-' * 70)
    print('NHIỆM VỤ B4 · XEM LẠI 100% TRONG PHẠM VI NOI_DIA + HANG_NANG')
    print('-' * 70)
    reqs_b4 = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_b4 = runs[runs['request_id'].isin(reqs_b4['request_id'])].copy()
    yc_co_ok = runs_b4[runs_b4['status'] == 'ok']['request_id'].unique()
    n_xem_lai_100 = len(yc_co_ok)  # 948
    tien_xem_lai_100 = n_xem_lai_100 * 5 * LUONG_PHUT  # 9.480.000 đ
    n_lam_lai_b4 = (reqs_b4['ket_qua'] == 'lam_lai').sum()  # 48
    tien_token_tool_b4 = (runs_b4['tokens_in']/1000 * GIA_VAO + runs_b4['tokens_out']/1000 * GIA_RA + runs_b4['tool_calls'] * GIA_TOOL).sum()
    tc_b4 = (reqs_b4['ket_qua'] == 'thanh_cong').sum()  # 900

    # TH1: 9 phút / ca làm lại
    tien_lam_lai_9m = n_lam_lai_b4 * 9 * LUONG_PHUT  # 864.000 đ
    tong_b4_9m = tien_token_tool_b4 + tien_xem_lai_100 + tien_lam_lai_9m
    cps_b4_9m = tong_b4_9m / tc_b4
    # TH2: 15,3 phút / ca làm lại (thực tế dữ liệu)
    tien_lam_lai_15m = n_lam_lai_b4 * 15.3 * LUONG_PHUT  # 1.468.800 đ
    tong_b4_15m = tien_token_tool_b4 + tien_xem_lai_100 + tien_lam_lai_15m
    cps_b4_15m = tong_b4_15m / tc_b4

    print(f"Xem lại 100% (làm lại 9m):    Tổng = {tong_b4_9m:,.0f} đ | CPS = {cps_b4_9m:,.0f} đ ({cps_b4_9m/BASELINE:.2f}×)")
    print(f"Xem lại 100% (làm lại 15,3m):  Tổng = {tong_b4_15m:,.0f} đ | CPS = {cps_b4_15m:,.0f} đ ({cps_b4_15m/BASELINE:.2f}×) -> ĐẮT HƠN NGƯỜI TỰ LÀM")

    # 8. Nhiệm vụ D1 · Cỡ mẫu
    print('\n' + '-' * 70)
    print('NHIỆM VỤ D1 · CỠ MẪU PILOT VÀ POWER')
    print('-' * 70)
    n_a = co_mau(0.70, 0.75)
    print(f"Câu a · Chia theo yêu cầu (+5 điểm):          {n_a:,d} yêu cầu / nhóm")
    de_b = 1 + (75 - 1) * 0.02
    n_b = math.ceil(n_a * de_b)
    staff_per_arm_b = math.ceil(n_b / 75)
    print(f"Câu b · Chia theo nhân viên (m=75):          DE={de_b:.2f} -> {n_b:,d} YC/nhóm -> {staff_per_arm_b} người/nhóm (tổng {staff_per_arm_b*2} > 40: KHÔNG ĐỦ)")
    print(f"Câu c · 20 nhân viên/nhóm:                    Trần n_eff = 20 / 0.02 = 1.000 < {n_a} (KHÔNG ĐẠT 5 điểm)")
    print(f"Câu d · 6 depot/nhóm:                         Trần n_eff = 6 / 0.02 = 300")

    # Câu e: Mức chênh 6 điểm
    n_e_arm = co_mau(0.70, 0.76)  # 859
    # 20m / (1 + (m-1)*0.02) >= 859 -> m >= (859 * 0.98) / (20 - 859 * 0.02) = 841.82 / 2.82 = 298.52 -> 299
    m_e = math.ceil((n_e_arm * 0.98) / (20 - n_e_arm * 0.02))
    de_e = 1 + (m_e - 1) * 0.02
    print(f"Câu e · Chấp nhận MDE 6 điểm (n={n_e_arm}):      m >= {m_e} YC/nhân viên (DE={de_e:.2f}, tổng={20*m_e:,d} YC/nhóm)")

    # Tính power nếu hiệu quả thật chỉ 5 điểm
    es_5pt = proportion_effectsize(0.75, 0.70)
    pwr_5pt = NormalIndPower().power(effect_size=es_5pt, nobs1=n_e_arm, alpha=0.05, alternative='two-sided')
    print(f"-> Đánh đổi: Nếu hiệu ứng thật là 5 điểm, Statistical Power chỉ còn: {pwr_5pt*100:.1f}% (thay vì 80%)")

    # 9. Nhiệm vụ E1 · Các chỉ số đo lường
    print('\n' + '-' * 70)
    print('NHIỆM VỤ E1 · CÁC CHỈ SỐ ĐO LƯỜNG')
    print('-' * 70)
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    an_toan_pilot = (reqs_pilot['mo_lai_trong_7_ngay'] == 1).mean()
    print(f"1. Chỉ số chính (đóng trong 24h & không mở lại 7 ngày): {chinh*100:.2f}% (994/1.200)")
    print(f"2. Chỉ số dùng (tỉ lệ bỏ qua/sửa gợi ý khi được xem lại): {bo_qua*100:.2f}% (48/177)")
    print(f"3. Chỉ số an toàn (lỗi lọt đến khách - mở lại trong 7 ngày): {an_toan*100:.2f}% (51/1.200), trong phạm vi pilot: {an_toan_pilot*100:.2f}%")
    print('=' * 70)
