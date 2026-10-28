# Quy trình tạo ảnh và kể chuyện

## Khóa brief và nguồn

Trước sản xuất lưu: modelId/strictLookId, bé nào/đôi nào, ảnh gốc mặt/toàn thân/vải, ảnh nền thật và nguồn/quyền sử dụng, dịp, insight (nguồn hay giả thuyết), mục tiêu cảm xúc, hành động cụ thể, đạo cụ, số ảnh/cỡ cảnh và file nhận xét hiện hành. Đọc source-model-registry ở dự án nếu có bản mới; bản đóng gói chỉ là snapshot27/10.

Lập bảng từng khung: `frameId | vai trò | hành động/ánh nhìn | đạo cụ & tay tiếp xúc | cỡ cảnh | nguồn người/vải | nền thật | rủi ro cần soi`. Giữ strictLook và danh tính cho cả bộ. Tránh5tư thế đứng giống nhau dù đổi địa điểm.

## Quy trình concept 0–9 từ cẩm nang dự án

0. Insight: hoàn cảnh mua, mong muốn/băn khoăn, điều muốn lưu giữ; giả thuyết ghi rõ, không bịa dữ liệu khách.
1. Tư liệu: concept, bối cảnh thật, hành động theo độ tuổi và đạo cụ cho từng hành động. Chọn ảnh nguồn phù hợp, có nguyên liệu cho tay/chân/vải.
2. Thử3–5hướng khi phát triển concept. Ahimum có thể truyền thống hóa concept hiện đại hoặc hiện đại hóa truyền thống; dùng ngôn ngữ nghệ thuật hỗ trợ câu chuyện.
3. Sửa đúng nguyên nhân; thiếu tư liệu thì bổ sung. Không cứ đẻ thêm batch cùng lỗi.
4. Chốt board: story, biểu tượng, màu/ánh sáng, hành động/đạo cụ, nguồn và một ảnh chuẩn. Thử nhóm toàn–trung–cận trước mở rộng, trừ khi người dùng yêu cầu fullset để review.
5. Tạo ảnh lẻ có mã `{model}-{occasion}-{concept}-{action}-{wide|medium|close}-{version}`. Sản xuất theo số lượng brief, chia lượt nếu công cụ giảm chất lượng. Không ép hành động không đọc được ở cận.
6. QC từng ảnh >85/nohardreject, người phụ trách xem lại bằng ảnh gốc và bản xuất thật.
7. Với bài tổng chuẩn5ảnh: đề xuất10cách sắp5khung (có thể dùng sơ đồ, không cần render10bộ). Với album20ảnh, dựngnhịp20 theo brief thay vì ép5; chia đoạn câu chuyện, không kéo dài bằng crop lặp.
8. Dàn ảnh lẻ từ nguồn native, chữ Sarabun cho nội dung dễ đọc và The Nautigal cho nhấn cảm xúc khi hợp; không phải ảnh nào cũng có chữ. Kiểm dấu, crop, thứ tự, màu.
9. Cover/caption kết nối hành động thật với sản phẩm. Không claim đọc/mở/trao nếu hình không có; thông tin giá/vải/ưu đãi cần xác nhận.

## Nền thật: điều kiện chọn và ghép

Đọc/xem ảnh nền thật trước. Lưu nguồn cụ thể và tên địa điểm có bằng chứng; nếu chỉ biết một con phố thì không đặt tên landmark. Tư liệu địa điểm/“hot” có thể thay đổi: kiểm nguồn hiện hành khi đề xuất và chỉ nói hot nếu có bằng chứng, không suy từ trang giới thiệu du lịch.

Chọn nền có góc máy/ngang tầm mắt, mặt sàn, đường chân trời, phối cảnh và hướng sáng tương thích với ảnh người. Đổi nền sai góc rồi cố blur không sửa được. Ánh sáng nắng gắt/âm trời/giờ xanh phải đồng nhất trên mặt, vải, chân và background. Kiểm tỷ lệ trẻ so cửa/ghế/lan can; màu phản xạ gần sàn/tường, mép tóc, contact shadow, phản chiếu mặt kính/nước, độ hạt/độ nét/DOF. Biển/du thuyền không tự có sàn đất hay bóng tường đỏ; gió và vật cầm phải cùng logic.

Ảnh ghép hoặc ảnhAI có thamchiếu địađiểm thật phải ghi đúng phươngpháp. Chỉ gọi “nền dùng ảnh chụp thật” nếu thực sự giữ nền chụp thật; không gọi “chụp tại” khi chỉ compositing. Không hứa pixel0 cho file JPEG có nén.

## Phụ kiện hợp background và câu chuyện

Đạo cụ đi sau dịp/hành động, không theo thói quen model. Giỏ/quạt trong ảnh gốc không mặc định hợp biển/du thuyền hay đámcưới. Chọn vật vừa tuổi, đúng quy mô và chất liệu, có lý do dùng; nếu muốn thay mà tay không tương thích, chọn nguồn/tư thế khác hoặc một hành động không cần cầm. Không nhét đạo cụ cho đủ5ảnh. Tết và cưới có tín hiệu văn hóa phù hợp, không chỉ đỏ/vàng; cảnh biển có hoạt động và phụ kiện biển hợp trang phục, không bịa sự kiện.

Tay cầm: ngón cái đối các ngón, có vùng che khuất và áp lực; kẹp giấy có độ dày/mép gấp; quai giỏ có điểm nối, lực kéo và hướng rơi; thân giỏ/nắp không tan/lệch. Tải nặng ảnh hưởng cổ tay/tay/đứng. Tay chỉ/chạm/cầm khác nhau, caption theo đúng hành động.

## Nghệ thuật mà vẫn thật

Nghệ thuật đến từ lựa chọn khoảnh khắc, bố cục, liên hệ hình dạng/motif, màu, ánh sáng và nhịp câu chuyện, không bắt buộc đồ trang trí AI. Khi cần một concept nghệ thuật riêng: thử3hệ thị giác, mỗi hệ có một cơ chế liên kết sảnphẩm–khônggian–cửchỉ; chọn1hệ đủ nguồn và chụp/ghép có thể tin được. Không dùng lại một cánh giấy nhỏ hay đổi màu phông để tuyên bố conceptmới. Không để nghệ thuật làm sai vải hoặc làm nền thật thành CGI. Khi có xungđột, giữ tiêu chí thật/đúngsảnphẩm và sửa artdirection.

## Cách sản xuất và giới hạn

- Mặc định thao tác theo công cụ người dùng chọn. ChatGPTtask phải nhận cả các ảnh gốc/đặc tả khóa/ảnh vải/nền thực có thể truy cập, không chỉ lời nhắc “giống ảnh gốc”. Đối soát đầu ra từng task, không tạo/gửi lặp khi task đang chạy.
- Ghép bảo toàn nguồn phù hợp khi người dùng chọn. Với pose mới doAI tạo, bảo toàn danh tính và sảnphẩm bằng ref mạnh và QC; ghi regeneratedregions, không tự gọi ảnh người gốc/pixel0. Nếu phạmvi hiện hành chỉcho ghép người/áo thật, không sinh tay/người mới để lách.
- Phân biệt thiếu nguyên liệu thật với công cụ không đạt. Tìm toàn kho nguồn được phép, đổi khung/tình huống/cỡcảnh vẫn giữ story; nếu vẫn thiếu báo đúng ảnh/vùngcần bổsung, không tựhạtiêuchuẩn.
- Không upscale để tạo chi tiết vải không có. Không sửa rách bằng cách phát minh thiết kế; nếu người dùng yêu cầu retouch riêng thì lưu bản riêng và ghi vùng sửa, không dùng bản retouch làm nguồnchấtliệu chuẩn.
