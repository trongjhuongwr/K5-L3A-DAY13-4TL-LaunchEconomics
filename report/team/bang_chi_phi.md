# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | **1,20 lần** (Công thức: $1 + (1 - p) = 1 + 0,2 = 1,20$) |
| Số lần chạy trung bình, chạy đến khi đúng | **1,25 lần** (Công thức: $1 / p = 1 / 0,8 = 1,25$) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | **1,25 lần** (Công thức: $(1 + 0,2 + 0,04) / (1 - 0,2^3) = 1,24 / 0,992 = 1,25$) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 đ | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 đ | Tổng 5 khoản trên | có thành phần simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 đ | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"?
  Gấp **16,3 lần** (4.472 đ / 274,7 đ = 16,28×); hoá đơn chỉ là phần nổi của tảng băng vì chưa tính chi phí nhân viên.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm?
  **Thời gian nhân viên chiếm 92,5% tổng chi phí** (Làm lại chiếm lớn nhất với **51,8%** tương ứng 2.264.000 đ; Xem lại chiếm **40,7%** tương ứng 1.780.000 đ; còn token và tool chỉ chiếm 7,5%).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không?
  **Loại `quoc_te` không đáng xử lý** vì CPS tới 22.515 đ (đắt 1,88× so với người làm 12.000 đ); chạy lại tới 3 lần **không giúp** vì tỉ lệ thành công giảm mạnh theo từng attempt (lần 1: 30%, lần 2: 11,4%, lần 3 chỉ 2,2%).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 việc | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng | 16.875 việc | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào?
  **Không đổi kết luận.** Ở cả 45.000 YC/tháng (4.599 đ = 0,38×) và một nửa khối lượng 22.500 YC/tháng (5.784 đ = 0,48×), chi phí vẫn thấp hơn rất nhiều mức 12.000 đ; chỉ khi dưới 4.656 việc/tháng mới hòa vốn cố định.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | -5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | -8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (simulated), tăng +46,3%**; mức tăng bằng đúng tổng hai kịch bản đơn lẻ (5,6% + 40,7%), chứng minh mô hình có tính cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** ($\pm 51,8\%$) · 2. **Tỉ lệ xem lại** ($\pm 40,7\%$) · 3. **Lương nhân viên** ($+23,1\%$). Giá token chỉ xếp thứ tư ($\pm 5,6\%$).

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
