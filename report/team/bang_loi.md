# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Minh Tân · Người gắn nhãn 2: Phạm Ngọc Trung Quân (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (Đạt tiêu chuẩn $\ge 80\%$)

## Quy tắc phân biệt cho các ca không trùng và ca dễ lẫn

- **Ca 6, 9 (Do người dùng, không phải Hệ thống):** Nguyên nhân gốc là khách chọn sai mục hoặc nhập sai mã vận đơn; việc trợ lý thiếu gợi ý là cơ hội cải tiến giao diện, thuộc về giải pháp khắc phục.
- **Ca 13 (Giới hạn hệ thống):** Nhu cầu hoàn phí bảo hiểm hàng hoá thuộc đối tác thứ ba hoàn toàn ngoài phạm vi của hệ thống, kể cả khi trợ lý xử lý chuyển giao chưa khéo.
- **Ca 8, 15 (Hệ thống, không phải Ngầm):** Lỗi trích dẫn sai điều khoản chính sách hoặc tính sai % hoàn tiền đã lộ rõ trên bề mặt kết quả và nhân viên kiểm duyệt bắt được ngay, không phải lỗi ngầm.
- **Ca 18 (Ngữ cảnh):** Số tiền hoàn 50% hoàn toàn đúng chính sách, chỉ có giả định "khách tự hiểu cách tính" là không khớp với ngữ cảnh tâm lý khách hàng.
- **Ca 12 (Ngầm):** Trợ lý vẫn cho ra câu trả lời đúng nhưng bị lặp tool làm chi phí token tăng gấp 3 lần suốt 3 tuần mà không ai hay biết; lỗi ngầm bao gồm cả bất thường về chi phí vận hành.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò cụ thể có thẩm quyền, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; kích hoạt cảnh báo khi vượt quá 2% tổng số yêu cầu/ngày | Tự động nhận diện định dạng mã sàn TMĐT và ánh xạ sang mã vận đơn LogiX; nếu không tra được thì hiển thị hướng dẫn kèm hình ảnh minh hoạ | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: phát hiện tin nhắn "đã hoàn" mà không có bản ghi sổ cái `status=ok` cùng `trace_id`; ngưỡng kích hoạt: > 0 ca | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả mã xác nhận 200/OK; nếu API sổ cái 503 sau 3 lần retry thì chuyển sang trạng thái "đang xử lý" và chuyển tiếp nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Đo lường tỉ lệ mở lại ticket với lý do "thắc mắc số tiền" nhưng thẩm định lại thấy đúng chính sách; ngưỡng: > 1% số ticket/tuần | Mẫu tin nhắn thông báo luôn hiển thị tường minh công thức tính: ví dụ "Cước vận chuyển 30.000 đ × 50% = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = thieu_du_lieu` theo từng phân loại đơn; ngưỡng: > 5% số đơn của loại đó | Chuyển giao tự động kèm bản tóm tắt tình trạng cho nhân viên; loại bỏ phân loại `quoc_te` ra khỏi phạm vi thử nghiệm pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán mẫu ngẫu nhiên 100 đơn hoàn tất mỗi tuần so với bảng giá hiện hành; ngưỡng phát hiện: $\ge 1\%$ đơn có chênh lệch tiền | Thiết lập cơ chế tự động xoá bộ nhớ đệm (cache invalidation) ngay khi phát hành bảng giá mới; ghi nhận phiên bản bảng giá vào thuộc tính của `trace_id` | Kế toán trưởng |
