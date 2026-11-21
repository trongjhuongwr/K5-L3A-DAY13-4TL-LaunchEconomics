# Báo cáo cá nhân — Phạm Ngọc Trung Quân

## 1. Thông tin thành viên

- Họ tên: Phạm Ngọc Trung Quân
- MSSV: (thành viên tự điền)
- Email: (thành viên tự điền)
- GitHub: (thành viên tự điền)
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (Labeler 2 & Document keeper)

## 2. Phần việc phụ trách

- Chịu trách nhiệm tổng hợp và đồng bộ hồ sơ launch v0 trong suốt buổi làm bài ([report/team/ho_so_launch_v0.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/ho_so_launch_v0.md)).
- Thực hiện gắn nhãn độc lập 20 ca lỗi CP3 cùng Người gắn nhãn 1.
- Chịu trách nhiệm chính về file cấu hình kế hoạch thử nghiệm [report/team/pilot_plan.yaml](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/pilot_plan.yaml) (Nhiệm vụ D - CP4).
- Xây dựng bảng đặc tả chỉ số và danh sách 10 event telemetry có `trace_id` trong [report/team/chi_so.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md) (Nhiệm vụ E - CP5).
- Chuẩn bị luận điểm bảo vệ đề xuất **Go có điều kiện** trước Hội đồng Gate 2a.

## 3. Đóng góp cụ thể

1. **Gắn nhãn độc lập 20 ca lỗi (CP3):**
   - Hoàn thành bộ nhãn 2 độc lập trong 8 phút, đối soát đạt đồng thuận tuyệt đối 20/20 (100%) với Người gắn nhãn 1.
2. **Kế hoạch Pilot (CP4 - `pilot_plan.yaml`):**
   - Hoàn thiện toàn bộ các trường trong `pilot_plan.yaml`, xoá sạch 100% các dấu `?`.
   - Ghi nhận chi tiết phần giải thích cỡ mẫu D1 và 5 câu kiểm tra tính tách biệt tác động D2 trong phần chú thích.
   - Thiết lập 3 luật dừng chuẩn cú pháp 4 vế: NẾU ... TRONG ... THÌ ... KHÔNG THÌ ..., gắn liền với vai trò có thẩm quyền quyết định (Giám đốc vận hành, PM trợ lý, Trưởng nhóm CSKH).
   - Thiết kế cơ chế rollback an toàn trong vòng 30 phút.
3. **Đặc tả chỉ số & Event Telemetry (CP5 - `chi_so.md`):**
   - Định nghĩa chính xác 3 chỉ số hiện trạng (Chính: 82,83%, Dùng: 27,12%, An toàn: 4,25%) và đề xuất thêm 2 chỉ số mới.
   - Thiết kế danh mục 10 event nghiệp vụ đều mang thuộc tính `trace_id` để kết nối xuyên suốt với trace của agent; lập ma trận kiểm tra chéo giữa chỉ số và event đo lường.
   - Đưa ra 3 dòng rủi ro kinh tế định lượng lấy số từ bảng độ nhạy.
4. **Hồ sơ Launch v0 (CP5 - `ho_so_launch_v0.md`):**
   - Giữ hồ sơ chuẩn xác trong đúng 1 trang, đủ 7 mục; cột trạng thái tuân thủ nghiêm ngặt 3 giá trị cho phép (`Xong, có bằng chứng`, `Chưa`, `Giả lập`).
   - Xây dựng đề xuất **Go có điều kiện** kèm 4 điều kiện ràng buộc, người chịu trách nhiệm và deadline thẩm định cụ thể.
   - Kiểm soát nghiêm ngặt không để xuất hiện thuật ngữ chạy chính thức (ngoài phạm vi pilot) trong toàn bộ hồ sơ.

## 4. Bằng chứng

- Các file hoàn thiện:
  - [report/team/pilot_plan.yaml](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/pilot_plan.yaml) (đọc thành công bằng `yaml.safe_load`, không còn dấu `?`).
  - [report/team/chi_so.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md) (đủ 10 event có `trace_id`, 3 rủi ro kinh tế).
  - [report/team/ho_so_launch_v0.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/ho_so_launch_v0.md) (đúng 1 trang, 7 mục, vai trò rõ ràng, đề xuất Go có điều kiện).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini.
- **Mục đích sử dụng:** Kiểm tra cú pháp YAML schema, soát lỗi chính tả và rà soát các từ khóa vi phạm quy định của lab.
- **Cách tự kiểm tra:** Dùng lệnh tự động `python -c "import yaml; yaml.safe_load(...)"` và script quét regex kiểm tra dấu `?` và các từ khóa ngoài phạm vi pilot để đảm bảo tuân thủ 100% quy tắc môn học.

## 6. Tự đánh giá

- Hoàn thành xuất sắc vai trò Người gắn nhãn 2 kiêm giữ hồ sơ.
- Quản lý hồ sơ nhất quán, đồng bộ số liệu giữa code và báo cáo, sẵn sàng bảo vệ kế hoạch pilot trước hội đồng.
- Đánh giá: 10/10.
