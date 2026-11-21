# Báo cáo cá nhân — Trần Minh Tân (2A202603688)

## 1. Thông tin thành viên

- Họ tên: Trần Minh Tân
- MSSV: 2A202603688
- Email: minhtantran.contact@gmail.com
- GitHub: minhtantran99
- Vai trong nhóm: Người gắn nhãn 1 (Labeler 1)

## 2. Phần việc phụ trách

- Đọc kỹ đề bài, tài liệu hướng dẫn và theo dõi toàn bộ các điều kiện nghiệm thu "Xong khi" của cả 5 checkpoint (CP1 → CP5) cho nhóm 4TL.
- Chủ trì triển khai Nhiệm vụ C (Checkpoint CP3): Gắn nhãn độc lập 20 ca lỗi từ đề bài vào 5 danh mục phân loại lỗi của Google PAIR (Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm).
- Phối hợp đối soát độc lập với Người gắn nhãn 2 (Phạm Ngọc Trung Quân), tính toán tỷ lệ đồng thuận và làm rõ các ca nhãn trùng khớp.
- Xây dựng các nguyên tắc và quy tắc phân biệt ranh giới giữa các ca dễ gây nhầm lẫn dựa trên nguyên lý cốt lõi: gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.
- Thiết kế bảng biện pháp khắc phục chi tiết cho 5 ca lỗi mẫu đại diện cho 5 loại lỗi, đảm bảo mỗi ca có cơ chế phát hiện định lượng đo lường được (tên event, ngưỡng số học, chu kỳ phát hiện) và quy rõ trách nhiệm cho đúng 1 vai trò vận hành cụ thể.
- Kiểm tra chéo chất lượng hồ sơ toàn nhóm: rà soát các điều kiện tiên quyết, đảm bảo mọi số liệu giả lập đều được gắn nhãn `simulated` và tuyệt đối không xuất hiện từ cấm về môi trường triển khai thực tế trong toàn bộ tài liệu báo cáo.

## 3. Đóng góp cụ thể

1. **Gắn nhãn độc lập 20 ca lỗi (CP3):**
   - Đọc và phân tích bản chất từng tình huống trong số 20 ca lỗi của đề bài.
   - Hoàn thành gắn nhãn độc lập (Nhãn người 1) trong vòng 8 phút, không trao đổi với người khác:
     - *Do người dùng (4 ca):* Ca 1 (khách nhập thiếu 2 số tài khoản), Ca 6 (khách chọn nhầm luồng giao trễ khi hàng bị vỡ), Ca 9 (khách nhập mã đơn sàn TMĐT thay vì mã vận đơn), Ca 14 (khách bấm nhầm nút xác nhận đã nhận tiền).
     - *Hệ thống (5 ca):* Ca 2 (truyền sai tham số hàng thường thay vì hàng nặng), Ca 7 (API sổ cái 503 vẫn báo hoàn tiền thành công), Ca 8 (ảo giác viện dẫn Điều 7.2 không tồn tại), Ca 15 (tính hoàn 100% thay vì 50% cho đơn trễ 26h), Ca 20 (hoàn tiền hai lần cho cùng một đơn do thiếu khóa chống trùng idempotency).
     - *Ngữ cảnh (4 ca):* Ca 3 (tiền về ví LogiX theo đúng thiết kế nhưng khách ngóng tiền về ngân hàng), Ca 10 (từ chối do bão đúng điều khoản bất khả kháng nhưng app vẫn cam kết 24h), Ca 16 (thông báo Zalo lúc 2:14 sáng theo thiết kế gửi ngay làm phiền khách), Ca 18 (hoàn 15.000 đ đúng 50% của 30.000 đ nhưng không ghi công thức khiến khách tưởng hoàn thiếu).
     - *Giới hạn hệ thống (4 ca):* Ca 4 (chặng giao quốc tế của hãng nước ngoài nằm ngoài phạm vi dữ liệu LogiX), Ca 11 (khách gửi tin nhắn thoại trong khi trợ lý chỉ xử lý văn bản), Ca 13 (nghiệp vụ bảo hiểm hàng hóa của đối tác ngoài phạm vi chức năng), Ca 19 (yêu cầu đơn từ 14 tháng trước vượt quá hạn mức truy xuất dữ liệu 12 tháng).
     - *Ngầm (3 ca):* Ca 5 (hoàn theo giá trước giảm cho đơn có voucher, thừa 12.000 đ/đơn mà khách không báo, không alert), Ca 12 (tool tra đơn D05 trả thiếu trường khiến agent retry ngầm làm tiền token tăng gấp 3 lần suốt 3 tuần), Ca 17 (cache giá cũ cho đơn dưới 2 kg lệch 1.000–2.000 đ suốt 9 ngày trên 212 đơn).
2. **Đối soát và xác nhận đồng thuận:**
   - Đối chiếu với bộ nhãn độc lập của Người gắn nhãn 2 (Phạm Ngọc Trung Quân).
   - Đạt tỷ lệ đồng thuận tuyệt đối: **20/20 ca trùng khớp (100%)**, vượt xa ngưỡng yêu cầu tối thiểu (≥ 80%).
3. **Quy tắc phân biệt các ca dễ lẫn:**
   - Làm rõ vì sao Ca 6 và Ca 9 là lỗi *Do người dùng* (nguyên nhân gốc là đầu vào khách nhập/chọn sai; việc trợ lý thiếu gợi ý là chỗ cần khắc phục).
   - Làm rõ vì sao Ca 13 là *Giới hạn hệ thống* (ngoài phạm vi nghiệp vụ, dù trợ lý trả lời chung chung chưa tốt).
   - Làm rõ vì sao Ca 8 và Ca 15 là *Hệ thống* chứ không phải Ngầm (sai lệch đã hiển thị ra ngoài và bị bắt được).
   - Làm rõ vì sao Ca 18 là *Ngữ cảnh* (số tiền tính đúng 100%, chỉ giả định khách tự hiểu công thức là không khớp bối cảnh).
   - Làm rõ vì sao Ca 12 là *Ngầm* (câu trả lời vẫn đúng, không có alert lỗi, nhưng âm thầm tiêu tốn gấp 3 lần token suốt 3 tuần; lỗi ngầm bao gồm cả sai lệch chi phí/tài nguyên).
4. **Bảng khắc phục đo lường được cho 5 ca mẫu:**
   - Ca 9 (Do người dùng): Bắt qua event `input_validation_failed` (> 2%/ngày); khắc phục bằng module regex nhận diện mã sàn TMĐT để tự tra mã vận đơn, kèm hướng dẫn bằng hình ảnh; phụ trách: *PM trợ lý hoàn phí*.
   - Ca 7 (Hệ thống): Đối soát mỗi giờ tin nhắn "đã hoàn" thiếu bản ghi sổ cái ok; áp dụng Two-phase commit chỉ báo hoàn khi sổ cái trả ok; phụ trách: *Kỹ sư trưởng agent*.
   - Ca 18 (Ngữ cảnh): Báo cáo tuần tỷ lệ mở lại vì lý do hoàn thiếu tiền mà kiểm tra thấy đúng; chuẩn hóa mẫu tin nhắn minh bạch công thức tính (30.000 đ × 50% = 15.000 đ); phụ trách: *Trưởng nhóm CSKH*.
   - Ca 4 (Giới hạn hệ thống): Theo dõi event `handoff_to_staff` với `reason = thieu_du_lieu` (> 5%); giữ cơ chế bàn giao kèm tóm tắt và đưa phân khúc `quoc_te` ra khỏi pilot; phụ trách: *PM trợ lý hoàn phí*.
   - Ca 17 (Ngầm): Hậu kiểm 100 đơn/tuần với bảng giá kế toán; xóa cache bảng giá tức thì bằng webhook và ghim `pricing_policy_version` vào trace; phụ trách: *Kế toán trưởng*.
5. **Kiểm tra chéo và rà soát điều kiện tiên quyết:**
   - Soát toàn bộ tài liệu hồ sơ, bảo đảm không có từ cấm theo quy định của môn học.
   - Giám sát các điều kiện "Xong khi" cho các phần việc của nhóm, hỗ trợ Đạt và Quân chuẩn bị hồ sơ bảo vệ trước Hội đồng Gate 2a.

## 4. Bằng chứng

- File bảng lỗi và khắc phục: [bang_loi.md](bang_loi.md).
- Bảng đồng thuận nhãn: Đạt 20/20 ca trùng khớp (100% tỷ lệ đồng thuận).
- Cập nhật thông tin thành viên và phân vai cá nhân tại [TEAM.md](../../TEAM.md).
- Nhánh git thực hiện: `tan_branch`, các commit được thực hiện bởi tài khoản `minhtantran99` (`minhtantran.contact@gmail.com`).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:**
  - Tra cứu hướng dẫn phân loại lỗi theo Google PAIR (People + AI Research Framework).
  - Soát lại các ca nhãn biên giới (borderline cases) nhằm đối chiếu với các nguyên lý thiết kế tương tác người - máy.
- **Cách tự kiểm tra và kiểm chứng:**
  - Tự mình đọc kỹ mô tả chi tiết của từng ca lỗi trong tài liệu `Ngay13_Lab13_De_bai_hoc_vien.docx` trước khi phân loại.
  - Áp dụng triệt để nguyên tắc "gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa" để không bị nhầm lẫn giữa lỗi người dùng với lỗi giao diện hỗ trợ.
  - Kiểm tra tính đo lường được của từng giải pháp khắc phục (phải có event cụ thể, ngưỡng số học và chu kỳ định lượng).

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chuẩn xác và đúng hạn 100% các yêu cầu của Người gắn nhãn 1 (Labeler 1).
- Tuân thủ nghiêm ngặt quy tắc liêm chính học thuật, gắn nhãn độc lập và đạt mức đồng thuận tuyệt đối 100%.
- Các đề xuất khắc phục có tính khả thi kỹ thuật và vận hành cao, phân vai trách nhiệm rõ ràng, sẵn sàng giải trình trước Hội đồng Gate 2a.
- Đánh giá: 10/10.
