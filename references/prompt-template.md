# Prompt giao tạo ảnh (điền và đính kèm ảnh)

Dùng trênChatGPT hoặc côngcụ người dùng chọn. Mỗiảnhlàfile riêng; sốlượng theo brief, không dùngcontactsheet thayđầura. Không tự tạo tác vụ mới khi chưa được yêu cầu.

```text
AHIMUM — ẢNH CHỤP THẬT, ĐÚNG NGƯỜI, ĐÚNG SẢN PHẨM

Đầu ra: [số] ảnh lẻ, tỷ lệ/kíchthước theo [kênh]; phiênbản[mã].
Mục tiêu: [dịp/câu chuyện/cảm xúc]. Insight: [nguồn hoặc giảthuyết].
Model/strictLook: [Lxx/..]; nhânvật: [béđỏ/béxanh/cả2theonguồn].

ĐÍNH KÈM (phải xem được):
A. Ảnhgốc người+trangphục: [fileID/tên + vai trò từngảnh].
B. Cậnvải/kếtcấu đúnglook: [file + ghi chú cổ/gấu/vân/độrủ/motif].
C. Ảnhchuẩnđộthật: [file01..05], chỉhọc ánhsáng, da, camera, cảm xúc.
D. NềnẢNHCHỤPTHẬT: [file/tênnguồn/địađiểmxácminh + góc/hướngsáng].
Không dùngC làmnguồn SKU/vải; không tựdựng landmark từ tênrồi gọi lànền thật.

KHÓA SẢN PHẨM:
[Danh tính; cổ; gấu; chiều dài tay/thân; cúc; motif; trâm/tua;
 màu; độrủ/vân/ánh; quần; dép/giày; phối riêng từngbé].
Khôngsuyđoán thànhphầnvải. Khôngtrộn look, khônggiảm2béthành1.

KHUNG HÌNH:
[ID | vaitrò story | hànhđộng/ánhnhìn/biểucảm | đạo cụ & grip |
 cỡcảnh | nguồn người/vải | nền | rủiroQC].
[Hệpalette/ánhsáng/biểutượng gắn sảnphẩm; sựkhácnhau có ýnghĩa].

PHƯƠNG PHÁP:
[Ghépbảotoànngười/áothật khiđượcchọn; hoặc vùngđượcphépsinhảnh].
Giữngười/vải/motif đãkhóa. Ghi rõ vùngsinh/ghép; khôngtựclaimRGB0.
Nềnthật phải ăn camera/perspective/scale/light/shadow/DOF/noise của người.
Phụkiện hợp nơi/dịp/tuổi/hànhđộng. Đừng thayvật cầm nếu taynguồnkhônghợp.
Khôngskinplastic, khôngvânvảiAI đều/sắcgiả, khônghalo/blurđồngloạt.
Khôngthêmghim/rách/sứtchỉ/đếbụcvà khôngretouchbịa sảnphẩm đểche nguồnxấu.
Nếu nguồncó góc hỏng/nhìn hỏng, đổi nguồn/góc sạch giữđúnglook.

CHẤT ẢNH NHƯ MÁY ẢNH:
Ghi điều kiện chụp nhất quán với ảnh nền: góc máy, khoảng cách, hướng/độ mềm
của ánh sáng, mặt phẳng nét và độ sâu trường ảnh. Không dùng “8K, ultra-real”
thay mô tả vật lý. Không tự thêm rim light, HDR, blur nền, hạt nhiễu hay da bóng.
Giữ biểu cảm tự nhiên: mắt–má–miệng chuyển động cùng nhau, răng và tuổi đúng.
Vải rủ/kéo/nén theo tư thế nhưng giữ đúng màu, vân, ánh và thiết kế từ ref.
Không thêm vân sắc hoặc lỗ chân lông giả để tạo cảm giác nét.
Thử vài khung đại diện cho nhóm biểu cảm/tư thế của brief, kiểm face/product/
fabric/hand contact trước mở rộng. Không lấy một pose đạt để chứng nhận pose khác.
Ghi vùng tái tạo, giới hạn nguồn và cổng photographic_realism có bằng chứng.
Nếu vẫn lộ AI, giữ needs-fix hoặc đổi nguồn/phương pháp, không nâng điểm cho đủ.

QC VÀ BÀN GIAO:
Xemtoànảnh5giây/50% và100–200%mặt,tay,đạocụ,vải,quần,giàydép,tiếpđất,nền.
Mỗiảnh>85/nohardreject; sai chi tiết hoặc nhìn giả thì sửa/loại dùđiểmcao.
Khôngchấm chỉ từthumbnail, không tựcoilàNhànduyệt.
Xuấtfileảnhlẻthật +caption +nguồn/crop/phươngpháp/prompt/hash +10điểm/QC.
Nếu thiếunguồn/ảnhkhôngtruycậpđược, nêu đúngfile/vùng cònthiếu và xửlý,
khônglấy ảnhbịbác hay scorecũ để đếmđủ sốlượng.
```

## Prompt kiểm độc lập

“Kiểm từng file xuất và các nguồn đínhkèm theo quality-review.md. Nêu assetID+vùng+evidence, tách lỗi nguồn với lỗi sinh/ghép, không dùng báo cáo producer thay việc xem. Trả10điểm, hardgates,3lỗi cần sửa, selfQCstatus; đối chiếu mặt/strictLook/vải, back ảnhthật, đạo cụhợpcảnh và tiếp xúc, quần/dép. Điểm>85 không bù lỗi bắtbuộc. Báo đúng sốpass, chưa đủ thì giữhold.”
