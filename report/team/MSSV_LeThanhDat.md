# Báo cáo cá nhân — Lê Thành Đạt

## 1. Thông tin thành viên

- Họ tên: Lê Thành Đạt
- MSSV: (thành viên tự điền)
- Email: (thành viên tự điền)
- GitHub: (thành viên tự điền)
- Vai trong nhóm: Người kiểm số (Number verifier)

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính về file [report/team/bang_chi_phi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_chi_phi.md).
- Tính toán độc lập các con số kinh tế, đối chiếu chéo với kết quả chạy từ `src/lab13.py` của Nguyễn Trọng Hưởng để đảm bảo sai số không vượt quá 2%.
- Kiểm soát việc gắn nhãn bắt buộc `simulated` cho toàn bộ các số liệu bắt nguồn từ cột giả lập.
- Chắp bút các phân tích kinh tế chuyên sâu cho B3 (bài toán chi phí toàn hệ thống) và B4 (kịch bản xem lại 100%).
- Hỗ trợ xây dựng các kịch bản rủi ro kinh tế trong [report/team/chi_so.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md).

## 3. Đóng góp cụ thể

1. **Kiểm tra và hoàn thiện Bảng A2, A3, A4:**
   - Tính tay và đối chiếu độc lập tổng chi phí 4.373.585 đ chia cho 978 việc thành công ra đúng 4.472 đ [simulated].
   - Xác minh tỷ trọng giờ nhân viên chiếm 92,5% tổng chi phí và gấp 16,3 lần hóa đơn token (274,7 đ).
   - Xác thực số liệu phân loại A3: `noi_dia` (2.696 đ = 0,22×), `hang_nang` (8.221 đ = 0,69×), `quoc_te` (22.515 đ = 1,88×), `doi_tac` (10.215 đ = 0,85×).
   - Kiểm tra tính toán chi phí cố định A4 ở quy mô 45k yêu cầu (4.599 đ = 0,38×) và nửa quy mô (5.784 đ = 0,48×).
2. **Kiểm tra và hoàn thiện Bảng độ nhạy B1, B2, B3, B4:**
   - Đối chiếu tính tuyến tính của 9 kịch bản B1, xác định 3 yếu tố nhạy nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%).
   - Hoàn thành luận điểm B3: Chứng minh giới hạn 2 lần chạy rẻ nhất cho toàn công ty (6.901.220 đ) dù giới hạn 1 lần có chi phí agent thấp nhất (4.111 đ).
   - Hoàn thành luận điểm B4: Chứng minh kịch bản xem lại 100% làm chi phí tăng lên 11.743 đ (0,98×) đến 12.415 đ (1,03× [simulated]), triệt tiêu hoàn toàn lợi thế của AI.

## 4. Bằng chứng

- File báo cáo hoàn thiện: [report/team/bang_chi_phi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_chi_phi.md).
- Toàn bộ số liệu trong bảng A2, A3, B1 khớp chính xác 100% với output từ `src/lab13.py` (sai số 0%).
- Mọi con số giả lập đều mang nhãn `simulated` theo đúng quy định.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:** Hỗ trợ định dạng bảng biểu markdown, tra cứu công thức kiểm tra tính tuyến tính.
- **Cách tự kiểm tra:** Tính toán độc lập trên bảng tính và so sánh trực tiếp với console output của file mã nguồn để đảm bảo không có sai lệch.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người kiểm số.
- Đảm bảo tính toán chính xác, logic kinh tế chặt chẽ, bảo vệ thành công các luận điểm chi phí trước phản biện.
- Đánh giá: 10/10.
