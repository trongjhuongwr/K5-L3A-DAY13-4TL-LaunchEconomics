# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200 yêu cầu) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (48/177 yêu cầu được xem lại; gồm 38 sửa + 10 bỏ) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200 yêu cầu; trong phạm vi pilot `noi_dia` + `hang_nang` là **3,97%**) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ phiên xử lý có kích hoạt trợ lý | Số phiên có event `agent_suggestion_shown` chia cho tổng số yêu cầu phân bổ cho nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hàng tuần | Số đơn lệch tiền khi kiểm toán mẫu `audit_sample_checked` chia cho tổng số đơn kiểm tra ngẫu nhiên | Không cần tính |

*Ghi chú văn phong:* Ghi nhận chỉ số trong đợt chạy thử là 82,83%, tuyệt đối không viết "trợ lý đã nâng chỉ số từ 0,70" do đợt chạy thử ban đầu chưa có nhóm đối chứng đồng thời.

## Danh sách event

Danh sách 10 event vận hành thu thập đầy đủ thuộc tính `trace_id` để liên kết xuyên suốt với trace kỹ thuật của trợ lý:

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí |
| `agent_run_completed` | Trợ lý (Agent) | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy hoàn tất, kể cả khi lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý xử lý của trợ lý hiển thị trên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `decision` (giu/sua/bo), `phut_xem_lai` (đo thực tế), `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ qua |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất việc làm lại thủ công |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi hệ thống ghi nhận giao dịch vào sổ cái tài chính |
| `handoff_to_staff` | Trợ lý (Agent) | `reason`, `tom_tat`, `trace_id` | Khi trợ lý chủ động chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `duration_minutes`, `trace_id` | Khi ticket khiếu nại được đóng |
| `ticket_reopened` | Khách hàng | `reopened_at`, `reason`, `trace_id` | Khi khách hàng mở lại ticket khiếu nại |
| `audit_sample_checked` | Kế toán đối soát | `so_tien_da_hoan`, `so_tien_dung`, `lech_tien`, `trace_id` | Khi kiểm toán viên đối soát mẫu hàng tuần |

### Bảng kiểm tra chéo (Mapping Chỉ số và Event)

| Chỉ số | Event đầu vào dùng để tính toán | Công thức trích xuất từ Event |
| --- | --- | --- |
| **Chính:** % đóng trong 24h & không mở lại 7 ngày | `ticket_closed`, `ticket_reopened` | Đếm `ticket_closed` có `duration_minutes <= 1440` VÀ không có event `ticket_reopened` cùng `trace_id` trong 7 ngày, chia tổng `refund_request_created`. |
| **Dùng:** Tỉ lệ bỏ qua gợi ý | `staff_review_decision` | Đếm event có `decision` thuộc `['sua', 'bo']` chia cho tổng số event `staff_review_decision`. |
| **An toàn:** Tỉ lệ lỗi lọt đến khách | `ticket_reopened`, `refund_request_created` | Đếm số `trace_id` xuất hiện event `ticket_reopened` trong vòng 7 ngày chia cho tổng số event `refund_request_created`. |
| **Dùng (đề xuất):** Tỉ lệ kích hoạt trợ lý | `agent_suggestion_shown`, `refund_request_created` | Đếm số event `agent_suggestion_shown` chia cho số event `refund_request_created` thuộc `arm == 'treatment'`. |
| **An toàn (đề xuất):** Tỉ lệ sai tiền kiểm toán | `audit_sample_checked` | Đếm số event có `lech_tien > 0` chia cho tổng số event `audit_sample_checked`. |

## E2 · Rủi ro kinh tế

Các rủi ro kinh tế định lượng trích xuất trực tiếp từ bảng phân tích độ nhạy (`bang_chi_phi.md`), có ngưỡng giám sát cụ thể và một vai trò chịu trách nhiệm:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| **Số ca làm lại tăng gấp đôi** | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ [simulated]** | Tỉ lệ yêu cầu cần làm lại theo tuần vượt ngưỡng **> 7%** (mức chạy thử ban đầu là 4,9% trong phạm vi pilot) | Tạm thời thu hẹp phạm vi về duy nhất nhóm `noi_dia`, trích xuất 20 trace làm lại gần nhất để rà soát nguyên nhân gốc rễ và hiệu chỉnh prompt | PM trợ lý hoàn phí |
| **Phải duy trì xem lại 100% kéo dài** | Chi phí tăng lên **11.743 đ [simulated]** (0,98×) nếu làm lại 9 phút, hoặc **12.414 đ [simulated]** (1,03×) nếu làm lại 15,3 phút, làm mất hoàn toàn lợi ích kinh tế so với người tự làm (12.000 đ) | Tỉ lệ yêu cầu được xem lại vẫn còn **> 50%** tại thời điểm kết thúc bước rollout 0.25 | Kích hoạt lộ trình giảm tỷ lệ xem lại theo bậc (giảm dần xuống 20% rồi 10%) khi tỷ lệ sửa + bỏ của nhân viên giảm xuống dưới 15% | Trưởng nhóm CSKH |
| **Khối lượng thực tế thấp hơn dự kiến** | Chi phí cố định 40 triệu đ/tháng phân bổ đội lên: cộng thêm **+1.185 đ/việc** ở quy mô 45.000 yc/tháng, và đội lên **+2.370 đ/việc** nếu khối lượng giảm một nửa [simulated] | Khối lượng yêu cầu thành công thực tế theo dõi hàng tuần đạt **< 50%** so với kế hoạch dự kiến | Dừng mở rộng quy mô pilot, tái đàm phán hợp đồng chi phí bảo trì cố định hoặc chuyển sang mô hình thanh toán biến đổi theo lượng sử dụng (pay-as-you-go) | PM trợ lý hoàn phí |
