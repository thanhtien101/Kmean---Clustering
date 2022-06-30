# THUẬT TOÁN KMEANS
## Giải thích 1 vài thuật ngữ:
* Đầu vào
  
  * observation: các điểm dữ liệu 
  
  * cluster : Cụm dữ liệu
  
* Đầu ra:

  * label: Các điểm dữ liệu sau khi được xác định gần ở cluster nào nhất sẽ được gắn nhãn ở cluster đó ( trong giao diện nó sẽ biểu thị cùng màu với cluster mà nó xác định )

## Giao diện
![image](https://user-images.githubusercontent.com/107552816/176353192-fdf6f7df-819b-479d-85c2-2f14d4668670.png)
## Khởi tạo các points (observation ):
![image](https://user-images.githubusercontent.com/107552816/176353369-42e8c0f8-0d66-4532-a7ba-6a051b93be64.png)
## Tăng số K ( Tăng số cluster )
![image](https://user-images.githubusercontent.com/107552816/176353771-4fb36d86-93c0-4fc0-aad0-760c3ea8a2d8.png)
## Bấm nút Random để đặt vị trí ngẫu nhiên cho các cluster
![image](https://user-images.githubusercontent.com/107552816/176354604-8d899b98-9298-4c6c-b28e-60f3d34f5ace.png)
## Sau đó bấm nút Run để chạy thuật toán
![image](https://user-images.githubusercontent.com/107552816/176354781-0b455635-1977-4829-b85c-6c58e3c39ac0.png)
Mỗi lần bấm nút Run, các cluster sẽ được tính toán lại vị trí trung tâm và cập nhập vị trí trên giao diện, vì thế các label cũng được cập nhập lại. Ta thấy distance= 8627,distance là khoảng cách giữa các label ( các observation sau khi đã được gắn nhãn) đến các cluster, số liệu này sẽ giảm xuống cho lần chạy tiếp theo, điều đó chứng tỏ các cluster đang tiến vào vị trí tối ưu của nó. Thuật toán chạy cho đến khi các label và cluster đã đạt được tối ưu thì dừng lại 
![image](https://user-images.githubusercontent.com/107552816/176358223-316884b2-a266-4816-9ec0-802edcd55fc7.png)
Tiếp tục bấm Run 
![image](https://user-images.githubusercontent.com/107552816/176358408-6d088593-2991-40f0-b5e5-f8968bb550a7.png)
Và cuối cùng
![image](https://user-images.githubusercontent.com/107552816/176358497-c302c3df-b539-4c54-b665-9b9e8f66bb4e.png)
Ta luôn thấy, label và vị trí cluster luôn được cập nhập qua mỗi lần chạy và distance luôn luôn giảm xuống cho đến khi không còn giảm được nữa . Cho thấy mô hình đã tối ưu.

