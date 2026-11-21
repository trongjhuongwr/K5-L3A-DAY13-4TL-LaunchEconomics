# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | Tổng 4 khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 đ ÷ 978 việc | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 đ + 84.000 đ) ÷ 1.200 | đo từ trace |

- **Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"?**
  Chi phí mỗi việc thành công (4.472 đ [simulated]) gấp **16,3 lần** hoá đơn token và tool chia số yêu cầu (274,7 đ).
- **Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm?**
  Thời gian nhân viên chiếm tới 92,5% tổng chi phí; trong đó khoản lớn nhất là **làm lại chiếm 51,8%** (2.264.000 đ [simulated]), tiếp theo là **xem lại chiếm 40,7%** (1.780.000 đ [simulated]).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- **Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không?**
  Loại `quoc_te` không đáng xử lý vì chi phí mỗi việc lên tới 22.515 đ (1,88× nhân viên, chỉ thành công 27,3%); chạy lại tới 3 lần không giúp vì tỉ lệ đúng giảm mạnh qua từng lần thử (lần 1: 30%, lần 2: 11,4%, lần 3: chỉ 2,2%).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- **Chi phí cố định có đổi kết luận không? Ở khối lượng nào?**
  Chi phí cố định không làm đổi kết luận ở cả hai mức khối lượng (đều rẻ hơn nhiều so với 12.000 đ, đạt 0,38× và 0,48× [simulated]); tuy nhiên khi khối lượng giảm một nửa thì phần chi phí cố định tăng gấp đôi (từ 1.185 đ lên 2.370 đ/việc).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- **Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi:**
  Chi phí mỗi việc tăng lên 6.543 đ (+46,3% [simulated]), đúng bằng tổng hai tác động riêng lẻ (+5,6% và +40,7%) do mô hình cộng tuyến tính.
- **Xếp hạng ba yếu tố ảnh hưởng mạnh nhất:**
  1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%). Giá token chỉ đứng thứ 4 (+5,6%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ (RẺ NHẤT) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- **Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không?**
  Giới hạn 2 lần chạy là rẻ nhất cho công ty (6.901.220 đ); không trùng với giới hạn cho chi phí mỗi việc thấp nhất (1 lần chạy: 4.111 đ) vì giới hạn 1 lần đẩy thêm 85 việc sang nhân viên làm tay, làm tốn thêm 1.020.000 đ của hệ thống.

## B4 · Nếu phải xem lại tất cả

- **Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ:**
  Chi phí mỗi việc thành công tăng vọt lên 11.743 đ = 0,98× (với 9 phút làm lại) và lên tới 12.415 đ = 1,03× (với 15,3 phút làm lại thực tế dữ liệu) [simulated], tức đắt hơn nhân viên tự làm.
- **Kết quả này nói gì về thứ pilot cần học được?**
  Pilot phải học được cách giảm an toàn tỉ lệ xem lại xuống dưới 50% theo bậc tin cậy và rút ngắn thời gian mỗi lượt xem lại xuống $\le 4,8$ phút; nếu duy trì xem lại 100% thì trợ lý không đem lại lợi ích kinh tế nào.
