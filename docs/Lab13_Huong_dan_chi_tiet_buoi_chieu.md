# Lab 13 · Hướng dẫn chi tiết buổi chiều

*Định giá agent và lập kế hoạch pilot (Gate 2a) · 14:00–18:00*

> Trong repo này, code và hai file CSV nằm trong `src/` (chạy lệnh trong `src/`); các file hồ sơ nộp trong `report/team/`. Cấu trúc nộp và deadline theo [SUBMISSION.md](../SUBMISSION.md), thay cho mục "Thư mục nộp" ở cuối tài liệu này.

Buổi chiều có 4 tiếng (14:00–18:00). Cuối buổi, mỗi nhóm nộp một bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN và bảo vệ nó trước hội đồng Gate 2a. Tài liệu này đi từng bước qua 5 nhiệm vụ A–E. Mỗi nhiệm vụ có cách làm, đoạn code mẫu, số để tự đối chiếu và lỗi hay gặp. Số đối chiếu được nhận nếu lệch không quá 2%.

## Tổng quan và chuẩn bị

**Bối cảnh.** LogiX-VN có 12 depot, 40 nhân viên CSKH và nhận 1.500 yêu cầu hoàn phí mỗi ngày. Trợ lý vừa chạy thử 2 tuần ở 6 depot. Nhóm nhận một mẫu 1.200 yêu cầu để trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot phải thiết kế thế nào. Toàn bộ dữ liệu là giả lập.

**File được phát**

| File | Nội dung |
|----|----|
| logix_runs.csv | 1.624 lần chạy: request_id, trace_id, attempt, tokens_in, tokens_out, tool_calls, status (ok/loi) |
| logix_requests.csv | 1.200 yêu cầu: depot, staff_id, loai, so_lan_chay, ket_qua, duoc_xem_lai, quyet_dinh_xem_lai, phut_xem_lai_simulated, phut_lam_lai_simulated, dong_trong_24h, mo_lai_trong_7_ngay |
| lab13_starter.py | Khung code có sẵn ba phép thử đáp án biết trước |

**Số liệu dùng chung (giả định của lab)**

| Khoản                  | Giá trị                          |
|----------------------------|--------------------------------------|
| Token đầu vào              | 26 đ / 1.000 token                   |
| Token đầu ra               | 130 đ / 1.000 token                  |
| Gọi tool                   | 15 đ / lần                           |
| Phút nhân viên             | 2.000 đ (đã gồm bảo hiểm, văn phòng) |
| Nhân viên tự làm 1 yêu cầu | 6 phút = 12.000 đ                    |
| Chi phí cố định của trợ lý | 40 triệu đ / tháng                   |

**Lịch và phân vai**

| Giờ | Việc                                     | Thời gian làm |
|---------|----------------------------------------------|-------------------|
| 14:00   | Chia nhóm 4 người, chạy thử lab13_starter.py | 10 phút           |
| 14:10   | A · Mô hình chi phí                          | 40 + 3 chữa       |
| 14:53   | B · Bảng độ nhạy                             | 25 + 2 chữa       |
| 15:35   | C · Bảng lỗi và cách khắc phục               | 30 + 3 chữa       |
| 16:08   | D · pilot_plan.yaml                          | 25 + 3 chữa       |
| 16:36   | E · Chỉ số, rủi ro, hồ sơ launch v0          | 20 + 4 chữa       |
| 17:00   | Duyệt chéo Gate 2a                           | 45 phút           |
| 17:45   | Đóng gói, nộp (hạn 18:00)                    | 15 phút           |

Vai trong nhóm: **người viết code** (lab13.py), **người kiểm số** (tính tay một con số để đối chiếu), **người gắn nhãn 1**, **người gắn nhãn 2 kiêm giữ hồ sơ** (điền trang hồ sơ ngay từ đầu buổi). Sau giải lao, đổi người viết code.

**Cài môi trường và đọc dữ liệu đúng cách**

```bash
python3 -m venv .venv
./.venv/bin/pip install pandas numpy scipy statsmodels pyyaml
./.venv/bin/python -c "import pandas, statsmodels; print('san sang')"
```

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Bắt buộc có `keep_default_na=False`. Thiếu nó, ô trống trong cột quyet_dinh_xem_lai bị đọc thành NaN và các phép so sánh phía sau sai.

**Năm quy tắc của lab**

1.  Qua đủ ba phép thử A1 (1,20 · 1,25 · 1,25) rồi mới làm tiếp.
2.  Mọi con số tính từ hai cột `_simulated` phải ghi nhãn **simulated**.
3.  Đối chiếu ngay khi slide chữa hiện lên; nhiệm vụ sau dùng lại số của nhiệm vụ trước.
4.  Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.
5.  Không dùng từ “production”: Gate 2a chỉ duyệt kế hoạch pilot.

## Nhiệm vụ A · Mô hình chi phí mỗi việc thành công (40 phút)

Chi phí thật cho mỗi yêu cầu được giải quyết là khoảng **4.472 đ** [simulated], gấp **16,3 lần** con số “hoá đơn token chia số yêu cầu”. Quy tắc cốt lõi: **tử số tính mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm yêu cầu có ket_qua là thanh_cong.**

``` math
\text{Chi phí mỗi việc thành công} = \frac{\text{token} + \text{tool} + \text{xem lại} + \text{làm lại}}{\text{số việc thành công}}
```

### A1 · Ba phép thử đáp án biết trước (10 phút)

Mỗi lần chạy đúng với xác suất p, tối đa k lần. Viết ba hàm trong lab13_starter.py:

``` math
E\lbrack\text{số lần chạy}\rbrack = \frac{1 - (1 - p)^{k}}{p}\quad\quad P(\text{thành công}) = 1 - (1 - p)^{k}\quad\quad\text{hệ số chi phí} = \frac{E\lbrack\text{số lần chạy}\rbrack}{P(\text{thành công})}
```

```python
def so_lan_chay_ky_vong(p, k=None):
    return 1 / p if k is None else (1 - (1 - p) ** k) / p

def ti_le_thanh_cong(p, k=None):
    return 1.0 if k is None else 1 - (1 - p) ** k

def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)
```

| Phép thử (p = 0,8) | Đáp án |
|----|----|
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1/p, vì k triệt tiêu) |

Chưa đạt cả ba thì dừng lại sửa: mọi con số phía sau sẽ sai theo.

### A2 · Tính từ trace (20 phút)

Viết `mo_hinh(runs, reqs, ...)` nhận sẵn tham số giá và hệ số, để nhiệm vụ B chỉ cần gọi lại:

```python
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
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
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))
```

Số để tự đối chiếu:

| Khoản                            | Số tiền (đ) | Nhãn          |
|--------------------------------------|-----------------|-------------------|
| Token (mọi lần chạy)                 | 245.585         | đo từ trace       |
| Tool (5.600 lần gọi)                 | 84.000          | đo từ trace       |
| Trong đó, lần chạy thứ 2 và 3        | 93.804          | đo từ trace       |
| Xem lại (890 phút)                   | 1.780.000       | simulated         |
| Làm lại (1.132 phút)                 | 2.264.000       | simulated         |
| Tổng chi phí                         | 4.373.585       | có phần simulated |
| Số việc thành công                   | 978             |                   |
| Chi phí mỗi việc thành công          | 4.472           | simulated         |
| Hoá đơn token + tool chia số yêu cầu | 274,7           | đo từ trace       |

Trả lời hai câu: chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu. Khoản lớn nhất là **làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]. Giờ nhân viên chiếm 92,5% tổng chi phí. Nếu số của bạn chỉ gấp 1–2 lần hoá đơn, bạn đã quên giờ của nhân viên.

**Lưu ý khi so với 12.000 đ.** Con số 4.472 đ chỉ chia cho việc trợ lý làm xong. Nó **chưa tính** phần nhân viên làm thay 148 ca `chuyen_nhan_vien` (các ca này có 0 phút trong cột simulated). Nếu so với nhân viên tự làm, dùng chi phí cả hệ thống trên mỗi yêu cầu: (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49× của 12.000 đ** [simulated]. Đừng viết "rẻ bằng 0,37×" nếu chưa cộng phần chuyển nhân viên.

### A4 · Chi phí cố định (5 phút)

Đề cho chi phí cố định 40 triệu đ/tháng, nhưng A2 không có khoản này. Hãy cộng nó vào chi phí mỗi việc thành công trong phạm vi pilot (noi_dia + hang_nang):

1.  Tỉ lệ thành công trong phạm vi: 900 / 1.200 yêu cầu của mẫu → số việc thành công mỗi tháng ở quy mô đầy đủ = 45.000 × 900 / 1.200 = **33.750**.
2.  Chi phí cố định mỗi việc = 40.000.000 / 33.750 = **1.185 đ**.
3.  Chi phí mỗi việc thành công trong phạm vi = 3.072.513 / 900 = 3.414 đ → cộng cố định = **4.599 đ = 0,38×** [simulated].
4.  Khối lượng giảm một nửa (ví dụ giai đoạn pilot) thì cố định thành 2.370 đ/việc → 5.784 đ = 0,48×.

Ý nghĩa: chi phí cố định không đổi kết luận ở quy mô đầy đủ, nhưng tăng mạnh khi khối lượng nhỏ. Hồ sơ launch phải nói rõ con số đã cộng cố định hay chưa, và ở khối lượng nào.

### A3 · Tách theo loại yêu cầu (10 phút)

Gọi `mo_hinh(runs, reqs[reqs.loai == loai])` cho từng loại. Hàm đã lọc runs theo request_id nên không cần lọc tay.

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy / yêu cầu | Chi phí mỗi việc thành công [sim] | So với 12.000 đ |
|----|----|----|----|----|----|
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

Để trả lời “chạy lại có giúp không”, hãy tính thêm tỉ lệ ok theo từng lần thử: `runs.merge(reqs[['request_id','loai']]).pivot_table(index='loai', columns='attempt', values=..., aggfunc='mean')`. Với quoc_te, lần 1 đúng 30%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2%. Lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.

**Kết luận mẫu:** quoc_te không đáng để trợ lý xử lý (1,88×, thành công 27,3%), và chạy lại tới 3 lần không giúp. doi_tac sát ngưỡng (0,85×) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot.

**Lỗi hay gặp ở A:** chỉ cộng token của lần chạy thành công; chia cho 1.200 thay vì 978; quên chia 1.000 trước khi nhân giá token; đọc CSV thiếu `keep_default_na=False`.

## Nhiệm vụ B · Bảng độ nhạy (25 phút)

Yếu tố làm chi phí thay đổi mạnh nhất là **số ca làm lại**, không phải giá token. Pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại. Mỗi kịch bản là một lần gọi `mo_hinh` với một tham số đã đổi.

### B1 · Đổi từng yếu tố (12 phút)

```python
kich_ban = {
    'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':           dict(luong_phut=2500),
    'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
}
goc = mo_hinh(runs, reqs)['cps']
for ten, kw in kich_ban.items():
    cps = mo_hinh(runs, reqs, **kw)['cps']
    print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')
```

Hai dòng giới hạn chạy: bỏ các lần chạy có attempt lớn hơn giới hạn. Yêu cầu có so_lan_chay lớn hơn giới hạn coi là chuyen_nhan_vien, phút xem lại và làm lại bằng 0.

| Kịch bản | Chi phí mỗi việc thành công [sim] | Thay đổi |
|----|----|----|
| Gốc (A2) | 4.472 đ |  |
| Giá token gấp đôi | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản “giảm một nửa” phải làm chi phí giảm đúng bằng nửa mức tăng của kịch bản “gấp đôi” (5,6 → 2,8; 40,7 → 20,3).

### B2 · Đổi một cặp và xếp hạng (3 phút)

Giá token gấp đôi cùng lúc với xem lại gấp đôi: `mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)` cho **6.543 đ (+46,3%)**, đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính. Xếp hạng: **1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên.**

### B3 · Giới hạn chạy lại có thật sự rẻ hơn (5 phút)

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, vì nhân viên phải làm thay.

| Giới hạn | Tổng trợ lý [sim] | Không thành công | Cả hệ thống | Chi phí mỗi việc thành công |
|----|----|----|----|----|
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Giới hạn 2 lần rẻ nhất cho công ty, nhưng không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần). Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm 85 việc sang nhân viên.

### B4 · Nếu phải xem lại tất cả (5 phút)

Chỉ lấy noi_dia và hang_nang (982 yêu cầu). Các bước:

1.  Đếm yêu cầu có ít nhất một lần chạy status = ok: 948, mỗi yêu cầu xem lại 5 phút → 9.480.000 đ.
2.  Đếm ca lam_lai: 48, mỗi ca làm lại 9 phút → 864.000 đ.
3.  Cộng token + tool của mọi lần chạy thuộc 982 yêu cầu: 224.513 đ.
4.  Chia tổng 10.568.513 đ cho 900 việc thành công → **11.743 đ = 0,98× của 12.000 đ** [simulated].

**Độ nhạy theo phút làm lại.** Đề cho 9 phút/ca, nhưng cột `phut_lam_lai_simulated` trung bình **15,3 phút/ca** trên toàn bộ ca lam_lai (trung vị 14,5). Thay 9 bằng 15,3: 48 × 15,3 × 2.000 = 1.468.800 đ → tổng 11.173.313 đ → 11.173.313 / 900 = **12.414,79 đ**, hiển thị **12.415 đ = 1,03×** sau khi làm tròn đến đồng gần nhất [simulated]. Xem lại 100% vì vậy đắt hơn nhân viên tự làm. Mức hoà vốn: mỗi lần xem lại phải ≤ 5,1 phút (với 9 phút làm lại) hoặc ≤ 4,8 phút (với 15,3 phút). Ghi cả hai con số khi báo cáo B4.

Ý nghĩa: xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm 90% chi phí. Pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào, và mỗi lần xem lại có ngắn hơn 5 phút được không.

**Xong khi:** bảng B1 đủ 9 dòng, có xếp hạng ba yếu tố, B3 và B4 mỗi câu không quá ba dòng và có số.

## Nhiệm vụ C · Bảng lỗi và cách khắc phục (30 phút)

Gắn 20 ca lỗi vào năm loại của Google PAIR, đạt đồng thuận từ 80% (16/20 ca), rồi gán cách khắc phục cho mỗi loại. Quy tắc quan trọng nhất: **gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.**

| Loại | Nghĩa là | Câu hỏi để nhận ra |
|----|----|----|
| Do người dùng | Người dùng nhập sai hoặc chọn sai | Đầu vào của khách có sai không? |
| Hệ thống | Trợ lý làm sai so với thiết kế hoặc chính sách | Có vi phạm thiết kế/chính sách, và có người thấy? |
| Ngữ cảnh | Làm đúng thiết kế nhưng khách thấy sai | Kết quả đúng, chỉ giả định không khớp hoàn cảnh? |
| Giới hạn hệ thống | Không thể trả lời: thiếu dữ liệu, ngoài phạm vi, đầu vào không xử lý được | Có làm được không, dù có cố gắng? |
| Ngầm | Có sai nhưng cả khách lẫn hệ thống đều không nhận ra | Chỉ phát hiện qua kiểm tra mẫu? |

### Các bước

1.  **8 phút:** hai người gắn nhãn ngồi tách nhau, gắn độc lập cả 20 ca, không trao đổi. Hai người còn lại hoàn thiện B.
2.  **3 phút:** so nhãn, tỉ lệ đồng thuận = số ca trùng ÷ 20.
3.  **5 phút:** với ca không trùng, thống nhất nhãn và ghi một câu quy tắc phân biệt. Dưới 80% thì viết lại định nghĩa trước khi đi tiếp.
4.  **14 phút:** chọn 5 ca, mỗi loại một ca, điền bảng khắc phục.

### Nhãn tham khảo cho 20 ca

Hãy tự gắn trước rồi mới xem bảng này. Trong bài mẫu, hai người gắn độc lập trùng 20/20.

| Loại          | Các ca      | Số ca |
|-------------------|-----------------|-----------|
| Do người dùng     | 1, 6, 9, 14     | 4         |
| Hệ thống          | 2, 7, 8, 15, 20 | 5         |
| Ngữ cảnh          | 3, 10, 16, 18   | 4         |
| Giới hạn hệ thống | 4, 11, 13, 19   | 4         |
| Ngầm              | 5, 12, 17       | 3         |

### Quy tắc cho các ca dễ lẫn

- **Ca 6, 9 là do người dùng, không phải hệ thống:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã. Việc trợ lý không gợi ý là việc cần cải thiện, nằm ở cột khắc phục.
- **Ca 13 là giới hạn:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là hệ thống, không phải ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- **Ca 18 là ngữ cảnh:** số tiền đúng chính sách, chỉ giả định “khách hiểu cách tính” là không khớp.
- **Ca 12 là ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; “sai” có thể là sai về chi phí, không chỉ về câu trả lời.

### Bảng khắc phục mẫu (5 ca, mỗi loại một ca)

Mỗi dòng cần: cách phát hiện **đo được** (event, ngưỡng, tần suất) và **một vai trò** chịu trách nhiệm, không ghi “cả đội”.

| Ca | Loại | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
|----|----|----|----|----|
| 9 | Do người dùng | Event input_validation_failed; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” không có bản ghi sổ cái ok cùng trace_id; ngưỡng 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo “đang xử lý” và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn | Event handoff_to_staff với reason = thieu_du_lieu, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa quoc_te ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |

**Xong khi:** có hai bộ nhãn độc lập và tỉ lệ đồng thuận từ 80% (hoặc định nghĩa đã sửa), bảng 5 ca đủ năm loại.

## Nhiệm vụ D · pilot_plan.yaml (25 phút)

Với 40 nhân viên, **không cách chia theo cụm nào đủ mẫu để thấy mức chênh 5 điểm**. Hãy tính đủ năm câu D1 trước rồi mới chọn cách chia, và ghi rõ đánh đổi đã chấp nhận. Cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02.

### D1 · Cỡ mẫu theo ba cách chia (12 phút)

``` math
n = \frac{\left( z_{1 - \alpha/2}\sqrt{2\bar{p}(1 - \bar{p})} + z_{1 - \beta}\sqrt{p_{1}(1 - p_{1}) + p_{2}(1 - p_{2})} \right)^{2}}{(p_{2} - p_{1})^{2}}
```

``` math
DE = 1 + (m - 1)\, ICC\quad\quad n_{\text{hiệu dụng}} = \frac{c \cdot m}{DE} < \frac{c}{ICC}
```

```python
import math
from statistics import NormalDist

def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)
```

Dùng z chính xác (1,95996 và 0,84162) thì ra 1.251; z làm tròn 1,96 và 0,84 cho 1.250, vẫn trong sai số 2%.

| Câu | Cách tính | Kết quả |
|----|----|----|
| a · Chia theo yêu cầu | co_mau(0.70, 0.75) | **1.251** yêu cầu mỗi nhóm |
| b · Theo nhân viên, m = 75 | DE = 1 + 74 × 0,02 = 2,48; n = 1.251 × 2,48 | **3.103** mỗi nhóm → 42 người mỗi nhóm, tổng 84 > 40: **không đủ người** |
| c · 20 nhân viên mỗi nhóm | giới hạn c / ICC = 20 / 0,02 | tối đa **1.000** < 1.251: **không đạt** |
| d · 6 depot mỗi nhóm | 6 / 0,02 | tối đa **300** |
| e · Mức chênh 6 điểm (859/nhóm), 20 người mỗi nhóm | giải 20m / (1 + (m − 1) × 0,02) ≥ 859 | m ≥ **299** yêu cầu mỗi người (DE 6,96) |

Câu e giải tay: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 298,5 → **299**.

### Chọn cách chia: so sánh nhanh

| Cách chia | Đủ mẫu cho 5 điểm? | Tách được tác động? | Nhận xét |
|----|----|----|----|
| Theo yêu cầu | Có (1.251) | Kém: cùng một nhân viên vừa dùng vừa không dùng, tràn tác động cao | Dễ đủ mẫu nhưng kết quả khó tin |
| Theo nhân viên, 20 + 20 | Không (tối đa 1.000); đạt 6 điểm nếu m ≥ 299 | Tốt: 20 cụm mỗi nhóm, ngẫu nhiên | **Phương án bài mẫu chọn**, chấp nhận mức chênh 6 điểm |
| Theo depot, 6 + 6 | Không (tối đa 300) | Chỉ 6 cụm, dưới 20 | Loại, dù dễ triển khai |

Nếu chọn mức chênh 6 điểm mà tác động thật chỉ là 5 điểm, power chỉ còn khoảng 0,64 (statsmodels `NormalIndPower().power(...)` với n = 859). Phải nói rõ con số bất lợi này trong hồ sơ.

### D2 · Năm câu kiểm tra “tách được tác động” (5 phút)

1.  **Đối chứng chạy cùng thời gian?** Có: 20 nhân viên đối chứng làm cùng tuần, cùng depot.
2.  **Ngẫu nhiên hay người chọn?** Bốc thăm bằng code với seed ghi trước, phân tầng theo depot.
3.  **Ảnh hưởng gián tiếp?** Có rủi ro chia sẻ câu trả lời trong depot; giảm bằng quyền truy cập theo tài khoản và log lượt mở trợ lý theo staff_id.
4.  **Viết trước?** Có: chỉ số chính, ngưỡng, luật dừng và ngày quyết định chốt trước ngày bắt đầu.
5.  **Ít nhất 20 cụm mỗi nhóm?** Có, đúng 20.

### D3 · Viết file (8 phút)

Trước khi chốt luật an toàn, tính tỉ lệ mở lại hiện tại: `reqs.mo_lai_trong_7_ngay.mean()` = **4,25%** (51/1.200); trong phạm vi noi_dia + hang_nang là 3,97%. Đặt ngưỡng tuyệt đối 3% thì pilot bị dừng ngay tuần đầu. Nên so với nhóm đối chứng (chênh +2 điểm) kèm trần tuyệt đối 6%.

Mỗi luật dừng đủ bốn vế: **NẾU** [chỉ số vượt mức] – **TRONG** [bao lâu] – **THÌ** [việc cụ thể, ai làm] – **KHÔNG THÌ** [việc bị cấm].

```yaml
pilot:
  owner: "Giám đốc vận hành LogiX-VN"
  scope: "Chỉ noi_dia và hang_nang (0,22× và 0,69× so với 12.000 đ, simulated); loại quoc_te (1,88×) và doi_tac (0,85×)"
  assignment: {unit: "staff", control_share: 0.5, randomized: true}
  rollout: [0.10, 0.25, 0.50]   # 4 → 10 → 20 nhân viên; chỉ đo chỉ số chính từ bước 0.50
  primary_metric:
    name: dong_trong_24h_khong_mo_lai_7_ngay
    baseline: 0.70
    mde: 0.06                   # đánh đổi đã chấp nhận
    alpha: 0.05
    power: 0.80
    n_per_arm: 859
    design_effect: 6.96
    clusters_per_arm: 20
  stop_rules:
    - "NẾU mở lại 7 ngày của nhóm trợ lý cao hơn đối chứng ≥ 2 điểm hoặc vượt 6%, hoặc có ≥ 1 ca hoàn trùng TRONG 3 ngày liên tiếp THÌ Giám đốc vận hành tắt trợ lý trong 30 phút KHÔNG THÌ không được sang bước rollout tiếp"
    - "NẾU chi phí mỗi việc thành công > 8.000 đ TRONG 2 tuần liên tiếp THÌ PM thu hẹp về noi_dia và giới hạn 2 lần chạy KHÔNG THÌ không được mở hang_nang"
    - "NẾU tỉ lệ bỏ qua gợi ý > 40% TRONG 1 tuần THÌ Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày KHÔNG THÌ không được chuyển bước rollout"
  rollback: "Giám đốc vận hành bấm cờ tắt, hiệu lực 30 phút; khách được phục vụ bằng luồng nhân viên tự làm"
  decision_date: "2027-01-05"
```

Đây là bản rút gọn. File nộp cần đủ cả các trường identifiability, interim_looks và simulated_inputs, và không còn dấu hỏi nào. Kiểm tra file đọc được bằng `yaml.safe_load(open('pilot_plan.yaml'))`.

**Lỗi hay gặp ở D:** chia theo depot vì dễ triển khai; đặt ngưỡng dừng mà không nhìn tỉ lệ hiện tại; ghi owner là “cả đội”; luật dừng thiếu vế KHÔNG THÌ.

## Nhiệm vụ E · Chỉ số, rủi ro kinh tế, hồ sơ launch v0 (20 phút)

E ghép A–D thành một trang để hội đồng ra quyết định. Người giữ hồ sơ nên điền trang này dần từ đầu buổi, không đợi đến 16:36.

### E1 · Đặc tả chỉ số (8 phút)

```python
chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()
xem = reqs[reqs.duoc_xem_lai == 1]
bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()
an_toan = (reqs.mo_lai_trong_7_ngay == 1).mean()
```

| Loại | Chỉ số | Tính thử trên 1.200 yêu cầu |
|----|----|----|
| Chính | % đóng trong 24 giờ và không mở lại trong 7 ngày | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý (sua + bo) / số được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách: mở lại trong 7 ngày | 4,25% (51/1.200) |
| Dùng (tự đề xuất) | Ví dụ: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Không cần tính |
| An toàn (tự đề xuất) | Ví dụ: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Không cần tính |

Viết “chỉ số trong đợt chạy thử là 82,83%”, **không viết** “trợ lý đã nâng chỉ số từ 0,70”: đợt chạy thử không có nhóm đối chứng.

**Danh sách event (tối thiểu 6, mỗi event có trace_id).** Mẫu gồm 10 event:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
|----|----|----|----|
| refund_request_created | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi |
| agent_run_completed | Agent | attempt, tokens_in/out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | giu/sua/bo, phut_xem_lai (đo thật), trace_id | Khi bấm gửi/sửa/bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

Kiểm tra chéo: với mỗi chỉ số, chỉ ra event nào dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

### E2 · Rủi ro kinh tế (4 phút)

Lấy số trực tiếp từ bảng độ nhạy. Ít nhất hai dòng, ví dụ:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
|----|----|----|----|----|
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ [sim] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [sim] | % yêu cầu được xem lại còn > 50% cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa [sim] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |

### E3 · Hồ sơ launch v0 (8 phút)

Một trang, bảy mục, mỗi mục có: con số chính, trạng thái, người phụ trách (một vai trò).

1.  Chi phí mỗi việc thành công
2.  Ba yếu tố nhạy nhất
3.  So với nhân viên tự làm
4.  Chỉ số chính, chỉ số dùng, chỉ số an toàn
5.  Bảng lỗi và cách khắc phục
6.  Pilot plan
7.  Rủi ro kinh tế

Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột _simulated (mục 1, 2, 3, 7) ghi Giả lập.

Dòng cuối là đề xuất: **Go**, **Go có điều kiện** (mỗi điều kiện có người phụ trách và ngày kiểm tra) hoặc **No-go** (ghi việc phải làm để quay lại cổng). Bài mẫu chọn **Go có điều kiện** cho pilot noi_dia + hang_nang, với các điều kiện:

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 ở mức 5 điểm).
- Bật đủ event có trace_id; thay phút simulated bằng phút đo thật sau tuần 1.
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì không tiết kiệm (B4).

## Duyệt chéo Gate 2a và nộp bài

Nhóm số n chấm nhóm n + 1; nhóm cuối chấm nhóm 1. Hội đồng chấm theo bằng chứng, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

| Giờ | Việc |
|----|----|
| 17:00 (10 phút) | Hoàn thiện trang hồ sơ, gửi cho nhóm hội đồng |
| 17:10 (15 phút) | Đọc hồ sơ nhóm khác, chấm, viết quyết định kèm lý do và một câu hỏi |
| 17:25 (15 phút) | Mỗi cặp: đội trình 1 phút, hội đồng công bố 1 phút, đội trả lời 1 phút |
| 17:40 (5 phút) | Giảng viên chốt quyết định nào khớp bằng chứng |

**Thang chấm hội đồng (30 điểm)**

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm |
|----|----|----|----|
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý |
| Số giả lập và phạm vi | Không nhãn; phạm vi “mọi yêu cầu” | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng |

Câu hỏi gợi ý khi làm hội đồng: “Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%?” · “Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?” · “Với tỉ lệ mở lại 4,25% hiện tại, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?”

### Thư mục nộp (trước 18:00, tên lop_nhom, ví dụ L3A_nhom04)

| File | Nội dung | Nhiệm vụ |
|----|----|----|
| lab13.py | Code chạy từ đầu đến cuối, in ra các bảng | A, B, D1 |
| bang_chi_phi.md | Bảng A2, A3, độ nhạy, trả lời B3 và B4 | A, B |
| bang_loi.md | Hai bộ nhãn, tỉ lệ đồng thuận, bảng khắc phục 5 ca | C |
| pilot_plan.yaml | Kế hoạch pilot, không còn dấu hỏi | D |
| chi_so.md | Đặc tả chỉ số, danh sách event, rủi ro kinh tế | E |
| ho_so_launch_v0.md | Một trang, bảy mục, dòng cuối là đề xuất | E |
| phieu_cham.md | Phiếu nhóm bạn chấm nhóm khác | Duyệt chéo |

### Checklist trước khi nộp

- [ ] `python3 lab13.py` chạy hết trên một máy khác trong nhóm
- [ ] Ba phép thử A1 in ra ĐẠT
- [ ] Mọi con số từ cột _simulated có nhãn simulated
- [ ] pilot_plan.yaml đọc được bằng yaml.safe_load và không còn dấu hỏi
- [ ] Ít nhất ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò, không ghi “cả đội”
- [ ] Đề xuất là một trong ba: Go, Go có điều kiện, No-go
- [ ] Không có từ “production” trong bất kỳ file nào

### Cách chấm (70 điểm đối chiếu + 30 điểm hội đồng)

| Nhiệm vụ | Điểm | Điều kiện |
|----|----|----|
| A | 20 | Ba phép thử đạt; A2, A3 lệch không quá 2% |
| B | 15 | B1 lệch không quá 2%; xếp hạng đúng; B3, B4 có số |
| C | 10 | Đồng thuận từ 80%; khớp đáp án từ 16/20 ca |
| D | 15 | Năm câu D1 đúng; file đủ trường; ít nhất ba luật dừng đúng mẫu |
| E | 10 | Ba chỉ số tính thử đúng; sáu event có trace_id; hai dòng rủi ro; hồ sơ đủ bảy mục |

### Mười lỗi hay gặp

| Lỗi | Cách tránh |
|----|----|
| Lấy hoá đơn token chia số yêu cầu làm chi phí | Cộng tiền xem lại, làm lại; chia cho số việc thành công |
| Chỉ cộng token của lần chạy thành công | Lần chạy lỗi vẫn tốn tiền |
| Quên giá tính cho 1.000 token | Chia 1.000 trước khi nhân giá |
| Tin rằng chạy lại luôn giúp | Xem tỉ lệ ok theo lần thử và theo loại |
| Tối ưu chi phí mỗi việc thành công mà quên phần việc để lại cho nhân viên | Tính thêm chi phí cả hệ thống (B3) |
| Gắn nhãn lỗi sau khi đã bàn với nhau | Gắn độc lập trước, so sau |
| Ghi người phụ trách là “cả đội” | Ghi một vai trò có quyền quyết định |
| Chia pilot theo depot vì dễ triển khai | Tính cỡ mẫu hiệu dụng tối đa trước khi chọn |
| Đặt ngưỡng dừng mà không nhìn dữ liệu chạy thử | Tính tỉ lệ hiện tại của chỉ số an toàn trước |
| Viết trợ lý “đã nâng” chỉ số khi chưa có đối chứng | Chỉ nói “chỉ số trong đợt chạy thử là…” |

*Nguồn: đề bài Lab 13 và Hướng dẫn học viên Ngày 13. Số đối chiếu lấy từ bài làm mẫu (lab13.py) trên logix_runs.csv và logix_requests.csv, toàn bộ là dữ liệu giả lập.*
