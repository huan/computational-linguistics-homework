# computational-linguistics-homework

## HOW TO RUN

### 1 Clone

```sh
$ git clone git@github.com:huan/computational-linguistics-homework.git
Cloning into 'computational-linguistics-homework'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (64/64), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 64 (delta 23), reused 56 (delta 19), pack-reused 0
Receiving objects: 100% (64/64), 14.10 KiB | 335.00 KiB/s, done.
Resolving deltas: 100% (23/23), done.
```

### 2 Download

```sh
$ make download
./scripts/download.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   141  100   141    0     0     61      0  0:00:02  0:00:02 --:--:--    61
100 8793k  100 8793k    0     0   313k      0  0:00:28  0:00:28 --:--:--  418k
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   157  100   157    0     0     72      0  0:00:02  0:00:02 --:--:--    72
100 21974  100 21974    0     0   4700      0  0:00:04  0:00:04 --:--:-- 12221
```

### 3 Preprocess

```sh
$ make preprocess
PYTHONPATH=. python3 bin/preprocess.py > data/corpus_preprocessed.txt
```

### 4 Train

```sh
$ make train
PYTHONPATH=. python3 bin/train.py
No checkponit fount.
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, 120, 64)           298944    
_________________________________________________________________
bidirectional (Bidirectional (None, 120, 128)          66048     
_________________________________________________________________
dropout (Dropout)            (None, 120, 128)          0         
_________________________________________________________________
time_distributed (TimeDistri (None, 120, 1)            129       
=================================================================
Total params: 365,121
Trainable params: 365,121
Non-trainable params: 0
_________________________________________________________________
Epoch 1/2
45478/45478 [==============================] - 55s 1ms/step - loss: 0.1920
Epoch 2/2
45478/45478 [==============================] - 54s 1ms/step - loss: 0.0803
```

### 5 Inference

```sh
$  make inference
PYTHONPATH=. python3 bin/inference.py
2018-12-15 02:13:58.718593: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
 本报 讯 春节 临近 ， 全国 各地 积极 开展 走访 慰问 困难 企业 和 特困 职工 的 送 温暖 活动 ，...
```

## AUTHOR

[@zixia](https://github.com/huan) [Huan LI](https://linkedin.com/in/zixia) \<zixia@zixia.net\>

<a href="http://stackoverflow.com/users/1123955/zixia">
  <img src="http://stackoverflow.com/users/flair/1123955.png" width="208" height="58" alt="profile for zixia at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for zixia at Stack Overflow, Q&amp;A for professional and enthusiast programmers">
</a>

## COPYRIGHT & LICENSE

- Code & Docs © 2018 - now Huan LI \<zixia@zixia.net\>
- Code released under the Apache-2.0 License
- Docs released under Creative Commons
