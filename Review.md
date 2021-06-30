## Probability

### Bayes Rule

<img src="C:\Users\28240\AppData\Roaming\Typora\typora-user-images\image-20210613234636861.png" alt="image-20210613234636861" style="zoom:80%;" />

![image-20210613234713178](C:\Users\28240\AppData\Roaming\Typora\typora-user-images\image-20210613234713178.png)

### Bayes network

## Scientific Computation

### LU 分解

![这里写图片描述](https://img-blog.csdn.net/20160925154352400)

![这里写图片描述](https://img-blog.csdn.net/20160925154429668)

L 为 G<sub>3</sub>G<sub>2</sub>G<sub>1</sub>的矩阵的逆

https://blog.csdn.net/Zijie123pea/article/details/113813747 介绍了 LU 的 L 比较快的求解方法

full pivoting相比partial pivoting更加稳定，但是更麻烦，速度会慢。

### Cholesky 分解

> Reference:
>
> https://zhuanlan.zhihu.com/p/112091443
>
> https://zhuanlan.zhihu.com/p/84210687

Ax = b 未必线性有解，即 A 不可逆，A<sup>-1</sup>无法计算，所以我们希望最小化 || Ax - b||<sub>2</sub>		

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Balign%2A%7D+%7C%7C+A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D+%7C%7C%5E2+%7B%7D+%26%3D+%28A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D%29%5Ccdot%28A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D%29+%5C%5C+%26%3D+%28A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D%29%5ET+%5Ccdot+%28A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D%29+%5C%5C+%26%3D+%28%5Cmathbf%7Bx%7D%5ETA%5ET+-+%5Cmathbf%7Bb%7D%5ET%29+%5Ccdot+%28A%5Cmathbf%7Bx%7D+-+%5Cmathbf%7Bb%7D%29%5C%5C+%26%3D+%28%5Cmathbf%7Bx%7D%5ETA%5ETA%5Cmathbf%7Bx%7D+-+2%5Cmathbf%7Bb%7D%5ETA%5Cmathbf%7Bx%7D+%2B+%5Cmathbf%7Bb%7D%5ET%5Cmathbf%7Bb%7D%29++%5Cend%7Balign%2A%7D%5C%5C)

Error 求导

![[公式]](https://www.zhihu.com/equation?tex=+%5Cfrac%7B%5Cpartial+E%7D%7B%5Cpartial+%5Cmathbf%7Bx%7D%7D+%3D++2A%5ETA%5Cmathbf%7Bx%7D+-+2+A%5ET+%5Cmathbf%7Bb%7D%3D+0+%5C%5C)

可得

![[公式]](https://www.zhihu.com/equation?tex=+%5Cmathbf%7Bx%7D+%3D+%28A%5ETA%29%5E%7B-1%7D+A%5ET+%5Cmathbf%7Bb%7D++%5Ctag%7B2%7D%5C%5C)

（A<sup>T</sup>A）<sup>-1</sup>也未必存在逆矩阵（underdetermined），所以才有 Tikhonov regularization

​	A<sup>T</sup>A 至少是半正定矩阵

![[公式]](https://www.zhihu.com/equation?tex=x%5ETA%5ETAx+%3D+%28Ax%29%5ET+%5Ccdot+Ax+%3D+%7C%7CAx%7C%7C%5E2%5C%5C)

对于正定矩阵（A 的列向量线性无关）有 Cholesky 分解(为 LU 分解的特殊情况)

![[公式]](https://www.zhihu.com/equation?tex=A+%3D+LL%5ET+%5C%5C)

如

![[公式]](https://www.zhihu.com/equation?tex=%7B%5Cdisplaystyle+%7B%5Cbegin%7Baligned%7D%5Cleft%28%7B%5Cbegin%7Barray%7D%7B%2A%7B3%7D%7Br%7D%7D4%2612%26-16%5C%5C12%2637%26-43%5C%5C-16%26-43%2698%5C%5C%5Cend%7Barray%7D%7D%5Cright%29%3D%5Cleft%28%7B%5Cbegin%7Barray%7D%7B%2A%7B3%7D%7Br%7D%7D2%260%260%5C%5C6%261%260%5C%5C-8%265%263%5C%5C%5Cend%7Barray%7D%7D%5Cright%29%5Cleft%28%7B%5Cbegin%7Barray%7D%7B%2A%7B3%7D%7Br%7D%7D2%266%26-8%5C%5C0%261%265%5C%5C0%260%263%5C%5C%5Cend%7Barray%7D%7D%5Cright%29%5Cend%7Baligned%7D%7D%7D%5C%5C)

![img](https://img-blog.csdn.net/20170512235036629)

## QR 分解

> Reference:
>
> https://blog.csdn.net/u010945683/article/details/45972819

## SVD 分解

>https://zhuanlan.zhihu.com/p/54681618?from_voters_page=true
>
>https://www.cnblogs.com/marsggbo/p/10155801.html

计算过程重点看第二个

## 非线性系统

> Newton’s Method:	https://zhuanlan.zhihu.com/p/46536960
>
> Secant’s Method: 