# Báo cáo nhóm · 4TL · Lab 13

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 4TL
- Lớp: L3A
- Repo: `K5-L3A-DAY13-4TL-LaunchEconomics`
- Thành viên và phân vai:
  1. Nguyễn Trọng Hưởng (2A202603607) — Người viết code (Code author)
  2. Lê Thành Đạt — Người kiểm số (Number verifier)
  3. Trần Minh Tân — Người gắn nhãn 1 (Labeler 1)
  4. Phạm Ngọc Trung Quân — Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Xây dựng bộ hồ sơ thẩm định launch v0 toàn diện cho trợ lý hoàn phí LogiX-VN để bảo vệ trước Hội đồng Gate 2a, trả lời 4 câu hỏi cốt lõi: hiệu quả kinh tế thật sự, mức độ đón nhận của nhân viên, phương án kiểm soát rủi ro lỗi và thiết kế kế hoạch thử nghiệm pilot có giá trị thống kê để ra quyết định.
- **Cách tiếp cận:** Tiếp cận định lượng dựa trên bằng chứng dữ liệu thực tế (1.200 yêu cầu, 1.624 lần chạy giả lập); tuân thủ nguyên tắc Cost-of-Pass (Erol et al., 2025) để tính toán chi phí trên mỗi việc thành công; áp dụng hướng dẫn Google PAIR để phân loại nguyên nhân gốc của lỗi; và vận dụng phương pháp thử nghiệm ngẫu nhiên phân cụm (Cluster RCT) để thiết kế pilot khoa học.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí - CP1):** Cài đặt mô hình `mo_hinh` trong [src/lab13.py](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/src/lab13.py) phân bổ toàn bộ chi phí token, tool và thời gian nhân viên (xem lại, làm lại) vào các yêu cầu thành công. Chi tiết tại [report/team/bang_chi_phi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_chi_phi.md).
- **Nhiệm vụ B (Phân tích độ nhạy - CP2):** Đánh giá 9 kịch bản biến thiên thông số. Khảo sát hàm mục tiêu toàn hệ thống để chỉ ra điểm cân bằng tối ưu giữa tỷ lệ retry của AI và chi phí nhân viên làm thay.
- **Nhiệm vụ C (Kiểm soát lỗi - CP3):** Hai thành viên độc lập gán nhãn 20 ca lỗi theo 5 nhóm Google PAIR, đạt đồng thuận 100%. Xây dựng cơ chế phát hiện tự động qua telemetry và chỉ định vai trò chịu trách nhiệm tại [report/team/bang_loi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot - CP4):** Thiết kế kế hoạch thử nghiệm trong [report/team/pilot_plan.yaml](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/pilot_plan.yaml) phân nhóm theo nhân viên (20 control vs 20 treatment), điều chỉnh MDE lên 6 điểm để giải quyết bài toán thiếu mẫu phân cụm; thiết lập 3 luật dừng 4 vế có ngưỡng và thẩm quyền rõ ràng.
- **Nhiệm vụ E (Hồ sơ launch v0 - CP5):** Đặc tả 10 event có `trace_id` tại [report/team/chi_so.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md) và đúc kết hồ sơ 1 trang tại [report/team/ho_so_launch_v0.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** Đạt **4.472 đ** [simulated] (gấp 16,3 lần hoá đơn token 274,7 đ; thời gian nhân viên chiếm 92,5% tổng chi phí).
- **Phạm vi hiệu quả:** `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69× so với 12.000 đ) đem lại hiệu quả vượt trội. Cắt bỏ `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×).
- **Tối ưu toàn hệ thống:** Giới hạn 2 lần chạy là rẻ nhất cho công ty (**6.901.220 đ**), dù giới hạn 1 lần có chi phí agent thấp nhất (4.111 đ).
- **Cảnh báo xem lại 100%:** Nếu duy trì xem lại 100%, chi phí tăng lên **11.743 đ – 12.415 đ** [simulated] (0,98×–1,03×), triệt tiêu hoàn toàn lợi nhuận AI.
- **Đề xuất cuối cùng tại Gate 2a:** **Go có điều kiện** (kèm 4 điều kiện: sửa lỗi hoàn tiền trùng ca 20, sửa đối soát sổ cái ca 7, phê duyệt đánh đổi MDE 6 điểm với power 64,2%, và triển khai lộ trình giảm xem lại theo bậc).

## 5. Khó khăn và cách xử lý

- *Khó khăn 1:* Môi trường Python ban đầu thiếu các thư viện chuyên sâu về thống kê (`statsmodels`, `scipy`). Nhóm đã xử lý nhanh bằng cách cấu hình môi trường ảo `.venv` thông qua công cụ `uv` với tốc độ cao, cài đặt chuẩn xác `requirements.txt` và xác minh bằng unit test.
- *Khó khăn 2:* Cột `quyet_dinh_xem_lai` chứa các ô trống bị pandas tự động chuyển thành `NaN` nếu đọc thông thường. Nhóm đã kịp thời xử lý bằng cờ `keep_default_na=False` theo đúng hướng dẫn kỹ thuật để đảm bảo các phép so sánh chuỗi chính xác.
- *Khó khăn 3:* Bài toán cỡ mẫu theo cụm nhân viên ($m=75$) đòi hỏi 84 nhân viên, vượt quá quy mô 40 nhân sự của công ty. Nhóm đã chủ động phân tích trade-off và đề xuất tăng MDE lên 6 điểm ($m \ge 299$ yêu cầu/nhân viên), đồng thời thẳng thắn công bố rủi ro suy giảm Statistical Power xuống 64,2% trước hội đồng.

## 6. Tổng hợp đóng góp

- **Nguyễn Trọng Hưởng (25%):** Hoàn thành 100% mã nguồn `src/lab13.py`, chạy mô hình và thuật toán tính toán thống kê.
- **Lê Thành Đạt (25%):** Thực hiện tính toán đối chứng độc lập, điền và rà soát bảng chi phí & độ nhạy `bang_chi_phi.md`.
- **Trần Minh Tân (25%):** Gắn nhãn độc lập 20 ca lỗi, xây dựng biện pháp khắc phục 5 ca đại diện `bang_loi.md`.
- **Phạm Ngọc Trung Quân (25%):** Gắn nhãn độc lập, hoàn thiện cấu trúc `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`.
*(Chi tiết từng hạng mục đóng góp được ghi nhận tại `TEAM.md`).*

## 7. Hạn chế và hướng cải thiện

- *Hạn chế:* Các con số về thời gian xem lại và làm lại hiện tại vẫn là dữ liệu giả lập (`_simulated`), chưa phản ánh hoàn toàn tác động từ giao diện và độ trễ phản hồi của nhân viên thực tế.
- *Hướng cải thiện:* Ngay khi bước vào giai đoạn rollout 0.10 của kế hoạch pilot, nhóm sẽ sử dụng dữ liệu đo thực tế từ event `staff_review_decision` và `staff_rework_completed` để tái hiệu chỉnh mô hình kinh tế.

## 8. Tài liệu tham khảo

- Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*, pair.withgoogle.com.
- Tài liệu statsmodels: `statsmodels.stats.power.NormalIndPower` & `proportion_effectsize`.
