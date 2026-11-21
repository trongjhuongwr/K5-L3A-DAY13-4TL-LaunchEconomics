# Báo cáo cá nhân — Phạm Ngọc Trung Quân (2A202603626)

## 1. Thông tin thành viên

- Họ tên: Phạm Ngọc Trung Quân
- MSSV: 2A202603626
- Email: trungquana123@gmail.com
- GitHub: jadenphm29
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper)

## 2. Phần việc phụ trách

- Phụ trách chính Nhiệm vụ C (Bảng lỗi và cách khắc phục theo khung Google PAIR).
- Phụ trách chính Nhiệm vụ D (Thiết kế thực nghiệm và hoàn thiện file cấu hình `report/team/pilot_plan.yaml`).
- Phụ trách chính Nhiệm vụ E1 (Đặc tả chỉ số chất lượng, thiết kế 10 Telemetry event có `trace_id` và ma trận kiểm tra chéo).
- Phụ trách chính Nhiệm vụ E2 (Phân tích ma trận rủi ro kinh tế từ bảng độ nhạy).
- Khởi tạo, duy trì và hoàn thiện Hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`) xuyên suốt buổi làm việc để bảo vệ trước Hội đồng Gate 2a.
- Phối hợp với Người viết code (Nguyễn Trọng Hưởng) và Người kiểm số (Lê Thành Đạt) để đối chiếu số liệu, rà soát tính nhất quán và loại bỏ triệt để các rủi ro vi phạm quy tắc nộp bài.

## 3. Đóng góp cụ thể

1. **Nhiệm vụ C (Phân loại lỗi Google PAIR & Kế hoạch khắc phục):**
   - Độc lập gắn nhãn 20 ca lỗi từ đề bài vào 5 nhóm nguyên nhân gốc rễ của Google PAIR trong vòng 8 phút mà không trao đổi:
     - *Do người dùng (4 ca):* 1, 6, 9, 14.
     - *Hệ thống (5 ca):* 2, 7, 8, 15, 20.
     - *Ngữ cảnh (4 ca):* 3, 10, 16, 18.
     - *Giới hạn hệ thống (4 ca):* 4, 11, 13, 19.
     - *Ngầm (3 ca):* 5, 12, 17.
   - Đối chiếu với Người gắn nhãn 1 (Trần Minh Tân), đạt tỉ lệ đồng thuận tuyệt đối 20/20 = 100% ($\ge 80\%$).
   - Soạn thảo quy tắc phân biệt rõ ràng cho các ca dễ gây nhầm lẫn: ca 6, 9 (Do người dùng vì gốc từ khách hàng); ca 13 (Giới hạn hệ thống do ngoài phạm vi); ca 8, 15 (Hệ thống vì sai lệch đã lộ trên giao diện); ca 18 (Ngữ cảnh vì công thức đúng nhưng giả định giao tiếp không khớp); ca 12 (Ngầm vì đội chi phí gấp 3 mà không hiển thị lỗi).
   - Xây dựng bảng khắc phục cho 5 ca mẫu (9, 7, 18, 4, 17) với cơ chế phát hiện định lượng đo lường được (event, ngưỡng số học, chu kỳ quét) và gán trách nhiệm duy nhất cho 1 vai trò chuyên môn (*PM trợ lý hoàn phí*, *Kỹ sư trưởng agent*, *Trưởng nhóm CSKH*, *Kế toán trưởng*).

2. **Nhiệm vụ D (Thiết kế thực nghiệm và hoàn thiện `pilot_plan.yaml`):**
   - Giải chi tiết và ghi nhận 5 bài toán cỡ mẫu D1 vào phần ghi chú đầu file:
     - Câu a: Chia theo yêu cầu cần 1.251 yêu cầu/nhóm.
     - Câu b: Chia theo nhân viên với $m = 75$ ($DE = 2,48$) cần 3.103 yêu cầu/nhóm $\rightarrow$ cần 84 nhân viên (vượt quá 40 nhân viên hiện có $\rightarrow$ không khả thi).
     - Câu c: Với 20 nhân viên/nhóm, trần cỡ mẫu hiệu dụng $n_{\text{eff}} = c / \text{ICC} = 20 / 0,02 = 1.000 < 1.251$ (không thể đạt MDE 5 điểm).
     - Câu d: Với 6 depot/nhóm, trần cỡ mẫu chỉ đạt 300 yêu cầu.
     - Câu e: Khi chấp nhận nới MDE lên 6 điểm ($n = 859$/nhóm), giải phương trình bậc nhất tìm ra số yêu cầu tối thiểu mỗi nhân viên là $m \ge 299$ ($DE = 6,96$, tổng quy mô 5.980 yêu cầu/nhóm).
   - Kiểm tra và trả lời 5 câu hỏi D2 về tính tách biệt tác động (Identifiability), khẳng định thử nghiệm A/B có đối chứng đồng thời, phân tầng ngẫu nhiên theo depot, giảm spillover bằng phân quyền tài khoản theo `staff_id` và tiền đăng ký chỉ số.
   - Xóa sạch 100% dấu `?` trong thân file YAML, điền đầy đủ các thông tin: `owner` (Giám đốc vận hành LogiX-VN), `scope` (chỉ chạy `noi_dia` và `hang_nang`, loại bỏ `quoc_te` và `doi_tac`), đơn vị chia cụm `staff`.
   - Thiết lập 3 luật dừng định lượng theo đúng chuẩn cú pháp 4 vế: **NẾU ... TRONG ... THÌ ... KHÔNG THÌ ...**
   - Thiết lập quy trình rollback khẩn cấp trong 30 phút và khai báo minh bạch danh mục các biến đầu vào giả lập `simulated_inputs`.

3. **Nhiệm vụ E (Đặc tả chỉ số, Telemetry, Rủi ro kinh tế & Hồ sơ launch v0):**
   - Trình bày 3 chỉ số hiện trạng E1 từ dữ liệu chạy thử: Chính (**82,83%**), Dùng (**27,12%** bỏ qua/sửa), An toàn (**4,25%** mở lại trong 7 ngày). Đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn độc lập. Tuân thủ chuẩn mực văn phong khách quan: *"chỉ số trong đợt chạy thử là..."*.
   - Thiết kế danh mục 10 telemetry event chuẩn hóa có trường `trace_id` để kết nối xuyên suốt các tầng hệ thống, kèm ma trận kiểm tra chéo (mapping) giữa chỉ số và event.
   - Lập ma trận 3 rủi ro kinh tế E2 lấy số trực tiếp từ bảng độ nhạy: số ca làm lại tăng gấp đôi (+51,8%), kịch bản xem lại 100% làm mất lợi thế chi phí (11.743 đ – 12.414 đ [simulated]), và rủi ro hụt khối lượng đội chi phí cố định.
   - Hoàn thiện Hồ sơ launch v0 đúng trong phạm vi 1 trang tóm tắt 7 mục. Cột trạng thái chỉ nhận 3 giá trị chuẩn (`Xong, có bằng chứng`, `Chưa`, `Giả lập`).
   - Đưa ra đề xuất **Go có điều kiện** (Conditional Go) trực diện, trung thực thừa nhận 4 điểm bất lợi cốt lõi và gắn kết 4 điều kiện ràng buộc có vai trò chịu trách nhiệm và deadline thẩm định rõ ràng.

## 4. Bằng chứng

- File bảng lỗi Google PAIR: [bang_loi.md](bang_loi.md).
- File kế hoạch thử nghiệm pilot: [pilot_plan.yaml](pilot_plan.yaml).
  - Đã kiểm tra cú pháp thành công bằng lệnh:
    `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml', encoding='utf-8'))"`
  - Hoàn toàn sạch dấu hỏi (`?`).
- File đặc tả chỉ số và telemetry: [chi_so.md](chi_so.md).
- File hồ sơ launch Gate 2a: [ho_so_launch_v0.md](ho_so_launch_v0.md).
- Rà soát toàn bộ thư mục `report/team/`: Không chứa từ cấm chỉ môi trường vận hành quy mô lớn, mọi số liệu chi phí từ trace giả lập đều được gắn nhãn `[simulated]` đúng quy định.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:**
  - Hỗ trợ rà soát cú pháp file YAML để đảm bảo tuân thủ nghiêm ngặt định dạng của thư viện `pyyaml`.
  - Hỗ trợ xây dựng cấu trúc bảng đối soát chéo (mapping) giữa các metric vận hành và schema của telemetry event.
  - Kiểm tra tính đầy đủ của các luật dừng theo cú pháp 4 vế (NẾU - TRONG - THÌ - KHÔNG THÌ).
- **Cách tự kiểm tra và kiểm chứng:**
  - Viết script Python chạy thực nghiệm kiểm tra `yaml.safe_load` để xác nhận parser không phát sinh bất kỳ lỗi thụt dòng (indentation) nào.
  - Đối chiếu độc lập từng ca lỗi trong 20 ca đề bài với tài liệu chính thống của Google People + AI Research (PAIR Guidebook) để đảm bảo không gắn nhầm giữa nguyên nhân gốc và triệu chứng biểu hiện.
  - Kiểm tra thủ công bằng mắt và chạy lệnh tìm kiếm regex để đảm bảo không còn bất kỳ dấu `?` nào trong file YAML và tuân thủ quy tắc từ cấm trong toàn bộ hồ sơ báo cáo.

## 6. Tự đánh giá

- Hoàn thành trọn vẹn và xuất sắc vai trò Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper).
- Đảm bảo tính trung thực, chuẩn xác và liên kết logic chặt chẽ giữa mã nguồn tính toán, bảng độ nhạy, thiết kế thực nghiệm và hồ sơ bảo vệ tại cổng Gate 2a.
- Đề xuất giải pháp có trách nhiệm (Go có điều kiện), bảo vệ quyền lợi và an toàn tài chính cho doanh nghiệp trước các rủi ro tiềm ẩn của hệ thống AI.
- Đánh giá: 10/10.
