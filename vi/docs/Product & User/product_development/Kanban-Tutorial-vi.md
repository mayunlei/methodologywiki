# Kanban

Khi theo đuổi các quy trình làm việc hiệu quả và mượt mà, chúng ta thường gặp phải các vấn đề như: các công việc chất đống, không hiểu rõ mọi người đang bận gì, không xác định được điểm nghẽn, và không thể dự đoán chính xác thời gian hoàn thành. **Kanban**, một thuật ngữ bắt nguồn từ từ tiếng Nhật có nghĩa là "bảng tín hiệu", là một phương pháp **quản lý luồng công việc trực quan** mạnh mẽ và dễ hiểu được thiết kế để giải quyết các vấn đề này. Nó không phải là một khuôn khổ cứng nhắc như Scrum yêu cầu các vai trò và sự kiện cụ thể, mà là một thực hành linh hoạt thuộc phương pháp Agile, tập trung vào **tối ưu hóa hiệu quả của luồng giá trị**.

Cốt lõi của phương pháp Kanban là làm cho các quy trình và công việc trước đây vô hình trở nên rõ ràng và hoàn toàn minh bạch thông qua một **Bảng Kanban**. Sau đó, bằng cách **giới hạn số lượng công việc đang thực hiện (WIP)** và thiết lập một hệ thống **Kéo (Pull System)** rõ ràng, nó có hệ thống xác định và loại bỏ các điểm nghẽn trong quy trình, giúp giá trị di chuyển nhanh hơn, mượt mà hơn và có thể dự đoán được từ "cần làm" đến "đã xong". Mục tiêu là tạo ra một nhịp điệu làm việc ổn định và bền vững, ngăn chặn việc nhóm rơi vào tình trạng hỗn loạn và kém hiệu quả do bị quá tải công việc.

## Sáu Thực Hành Cốt Lõi Của Phương Pháp Kanban

Thành công của Kanban dựa vào việc áp dụng liên tục sáu thực hành cốt lõi sau đây.

1.  **Hình dung quy trình làm việc**: Đây là điểm khởi đầu của Kanban. Bạn cần làm việc cùng nhóm để vẽ sơ đồ tất cả các bước trong quy trình làm việc từ đầu đến cuối (ví dụ: "Cần làm", "Thiết kế", "Phát triển", "Kiểm thử", "Hoàn tất") trên bảng trắng hoặc bảng Kanban điện tử, và biểu diễn mỗi công việc (ví dụ: một câu chuyện người dùng, một lỗi) dưới dạng một thẻ trên bảng.

2.  **Giới hạn số lượng công việc đang thực hiện (WIP)**: Đây là linh hồn của Kanban. Đối với từng bước hoặc một số bước trong quy trình, hãy đặt một **giới hạn trên rõ ràng** cho số lượng công việc được phép thực hiện đồng thời. Ví dụ, quy định cột "Phát triển" chỉ được chứa tối đa 3 thẻ. Khi cột này đã đầy, không ai có thể "kéo" công việc mới từ bước trước đó cho đến khi một công việc hiện tại được hoàn tất và di chuyển ra khỏi cột. Việc giới hạn WIP **ngăn chặn việc tích tụ công việc, phơi bày các điểm nghẽn trong quy trình và tạo ra môi trường làm việc tập trung**.

3.  **Quản lý luồng công việc**: Mục tiêu của Kanban là tối đa hóa tốc độ và sự mượt mà của luồng giá trị. Bạn cần liên tục theo dõi luồng các công việc trên bảng, xác định nơi mà các công việc bị kẹt lâu nhất (tức là điểm nghẽn), rồi tập trung nguồn lực của nhóm để giải quyết các điểm nghẽn này, giúp toàn bộ hệ thống vận hành trơn tru.

4.  **Làm rõ các chính sách quy trình**: Hãy làm cho các quy tắc làm việc của nhóm rõ ràng và minh bạch. Ví dụ, rõ ràng định nghĩa thế nào là "Hoàn tất" (Definition of Done)? Giới hạn WIP cho từng hàng dọc (swimlane) là bao nhiêu? Cách xác định mức độ ưu tiên của các công việc như thế nào? Các quy tắc rõ ràng là nền tảng để nhóm làm việc tự chủ và phối hợp hiệu quả.

5.  **Thiết lập các vòng phản hồi**: Kanban khuyến khích thiết lập các vòng phản hồi với các nhịp độ khác nhau. Ví dụ, họp nhóm hàng ngày (để đồng bộ công việc hàng ngày), các cuộc họp đánh giá Kanban định kỳ (để xem xét và tối ưu hóa quy trình), và các cuộc họp đánh giá việc giao sản phẩm cho khách hàng.

6.  **Cải tiến cộng tác, tiến hóa qua thử nghiệm**: Kanban là một phương pháp khuyến khích "bắt đầu từ chỗ bạn đang đứng và tiến hóa liên tục". Nó không yêu cầu bạn thực hiện những thay đổi tổ chức mang tính đột phá. Nhóm nên liên tục và cộng tác thực hiện các cải tiến nhỏ, mang tính thử nghiệm đối với quy trình làm việc dựa trên dữ liệu và sự hiểu biết chung.

### Ví dụ về cấu trúc bảng Kanban

<!--

<!--

![Kanban Board Example](../../../../docs/en/Product & User/product_development/Kanban-Tutorial-en-diagram.png)

*   **Quy trình**: Một thẻ (biểu diễn cho một công việc) di chuyển từ trái sang phải, đi qua từng giai đoạn. Một thành viên chỉ có thể "kéo" một thẻ mới từ cột bên trái khi còn chỗ trống trong cột bên phải (tức là chưa đạt đến giới hạn WIP của cột đó).

## Cách Triển Khai Phương Pháp Kanban

1.  **Bước Một: Hình dung quy trình hiện tại**
    Đừng cố gắng thiết kế một quy trình "hoàn hảo". Hãy bắt đầu với cách bạn và nhóm bạn **đang làm việc hiện tại**. Vẽ các bước công việc thực tế lên bảng trắng và đặt tất cả các công việc đang thực hiện lên đó dưới dạng thẻ. Mục tiêu của bước này là làm cho trạng thái hiện tại trở nên minh bạch.

2.  **Bước Hai: Thiết lập giới hạn WIP ban đầu**
    Làm việc cùng nhóm để đặt giới hạn WIP ban đầu cho các bước quan trọng trong quy trình (thường là những bước dễ bị nghẽn, như "Đang thực hiện", "Đang kiểm thử"). Một điểm khởi đầu tốt có thể là "một nửa số thành viên trong nhóm" hoặc "ít hơn một chút so với số lượng công việc đang thực hiện hiện tại". Giới hạn WIP không cố định và có thể điều chỉnh sau này dựa trên tình hình thực tế.

3.  **Bước Ba: Bắt đầu "kéo" công việc**
    Thiết lập một quy tắc đơn giản: khi một thành viên hoàn tất công việc hiện tại, họ nên nhìn vào cột "bên phải nhất" trên bảng và hỗ trợ nơi cần giúp đỡ. Nếu không có gì để làm, họ có thể "kéo" một công việc ưu tiên cao nhất mới từ cột "bên trái nhất" cho phép kéo.

4.  **Bước Bốn: Thiết lập các cuộc họp hàng ngày và họp đánh giá**
    *   Tổ chức một cuộc họp ngắn hàng ngày trước bảng Kanban. Trọng tâm của cuộc họp không phải là mọi người đã làm gì, mà là **luồng di chuyển của các thẻ**: "Những thẻ nào đã di chuyển hôm qua?" "Thẻ nào bị kẹt? Làm sao để giúp chúng di chuyển?"
    *   Tổ chức các cuộc họp đánh giá định kỳ (ví dụ: hai tuần một lần) để xem xét dữ liệu trên bảng Kanban (ví dụ: "thời gian chu kỳ trung bình") và thảo luận cách cải tiến quy trình và giới hạn WIP.

## Các Trường Hợp Ứng Dụng

**Trường hợp 1: Nhóm Vận hành CNTT**

*   **Vấn đề**: Nhóm vận hành mỗi ngày đều bị ngập trong các yêu cầu khẩn cấp từ nhiều nguồn khác nhau, dẫn đến công việc hỗn loạn và phản hồi chậm trễ.
*   **Ứng dụng Kanban**: Họ thiết lập một bảng Kanban đơn giản với các hàng dọc như "Cần làm", "Đang thực hiện", "Chờ phản hồi từ bên ngoài", và "Đã giải quyết". Bằng cách giới hạn số lượng công việc trong hàng "Đang thực hiện" bằng số lượng thành viên trong nhóm, họ đảm bảo rằng nhóm có thể tập trung giải quyết các vấn đề hiện tại thay vì bắt đầu nhiều việc cùng lúc. Kanban cũng làm cho tất cả các yêu cầu trở nên minh bạch, giúp quản lý hiểu rõ khối lượng công việc thực tế của nhóm.

**Trường hợp 2: Quản lý công việc cá nhân (Kanban cá nhân)**

*   **Vấn đề**: Một cá nhân đang làm việc trên nhiều dự án cùng lúc, cảm thấy quá tải và căng thẳng.
*   **Ứng dụng Kanban**: Họ có thể sử dụng Trello hoặc một cuốn sổ tay đơn giản để tạo bảng Kanban cá nhân với các danh sách như "Mục tiêu tuần này", "Việc cần làm hôm nay", "Đang làm (WIP Limit: 1)", và "Đã xong". Bằng cách tuân thủ nghiêm ngặt giới hạn WIP là 1 cho cột "Đang làm", họ buộc bản thân phải tập trung vào một việc quan trọng nhất tại một thời điểm, cải thiện đáng kể khả năng tập trung và chất lượng công việc.

**Trường hợp 3: Nhóm sáng tạo nội dung (ví dụ: một tòa soạn tạp chí)**

*   **Quy trình**: "Ngân hàng ý tưởng" -> "Viết bài" -> "Chỉnh sửa" -> "Thiết kế/Trình bày" -> "Xuất bản."
*   **Ứng dụng Kanban**: Bằng cách đặt giới hạn WIP cho từng giai đoạn, họ có thể đảm bảo rằng các biên tập viên không tiếp tục yêu cầu viết bài khi đã có quá nhiều bản thảo tồn đọng. Điều này giúp toàn bộ quy trình sản xuất nội dung trơn tru hơn và phơi bày rõ ràng các điểm nghẽn (ví dụ: nếu cột "Chỉnh sửa" luôn đầy ắp bản thảo, điều đó cho thấy nguồn lực chỉnh sửa không đủ).

## Ưu Điểm và Thách Thức Của Phương Pháp Kanban

**Ưu điểm cốt lõi**

*   **Tính linh hoạt và thích nghi**: Không yêu cầu thay đổi mang tính đột phá đối với các quy trình và vai trò hiện có; bạn có thể "bắt đầu từ chỗ bạn đang đứng" và tiến hóa dần dần.
*   **Cải thiện hiệu quả và khả năng dự đoán**: Bằng cách quản lý luồng công việc và giới hạn WIP, nó rút ngắn đáng kể thời gian chu kỳ và làm cho thời gian giao hàng trở nên dễ dự đoán hơn.
*   **Giảm áp lực cho nhóm**: Giới hạn WIP ngăn chặn việc nhóm phải chịu áp lực lớn do làm nhiều việc cùng lúc và cam kết quá mức, tạo ra một nhịp điệu làm việc bền vững.
*   **Phơi bày các vấn đề hệ thống**: Có thể trực quan và rõ ràng phơi bày các điểm nghẽn và cản trở trong quy trình.

**Thách thức tiềm ẩn**

*   **Dễ trở thành "hình thức"**: Nếu nhóm chỉ thực hiện "hình dung hóa" mà không nghiêm túc thực hiện "giới hạn WIP" và "quản lý luồng", Kanban sẽ chỉ là một bảng công việc "đẹp mắt" và không phát huy được sức mạnh thực sự.
*   **Yêu cầu kỷ luật tự giác của nhóm**: Hệ thống kéo và giới hạn WIP đòi hỏi mức độ tự giác và tinh thần hợp tác cao từ các thành viên trong nhóm.
*   **Hiểu nhầm về "không có khung thời gian"**: Mặc dù bản thân Kanban không có các chu kỳ cố định như Scrum, nhưng điều đó không có nghĩa là không có kế hoạch và nhịp điệu. Nhóm áp dụng Kanban cũng cần ưu tiên công việc, dự báo thời gian giao hàng và tổ chức các cuộc họp đánh giá định kỳ.

## Mở rộng và Liên kết

*   **Scrum**: Kanban và Scrum là hai phương pháp phổ biến nhất trong thế giới Agile. Scrum dựa trên nhịp điệu lặp lại theo "khung thời gian", trong khi Kanban dựa trên nhịp điệu "kéo liên tục". Mỗi phương pháp đều có ưu và nhược điểm riêng, phù hợp với các tình huống khác nhau. **Scrumban** là phương pháp lai kết hợp ưu điểm của cả hai.
*   **Tư duy Lean (Lean Thinking)**: Phương pháp Kanban là ứng dụng trực tiếp và cốt lõi nhất của tư duy Lean trong công việc tri thức. Nó thể hiện hoàn hảo các nguyên tắc cốt lõi của Lean như "hình dung hóa", "hệ thống kéo", "loại bỏ lãng phí", và "cải tiến liên tục".
*   **Lý thuyết Ràng buộc (Theory of Constraints - TOC)**: Bằng cách phơi bày các điểm nghẽn, phương pháp Kanban rất phù hợp với tư tưởng của TOC về "nhận diện và tối ưu hóa các ràng buộc".

---
*Tham khảo: Việc áp dụng phương pháp Kanban trong phát triển phần mềm lần đầu tiên được thực hành và tổng kết bởi David J. Anderson trong quá trình làm việc tại Microsoft và Corbis. Cuốn sách của ông mang tên "Kanban: Successful Evolutionary Change for Your Technology Business" là tác phẩm nền tảng cho phương pháp này. Tư tưởng của Kanban bắt nguồn sâu sắc từ Hệ thống Sản xuất Toyota (TPS) và Sản xuất Lean (Lean Manufacturing).*