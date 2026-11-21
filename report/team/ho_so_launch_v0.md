# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 4TL · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Chi phí mỗi việc thành công là **4.472 đ [simulated]**; trong đó giờ làm việc của nhân viên chiếm 92,5% tổng chi phí và gấp 16,3 lần hóa đơn token và tool | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | Xếp hạng tác động: **1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)**. Biến động giá token chỉ ảnh hưởng nhỏ (+5,6%) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí trợ lý bằng 0,37× mức tự làm (12.000 đ); `noi_dia` đạt **2.696 đ (0,22×)**, `hang_nang` đạt **8.221 đ (0,69×)**; tuy nhiên `quoc_te` lỗ nặng **22.515 đ (1,88×)** và `doi_tac` đạt **10.215 đ (0,85×)** [simulated] | Giả lập | Chuyên viên phân tích tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: Chính (**82,83%** đóng trong 24h & không mở lại 7 ngày) · Dùng (**27,12%** bỏ qua hoặc sửa gợi ý) · An toàn (**4,25%** mở lại trong 7 ngày; trong phạm vi pilot: 3,97%) | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Phân loại 20 ca lỗi Google PAIR (đồng thuận 100%): 4 Người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn, 3 Ngầm. Bảng 5 ca mẫu có event định lượng và vai trò xử lý cụ thể | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Thiết kế A/B 20 vs 20 nhân viên phân tầng theo depot; chấp nhận MDE 6 điểm ($n = 859$/nhóm, $m \ge 299$ yc/người); 3 luật dừng chuẩn cú pháp 4 vế, rollback 30 phút, chốt ngày 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi tăng +51,8% (6.787 đ); Duy trì xem lại 100% tốn 11.743 đ – 12.415 đ (0,98× – 1,03×) [simulated], triệt tiêu lợi ích kinh tế; Hụt khối lượng đội chi phí cố định (+1.185 đ đến +2.370 đ/việc) | Giả lập | Kế toán trưởng |

**Đề xuất:** **Go có điều kiện** (Conditional Go cho phạm vi thử nghiệm pilot `noi_dia` + `hang_nang`)

Hồ sơ thẳng thắn thừa nhận 4 điểm bất lợi cốt lõi từ dữ liệu thực tế:
1. Luồng yêu cầu `quoc_te` gây lỗ nặng 1,88× (22.515 đ so với 12.000 đ của nhân viên tự làm) và retry 3 lần không cải thiện tỷ lệ thành công (tụt từ 30% xuống 2,2%).
2. Kịch bản xem lại 100% tiêu tốn 11.743 đ (0,98×) đến 12.414,79 đ ≈ 12.415 đ (1,03× [simulated]), làm biến mất hoàn toàn hiệu quả tiết kiệm chi phí của trợ lý.
3. Cỡ mẫu 20 nhân viên mỗi nhóm không thể phát hiện mức chênh 5 điểm; khi chấp nhận MDE 6 điểm, Statistical Power suy giảm còn 64,2% nếu hiệu quả thật chỉ là 5 điểm.
4. Nguy cơ rủi ro tài chính cao từ lỗi hoàn tiền trùng 2 lần (ca 20) và lỗi không đồng bộ trạng thái sổ cái (ca 7).

Kèm theo 4 điều kiện ràng buộc bắt buộc trước và trong quá trình chạy thử nghiệm pilot:
- **Điều kiện 1 (Thu hẹp phạm vi):** Cắt bỏ hoàn toàn luồng `quoc_te` và `doi_tac`, chỉ cấp phép chạy pilot cho hai nhóm có hiệu quả kinh tế rõ rệt là `noi_dia` (0,22×) và `hang_nang` (0,69×).
  - *Người phụ trách:* PM trợ lý hoàn phí. *Ngày kiểm tra:* 2026-11-25.
- **Điều kiện 2 (Khắc phục lỗi trọng yếu):** Hoàn tất cài đặt khóa chống trùng (idempotency key) và đối soát hai chiều tự động với dịch vụ sổ cái (giải quyết triệt để ca 7 và ca 20) trước khi mở cổng pilot.
  - *Người phụ trách:* Kỹ sư trưởng agent. *Ngày kiểm tra:* 2026-11-28.
- **Điều kiện 3 (Phê duyệt đánh đổi thống kê):** Giám đốc vận hành ký văn bản chấp thuận đánh đổi MDE 6 điểm (chấp nhận rủi ro Statistical Power còn 64,2% trong trường hợp tác động thật là 5 điểm).
  - *Người phụ trách:* Giám đốc vận hành LogiX-VN. *Ngày kiểm tra:* 2026-11-30.
- **Điều kiện 4 (Kiểm soát xem lại):** Bắt buộc kích hoạt lộ trình giảm tỷ lệ xem lại theo bậc (từ 50% xuống 20% rồi 10%) ngay khi tỷ lệ sửa và bỏ gợi ý của nhân viên giảm xuống dưới 15%, tuyệt đối không duy trì xem lại 100%.
  - *Người phụ trách:* Trưởng nhóm CSKH. *Ngày kiểm tra:* 2026-12-15.
