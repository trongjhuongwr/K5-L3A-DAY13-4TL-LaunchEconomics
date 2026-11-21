# Báo cáo nhóm · 4TL · Gate 2a Dossier

Báo cáo ngắn tóm tắt toàn bộ hồ sơ thẩm định kinh tế và kế hoạch thử nghiệm pilot (Gate 2a) cho trợ lý hoàn phí LogiX-VN.

## 1. Thông tin nhóm

- **Tên nhóm:** 4TL
- **Lớp:** L3A
- **Repo nhóm:** `K5-L3A-DAY13-4TL-LaunchEconomics` (URL: `https://github.com/trongjhuongwr/K5-L3A-DAY13-4TL-LaunchEconomics.git`)
- **Nhánh nộp:** `main`
- **Thành viên & Vai trò (xem chi tiết tại [TEAM.md](../../TEAM.md)):**
  1. Nguyễn Trọng Hưởng (2A202603607) - Người viết code (Code author)
  2. Lê Thành Đạt (2A202603579) - Người kiểm số (Number verifier)
  3. Trần Minh Tân (2A202603688) - Người gắn nhãn 1 (Labeler 1)
  4. Phạm Ngọc Trung Quân (2A202603626) - Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper)

## 2. Mục tiêu và cách tiếp cận

- **Mục tiêu:** Xây dựng hồ sơ thẩm định kinh tế vòng Gate 2a nhằm quyết định có cấp phép thử nghiệm thực địa có đối chứng (pilot) cho trợ lý AI hoàn phí LogiX-VN hay không.
- **Cách tiếp cận:**
  - Không nhìn nhận chi phí đơn thuần từ hoá đơn API/token (274,7 đ/yêu cầu), mà mô hình hoá toàn diện **Chi phí cho mỗi việc thành công (Cost of Pass - CPS)** bao gồm cả chi phí công cụ, chạy lại, nhân viên xem lại và làm lại.
  - Phân rã dữ liệu theo 4 nhóm yêu cầu nghiệp vụ để xác định biên độ an toàn kinh tế, loại bỏ các phân khúc gây lãng phí.
  - Thiết kế thực nghiệm pilot ngẫu nhiên phân cụm (Cluster-RCT) theo nhân viên CSKH nhằm tránh hiện tượng rò rỉ tri thức (contamination), đồng thời tính toán cỡ mẫu và Statistical Power để bảo đảm độ tin cậy khoa học.
  - Thiết lập ma trận quan sát telemetry, luật dừng tự động 4 vế và quy trình phục hồi khẩn cấp bảo vệ an toàn vận hành.

## 3. Giải pháp từng nhiệm vụ (A–E)

- **Nhiệm vụ A (Mô hình chi phí & Phạm vi):** 
  - Lập trình hàm `mo_hinh` trong [src/lab13.py](../../src/lab13.py) tính toán từ 1.200 trace yêu cầu giả lập.
  - Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md): Tổng chi phí 4.373.585 đ chia cho 978 ca thành công cho ra CPS = **4.472 đ [simulated]** (gấp 16,3 lần hoá đơn token). Thời gian nhân viên chiếm tới 92,5% tổng chi phí.
  - Xác lập phạm vi kinh tế (A3): Thu hẹp pilot chỉ nhận `noi_dia` (CPS 2.696 đ = 0,22× baseline) và `hang_nang` (CPS 8.221 đ = 0,69× baseline). Cắt bỏ hoàn toàn `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×, tỷ lệ thành công attempt 1 chỉ 51,5%).
- **Nhiệm vụ B (Phân tích độ nhạy & Bài toán toàn hệ thống):**
  - Xây dựng 9 kịch bản độ nhạy (B1), chứng minh tính cộng tuyến tính (B2): biến thiên nhân sự chi phối áp đảo, giá token chỉ ảnh hưởng $\pm 5,6\%$.
  - Giải quyết bài toán giới hạn số lần chạy (B3): Giới hạn 2 lần chạy là phương án rẻ nhất cho cả hệ thống công ty (**6.901.220 đ [simulated]**), giải tỏa xung đột mục tiêu cục bộ của giới hạn 1 lần (CPS trợ lý 4.111 đ nhưng xả 319 ca cho nhân viên gánh, tổng chi phí vọt lên 7.449.781 đ).
  - Phân tích rủi ro xem lại 100% (B4): Đẩy chi phí lên **12.414,79 đ ≈ 12.415 đ [simulated]** (1,03× baseline) khi thời gian làm lại là 15,3 phút, đắt hơn người tự làm (12.000 đ).
- **Nhiệm vụ C (Phân loại lỗi Google PAIR & Biện pháp khắc phục):**
  - Chi tiết tại [bang_loi.md](bang_loi.md): Hai người gắn nhãn độc lập hoàn thành 20 ca lỗi với tỷ lệ đồng thuận tuyệt đối 100% (20/20).
  - Đúc kết 5 quy tắc phân biệt ca dễ lẫn (theo nguyên nhân gốc, không theo nơi sửa) và lập bảng khắc phục 5 ca mẫu với ngưỡng định lượng, event đo lường cụ thể và 1 vai trò chịu trách nhiệm duy nhất (không ghi "cả đội").
- **Nhiệm vụ D (Kế hoạch thử nghiệm pilot):**
  - Hoàn thiện cấu hình chuẩn tại [pilot_plan.yaml](pilot_plan.yaml).
  - Giải bài toán phân cụm D1: 20 nhân viên/nhóm với ICC = 0,02 dẫn đến trần cỡ mẫu hiệu dụng $n_{\text{eff}} = 1.000 < 1.251$ (không thể phát hiện chênh lệch 5 điểm ở power 80%). Nhóm đề xuất đánh đổi kỹ thuật nâng MDE lên 6 điểm ($n=859$, $m \ge 299$, tổng 5.980 YC/nhóm, $DE=6,96$), chấp nhận power = 64,2% nếu hiệu ứng thực tế là 5 điểm.
  - Thiết lập 3 luật dừng 4 vế (NẾU – TRONG – THÌ – KHÔNG THÌ), cơ chế rollback 30 phút và quy trình vận hành chi tiết.
- **Nhiệm vụ E (Đặc tả chỉ số, Rủi ro & Hồ sơ launch):**
  - Chi tiết tại [chi_so.md](chi_so.md) và [ho_so_launch_v0.md](ho_so_launch_v0.md).
  - Xác lập 3 chỉ số hiện trạng E1: Chỉ số chính = 82,83%, Chỉ số dùng = 27,12%, Chỉ số an toàn = 4,25% (trong pilot là 3,97%). Xây dựng 10 telemetry event chuẩn liên kết bằng `trace_id`.
  - Phân tích 3 rủi ro kinh tế trọng yếu E2 và hoàn thiện hồ sơ launch v0 đúng 1 trang 7 mục.

## 4. Kết quả & Đề xuất cuối cùng

- **Đề xuất của nhóm tại Gate 2a:** **GO CÓ ĐIỀU KIỆN (CONDITIONAL GO)**.
- **Căn cứ từ các con số cốt lõi:**
  1. *Lợi ích kinh tế rõ rệt trong phạm vi thu hẹp:* CPS của phân khúc `noi_dia` là 2.696 đ (tiết kiệm 77,5%) và `hang_nang` là 8.221 đ (tiết kiệm 31,5% so với baseline 12.000 đ).
  2. *Bảo đảm an toàn toàn hệ thống:* Giới hạn chạy tối đa 2 lần giúp tối ưu hóa tổng chi phí công ty ở mức 6.901.220 đ [simulated].
- **4 Điều kiện tiên quyết bắt buộc để khởi chạy:**
  1. *Khoanh vùng phạm vi:* Chỉ nhận đơn `noi_dia` và `hang_nang`; 100% đơn `quoc_te` và `doi_tac` chuyển thẳng cho nhân viên.
  2. *Khống chế tỷ lệ xem lại:* Duy trì tỷ lệ xem lại chọn lọc ở mức $\le 20\%$. Tuyệt đối không áp dụng chính sách xem lại 100% vì sẽ làm chi phí đội lên 12.415 đ [simulated], gây lỗ so với nhân viên tự làm.
  3. *Cấu hình hệ thống:* Ghim cứng tham số `max_retries = 2`.
  4. *Kích hoạt hàng rào bảo vệ tự động:* Duy trì 3 luật dừng tự động và quy trình rollback về trạng thái thủ công hoàn toàn trong vòng 30 phút nếu vi phạm ngưỡng an toàn tài chính hoặc chất lượng dịch vụ.

## 5. Khó khăn và cách xử lý

1. **Xung đột chỉ số ở B3:** Lúc đầu xuất hiện mâu thuẫn giữa việc giới hạn 1 lần có CPS trợ lý rẻ nhất (4.111 đ) nhưng chi phí cả hệ thống lại đắt (7.449.781 đ). Nhóm đã làm rõ bài toán tối ưu tổng thể của doanh nghiệp: giới hạn 2 lần giúp giảm số lượng yêu cầu hỏng giao cho người từ 319 xuống 234 ca, tiết kiệm hơn 548.000 đ cho toàn công ty.
2. **Rào cản trần cỡ mẫu hiệu dụng ở D1:** Thiết kế phân cụm 20 nhân viên gặp trần $n_{\text{eff}} = 20 / 0,02 = 1.000$, không thể đạt power 80% với MDE 5 điểm. Nhóm đã tính toán lại và đưa ra phương án đánh đổi kỹ thuật nâng MDE lên 6 điểm, minh bạch chỉ số statistical power (64,2%) cho hội đồng ra quyết định.
3. **Thống nhất độ chính xác làm tròn ở B4:** Nhóm đã đối soát chi tiết phép tính $11.173.313 / 900 = 12.414,7922\dots$ đ, làm rõ sự khác biệt giữa làm tròn đến đồng gần nhất (12.415 đ) và cắt phần thập phân (12.414 đ) để bảo đảm tính nhất quán dữ liệu xuyên suốt các báo cáo.

## 6. Tổng hợp đóng góp thành viên

- Toàn bộ 4 thành viên hoàn thành 100% vai trò, phối hợp qua quy trình Git flow chuyên nghiệp (tạo nhánh, mở PR, review và merge vào `main`).
- Chi tiết đóng góp, tỷ lệ hoàn thành và bằng chứng nghiệm thu của từng cá nhân được ghi nhận đầy đủ tại [TEAM.md](../../TEAM.md) và các báo cáo cá nhân:
  - [2A202603607_NguyenTrongHuong.md](2A202603607_NguyenTrongHuong.md) (Code author - 100%)
  - [2A202603579_LeThanhDat.md](2A202603579_LeThanhDat.md) (Number verifier - 100%)
  - [2A202603688_TranMinhTan.md](2A202603688_TranMinhTan.md) (Labeler 1 - 100%)
  - [2A202603626_PhamNgocTrungQuan.md](2A202603626_PhamNgocTrungQuan.md) (Document keeper - 100%)

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Cỡ mẫu phân cụm tại đợt pilot v0 còn bị khống chế bởi số lượng 20 nhân viên CSKH/nhóm, khiến statistical power bị hạn chế nếu hiệu ứng cải thiện chỉ ở mức nhỏ (5 điểm). Ngoài ra, tỷ lệ lỗi Do người dùng (4/20 ca) và Ngữ cảnh (4/20 ca) còn khá cao do khách hàng nhập nhầm mã sàn TMĐT hoặc khiếu nại do chưa hiểu rõ công thức trừ khấu hao.
- **Hướng cải thiện:**
  - Mở rộng số lượng nhân viên tham gia thử nghiệm ở các giai đoạn tiếp theo hoặc áp dụng kỹ thuật stratified randomisation theo thâm niên/hiệu suất nhân viên để giảm hệ số tương quan nội cụm (ICC).
  - Triển khai giải pháp nhận diện định dạng mã sàn TMĐT tự động tra cứu mã vận đơn nội bộ (khắc phục ca 9) và bổ sung chi tiết công thức tính bồi hoàn minh bạch vào nội dung tin nhắn gửi khách hàng (khắc phục ca 18).

## 8. Tài liệu tham khảo

1. Google PAIR (People + AI Research) Guidebook: *Errors + Failing Gracefully & Feedback + Control*.
2. VinAI Research & Education: *Lab 13 - Gate 2a: Pricing Agent & Pilot Planning (Launch Economics)*.
3. Tài liệu mô tả quy trình vận hành và chính sách bồi hoàn LogiX-VN.
