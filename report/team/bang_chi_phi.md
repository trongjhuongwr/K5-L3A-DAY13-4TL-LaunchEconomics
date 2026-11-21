# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | ... |
| Số lần chạy trung bình, chạy đến khi đúng | ... |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | ... |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | ... | `logix_runs.csv` | đo từ trace |
| Tool | ... | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | ... | attempt lớn hơn 1 | đo từ trace |
| Xem lại | ... | `phut_xem_lai_simulated` | simulated |
| Làm lại | ... | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | ... | | |
| Số việc thành công | ... | `ket_qua` | |
| Chi phí mỗi việc thành công | ... | | |
| Hoá đơn token và tool chia cho số yêu cầu | ... | | |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? ...
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? ...

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | ... | ... | ... | ... | ... |
| hang_nang | ... | ... | ... | ... | ... |
| quoc_te | ... | ... | ... | ... | ... |
| doi_tac | ... | ... | ... | ... | ... |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? ...

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | ... | ... | ... | ... |
| Một nửa khối lượng | ... | ... | ... | ... |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? ...

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated; CPS trợ lý thấp nhất) |
| 2 lần | 4.093.220 đ (simulated) | 234 | **6.901.220 đ (simulated; tổng hệ thống thấp nhất)** | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn **2 lần** rẻ nhất cho công ty (**6.901.220 đ simulated**); giới hạn **1 lần** có CPS trợ lý thấp nhất (**4.111 đ simulated**). Hai tiêu chí không trùng nhau.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% trong `noi_dia` + `hang_nang`: **11.743 đ simulated (0,98×)** nếu làm lại 9 phút; **12.414,79 đ simulated**, tức **12.415 đ (1,03×)** khi dùng 15,3 phút/ca.
- Ở 15,3 phút, CPS cao hơn baseline **12.000 đ**; pilot cần đo thời gian thật và xác định mức xem lại an toàn đủ thấp để duy trì hiệu quả kinh tế.
