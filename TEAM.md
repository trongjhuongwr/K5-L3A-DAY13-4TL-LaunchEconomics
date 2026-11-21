# Team

## Thông tin nhóm

- Tên nhóm: 4TL
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-4TL-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Trọng Hưởng | 2A202603607 | nguyentronghuong05@gmail.com | trongjhuongwr | Người viết code (Code author) |
|   2 | Lê Thành Đạt | (thành viên tự điền) | (thành viên tự điền) | (thành viên tự điền) | Người kiểm số (Number verifier) |
|   3 | Trần Minh Tân | (thành viên tự điền) | (thành viên tự điền) | (thành viên tự điền) | Người gắn nhãn 1 (Labeler 1) |
|   4 | Phạm Ngọc Trung Quân | (thành viên tự điền) | (thành viên tự điền) | (thành viên tự điền) | Người gắn nhãn 2 kiêm giữ hồ sơ (Labeler 2 & Document keeper) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603607_NguyenTrongHuong.md`.

---

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

- File code: `src/lab13.py`.
- Output console chạy lệnh `python lab13.py` in đầy đủ bảng số liệu khớp 100% đáp án chuẩn.
- File báo cáo cá nhân: `report/team/2A202603607_NguyenTrongHuong.md`.

---

## LeThanhDat-MSSV

### Phần việc phụ trách

- Người kiểm số (Number verifier): Tính tay độc lập các con số, đối chiếu sai số < 2%, điền bảng chi phí và độ nhạy `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Tính toán độc lập đối chiếu bảng A2, A3, A4 và B1, B2, B3, B4.
- Trả lời các câu hỏi phân tích kinh tế B3 và B4.

### Bằng chứng

- File `report/team/bang_chi_phi.md`.

---

## TranMinhTan-MSSV

### Phần việc phụ trách

- Người gắn nhãn 1 (Labeler 1): Gắn nhãn độc lập 20 ca lỗi theo Google PAIR, giám sát điều kiện nghiệm thu "Xong khi".

### Đóng góp cụ thể

- Bộ nhãn độc lập 1 cho 20 ca lỗi CP3.
- Xây dựng bảng khắc phục cho 5 ca lỗi đại diện.

### Bằng chứng

- File `report/team/bang_loi.md`.

---

## PhamNgocTrungQuan-MSSV

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ (Labeler 2 & Document keeper): Gắn nhãn độc lập 20 ca lỗi, phụ trách `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Bộ nhãn độc lập 2 cho 20 ca lỗi CP3, đối soát tỷ lệ đồng thuận.
- Hoàn thiện kế hoạch `pilot_plan.yaml`, 10 event có `trace_id` trong `chi_so.md`.
- Chắp bút hồ sơ duyệt Gate 2a trong `ho_so_launch_v0.md`.

### Bằng chứng

- Các file: `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
