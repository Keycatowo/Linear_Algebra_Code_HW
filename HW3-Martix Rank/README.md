# 以高斯消去法求矩陣的rank
[english version](README(en).md)

## 矩陣的列運算
矩陣一共可以進行三種不同的列運算
1. 將一矩陣的某一列乘以某一數值加入另一列
2. 將一矩陣的某一列乘以一個不為0的數
3. 將一矩陣中的某兩列互換位置


## 程式說明
請完成矩陣的三種不同列運算及用高斯消去法求秩(rank)
+ [x] 完成矩陣列運算`matrix_op3()`——交換兩列，-> 此已經完成作為範例
+ [ ] 完成矩陣列運算`matrix_op2()`
+ [ ] 完成矩陣列運算`matrix_op1()`
+ [ ] 完成高斯消去求秩(rank)`get_rank()`

> 內附範例測資提供除錯使用，通過範例測資者可以得60%分數，剩下40%分數由不公開測資所提供
### Python執行範例測資
```
pytest test_hw3.py
```
通過畫面
![](https://i.imgur.com/Wc1u2P6.png)

失敗畫面
![](https://i.imgur.com/1207NOe.png)


### Matlab執行範例測資

成功畫面
```
PASS: test op3
PASS: test op2
PASS: test op1
PASS: test rank
```

失敗畫面
```
Error using test_hw3 (line 25)
The row operation 2 get the wrong answer
```


## 其他注記
+ 在計算第幾列時候所用的index，在Python中為從0開始、在Matlab中為從1開始
+ 繳交python作業的時候請交以下檔案：`my_solve.py`
+ 繳交matlab作業的時候請交以下檔案：`row_op1.m`, `row_op2.m`, `row_op3.m`, `get_rank.m`,