# Team

## Thông tin nhóm

- Tên nhóm: 4TL
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-4TL-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Trọng Hưởng | 2A202603607 | nguyentronghuong05@gmail.com | trongjhuongwr | Người viết code (Code author) |
|   2 |        |      |       |        | Người kiểm số (Number verifier) |
|   3 |        |      |       |        | Người gắn nhãn 1 (Labeler 1) |
|   4 | Phạm Ngọc Trung Quân | 2A202603626 | trungquana123@gmail.com | jadenphm29 | Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603607_NguyenTrongHuong.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenTrongHuong-2A202603607

### Phần việc phụ trách

- Người viết code (Code author): Chịu trách nhiệm chính về toàn bộ mã nguồn `src/lab13.py` (A1, A2, A3, A4, B1, B2, B3, B4, D1, E1).

### Đóng góp cụ thể

- Hoàn thiện 3 hàm A1 đạt chuẩn 100% ba phép thử (1,20 · 1,25 · 1,25).
- Xây dựng hàm `mo_hinh` tính toán CPS từ trace và log giả lập: 4.472 đ [simulated].
- Lập trình phân loại A3 (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`) và chi phí cố định A4.
- Lập trình 9 kịch bản độ nhạy B1, chứng minh tính cộng tuyến tính B2, giải bài toán chi phí toàn hệ thống B3 và kịch bản xem lại 100% B4.
- Lập trình tính toán cỡ mẫu phân cụm D1 và tính Statistical Power bằng `statsmodels`.
- Tính 3 chỉ số đo lường hiện trạng E1.

### Bằng chứng

- File code: [src/lab13.py](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/src/lab13.py).
- Output console chạy lệnh `python lab13.py` in đầy đủ bảng số liệu khớp 100% đáp án chuẩn.
- File báo cáo cá nhân: [report/team/2A202603607_NguyenTrongHuong.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/2A202603607_NguyenTrongHuong.md).

---

## PhamNgocTrungQuan-2A202603626

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper): Phụ trách chính Nhiệm vụ C (Gắn nhãn độc lập 20 ca lỗi Google PAIR & xây dựng bảng khắc phục), Nhiệm vụ D (hoàn thiện file cấu hình thực nghiệm `pilot_plan.yaml`), Nhiệm vụ E (đặc tả chỉ số E1, 10 event telemetry, phân tích rủi ro kinh tế E2, và hoàn thiện Hồ sơ launch v0 tại Gate 2a).

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi theo phân loại Google PAIR, đạt tỉ lệ đồng thuận tuyệt đối 100% (20/20 ca) với Người gắn nhãn 1. Soạn thảo quy tắc phân biệt cho 5 ca dễ nhầm lẫn và thiết lập bảng khắc phục 5 ca mẫu với ngưỡng định lượng và vai trò chịu trách nhiệm cụ thể.
- Hoàn thiện kế hoạch thực nghiệm [report/team/pilot_plan.yaml](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/pilot_plan.yaml), giải chi tiết bài toán cỡ mẫu phân cụm D1 và kiểm tra tính tách biệt tác động D2. Thiết lập 3 luật dừng chuẩn cú pháp 4 vế (NẾU - TRONG - THÌ - KHÔNG THÌ), cơ chế rollback 30 phút và loại bỏ 100% dấu `?`.
- Đặc tả 3 chỉ số hiện trạng E1 (Chính 82,83%, Dùng 27,12%, An toàn 4,25%), đề xuất thêm 2 chỉ số mới, xây dựng danh mục 10 telemetry event chuẩn có `trace_id` kèm ma trận kiểm tra chéo tại [report/team/chi_so.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md).
- Phân tích 3 rủi ro kinh tế trọng yếu E2 từ bảng độ nhạy kèm biện pháp ứng phó định lượng.
- Hoàn thiện Hồ sơ launch v0 [report/team/ho_so_launch_v0.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/ho_so_launch_v0.md) đúng 1 trang tóm tắt 7 mục, gắn nhãn `[simulated]` minh bạch, đưa ra đề xuất Go có điều kiện kèm 4 điều kiện ràng buộc bảo vệ an toàn tài chính và vận hành.

### Bằng chứng

- File bảng lỗi: [report/team/bang_loi.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_loi.md)
- File kế hoạch pilot: [report/team/pilot_plan.yaml](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/pilot_plan.yaml)
- File chỉ số & telemetry: [report/team/chi_so.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/chi_so.md)
- File hồ sơ launch: [report/team/ho_so_launch_v0.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/ho_so_launch_v0.md)
- File báo cáo cá nhân: [report/team/2A202603626_PhamNgocTrungQuan.md](file:///E:/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/2A202603626_PhamNgocTrungQuan.md)

---

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

