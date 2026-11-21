# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Minh Tân · Người gắn nhãn 2: Phạm Ngọc Trung Quân (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
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

**Thống kê theo 5 nhóm:**
- **Do người dùng (4 ca):** 1, 6, 9, 14
- **Hệ thống (5 ca):** 2, 7, 8, 15, 20
- **Ngữ cảnh (4 ca):** 3, 10, 16, 18
- **Giới hạn hệ thống (4 ca):** 4, 11, 13, 19
- **Ngầm (3 ca):** 5, 12, 17

## Quy tắc phân biệt cho các ca dễ lẫn

Các quy tắc giúp phân biệt chính xác nguyên nhân gốc giữa các nhóm lỗi dễ gây nhầm lẫn:

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** Nguyên nhân gốc phát sinh lỗi xuất phát từ việc người dùng chọn sai danh mục yêu cầu (chọn nhầm luồng "giao trễ" khi hàng vỡ) hoặc nhập sai định dạng mã định danh (nhập mã đơn sàn TMĐT thay vì mã vận đơn LogiX). Việc trợ lý chưa chủ động phát hiện để gợi ý chuyển luồng hay hướng dẫn lại là điểm hạn chế trong trải nghiệm người dùng cần giải quyết ở phương án khắc phục, không làm thay đổi bản chất nguyên nhân lỗi ở đầu vào.
- **Ca 13 là Giới hạn hệ thống, không phải Hệ thống:** Nghiệp vụ hoàn phí bảo hiểm hàng hoá thuộc về đơn vị bảo hiểm đối tác, nằm hoàn toàn ngoài ranh giới phạm vi chức năng và dữ liệu được cấp quyền của trợ lý hoàn phí LogiX-VN. Ngay cả khi trợ lý xử lý giới hạn này vụng về (trả lời chung chung thay vì từ chối dứt khoát), nguyên nhân gốc vẫn là yêu cầu vượt ngoài giới hạn cho phép của hệ thống.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** Lỗi sai đã biểu hiện trực tiếp ra bề mặt giao diện và có thể nhận diện được ngay trong luồng vận hành (trích dẫn sai điều khoản 7.2 không có thực bị lộ trong câu trả lời; tính sai tỷ lệ hoàn 100% thay vì 50% được nhân viên phát hiện ngay khi xem lại trước khi gửi). Loại lỗi "Ngầm" chỉ áp dụng khi cả người dùng lẫn hệ thống đều hoàn toàn không nhận ra sự sai lệch cho tới khi tiến hành kiểm tra đối soát mẫu.
- **Ca 18 là Ngữ cảnh, không phải Do người dùng hay Hệ thống:** Trợ lý tính toán số tiền bồi hoàn 15.000 đ hoàn toàn chuẩn xác theo đúng chính sách (30.000 đ × 50%). Tuy nhiên, giả định ngầm "khách hàng tự hiểu cách tính" không tương thích với bối cảnh tâm lý của khách, khiến khách hiểu nhầm là hoàn thiếu và dẫn đến khiếu nại mở lại yêu cầu.
- **Ca 12 là Ngầm, không phải Giới hạn hệ thống:** Kết quả trả về cho khách hàng vẫn đúng và hệ thống không kích hoạt cảnh báo lỗi hay ngoại lệ nào, nhưng công cụ tra đơn của depot D05 trả thiếu trường khiến trợ lý phải âm thầm gọi lại nhiều lần, làm chi phí token tại depot D05 tăng vọt gấp 3 lần bình thường suốt 3 tuần mà không ai phát hiện; loại lỗi ngầm bao hàm cả các thất thoát và sai lệch âm thầm về tài nguyên, chi phí vận hành.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò cụ thể, tuyệt đối không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ phát sinh vượt quá 2% tổng số yêu cầu/ngày | Nhận diện mẫu mã sàn TMĐT (Shopee, TikTok, Lazada) và tự động gọi API tra cứu sang mã vận đơn LogiX; nếu không tra được thì phản hồi hướng dẫn định dạng kèm ảnh minh họa | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: phát hiện tin nhắn thông báo "đã hoàn" mà không có bản ghi sổ cái trạng thái `ok` cùng `trace_id`; ngưỡng cảnh báo = 0 ca | Áp dụng cơ chế kiểm tra tính toàn vẹn 2 pha: chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok`; nếu gặp lỗi 503 sau 3 lần retry thì chuyển trạng thái "đang xử lý" và bàn giao cho nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Báo cáo tuần theo dõi tỷ lệ yêu cầu có event `reopened_within_7d` với lý do khiếu nại "hoàn thiếu tiền" mà kiểm tra đối soát thấy đúng chính sách; ngưỡng cảnh báo > 1% | Chuẩn hóa mẫu thông báo tin nhắn luôn minh bạch chi tiết công thức tính: Phí vận chuyển × Tỷ lệ bồi hoàn chính sách = Số tiền hoàn thực tế (Ví dụ: 30.000 đ × 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Giám sát tần suất event `handoff_to_staff` với thuộc tính `reason = thieu_du_lieu`, phân rã theo từng loại yêu cầu; ngưỡng cảnh báo > 5% ở bất kỳ nhóm yêu cầu nào | Duy trì cơ chế bàn giao sang nhân viên xử lý kèm bản tóm tắt tự động; đồng thời loại bỏ phân khúc đơn hàng quốc tế (`quoc_te`) ra khỏi phạm vi thử nghiệm pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra đối soát ngẫu nhiên mẫu 100 đơn/tuần so với bảng giá chính thức có hiệu lực của phòng kế toán; ngưỡng phát hiện sai lệch $\ge 1\%$ số đơn kiểm tra | Thiết lập webhook tự động xóa bộ nhớ đệm (cache invalidation) ngay khi bảng giá mới có hiệu lực trên ERP; bắt buộc ghim phiên bản bảng giá (`pricing_policy_version`) trực tiếp vào trace | Kế toán trưởng |
