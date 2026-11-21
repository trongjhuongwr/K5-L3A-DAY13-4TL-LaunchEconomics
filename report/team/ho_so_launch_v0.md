# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 4TL · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ (gấp 16,3 lần hoá đơn token 274,7 đ; giờ nhân viên chiếm 92,5%) | Giả lập | Người viết code (Nguyễn Trọng Hưởng) |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (+51,8%) · 2. Xem lại (+40,7%) · 3. Lương (+23,1%); token chỉ +5,6% | Giả lập | Người kiểm số (Lê Thành Đạt) |
| 3 · So với nhân viên tự làm | Trong phạm vi: 3.414 đ (0,28×); cả hệ thống: 5.865 đ (0,49× so với 12.000 đ) | Giả lập | Người kiểm số (Lê Thành Đạt) |
| 4 · Chỉ số chính, dùng, an toàn | Đợt chạy thử: Chính 82,83% (994/1.200) · Bỏ qua 27,12% (48/177) · Mở lại 4,25% | Xong, có bằng chứng | Người giữ hồ sơ (Phạm Ngọc Trung Quân) |
| 5 · Bảng lỗi và cách khắc phục | 20 ca đồng thuận 100%; khắc phục 5 ca mẫu đủ 5 loại; chặn lỗi sổ cái và hoàn trùng | Xong, có bằng chứng | Người gắn nhãn 1 (Trần Minh Tân) |
| 6 · Pilot plan | 20 vs 20 nhân viên, MDE 6 điểm, 3 luật dừng 4 vế, rollback 30 phút, chốt 2027-01-05 | Xong, có bằng chứng | Người giữ hồ sơ (Phạm Ngọc Trung Quân) |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi lên 6.787 đ (+51,8%); xem lại 100% lên 11.743 đ – 12.415 đ (0,98×–1,03×) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** (cho phép triển khai thử nghiệm pilot có kiểm soát trong phạm vi thu hẹp `noi_dia` và `hang_nang`).

**Các điều kiện tiên quyết và lộ trình thẩm định trước khi bắt đầu:**
1. **Khắc phục lỗi hệ thống trọng yếu:** Kỹ sư trưởng agent hoàn thành việc triển khai khoá chống trùng idempotency key (xử lý triệt để ca 20) và cơ chế kiểm tra đối soát 2 pha với sổ cái kế toán (xử lý triệt để ca 7) trước ngày 15/12/2026.
2. **Ký duyệt đánh đổi thiết kế thực nghiệm:** Giám đốc vận hành LogiX-VN ký biên bản phê duyệt chấp thuận mức chênh MDE 6 điểm (859 yêu cầu/nhóm, $m \ge 299$ yêu cầu/nhân viên) và chấp nhận rủi ro Statistical Power giảm xuống 64,2% nếu hiệu quả can thiệp thực tế chỉ đạt 5 điểm trước ngày 20/12/2026.
3. **Kích hoạt hạ tầng đo lường toàn diện:** Kỹ sư trưởng agent hoàn tất tích hợp và kiểm thử 10 event telemetry có thuộc tính `trace_id` trên giao diện CSKH; thay thế số phút giả lập bằng dữ liệu đo thời gian thực tế ngay sau tuần rollout 0.10 trước ngày 25/12/2026.
4. **Cơ chế giảm xem lại theo bậc (Tiered Review):** Trưởng nhóm CSKH ban hành quy trình phân loại rủi ro ticket để giảm tỉ lệ xem lại từng bước từ 100% xuống dưới 50% ở bước rollout 0.25 nhằm bảo vệ biên độ tiết kiệm chi phí trước ngày 28/12/2026.
