# Ahimum Image Quality — Full Skill

Skill tạo và kiểm ảnh Ahimum: người thật, nền thật, đúng mẫu và chất liệu; tư thế, biểu cảm và phụ kiện có vật lý thuyết phục.

- [Đọc toàn bộ hướng dẫn trong một file](FULL-SKILL.md)
- [Skill entrypoint](SKILL.md)
- [Tải ZIP đầy đủ gồm 5 ảnh chuẩn và 2 mốc tư thế](ahimum-image-quality.zip)
- [Độ thật như máy ảnh, pose và biểu cảm](references/camera-realism.md)
- [Prompt tạo ảnh](references/prompt-template.md)
- [QC từng ảnh](references/quality-review.md)
- [Hai mốc tư thế được nhận xét tích cực](references/pose-realism-examples.md)
- [Khóa mẫu](references/product-locks.json)

## Sử dụng

Giải nén ZIP, đặt thư mục `ahimum-image-quality` vào thư mục skills của Codex. Gọi: `Dùng $ahimum-image-quality tạo ảnh Ahimum theo ảnh gốc và nền chụp thật, kiểm chất lượng từng ảnh.`

Trên ChatGPT: đính kèm ảnh người/trang phục/vải/nền và ảnh chuẩn cần thiết; dùng FULL-SKILL.md cùng prompt template. Đường link không tự bảo đảm mô hình đã đọc ảnh.

Mỗi ảnh >85/100 và không có lỗi bắt buộc. Cổng photographic_realism chặn ảnh còn nhìn AI dù điểm tổng cao. Không có prompt bảo đảm mọi tư thế và chất liệu; thử từng nhóm và kiểm file xuất. Script chỉ kiểm hồ sơ/hash/điểm, không tự nhìn ảnh hay chứng nhận Nhàn duyệt.

Repository public theo yêu cầu của chủ sở hữu; ai có link đều có thể đọc và tải. Không chứa credential/token hoặc nhật ký chat riêng.
