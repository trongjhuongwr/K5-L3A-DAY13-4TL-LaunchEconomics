# Báo cáo cá nhân — Lê Thành Đạt (2A202603579)

## 1. Thông tin thành viên

- Họ tên: Lê Thành Đạt
- MSSV: 2A202603579
- Email: dat.ltforwork@gmail.com; 26ai.datlt7@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (Number verifier)

## 2. Phần việc phụ trách

Đối chiếu output của `src/lab13.py` với công thức và số tham chiếu trong hướng dẫn; kiểm tra các phép tính chi phí, làm rõ cách so sánh chi phí của trợ lý với chi phí cả hệ thống, và ghi nhận cách làm tròn số B4.

## 3. Đóng góp cụ thể

- Đối chiếu A1: 1,20; 1,25; 1,25. Rà phép tính A2: tổng chi phí 4.373.585 đ chia 978 việc thành công, xấp xỉ 4.472 đ/việc thành công. CPS có thành phần dựa trên thời gian simulated.
- Kiểm tra B3: giới hạn 2 lần chạy có tổng chi phí hệ thống thấp nhất, 6.901.220 đ; giới hạn 1 lần chạy có CPS trợ lý thấp nhất, 4.111 đ. Hai số đo trả lời hai câu hỏi khác nhau.
- Kiểm tra B4: 11.173.313 / 900 = 12.414,79 đ; làm tròn đến đồng gần nhất thành 12.415 đ (1,03× mức 12.000 đ). Đề xuất thống nhất hiển thị cả số chính xác và số làm tròn.
- Cập nhật phần B3–B4 trong `report/team/bang_chi_phi.md` và sửa số tham chiếu B4 trong hướng dẫn chi tiết để thống nhất với output chương trình.

## 4. Bằng chứng

- Output xác nhận từ `src/lab13.py` (chạy với UTF-8): A1 đạt; B3 đánh dấu đúng CPS trợ lý thấp nhất và tổng chi phí hệ thống thấp nhất; B4 in 12.414,79 đ và số làm tròn 12.415 đ.
- `report/team/bang_chi_phi.md`
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
- `TEAM.md`

## 5. Công cụ AI đã dùng

Dùng ChatGPT để hỗ trợ đối chiếu số trong output với công thức, phát hiện chỗ nhãn B3 dễ gây hiểu nhầm và rà cách làm tròn B4. Kiểm tra lại bằng output chương trình và phép tính trực tiếp `11.173.313 / 900`.

## 6. Tự đánh giá

Đã hoàn thành phần kiểm tra và thống nhất cách trình bày B3–B4. Trước khi nộp, cần nhóm rà lại các phần còn lại trong bảng chi phí và xác nhận các thông tin thành viên khác trong `TEAM.md`.
