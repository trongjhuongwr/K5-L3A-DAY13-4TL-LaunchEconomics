# Báo cáo cá nhân — Trần Minh Tân

## 1. Thông tin thành viên

- Họ tên: Trần Minh Tân
- MSSV: (thành viên tự điền)
- Email: (thành viên tự điền)
- GitHub: (thành viên tự điền)
- Vai trong nhóm: Người gắn nhãn 1 (Labeler 1)

## 2. Phần việc phụ trách

- Chịu trách nhiệm chính về file [report/team/bang_loi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_loi.md) (Nhiệm vụ C - CP3).
- Thực hiện gắn nhãn độc lập 20 ca lỗi từ đề bài theo 5 phân loại của Google PAIR (Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống, Ngầm) trong 8 phút mà không trao đổi.
- Đối soát nhãn với Người gắn nhãn 2 (Phạm Ngọc Trung Quân) để đạt tỉ lệ đồng thuận tuyệt đối $\ge 80\%$.
- Xây dựng quy tắc phân biệt cho các ca dễ nhầm lẫn theo nguyên nhân gốc.
- Thiết lập bảng biện pháp khắc phục cho 5 ca lỗi đại diện (mỗi loại 1 ca) với cơ chế phát hiện đo lường được và chỉ định vai trò chịu trách nhiệm cụ thể.
- Giám sát điều kiện nghiệm thu "Xong khi" của từng checkpoint trong suốt buổi làm bài.

## 3. Đóng góp cụ thể

1. **Gắn nhãn độc lập 20 ca lỗi:**
   - Hoàn thành bộ nhãn 1 độc lập cho toàn bộ 20 ca lỗi, kết quả đối soát đạt **đồng thuận 20/20 (100%)** với Người gắn nhãn 2.
   - Phân loại chuẩn xác: Do người dùng (ca 1, 6, 9, 14), Hệ thống (ca 2, 7, 8, 15, 20), Ngữ cảnh (ca 3, 10, 16, 18), Giới hạn hệ thống (ca 4, 11, 13, 19), Ngầm (ca 5, 12, 17).
2. **Xây dựng quy tắc phân biệt:**
   - Phân tích rõ ca 6, 9 thuộc lỗi Người dùng (nhập sai mã, chọn sai mục; trợ lý thiếu gợi ý là chỗ cần khắc phục).
   - Phân tích rõ ca 13 là Giới hạn hệ thống (ngoài phạm vi bảo hiểm).
   - Phân tích rõ ca 8, 15 là lỗi Hệ thống vì lỗi đã lộ ra trên bề mặt; còn ca 12, 17 là lỗi Ngầm vì chỉ phát hiện qua kiểm toán hoặc audit log.
3. **Bảng khắc phục cho 5 ca đại diện:**
   - Ca 9 (Người dùng): Event `input_validation_failed`, ánh xạ mã sàn TMĐT, phụ trách: PM trợ lý.
   - Ca 7 (Hệ thống): Đối soát sổ cái mỗi giờ, chỉ báo hoàn khi sổ cái trả mã xác nhận, phụ trách: Kỹ sư trưởng agent.
   - Ca 18 (Ngữ cảnh): Đo tỉ lệ mở lại thắc mắc tiền, template tin nhắn hiển thị công thức chi tiết, phụ trách: Trưởng nhóm CSKH.
   - Ca 4 (Giới hạn): Event `handoff_to_staff`, loại `quoc_te` khỏi pilot, phụ trách: PM trợ lý.
   - Ca 17 (Ngầm): Kiểm toán mẫu 100 đơn/tuần, tự động xóa cache khi đổi bảng giá, phụ trách: Kế toán trưởng.

## 4. Bằng chứng

- File báo cáo hoàn thiện: [report/team/bang_loi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_loi.md).
- Hai bộ nhãn độc lập có tỷ lệ đồng thuận 100%, khớp hoàn toàn với đáp án chuẩn Google PAIR của môn học.
- Bảng khắc phục 5 ca không có ô nào ghi chung chung là "cả đội", 100% có vai trò và ngưỡng định lượng rõ ràng.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:** Tra cứu định nghĩa nguyên nhân gốc từ cẩm nang Google PAIR Guidebook (chương Errors + Graceful Failure).
- **Cách tự kiểm tra:** Đối chiếu chéo độc lập với Người gắn nhãn 2, thảo luận dựa trên câu hỏi bản chất: "Nguyên nhân gốc nằm ở đâu? Có vi phạm chính sách không? Ai nhận ra lỗi trước?" để chốt quy tắc.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người gắn nhãn 1.
- Nắm vững lý thuyết Google PAIR, phương pháp phân loại lỗi AI và thiết kế giải pháp khắc phục có tính khả thi kỹ thuật cao.
- Đánh giá: 10/10.
