# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Minh Tân · Người gắn nhãn 2: Phạm Ngọc Trung Quân (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Đúng | Do người dùng |
| 2 | Hệ thống | Hệ thống | Đúng | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Đúng | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Đúng | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Đúng | Ngầm |
| 6 | Do người dùng | Do người dùng | Đúng | Do người dùng |
| 7 | Hệ thống | Hệ thống | Đúng | Hệ thống |
| 8 | Hệ thống | Hệ thống | Đúng | Hệ thống |
| 9 | Do người dùng | Do người dùng | Đúng | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Đúng | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Đúng | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Đúng | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Đúng | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Đúng | Do người dùng |
| 15 | Hệ thống | Hệ thống | Đúng | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Đúng | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Đúng | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Đúng | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Đúng | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Đúng | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (Đạt tiêu chuẩn $\ge 80\%$)

**Thống kê theo 5 nhóm:**
- **Do người dùng (4 ca):** 1, 6, 9, 14
- **Hệ thống (5 ca):** 2, 7, 8, 15, 20
- **Ngữ cảnh (4 ca):** 3, 10, 16, 18
- **Giới hạn hệ thống (4 ca):** 4, 11, 13, 19
- **Ngầm (3 ca):** 5, 12, 17

## Quy tắc phân biệt cho các ca dễ lẫn

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** Gốc lỗi là khách hàng chọn sai mục lý do hoặc nhập nhầm mã đơn sàn TMĐT thay vì mã vận đơn. Trợ lý không gợi ý là điểm cần cải thiện nghiệp vụ, thuộc cột giải pháp khắc phục.
- **Ca 13 là Giới hạn hệ thống:** Đơn hàng phát sinh từ khiếu nại đối tác sàn ngoài phạm vi tích hợp dữ liệu thì thuộc về giới hạn biên của hệ thống, kể cả khi khả năng xử lý từ chối của trợ lý còn hạn chế.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** Lỗi logic đã bộc lộ ra bề mặt hiển thị và có người nhìn thấy (trích dẫn sai điều khoản hiển thị trên màn hình, nhân viên bắt được khi xem lại). Nhãn "Ngầm" chỉ dành cho lỗi hoàn toàn không ai hay biết cho tới khi kiểm toán mẫu.
- **Ca 18 là Ngữ cảnh:** Số tiền hoàn 15.000 đ là hoàn toàn chuẩn xác theo chính sách (30.000 đ × 50%), nhưng giả định "khách hàng tự hiểu công thức tính khấu trừ" không khớp với tâm lý thực tế của người dùng.
- **Ca 12 là Ngầm:** Trợ lý vẫn ra kết quả đúng nhưng bị kẹt vòng lặp ngầm khiến chi phí token tăng vọt gấp 3 lần suốt 3 tuần mà không ai phát hiện; lỗi ngầm bao gồm cả sai lệch về chi phí tài nguyên chứ không chỉ là sai câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng số học, tần suất). Người phụ trách là một vai trò cụ thể, tuyệt đối không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ vượt quá 2% tổng số yêu cầu/ngày | Tự động nhận diện định dạng mã sàn TMĐT để đối soát tra sang mã vận đơn nội bộ LogiX; nếu không tra cứu được thì hiển thị hướng dẫn kèm hình ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: event tin nhắn "đã hoàn" nhưng không có bản ghi sổ cái `status == 'ok'` cùng `trace_id`; ngưỡng báo động là $\ge 1$ ca lệch | Chỉ gửi thông báo "đã hoàn" cho khách sau khi hệ thống sổ cái xác nhận `ok`; nếu gặp lỗi HTTP 503 sau 3 lần retry thì thông báo "đang xử lý" và tự động chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Giám sát tỷ lệ mở lại ticket với lý do thắc mắc số tiền mà kết quả kiểm tra đối soát là đúng, theo chu kỳ hàng tuần (ngưỡng cảnh báo > 3%) | Chuẩn hóa mẫu tin nhắn phản hồi luôn ghi rõ ràng công thức chi tiết từng bước: `30.000 đ × 50% = 15.000 đ` kèm lý do khấu trừ theo điều khoản | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = 'thieu_du_lieu'`, thống kê theo từng phân loại yêu cầu (ngưỡng cảnh báo > 15%) | Duy trì cơ chế chuyển tiếp sang nhân viên kèm toàn bộ tóm tắt thông tin đã trích xuất; loại bỏ hẳn luồng `quoc_te` ra khỏi phạm vi triển khai pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu ngẫu nhiên (audit) 100 đơn/tuần đối chiếu với bảng giá dịch vụ hiện hành; ngưỡng báo động khi có $\ge 1\%$ đơn bị lệch giá | Tự động xóa sạch bộ nhớ cache khi cập nhật bảng giá cước mới; bắt buộc ghi nhận phiên bản bảng giá (`pricing_version`) vào metadata của mỗi `trace_id` | Kế toán trưởng |
