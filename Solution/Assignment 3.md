# Homework 3

## Problem 1

### 1)

![](C:\Users\28240\Downloads\未命名文件.svg)

### 2)

$$
p(S1,S2,S3,S4,D1,D2,D3)=p(S1|D1)p(S2|D1,D2)p(S3|D1,D3)p(S4|D3)p(D1)p(D2)p(D3)
$$

### 3)

$$
D1,D2
$$

### 4)

$$
\begin{align*}
{P(D_3=1|S_4=1) }
&=\frac{P(S_4=1|D_3=1)P(D_3=1)}{P(S_4=1)}\\
&=\frac{P(S_4=1|D_3=1)P(D_3=1)}{P(S_4=1|D_3=1)P(D3=1)+P(S_4=1|D_3=0)P(D_3=0)}\\
&=\frac{0.9*0.1}{0.9*0.1+0.6*0.9}\\
&=\frac{1}{7}
\end{align*}
$$



## Problem 2

$$
P(X=0)=\frac{1}{3}\\
P(X=1)=\frac{1}{2}\\
P(X=2)=\frac{1}{6}\\
P(Y=0)=\frac{1}{4}\\
P(Y=1)=\frac{5}{12}\\
P(Y=2)=\frac{1}{3}\\
P(Y=0|X=0)=\frac{P(X=0,Y=0)}{P(X=0)}=\frac{\frac{1}{12}}{\frac{1}{3}}=\frac{1}{4}\\
P(Y=0|X=1)=\frac{P(X=1,Y=0)}{P(X=1)}=\frac{\frac{1}{6}}{\frac{1}{2}}=\frac{1}{3}\\
P(Y=0|X=2)=\frac{P(X=2,Y=0)}{P(X=2)}=\frac{0}{\frac{1}{6}}=0\\
P(Y=1|X=0)=\frac{P(X=0,Y=1)}{P(X=0)}=\frac{\frac{1}{6}}{\frac{1}{3}}=\frac{1}{2}\\
P(Y=1|X=1)=\frac{P(X=1,Y=1)}{P(X=1)}=\frac{\frac{1}{6}}{\frac{1}{2}}=\frac{1}{3}\\
P(Y=1|X=2)=\frac{P(X=2,Y=1)}{P(X=2)}=\frac{\frac{1}{12}}{\frac{1}{6}}=\frac{1}{2}\\
P(Y=2|X=0)=\frac{P(X=0,Y=2)}{P(X=0)}=\frac{\frac{1}{12}}{\frac{1}{3}}=\frac{1}{4}\\
P(Y=2|X=1)=\frac{P(X=1,Y=2)}{P(X=1)}=\frac{\frac{1}{6}}{\frac{1}{2}}=\frac{1}{3}\\
P(Y=2|X=2)=\frac{P(X=2,Y=2)}{P(X=2)}=\frac{\frac{1}{12}}{\frac{1}{6}}=\frac{1}{2}\\
$$

### (a)

$$
\begin{align*}
H(X)&=-\frac{1}{3}\log_2{\frac{1}{3}}-\frac{1}{2}\log_2{\frac{1}{2}}-\frac{1}{6}\log_2{\frac{1}{6}}\\
&\approx 1.45915 \\
H(Y)&=-\frac{1}{4}\log_2{\frac{1}{4}}-\frac{5}{12}\log_2{\frac{5}{12}}-\frac{1}{3}\log_2{\frac{1}{3}}\\
&\approx 1.55459
\end{align*}
$$



### (b)

$$
\begin{align*}
H(X,Y)&=-\frac{1}{12}\log_2{\frac{1}{12}}-\frac{1}{6}\log_2{\frac{1}{6}}-\frac{1}{12}\log_2{\frac{1}{12}}\\
&-\frac{1}{6}\log_2{\frac{1}{6}}
-\frac{1}{6}\log_2{\frac{1}{6}}-\frac{1}{6}\log_2{\frac{1}{6}}\\
&-\frac{1}{12}\log_2{\frac{1}{12}}-\frac{1}{12}\log_2{\frac{1}{12}}\\
&\approx 2.9183
\end{align*}
$$



### (c)

$$
\begin{align*}
H(Y|X)&=-\frac{1}{12}\log_2{\frac{1}{4}}-\frac{1}{6}\log_2{\frac{1}{3}}-0\\
&-\frac{1}{6}\log_2{\frac{1}{2}}-\frac{1}{6}\log_2{\frac{1}{3}}-\frac{1}{12}\log_2{\frac{1}{2}}\\
&-\frac{1}{12}\log_2{\frac{1}{4}}-\frac{1}{6}\log_2{\frac{1}{3}}-\frac{1}{12}\log_2{\frac{1}{2}}\\
&\approx 1.45915
\end{align*}
$$



### (d)

$$
\begin{align*}
I(X;Y) &= \frac{1}{12}\log_2\frac{\frac{1}{12}}{\frac{1}{3}\times\frac{1}{4}}
+\frac{1}{6}\log_2\frac{\frac{1}{6}}{\frac{1}{3}\times\frac{5}{12}}
+\frac{1}{12}\log_2\frac{\frac{1}{12}}{\frac{1}{3}\times\frac{1}{3}}\\
&+\frac{1}{6}\log_2\frac{\frac{1}{6}}{\frac{1}{2}\times\frac{1}{4}}
+\frac{1}{6}\log_2\frac{\frac{1}{6}}{\frac{1}{2}\times\frac{5}{12}}
+\frac{1}{6}\log_2\frac{\frac{1}{6}}{\frac{1}{2}\times\frac{1}{3}}\\
&+0
+\frac{1}{12}\log_2\frac{\frac{1}{12}}{\frac{1}{6}\times\frac{5}{12}}
+\frac{1}{12}\log_2\frac{\frac{1}{12}}{\frac{1}{6}\times\frac{1}{3}}\\
&\approx 0.095437
\end{align*}
$$



### (e)

![](D:\Desktop\hw3_2_e.bmp)

## Problem 3

$$
P(Y=-)=\frac{1}{4},P(Y=+)=\frac{3}{4}\\
P(A=1)=1,P(A=0)=0\\
P(B=1)=\frac{1}{2},P(B=0)=\frac{1}{2}\\
P(Y=-|A=1)=\frac{1}{4},P(Y=+|A=1)=\frac{3}{4}\\
P(Y=-|A=0)=0,P(Y=+|A=0)=0\\
P(Y=-|B=1)=0,P(Y=+|B=1)=1\\
P(Y=-|B=0)=\frac{1}{2},P(Y=+|B=0)=\frac{1}{2}\\
\begin{align}
H(Y)&=-\frac{1}{4}\log_2{\frac{1}{4}}-\frac{3}{4}\log_2{\frac{3}{4}}\\
	&\approx 0.811278\\
H(Y|A) &= -\frac{1}{4}\log_2{\frac{1}{4}}-\frac{3}{4}\log_2{\frac{3}{4}}\\
	&\approx 0.811278\\
H(Y|B) &= \frac{1}{2}\times(\log_2{1})+\frac{1}{2}\times(-\frac{1}{2}\log_2{\frac{1}{2}}-\frac{1}{2}\log_2{\frac{1}{2}})\\
	&=0.5\\
	I(Y;A)&=0,	\qquad I(Y;B)\approx 0.311278\\
\end{align}
$$

*So choose option 2 i.e. B*.