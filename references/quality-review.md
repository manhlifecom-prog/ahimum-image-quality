# QC ảnh Ahimum

## Thứ tự

1. 5giây toànảnh: cảm giác ảnh chụp hay CGI? Ghi AI suspicion0–10, nguyênnhân thấyđược. Cần cân bằng tự nhiên, không cố tạo bẩn/hỏng để chứngminh thật.
2. 50%: người, sản phẩm, bố cục, nền/khônggian/ánh sáng, tỷ lệ và lực lớn.
3. Native100–200%: cận mặt/mắt/răng/tai/tóc; mọi tay, quai, giấy, nút, khóa, đường may, vân vải, motif, quần, dép/đế/chân, contactshadow, biên ghép/reflect/text.
4. Đối chiếu cạnh ảnhgốc đúnglook, ảnhvải và nềnnguồn. Ghi rõ lỗi có sẵn trongnguồn, lỗi ghép/sinh hoặc chưa đủ bằngchứng. Nguồn thật không tự làm cropđẹp.
5. Xem toànbộ: nhấtquán người/mẫu/vải/màu/ánhsáng/camera, hànhđộng/đạo cụ lặp, mạch kểchuyện. Lỗi lặp là vấnđề hệthống, sửa master/prompt trước batch.

## Hard reject / cổng bắt buộc

- HR1 Anatomy: thừa/thiếu/dính ngón, sai khớp, mắt/răng/da nhựa rõ, bàn tay không cấu trúc.
- HR2 Identity: đổi mặt/tuổi/tỷ lệ rõ, cặp hai bé mất một người, mặt đồng nhấtAI thay người nguồn.
- HR3 Product: sai cổ/gấu/tay/cúc/motif/tua/màu/phối, vải từ rủ mềm thành cứng hoặc hoa nhỏ đều; thiếu nguồn không được đánh PASS. Nếp gấp/khe xẻ là kết cấu thật thì mô tả đúng, nhưng góc quảngcáo trôngrách vẫn needs-fix/source-reselect.
- HR4 Physics: cầm không chạm, vật xuyên, quai không có điểm nối, thiệp mất lực/kíchthước, quần/đế/chân biến dạng, thiếu trọng lượng/tiếp đất, bóng/reflection sai lớn.
- HR5 Text/logo: sai chữ/chữ giả khi có chữ; dàn chữ riêng nếu tool không giữ được. Không có chữ vẫn ghi đãkiểmkhôngchữ, không bỏ vùng.
- HR6 ObviousAI: nền nhựa/giả/landmark bịa, da porcelain, mắt kính đồng loạt, vật liệu/camera quá synthetic hoặc artifact rõ.
- Cổng riêng dựán: back phải dùng nền ảnh chụp thật khi brief yêu cầu, phụkiện đúngdịp/địađiểm/hànhđộng; trangphục phù hợp quảngcáo, không chọn góc nhìn đứtrách/hỏng. Cổng thiếu xácminh giữ NEEDS-CHECK, không PASS.

Chỉ một lỗi bắt buộc là FAIL/HOLD dù99điểm. Không lấy điểmđẹp để bù lỗi mặt/tay/vải. Không bỏ lỗi vì chúng có sẵn trong ảnh nguồn.

## Thang10thànhphần /100

Theo prompt chấm điểm dựán (Doc1KAlcGBP1NZbynwA9W0PCUnLLZd55jPNQWITWhKqGjC4):

| Thành phần | Tối đa |
|---|---:|
| Human realism & anatomy |15|
| Identity consistency |10|
| Product fidelity |20|
| Material & texture |10|
| Lighting & shadow |10|
| Physics & contact |10|
| Camera realism |10|
| Environment & props |5|
| Art direction & variety |5|
| Brand & set consistency |5|

90–100 tựQChero/campaigncandidate; 86–89 tựQCsocialcandidate;85khôngqua yêu cầu >85;80–84cầnsửa;70–79nênsinh/chụplại;<70loại. Các nhãn này khôngphải humanapproval hay quyềnđăng. Không nângđiểm vì béxinh, màuđẹp, scene sang. 95+chỉ khi mọi yếu tố thuyếtphục, không tự cho cảbatch.

Chỉ báo PhotographicEntropy0–10 không cộng vào100: độ bất quy tắc tự nhiên của tóc, vải, môi trường, biểu cảm. Không cố làm hỏng đồ/da/bẩnảnh để tăngentropy. AI suspicion cũng là chỉbáo, không thay hardgates.

## Phiếu từng ảnh

`assetId/version/hash; model/strictLook; ảnhnguồn/vải/nền; phươngpháp/vùngsinh; điểm10mục+total; hardgates pass/fail/needs-check với evidence; cậnQC đãxem;3lỗi lớn nhất (nếu có); điểmgiữlại; AI suspicion/entropy; reviewer/time; quyếtđịnh.`

Quyếtđịnh một trong: SELF-QC-PASS / NEEDS-FIX / NEEDS-CHECK / REGENERATE / REJECTED. Chấm lại sau sửa, hashmới. Nghi vấn chưa thấy rõ khôngkhẳngđịnh lỗiAI; ghi cầnkiểmtra. Nhàn/Mạnhduyệt riêng đúngasset/version/hash/caption/concept và bằng chứng, không tự điền approval.

## Các ca kiểm thử ra quyết định

-86/100nhưngquai giỏ xuyên tay →REJECTED, không SELF-QC-PASS.
-94/100nhưng nền sinhAI từ tênđịađiểm, brief yêu cầu backthật →NEEDS-FIX; tìmảnhnền thật.
-90/100, thayL01-AkhuyếtV bằngcổcúcL01-B →REJECTEDproduct.
-Cropđúngpixelnguồnnhưng kheáo trông rách/quầnméo →đổi góc/nguồn, khôngpass vìRGB0.
-NguồnL01-B có cúc cổ thật →giữ, không tựxoácúc để bắtchướcL01-A.
-5ảnhmới chỉđổi nền/cropcùngpose →không gọi5concept/hànhđộng, quaylạistoryboard.
-Người thậtghép vào ảnhHàNộithật nhưng hướngsáng/mặtđất sai →NEEDS-FIX, nguồnthật chưađủ.
-Đãnhận/reaction/duyệtvải ởbảncũ →khônghumanapprovedfilemới.


## Cổng độ thật như máy ảnh

Áp dụng camera-realism.md trước khi tổng điểm. Hồ sơ ghi photographic_realism pass/fail/needs-check với bằng chứng toàn ảnh và các vùng khó, kèm nhóm biểu cảm/tư thế và nguồn vải. Không chỉ kiểm ngón đúng số: da nhựa, nét mặt đóng băng, vật liệu sai nếp, bóng CGI, nền blur vô lý hoặc biên ghép vẫn không đạt. Không có prompt hay điểm detector nào bảo đảm đúng mọi tư thế/biểu cảm. File mới hoặc nhóm pose mới đều cần xem lại.
