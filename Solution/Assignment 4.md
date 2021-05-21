# HW2_2

## 1

### 1)

$$
\begin{align*}
maximize \qquad &x_1+x_2\\
subject\ to \qquad &x_1+2x_2 \le4\\
&-x_1+x_2\le1\\
&4x_1+2x_2\le12\\
&x_1,x_2\ge0
\end{align*}
$$

### 2)

$$
\begin{align*}
&y_1\times\qquad x_1+2x_2 \le4\\
&y_2\times\qquad -x_1+x_2\le1\\
&y_3\times\qquad 4x_1+2x_2\le12\\
yields\qquad &(y_1-y_2+4y_3)x_1+(2y_1+y_2+2y_3)x_2\le4y_1+y_2+12y_3\\
we\ want\qquad &z=x_1+x_2 \le (y_1-y_2+4y_3)x_1+(2y_1+y_2+2y_3)x_2\\
so\ dual\ problem\ should\ be\qquad minimize\qquad &4y_1+y_2+12y_3\\
subject\ to \qquad &y_1-y_2+4y_3\ge1\\
&2y_1+y_2+2y_3\ge1\\
&y_1,y_2,y_3\ge0
\end{align*}
$$

## 2

- (a) GP
- (b) LP
- (c) SDP
- (d) QP

## 3

$$
\begin{align*}
&L(x,\nu)=f(x)+\nu(2x_1-x_2-5)=x^THx+\nu^T(Ax-b)\\
where\ &H=\begin{bmatrix}
\frac{1}{2} & 0\\
0 & \frac{1}{2}
\end{bmatrix},
A=\begin{bmatrix}
2\\
-1
\end{bmatrix}^T,
b=[5]\\
&\nabla_x L(x,\nu)=x+A^T\nu=0 \Rightarrow x=-A^T\nu\\
&g(\nu)=L(-A^T\nu,\nu)=-\frac{1}{2}\nu^TAA^T\nu-b^T\nu\\
\nu\in \R, ^{1}the\ dual\ problem\ should\ be\ QP\quad&
maximize\quad -\frac{1}{2}\nu^TAA^T\nu-b^T\nu= -\frac{5}{2}\nu^2-5\nu

\end{align*}
$$

## 4

### 1)

13

### 2)

$$
\{s,a,b,c,d\}\ and \ \{t\}
$$

