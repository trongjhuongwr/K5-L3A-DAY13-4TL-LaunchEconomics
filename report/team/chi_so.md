# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng (tự đề xuất) | Tỉ lệ nhân viên nhóm can thiệp mở giao diện trợ lý hoàn phí | Số ticket nhóm can thiệp có gọi trợ lý chia tổng số ticket của nhóm | Không cần tính |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền phát hiện qua kiểm toán mẫu ngẫu nhiên hàng tuần | Số đơn có chênh lệch tiền hoàn chia tổng 100 đơn kiểm toán mẫu mỗi tuần | Không cần tính |

*Ghi chú quan trọng:* Chỉ số trong đợt chạy thử là 82,83%; không được viết "trợ lý đã nâng chỉ số lên 82,83%" vì đợt chạy thử 2 tuần chưa thiết lập nhóm đối chứng song song.

## Danh sách event

Hệ thống ghi nhận 10 event telemetry chuẩn, mọi event đều mang thuộc tính `trace_id` để liên kết xuyên suốt toàn bộ vòng đời yêu cầu:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng / Web | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách bấm gửi yêu cầu hoàn tiền |
| `agent_run_completed` | Agent runtime | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Ngay khi một lần chạy của agent kết thúc (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `noi_dung_de_xuat`, `trace_id` | Khi gợi ý của agent hiển thị trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `decision` (giu/sua/bo), `phut_xem_lai` (đo thực tế), `trace_id` | Khi nhân viên bấm nút xác nhận gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai` (đo thực tế), `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn thành xử lý lại ca bị lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái kế toán | `idempotency_key`, `so_tien`, `status` (ok/fail), `trace_id` | Khi hệ thống gọi ghi nhận lệnh hoàn vào sổ cái |
| `handoff_to_staff` | Agent runtime | `reason` (qua_lan_chay/thieu_du_lieu), `tom_tat`, `trace_id` | Khi agent dừng xử lý và chuyển hồ sơ sang nhân viên |
| `ticket_closed` | Hệ thống Helpdesk | `closed_at`, `duration_hours`, `trace_id` | Khi ticket hoàn tất và đóng trên hệ thống |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại ticket trong vòng 7 ngày sau đóng |
| `audit_sample_checked` | Kế toán nội bộ | `so_tien_da_hoan`, `so_tien_chuan`, `lech_tien`, `trace_id` | Định kỳ hàng tuần khi kiểm toán mẫu 100 đơn |

**Kiểm tra chéo tính khả thi đo lường:**
- *Chỉ số chính:* Tính từ cặp event `ticket_closed` (`closed_at - created_at <= 24h`) và không có event `ticket_reopened` trong vòng 7 ngày cùng `trace_id`.
- *Chỉ số dùng:* Đếm `staff_review_decision` với `decision in ['sua', 'bo']` chia cho tổng số event `agent_suggestion_shown`.
- *Chỉ số an toàn:* Đếm số lượng event `ticket_reopened` phát sinh trong vòng 7 ngày chia cho tổng số event `ticket_closed`.
- *Chỉ số dùng đề xuất:* Đếm event `agent_suggestion_shown` chia cho tổng `refund_request_created` của nhóm can thiệp (`arm == 'treatment'`).
- *Chỉ số an toàn đề xuất:* Tính từ thuộc tính `lech_tien > 0` trong event `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Lấy số liệu định lượng trực tiếp từ Bảng phân tích độ nhạy (`bang_chi_phi.md`):

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Tỉ lệ ca làm lại tăng gấp đôi | Chi phí mỗi việc tăng +51,8%, lên 6.787 đ [simulated] | Tỉ lệ đơn làm lại theo tuần vượt quá 7% (mức chạy thử là 4,9% trong phạm vi) | Thu hẹp phạm vi về riêng `noi_dia`, tạm dừng `hang_nang` và rà soát lại 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Buộc phải xem lại 100% kéo dài | Chi phí tăng lên 11.743 đ (0,98×) đến 12.415 đ (1,03×) [simulated], triệt tiêu hiệu quả kinh tế | Tỉ lệ đơn cần xem lại vẫn duy trì > 50% ở cuối bước rollout 0.25 | Triển khai phân tầng xem lại tự động theo điểm tin cậy (chỉ xem lại ca rủi ro cao khi tỉ lệ sửa+bỏ < 15%) | Trưởng nhóm CSKH |
| Khối lượng xử lý thực tế sụt giảm một nửa | Chi phí cố định 40 triệu đ/tháng tăng từ 1.185 đ lên 2.370 đ/việc, nâng CPS lên 5.784 đ (0,48×) [simulated] | Số lượng yêu cầu thành công trung bình tuần thấp hơn 50% so với kế hoạch | Không mở rộng pilot ra các depot tiếp theo; đàm phán lại hợp đồng hạ tầng để tối ưu chi phí cố định | PM trợ lý hoàn phí |
