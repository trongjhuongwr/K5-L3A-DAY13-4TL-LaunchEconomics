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
|   2 | Lê Thành Đạt | 2A202603579 | dat.ltforwork@gmail.com / 26ai.datlt7@vinuni.edu.vn | datlt203357 | Người kiểm số (Number verifier) |
|   3 | Trần Minh Tân | 2A202603688 | minhtantran.contact@gmail.com | minhtantran99 | Người gắn nhãn 1 (Labeler 1) |
|   4 |        |      |       |        | Người gắn nhãn 2 kiêm giữ hồ sơ (Document keeper) |

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

## TranMinhTan-2A202603688

### Phần việc phụ trách

- Người gắn nhãn 1 (Labeler 1): Phụ trách đọc kỹ đề bài, giám sát và bảo đảm thỏa mãn tất cả các điều kiện "Xong khi" của 5 checkpoint; chủ trì gắn nhãn độc lập 20 ca lỗi ở CP3 theo khung 5 loại lỗi của Google PAIR; đối soát đồng thuận nhãn với Người gắn nhãn 2 (Phạm Ngọc Trung Quân); xây dựng các quy tắc phân biệt cho ca dễ lẫn và lập bảng biện pháp khắc phục định lượng cho 5 ca mẫu; đồng thời kiểm tra chéo các điều kiện tiên quyết (tuyệt đối không dùng từ cấm về môi trường vận hành thực tế, bảo đảm gắn nhãn giả lập [simulated]).

### Đóng góp cụ thể

- Gắn nhãn độc lập toàn bộ 20 ca lỗi trong tài liệu đề bài vào 5 nhóm Google PAIR trong 8 phút (Nhãn người 1): Do người dùng (4 ca: 1, 6, 9, 14), Hệ thống (5 ca: 2, 7, 8, 15, 20), Ngữ cảnh (4 ca: 3, 10, 16, 18), Giới hạn hệ thống (4 ca: 4, 11, 13, 19), Ngầm (3 ca: 5, 12, 17).
- Tiến hành đối soát với Người gắn nhãn 2 (Quân), đạt tỷ lệ đồng thuận tuyệt đối 20/20 (100% ≥ 80%).
- Đúc kết 5 quy tắc phân biệt chuẩn xác cho các ca dễ lẫn (ca 6, 9, 13, 8, 15, 18, 12) dựa trên nguyên tắc gắn nhãn theo nguyên nhân gốc, không theo nơi sửa lỗi.
- Xây dựng bảng khắc phục cho 5 ca mẫu đại diện cho 5 loại lỗi (Ca 9, 7, 18, 4, 17) với đầy đủ cơ chế phát hiện định lượng đo lường được (tên event, ngưỡng số học, chu kỳ quét) và phân định rõ 1 vai trò chịu trách nhiệm duy nhất (PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng; tuyệt đối không ghi "cả đội").
- Soát lỗi toàn bộ thư mục `report/team/` xác nhận không vi phạm từ cấm và các quy định liêm chính học thuật.

### Bằng chứng

- File bảng lỗi hoàn chỉnh: [report/team/bang_loi.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/bang_loi.md).
- Kết quả đối soát nhãn: 20/20 ca trùng khớp (tỉ lệ đồng thuận 100%).
- File báo cáo cá nhân: [report/team/2A202603688_TranMinhTan.md](file:///h:/VinAI/K5-L3A-DAY13-4TL-LaunchEconomics/report/team/2A202603688_TranMinhTan.md).

---

## LeThanhDat-2A202603579

### Phần việc phụ trách

- Người kiểm số: đối chiếu kết quả `src/lab13.py` với công thức và số tham chiếu; kiểm tra các phép tính chi phí, chi phí cả hệ thống và kịch bản B4.

### Đóng góp cụ thể

- Kiểm tra A1 đạt 1,20; 1,25; 1,25 và rà phép tính A2: 4.373.585 / 978 ≈ 4.472 đ mỗi việc thành công (có chi phí dựa trên dữ liệu simulated).
- Xác nhận ở B3, giới hạn 2 lần có tổng chi phí hệ thống thấp nhất (6.901.220 đ simulated), còn giới hạn 1 lần có CPS trợ lý thấp nhất (4.111 đ simulated); cập nhật cách ghi nhãn để phân biệt hai tiêu chí.
- Đối chiếu B4: 11.173.313 / 900 = 12.414,79 đ; thống nhất hiển thị 12.415 đ khi làm tròn đến đồng gần nhất và đồng bộ số trong hướng dẫn.

### Bằng chứng

- Output chạy `src/lab13.py`; cập nhật trong `report/team/bang_chi_phi.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Báo cáo cá nhân: `report/team/2A202603579_LeThanhDat.md`.
