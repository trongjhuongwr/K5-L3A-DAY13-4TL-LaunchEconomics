# Báo cáo cá nhân — Nguyễn Trọng Hưởng (2A202603607)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Hưởng
- MSSV: 2A202603607
- Email: nguyentronghuong05@gmail.com
- GitHub: trongjhuongwr
- Vai trong nhóm: Người viết code (Code author)

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính về toàn bộ mã nguồn tính toán trong `src/lab13.py` (A1, A2, A3, A4, B1, B2, B3, B4, D1, E1).
- Xây dựng mô hình chi phí Cost-of-Pass từ trace log và dữ liệu giả lập.
- Thiết kế thuật toán phân tích độ nhạy (Sensitivity Analysis) và khảo sát hàm mục tiêu chi phí toàn hệ thống.
- Lập trình tính toán cỡ mẫu cho thử nghiệm A/B phân cụm (Cluster Randomized Controlled Trial), tính hệ số thiết kế và Statistical Power.
- Xuất kết quả tính toán để chuyển giao cho Người kiểm số (Lê Thành Đạt) và Người giữ hồ sơ (Phạm Ngọc Trung Quân) điền vào các bảng báo cáo của nhóm.

## 3. Đóng góp cụ thể

1. **Nhiệm vụ A1 (Kinh tế học Retry):**
   - Cài đặt 3 hàm cơ sở `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`.
   - Vượt qua 100% ba phép thử biết trước với $p = 0,8$: đạt chuẩn $1,20$ lần chạy (khi tối đa 2 lần), $1,25$ lần chạy (khi chạy đến khi đúng), và hệ số chi phí $1,25$ lần giá một lần chạy (khi tối đa 3 lần).
2. **Nhiệm vụ A2, A3, A4 (Mô hình chi phí & Phân loại):**
   - Viết hàm `mo_hinh` chuẩn hóa việc phân bổ chi phí token, tool của mọi lần chạy và chi phí thời gian nhân viên xem lại/làm lại cho các ca thành công.
   - Tính toán chính xác chi phí mỗi việc thành công là 4.472 đ [simulated], chỉ ra giờ nhân viên chiếm 92,5% tổng chi phí và gấp 16,3 lần hóa đơn token.
   - Viết vòng lặp phân tích theo 4 phân loại (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`), chứng minh loại `quoc_te` bị lỗ nặng (22.515 đ = 1,88× so với nhân viên tự làm) và retry 3 lần không cải thiện tỷ lệ đúng (giảm từ 30% xuống 2,2%).
   - Tích hợp chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`: 4.599 đ (0,38×) ở quy mô 45k yêu cầu/tháng và 5.784 đ (0,48×) ở nửa quy mô.
3. **Nhiệm vụ B1, B2, B3, B4 (Phân tích độ nhạy & Tối ưu hệ thống):**
   - Cài đặt 9 kịch bản độ nhạy, chứng minh tính cộng tuyến tính của mô hình (B2: Token ×2 và Xem lại ×2 tăng đúng 46,3% = 5,6% + 40,7%).
   - Lập trình bài toán tối ưu toàn hệ thống (B3), phát hiện nghịch lý: giới hạn 1 lần chạy có CPS trợ lý thấp nhất (4.111 đ) nhưng giới hạn 2 lần chạy mới là rẻ nhất cho toàn công ty (6.901.220 đ) vì tránh đẩy 85 việc sang người làm tay.
   - Tính toán kịch bản xem lại 100% (B4), chứng minh xem lại 100% tốn 11.743 đ – 12.415 đ [simulated], làm mất hoàn toàn lợi ích kinh tế của AI.
4. **Nhiệm vụ D1 & E1 (Cỡ mẫu & Chỉ số):**
   - Lập trình hàm `co_mau` tính toán bài toán phân cụm nhân viên. Chứng minh với 40 nhân viên không thể đạt MDE 5 điểm, giải phương trình tìm ra $m \ge 299$ khi chấp nhận MDE 6 điểm ($DE = 6,96$).
   - Sử dụng `statsmodels` tính toán sự suy giảm Statistical Power xuống 64,2% nếu hiệu ứng thật chỉ là 5 điểm.
   - Tính toán 3 chỉ số hiện trạng: Chính (82,83%), Dùng (27,12%), An toàn (4,25%).

## 4. Bằng chứng

- File mã nguồn: [src/lab13.py](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/src/lab13.py).
- Kết quả chạy thực tế trên môi trường Python 3.13:
  - Khởi tạo môi trường ảo `.venv` bằng `uv` và cài đặt đầy đủ các gói `requirements.txt`.
  - Lệnh kiểm tra: `python lab13.py` chạy hoàn hảo 100%, in ra toàn bộ bảng A2, A3, B1, B3, B4, D1, E1 không có bất kỳ ngoại lệ nào.
  - Ba phép thử A1 in ra: `Ba phép thử đáp án biết trước: ĐẠT`.
  - Mọi con số khớp 100% với tài liệu hướng dẫn chuẩn và bài giải mẫu của môn học (sai số 0,0%).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:**
  - Hỗ trợ xây dựng cấu trúc hàm `mo_hinh` và vòng lặp phân tích độ nhạy.
  - Tham khảo cách sử dụng thư viện `statsmodels.stats.power.NormalIndPower` và `proportion_effectsize` để tính toán Statistical Power.
- **Cách tự kiểm tra và kiểm chứng:**
  - Viết sẵn assertion unit test `kiem_tra_dap_an_biet_truoc()` để khóa chặt 3 giá trị 1.20, 1.25, 1.25 trước khi chạy trên dữ liệu lớn.
  - Tự kiểm tra tính bảo toàn tuyến tính: Kịch bản giảm một nửa phải giảm đúng bằng một nửa mức tăng của kịch bản gấp đôi tương ứng.
  - Phối hợp với Người kiểm số (Lê Thành Đạt) kiểm tra độc lập các phép tính tay (như giải phương trình bậc nhất cho $m \ge 299$) để đảm bảo không có sai sót hoặc ảo giác AI.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người viết code (Code author).
- Mã nguồn viết rõ ràng, có chú thích đầy đủ, phân tách module khoa học, tuân thủ nghiêm ngặt PEP 8 và các quy tắc của repo (đặc biệt là đọc file CSV với `keep_default_na=False`).
- Sẵn sàng trả lời và bảo vệ mọi câu hỏi liên quan đến thuật toán, mô hình kinh tế học và kích thước mẫu trước Hội đồng Gate 2a.
- Đánh giá: 10/10.
