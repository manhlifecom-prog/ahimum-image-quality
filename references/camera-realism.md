# Độ thật như ảnh máy ảnh: quy trình theo tư thế, biểu cảm và chất liệu

## Mục tiêu và giới hạn

Ảnh phải thuyết phục như một lần bấm máy: người, vải, vật cầm, nền và ánh sáng cùng tồn tại trong một không gian. “Photorealistic”, tên máy, tên ống kính hoặc “8K” không chứng minh điều này. Không bảo đảm mọi tư thế/biểu cảm hoặc chất liệu sẽ đúng chỉ từ một ảnh; cần đủ nguồn và thử thực tế. Không thêm EXIF/chứng nhận chụp thật, không gọi người được chụp ở địa điểm khi ảnh là tổng hợp.

Tách hai chế độ:
- **Giữ ảnh người/trang phục gốc:** giữ chi tiết đã có trong vùng bảo toàn, nhưng không có quyền suy ra biểu cảm, góc khuất hay tư thế chưa được chụp. Chất lượng vẫn phụ thuộc nguồn và hòa cảnh; RGB0 không tự làm ảnh đẹp/thật.
- **Tạo tư thế hoặc biểu cảm mới, khi phạm vi cho phép:** có vùng tái tạo, nguy cơ đổi mặt/cổ/vải/nếp tăng; dùng bộ ref đúng look và kiểm từng ảnh. Nếu phạm vi chỉ cho ghép người/áo thật, tìm pose nguồn khác hoặc báo thiếu nguồn, không tự vẽ tay/người mới.

## 1. Bộ khóa tham chiếu có thể dùng được

Xem và đánh dấu vai trò từng ảnh, không nhét lẫn tất cả vào một prompt:
- Danh tính: mặt trực diện, ba phần tư, nghiêng và các biểu cảm nguồn có sẵn; mắt, miệng, má, tai, đường tóc theo chính bé. Không dùng ảnh AI mặt đẹp thay nguồn người.
- Trang phục: toàn thân trước, góc bên/lưng nếu có, đường cổ/gấu/xẻ/cúc, quần, giày dép. Cặp hai bé có ref riêng từng người và cách phối.
- Vải: cận native đủ rõ; cùng loại vải ở vùng phẳng, nếp gấp và vùng bắt sáng. Đánh dấu tỷ lệ vân, hướng vân, độ bóng, độ trong/đục, dày/mỏng biểu kiến và độ rủ. Không suy thành phần sợi.
- Hành động: ref tư thế/hành động phù hợp độ tuổi, quần áo và vật cầm. Ref hành động chỉ định chuyển động, không được mang theo mặt hoặc bộ đồ của người khác.
- Cảnh: ảnh chụp nền thật, mặt sàn, góc máy, hướng sáng, tỷ lệ và chỗ đủ cho hành động.

Chỉ dùng ref thực sự truy cập/xem được. Thiếu góc sản phẩm thì tìm trong kho gốc được phép, hoặc chọn tư thế có đủ bằng chứng; không bịa thiết kế mặt sau/góc khuất. Không ép một số ảnh nguồn cố định nếu ít hơn đã đủ cho nhiệm vụ đơn giản.

## 2. Lập bảng thử biểu cảm × tư thế

Mỗi khung ghi: nhân vật, strictLook, biểu cảm/hướng nhìn, pose/tải trọng, vật cầm, góc máy, phần sản phẩm nhìn thấy, nguồn từng phần và rủi ro.

Các nhóm cần thử khi xuất hiện trong brief:
- Mặt yên / cười nhẹ / cười mở miệng hoặc nói / tò mò / nhìn xuống / nhìn nghiêng. Trẻ không cần làm đủ nhóm nếu câu chuyện không yêu cầu.
- Đứng / bước / ngồi hoặc cúi / đưa hoặc cầm vật / tương tác hai người. Không tự thêm pose khó chỉ để đủ ma trận.

Bắt đầu với vài khung đại diện có rủi ro cao của chính brief, kiểm cả mặt và vải. Chỉ mở rộng nhóm đã qua. Một nụ cười đạt không chứng minh ảnh nói/cười lớn cũng đạt; đứng đạt không chứng minh ngồi/cúi/cầm vật cũng đạt. Không nhân bản cùng khuôn mặt cười lên nhiều pose.

Kiểm biểu cảm: khóe mắt–má–miệng chuyển động cùng nhau; hàm/răng không thành dải trắng; hướng đồng tử phù hợp; độ tuổi và cấu trúc khuôn mặt giữ đúng, không làm mặt người lớn thu nhỏ.

Kiểm pose: trọng tâm/hông/vai/chân có lực đỡ, các khớp nối được; tay phải có nhiệm vụ rõ; hai bé chạm nhau có vùng che khuất và phản ứng tự nhiên. Vải kéo/rủ/nén theo pose chứ không giữ cùng nếp dán lên mọi tư thế.

## 3. Duy trì đúng chất liệu khi đổi pose

Lưu “fabric fingerprint” bằng ảnh đối chiếu và mô tả ngắn: màu trong điều kiện ánh sáng đã biết; tỷ lệ/hướng vân; vùng bóng không đều; độ mềm/rủ; mật độ nếp; chi tiết hoa văn và đường may. Nó là tài liệu đối chiếu, không phải chứng nhận mô hình giữ vải.

- Ở vai/khuỷu/gối/gấu: nếp hình thành theo lực và chỗ tỳ, có vùng căng xen vùng rủ. Không tạo vân nhăn nhỏ đều trên toàn áo.
- Khi đổi ánh sáng: highlight có thể đổi nhưng vật liệu không tự biến thành cotton khô, satin nhựa, gấm cứng hay hoa văn khác. So thêm ảnh nguồn ở ánh sáng tương tự nếu có; đừng làm phẳng sáng để che sai.
- Họa tiết nằm trên bề mặt vải và biến dạng liên tục theo nếp, không nổi như decal hoặc trôi khỏi đường ráp. Không suy mất họa tiết do nếp che là lỗi nếu ảnh nguồn giải thích được.
- Cận sản phẩm dùng crop native thực sự đủ rõ. Không sharpening/upscale sinh vân để đáp ứng yêu cầu “siêu nét”.
- Nếu không chắc độ rủ/vân/màu có đúng không, ghi needs-check, dùng góc có nguồn chắc hơn hoặc bổ sung ảnh, không tự cho product/material pass.

## 4. Một không gian và một lần chụp hợp lý

Mô tả điều kiện chụp có lý do thay vì dồn tên máy/thông số:
- Góc máy, khoảng cách, phối cảnh phù hợp trẻ và ảnh nền; không góc rộng méo tay/chân trừ khi chủ đích và vẫn giữ đúng sản phẩm.
- Mặt phẳng nét và độ sâu trường ảnh nhất quán; hai bé cùng khoảng cách không một bé nét như dao còn bé kia mờ không lý do. Không blur mọi nền thành kem; nền thật có chi tiết, khoảng xa và nhiễu hợp nguồn.
- Ánh sáng có hướng và độ mềm giải thích được: catchlight, bóng mũi/cằm, nếp vải, vật cầm, bóng chân và reflection cùng logic. Không tự thêm rim light vàng mọi cảnh.
- Màu da không trắng sứ, vùng tối không bị HDR nâng phẳng, bão hòa không gắt đều. Giữ chất ảnh nguồn, không ép hạt nhiễu/viền tím/vignette như bộ lọc “giả ảnh máy”.
- Da có chuyển sắc và vi chi tiết vừa mức độ phân giải; không thêm lỗ chân lông giả lên da trẻ. Tóc có sợi và khoảng rối tự nhiên; mắt ướt vừa phải, không thủy tinh phát sáng.
- Mọi tay–vật–quai–giày–sàn có tiếp xúc, che khuất, bóng nhỏ và lực hợp lý. Không sửa một bàn tay đẹp nhưng làm mất quai hoặc làm sản phẩm biến dạng.

Không tự làm bẩn/rách/nhăn quá mức, không làm hỏng dép để ảnh “thật hơn”. Bất quy tắc tự nhiên khác lỗi sản phẩm.

## 5. Sửa có kiểm soát, không tăng sinh hàng loạt cùng lỗi

Phân loại lỗi trước: sai nguồn/look; ref thiếu; pose quá khó; vải bị mô hình tái tạo sai; ánh sáng/phối cảnh không hòa; chi tiết bị hỏng ở xuất file.

Sửa phần nhỏ nhất phù hợp với phạm vi được cho phép, giữ nguyên file gốc/version và chấm lại file xuất mới. Sau sửa tay phải kiểm lại vải và vật cầm; sau sửa vải phải kiểm lại thiết kế/mặt. Không dùng cùng pass cho file sửa.

Nếu cùng lỗi xuất hiện ở các bản thử kế tiếp mà nguyên liệu/phương pháp không đổi, dừng mở rộng batch, đổi ảnh nguồn/pose/cảnh/phương pháp hoặc báo rõ cần nguồn nào. Không hứa một lượt nữa sẽ chắc chắn đúng. Không chặn một cách làm khác có bằng chứng tốt hơn chỉ vì master ban đầu dùng cách cũ.

## 6. Cổng photographic_realism riêng, trước điểm tổng

Ghi pass/fail/needs-check cùng bằng chứng cho: cảm giác toàn ảnh; biểu cảm/danh tính; quang học/ánh sáng; vật liệu theo pose; tiếp xúc/khối lượng; hòa người–nền; tính nhất quán cả bộ. Chỉ pass khi đã xem đủ toàn ảnh và cận khó, không có dấu hiệu synthetic rõ hoặc nghi vấn bắt buộc chưa giải quyết.

So cạnh ảnh chuẩn ở kích thước hiển thị tương đương, không để ảnh mẫu thumbnail che độ giả của file mới. Nếu người xem dễ nhận ra da nhựa, biểu cảm đóng băng, vải hoa nhỏ lặp, ánh sáng CGI, biên ghép hoặc vật cầm vô lực thì fail dù không có lỗi giải phẫu lớn. Ảnh đẹp không phải ảnh thật.

Điểm >85 và mọi hard gate vẫn áp dụng; camera realism không thay product fidelity, và ngược lại. AI suspicion/entropy là nhận xét phụ có lý do, không phải máy phát hiện AI hoặc xác suất khoa học. Không đặt ngưỡng “detector score” để chứng nhận ảnh thật.

Hồ sơ phải ghi rõ: nhóm biểu cảm/pose đã thử, ref vải, vùng tái tạo, kết quả và phần chưa đủ nguồn. “Đạt cho nhóm này” không thành “đúng mọi biểu cảm và tư thế”.
