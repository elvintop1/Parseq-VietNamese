# Hướng dẫn sử dụng Parseq

## 0. Cài đặt môi trường
- Load Docker Image đội cung cấp (trttung1610/bkai_parseq:latest)
```
cd Parseq 
pip install -r requirements.txt

```


## 1. Chuẩn bị data
Chuân bị data như sau vào thư mục Parseq/: 


![data-dir-parseq](https://user-images.githubusercontent.com/82688630/220395775-e6d6f913-7755-4816-a2cb-a9a2355e2f6f.png)


train.txt, val.txt có dạng sau: `img_path <tab> text_label`
```
img/im3671.jpg_box0.jpg	Trà
img/im3671.jpg_box1.jpg	m
img/im3671.jpg_box2.jpg	ĐC:
img/im3671.jpg_box3.jpg	K
```
Tại đậy , đội sẽ chia bộ new_train được BTC cung cấp với tỉ lệ là train : 0.95 , val : 0.05

Sau khi để ảnh và annotation theo cấu trúc này, ta chạy lệnh:
```
sh scripts/create_dataset.sh
```

## 2. Train model
Đội đã điều chỉnh file config để phù hợp và tối ưu với cuộc thi .

Sau đó chạy lệnh: `sh scripts/training.sh`. Weight sẽ được lưu trong `outputs/`.
Weight được đội cung cấp đã được chọn là ckpt dùng để dự đoán tại epoch thứ 72 . 


## 3. Predict model
### 3.1. Predict with CLI
```
sh scripts/predict.sh

```


### 3.2. Format 
Sau khi có file prediction.txt từ mô hình , file dự đoán sẽ được đưa qua format_result_file.py để kiểm tra và chỉnh lại giống định dạng của file submit 
```
sh scripts/format.sh

```
