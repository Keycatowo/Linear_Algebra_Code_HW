# Least Square Problem


## Concept
+ 什麼時候我們可以解$A\vec{x}=\vec{b}$
	+ 當$\vec{b} \in Col(A)$
+ 試想一下，當$\vec{b} \notin Col(A)$應該要怎麼辦？
	+ 我們沒辦法解出一個完美的$\vec{x}$
	+ 但可以找到一個$\vec{x}$盡可能的靠近b,  s.t. $A\vec{x} \to \vec{b}$ -> 這就是**最小平方問題(Least Square Problem)**
+ 當$\vec{b} \notin Col(A)$
	+ $\vec{b} = \vec{b}_{\parallel} + \vec{b}_{\perp}$,   $\vec{b}_{\parallel} \in Col(A)$
	+ $A\vec{x}=\vec{b}$的**最小平方**解即是$A\vec{x}=\vec{b}_\parallel$的解
	+ 目標：最小化$|\vec{b}-A\vec{x}|^2 = \sum(\vec{b} - A\vec{x})^2_i$
+ 推導過程
	+ 把b拆分成平行和垂直，$A\vec{x} = \vec{b}_\parallel = \vec{b} - \vec{b}_\perp$
	+ 左右同乘$A^T$，得到$A^TA\vec{x} = A^T\vec{b} - A^T\vec{b}_\perp$
		+ $\vec{b}_\perp \notin Col(A) \to A^T\vec{b}_\perp=0$
		+ $A^TA\vec{x} = A^T\vec{b}$
	+ 左右同乘$(A^TA)^{-1}$
		+ $\vec{x} = (A^TA)^{-1}(A^T\vec{b})$
		+ **Note: 這邊不可以把$(A^TA)^{-1}$拆開變成$A^{-1}(A^{T})^{-1}$，因為$A$和$A^T$都不是方陣**
> 發現Github好像不支援部分的Latex語法，所以我更新一下圖片
> ![](https://i.imgur.com/jVmSciF.png)

## HW Objective and summbit
### Objective
Finsh the code and solve the least square sol with `Ax=b`, we name the sol `beta`.
+ For Matlab, you should finish the part in line `10~12`.
+ For Python, you should finish the part in line `20~21`.

### Submmit
+ For Matlab, please submmit:
    + `HW5_{ID}.m`: Finish the `HW5_starter.m` and rename it. (eg. `HW5_110061553.m`)
+ For Python, please submmit:
    + `HW5_{ID}.py`: Finish the `HW5_starter.m` and rename it. (eg. `HW5_110061553.m`)

## Reference
+ [Diabetes Data](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html)
+ [Least squares I: Matrix problems - YouTube](https://www.youtube.com/watch?v=Z0wELiinNVQ)
