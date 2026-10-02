# 5 Tại sao

Khi xử lý các vấn đề hàng ngày, chúng ta thường rơi vào vòng tuần hoàn "chữa cháy chứ không chữa gốc": chúng ta sửa một vấn đề, nhưng không lâu sau, vấn đề đó lại tái diễn theo cách tương tự hoặc gần giống. Điều này thường xảy ra vì chúng ta chỉ xử lý các **triệu chứng bề nổi** của vấn đề, chứ chưa chạm đến **nguyên nhân gốc rễ** dẫn đến nó. **5 Tại sao** là một kỹ thuật **Phân tích nguyên nhân gốc (RCA)** cực kỳ đơn giản nhưng lại rất sâu sắc. Phương pháp này được Sakichi Toyoda, người sáng lập tập đoàn ô tô Toyota, đề xuất và là một công cụ giải quyết vấn đề cốt lõi trong Hệ thống Sản xuất Toyota (TPS).

Ý tưởng cốt lõi của phương pháp 5 Tại sao là liên tục và lặp lại đặt câu hỏi "**Tại sao?**" về một vấn đề hiện tại, đào sâu từng lớp một, giống như bóc lớp vỏ hành tây, cho đến khi tìm ra nguyên nhân gốc rễ. Nếu nguyên nhân gốc rễ được giải quyết, vấn đề sẽ không thể tái diễn. Phương pháp này không bắt buộc phải hỏi đúng năm lần; đôi khi nguyên nhân gốc có thể được tìm thấy sau ba lần hỏi, và đôi khi có thể cần nhiều hơn. Cốt lõi nằm ở **tinh thần tìm hiểu kiên trì, không hài lòng với những câu trả lời hời hợt**. Đây là một công cụ tư duy mạnh mẽ, giúp chuyển sự tập trung của nhóm từ "Lỗi là của ai?" sang "Tại sao việc này lại xảy ra?", và từ "chữa cháy" sang "phòng ngừa".

## Chuỗi logic của phương pháp 5 Tại sao

Quy trình 5 Tại sao xây dựng một chuỗi nhân quả rõ ràng từ triệu chứng đến nguyên nhân gốc rễ. Câu trả lời cho mỗi câu hỏi "Tại sao?" sẽ trở thành chủ đề cho câu hỏi "Tại sao?" tiếp theo.

<!-- 
![The Causal Chain of 5 Whys](../../../../docs/en/Problem Solving & Decision Making/root_cause_analysis/5-Whys-Tutorial-en-diagram.png)
 -->

## Cách thực hiện phân tích 5 Tại sao

1.  **Bước 1: Thành lập nhóm, xác định vấn đề**
    *   Tập hợp một nhóm nhỏ những người trực tiếp làm việc, quen thuộc với vấn đề và ngữ cảnh của nó.
    *   Cùng nhau viết một **phát biểu vấn đề** chính xác bằng ngôn ngữ rõ ràng, khách quan. Ví dụ: "Vào lúc 10:00 sáng ngày 26 tháng 10 năm 2023, máy chủ hệ thống đơn hàng khách hàng đã sập."

2.  **Bước 2: Bắt đầu liên tục hỏi "Tại sao?"**
    *   **Tại sao đầu tiên?**: Hỏi câu hỏi "Tại sao?" đầu tiên về phát biểu vấn đề.
        *   *Câu hỏi*: "Tại sao máy chủ hệ thống đơn hàng khách hàng lại sập?"
        *   *Câu trả lời*: "Vì mức sử dụng CPU của máy chủ đạt 100%."

    *   **Tại sao thứ hai?**: Sử dụng câu trả lời trước đó làm chủ đề mới và tiếp tục hỏi.
        *   *Câu hỏi*: "Tại sao mức sử dụng CPU của máy chủ đạt 100%?"
        *   *Câu trả lời*: "Vì một truy vấn SQL trong cơ sở dữ liệu bị rơi vào vòng lặp vô hạn."

    *   **Tại sao thứ ba?**:
        *   *Câu hỏi*: "Tại sao truy vấn SQL này lại bị rơi vào vòng lặp vô hạn?"
        *   *Câu trả lời*: "Vì có lỗi logic trong truy vấn khi xử lý một loại dữ liệu người dùng đặc biệt."

    *   **Tại sao thứ tư?**:
        *   *Câu hỏi*: "Tại sao đoạn mã lỗi này lại được triển khai lên môi trường sản phẩm?"
        *   *Câu trả lời*: "Vì quy trình kiểm tra mã của chúng ta không bao quát được trường hợp kiểm thử cụ thể này."

    *   **Tại sao thứ năm?**:
        *   *Câu hỏi*: "Tại sao quy trình kiểm tra mã của chúng ta lại có sự sơ suất này?"
        *   *Câu trả lời*: "Vì chúng ta chưa thiết lập một danh sách kiểm tra **kiểm tra mã chuẩn hóa** bao gồm tất cả các mục cần kiểm tra."

3.  **Bước 3: Xác định nguyên nhân gốc rễ và đề xuất biện pháp khắc phục**
    *   **Xác định nguyên nhân gốc rễ**: Trong ví dụ trên, nguyên nhân gốc rễ được xác định là "thiếu danh sách kiểm tra mã chuẩn hóa". Đây là một vấn đề ở cấp **quy trình**. Nếu chúng ta chỉ sửa lỗi logic trong truy vấn SQL (câu trả lời cho câu hỏi "Tại sao" thứ ba), rất có thể các đoạn mã tương tự chưa được kiểm thử kỹ sẽ tiếp tục gây ra vấn đề trong tương lai.
    *   **Đề xuất biện pháp khắc phục**: Xây dựng một biện pháp sửa lỗi cụ thể, có thể thực hiện được cho nguyên nhân gốc rễ. Ví dụ: "Trưởng nhóm kỹ thuật sẽ chịu trách nhiệm tạo danh sách kiểm tra mã chuẩn hóa, bao gồm hiệu năng cơ sở dữ liệu, bảo mật và kiểm thử điều kiện biên, trong tuần này, và tất cả các nhóm phải tuân thủ trong tương lai."

## Các trường hợp áp dụng

**Trường hợp 1: Sự ăn mòn của bức tường đá ở Đài tưởng niệm Jefferson ở Washington D.C.**

*   **Vấn đề**: Các bức tường đá của đài tưởng niệm bị ăn mòn nghiêm trọng.
*   **Tại sao? (1)** Vì nhân viên vệ sinh sử dụng quá thường xuyên các loại hóa chất tẩy rửa có độ mạnh cao để lau rửa tường.
*   **Tại sao? (2)** Vì mỗi ngày có rất nhiều phân chim bám trên tường, khiến việc lau rửa thường xuyên là cần thiết.
*   **Tại sao? (3)** Vì có rất nhiều chim én tụ tập quanh đài tưởng niệm, kiếm ăn các con nhện sinh sản ở đó.
*   **Tại sao? (4)** Vì rất nhiều con nhện bị thu hút bởi ánh sáng của đài tưởng niệm, thích tụ tập ở nơi sáng để giăng mạng vào buổi chiều tối.
*   **Tại sao? (5)** Vì hệ thống ánh sáng của đài tưởng niệm được bật sớm một tiếng trước khi mặt trời lặn.
*   **Nguyên nhân gốc rễ**: Cài đặt thời gian bật đèn của hệ thống ánh sáng không phù hợp.
*   **Giải pháp**: Điều chỉnh hệ thống ánh sáng của đài tưởng niệm để bật sau khi mặt trời lặn. Thay đổi đơn giản này theo hướng quy trình đã giải quyết triệt để vấn đề ăn mòn bức tường đá.

**Trường hợp 2: Một vũng dầu trên sàn nhà máy**

*   **Vấn đề**: Có một vũng dầu trên sàn nhà máy.
*   **Tại sao? (1)** Vì khớp nối ống dẫn dầu của một máy bị rò rỉ.
*   **Tại sao? (2)** Vì vòng đệm ở khớp nối ống dẫn dầu đó bị cũ và nứt.
*   **Tại sao? (3)** Vì công ty mua một lô vòng đệm giá rẻ, chất lượng thấp.
*   **Tại sao? (4)** Vì chính sách mua hàng của công ty chỉ yêu cầu "giá thấp nhất là trúng thầu".
*   **Tại sao? (5)** Vì hiệu quả làm việc của bộ phận mua hàng chỉ được đánh giá dựa trên số tiền họ "tiết kiệm" được cho công ty, mà không liên quan đến chất lượng và tuổi thọ của các phụ tùng.
*   **Nguyên nhân gốc rễ**: Hệ thống đánh giá hiệu quả làm việc của bộ phận mua hàng không hợp lý.
*   **Giải pháp**: Sửa đổi chính sách mua hàng và hệ thống đánh giá để đưa vào hệ thống đánh giá chất lượng nhà cung cấp, độ tin cậy và chi phí dài hạn.

**Trường hợp 3: Một học sinh thi trượt môn cuối kỳ**

*   **Vấn đề**: Tiểu Minh thi trượt môn toán cuối kỳ.
*   **Tại sao? (1)** Vì cậu ấy chỉ bắt đầu ôn tập vào tuần cuối trước kỳ thi, điều này không đủ thời gian.
*   **Tại sao? (2)** Vì cậu ấy không hiểu nhiều nội dung được giảng dạy trên lớp.
*   **Tại sao? (3)** Vì cậu ấy luôn chơi điện thoại trong giờ học và không thể tập trung.
*   **Tại sao? (4)** Vì cậu ấy cơ bản là không thích môn toán và không có hứng thú với nó.
*   **Tại sao? (5)** Vì hồi trung học cơ sở, cậu ấy từng bị một giáo viên phê bình nặng nề sau khi thi trượt môn toán, điều này đã tạo ra bóng đen tâm lý và nỗi sợ môn toán.
*   **Nguyên nhân gốc rễ**: Những trải nghiệm học tập tiêu cực ban đầu dẫn đến rào cản tâm lý.
*   **Giải pháp**: Có thể cần tư vấn tâm lý và xây dựng lại sự tự tin, đồng thời khơi gợi lại hứng thú với môn toán bằng cách bắt đầu với những kiến thức cơ bản hơn, nơi cậu ấy có thể trải nghiệm thành công.

## Ưu điểm và thách thức của phương pháp 5 Tại sao

**Ưu điểm cốt lõi**

*   **Đơn giản và dễ sử dụng**: Không yêu cầu công cụ thống kê phức tạp hay kiến thức chuyên môn; bất kỳ nhóm nào cũng có thể bắt đầu nhanh chóng.
*   **Đi đến tận gốc rễ**: Giúp các nhóm vượt qua các triệu chứng bề nổi của vấn đề để tìm ra các giải pháp then chốt có thể giải quyết vấn đề một cách căn bản.
*   **Khuyến khích thấu hiểu, không đổ lỗi**: Chuyển sự tập trung từ "ai đã mắc sai lầm" sang "tại sao quy trình lại cho phép sai lầm xảy ra", giúp xây dựng văn hóa giải quyết vấn đề lành mạnh, tập trung vào vấn đề.

**Thách thức tiềm ẩn**

*   **Có thể có nhiều nguyên nhân gốc rễ**: Với các vấn đề phức tạp, nguyên nhân gốc rễ có thể không đơn nhất mà là một hệ thống liên kết. Trong trường hợp này, phương pháp 5 Tại sao có thể đơn giản hóa quá mức vấn đề.
*   **Phụ thuộc vào kiến thức của người tham gia**: Độ sâu của phân tích phụ thuộc rất nhiều vào việc nhóm tham gia hiểu rõ quy trình và tình huống thực tế.
*   **Có thể dừng giữa chừng**: Nhóm có thể dừng việc hỏi "Tại sao?" sau khi tìm được một nguyên nhân có vẻ hợp lý nhưng chưa phải là nguyên nhân gốc rễ nhất.

## Mở rộng và liên kết

*   **Sơ đồ xương cá (Ishikawa)**: Khi một vấn đề có thể do nhiều nguyên nhân khác nhau, song song từ nhiều lĩnh vực, một sơ đồ xương cá có thể được sử dụng trước để hệ thống hóa việc suy nghĩ và tổ chức tất cả các nguyên nhân tiềm năng. Sau đó, phương pháp 5 Tại sao có thể được sử dụng để đào sâu vào các nguyên nhân đáng ngờ nhất.
*   **Sản xuất tinh gọn (Lean Production)** và **Six Sigma**: Phương pháp 5 Tại sao là một trong những công cụ phổ biến và cơ bản nhất để phân tích nguyên nhân gốc rễ trong cả hai phương pháp cải tiến chất lượng và vận hành này.

---
*Tham khảo nguồn: Phương pháp 5 Tại sao, như một trong những nền tảng của Hệ thống Sản xuất Toyota (TPS), được Sakichi Toyoda sáng tạo và Taiichi Ohno phổ biến trong các tác phẩm của ông. Đây là một biểu hiện cốt lõi của văn hóa giải quyết vấn đề và cải tiến liên tục trong tư duy tinh gọn.*