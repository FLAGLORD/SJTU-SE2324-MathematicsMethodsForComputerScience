# Homework 2

## 2.4

### (b)

$$
S\rightarrow0P0\vert1P1|0|1\\
P\rightarrow1P|0P|\varepsilon
$$

### (c)

$$
S\rightarrow01S|10S|00S|11S|0|1
$$

### (d)

$$
S\rightarrow0S0|1S0|1S1|0S1|0
$$

## 2.6

### (a）

$$
S \rightarrow TaT\\
T\rightarrow TT|aTb|bTa|a|\varepsilon
$$

### (d)

$$
R\rightarrow S|J\#S\#J|J\#S|S\#J\\
S\rightarrow aSa|bSb|\#|\#J\#\\
J\rightarrow aJ|bJ|\#J|\varepsilon
$$

## 2.14

首先添加一个 start variable **S<sub>0</sub>**,则有
$$
S_0\rightarrow A\\
A \rightarrow BAB |B|\varepsilon\\
B\rightarrow  00|\varepsilon
$$
接着消除$$A\rightarrow\varepsilon$$和$$B \rightarrow \epsilon$$,可以得到
$$
S_0 \rightarrow A|\varepsilon\\
A\rightarrow  BAB|BA|AB|BB|A|B
\\B\rightarrow00
$$
消除$$A\rightarrow A$$可以得到
$$
S_0 \rightarrow A|\varepsilon\\
A\rightarrow  BAB|BA|AB|BB|B
\\B\rightarrow00
$$
消除$$A\rightarrow B$$可以得到
$$
S_0 \rightarrow A|\varepsilon\\
A\rightarrow  BAB|BA|AB|BB|00
\\B\rightarrow00
$$
消除$$S_0\rightarrow A$$可以得到
$$
S_0 \rightarrow BAB|BA|AB|BB|00|\varepsilon\\
A\rightarrow  BAB|BA|AB|BB|00
\\B\rightarrow00
$$
添加新的variable $$U$$来表示terminals $$0$$
$$
S_0 \rightarrow BAB|BA|AB|BB|UU|\varepsilon\\
A\rightarrow  BAB|BA|AB|BB|UU
\\B\rightarrow UU
\\U\rightarrow 0
$$


## 2.18

### (b)

使用反证法，假设A属于CFL，设R为$$a^*b^*c^*$$,那么$$A\cap R$$ 也应该属于CFL.

$$A\cap R = \{ a^n b^n c^n | n \geq0 \}$$

假定字符串 $$s = a^p b^p c^p = xuyvz$$ 属于$$A\cap R$$,pumping length 为 p.

- 如果$$u,v$$都仅包含一种symbol(如a,b,c的任意一种)，那么$$xu^2yv^2z$$不能包含相同数量的a,b,c,矛盾
- 如果$$u $$或$$v$$包含超过一种以上的symbol，那么$$xu^2yv^2z$$将会有symbol彼此交错，不再满足同一种symbol连续出现且只存在一段，矛盾

因此$$A\cap R$$ 不是CFL.因而A不属于CFL

## 2.20

设$$PDA\space M_A = (Q_A,\sum,\Gamma,\delta_A,q_A,F_A),NFA\space M_B=(Q_B,\sum,\delta_B,q_B,F_B)$$

构建
$$
M_{A/ B}=(Q^{A/B},\sum,\Gamma_{A/B},\delta_{A/B},q_{A/B},F_{A/B})\\
where \space Q^{A/B} =Q^A(Q^A\times Q^B)\\
\Gamma_{A/B} = \Gamma\\
q_{A/B}=q_Aq_0\space ,q_0=q_A\space or\space q_B\\
F_{A/B} = F_A\times F_B\\
For \space q_A \in Q_A:\delta_{A/B}(q_A,a,u)=
\{\begin{array}{rcl} \delta_A(q_A,a,u) \space if\space a \in \sum \\
\delta_A(q_A,\varepsilon,u)\cup\{(q_A,q_B),\varepsilon\}\space if\space a=\varepsilon
\end{array} \\
For \space (q_A,q_B)\in Q_A \times Q_B:\delta_{A/B}((q_A,q_B),a,u)=
\{\begin{array}
 \right \phi, if\space a\in\sum\\
\cup_{b\in\sum}\{((r_A,r_B),v):(r_A,v)\in\delta_A(q_A,b,u)\space and\space  r_A  \in\delta_B(q_B,b)\}, if\space a = \varepsilon
\end{array}
$$
因此 A/B 为CFL

## 2.26

使用数学归纳法

- **n = 1**: 考虑长度为1的字符串 a,derivation可以为$$S\rightarrow a$$，$$steps  = 2n - 1 = 1$$,成立

- **假设n = k时结论成立**：即对于长度为k的字符串 s ,derivation将需要 2k - 1 steps.

- **n = k + 1**: 考虑一满足CNF的language如下
  $$
  S\rightarrow AB\\
  A \rightarrow *x\\
  B\rightarrow *y
  $$
  $|w| = xy$其中 $$|x|>0, |y|  > 0$$

  则$$|w| = 1+(2|x| - 1) +(2|y| - 1) = 2(|x|+|y|)-1$$

  $$|x| + |y| = n = k +1$$，故结论成立

## 2.30

使用反证法，在各小题中以B来代指language

### （a）

设 p 为pumping length，考虑字符串$$s= 0^p1^p0^p1^p=xuyvz$$

- 如果u, v都仅包含一种symbol(即0,1的任意一种 )，那么$$xu^2yv^2z$$的 0,1段的长度 不相等，其不属于B，矛盾
- 如果u或v包含超过一种以上的symbol(即0,1都有)，那么$$xu^2yv^2z$$的连续0,1段必定超过了4段，其 不属于B，矛盾

所以B 不是 CFL

### （b）

设 p 为pumping length，考虑字符串$$s= 0^p\#0^{2p}\#0^{3p}=xuyvz$$

u,v 都不包含#，否则$$xu^2yv^2z$$中#的数目必定大于2.所以u,v必定属于$$0^p,0^{2p},0^{3p}$$任意一段的子集，那么$$xu^2yv^2z$$中其由#分割的三段长度不能满足1:2:3，矛盾，其不属于B

所以B不是CFL

### （c）

设 p 为pumping length，考虑字符串$$s= a^bb^p\#a^pb^p=xuyvz$$

u,v 都不包含#，否则$$xu^2yv^2z$$中#的数目必定大于2.其次，u,v不可能都位于#的左段，否则$$xu^2yv^2z$$左段的长度必定大于右段，不再满足w为t的子字符串这一条件；另一方面，u,v也不可能都位于#的右段，否则$xu^0yv^0z$$右段的长度必定小于左段，所以只可能存在u在左段，v在右段这一情况

由于$$|uyv| \leq p$$,那么u由b组成，v由a组成，$$xu^2yv^2z$$左段的b的数目大于右段，不满足w为t的子字符串这一条件，其不属于B

所以B不是CFL

### (d)

设 p 为pumping length，考虑字符串$$s= a^bb^p\#a^pb^p=xuyvz$$

- u,v 都不包含#，否则$$xu^2yv^2z$$中#的数目必定大于2
- u,v不可能都位于#的左段,否则$$xu^2yv^2z$$左段不等于右段
- u,v也不可能都位于#的右段，理由同上
- 考虑u在左段，v在右段这一情况，由于$$|uyv| \leq p$$,那么u由b组成，v由a组成，$$xu^2yv^2z$$左段的b的数目大于右段，不满足左段和右段b的数目应该相等这一条件，其不属于B

所以B不是CFL

## 2.40

设 C 为prefix-closed,且为CFL.

使用pumping lemma,设 p 为pumping length,考虑属于 C 的字符串$$s= xuyvz,|u| \geq 1$$

则$$s'= xu^kyv^kz \in C \space  ,k \geq 0$$,由于 C 满足prefix-closed的性质，因此$$xu^k \in C,k\geq  0$$.因此由$$xu^*$$构成的语言为regular language,且属于 C 的子集.

同时，由于$$|u|\geq1$$,所以$$ab^*$$满足infinite这一性质.

综上可证得，C contains an infinite regular  language

## 2.42

使用反证法，假设 Y 为 CFL

设 p 为pumping length，考虑字符串$$s=xuyvz$$

- u,v都不包含#，否则不妨假设$$u=1^m\#1^n,m\geq0 \space ,n\geq0$$,那么对于$$xu^3yv^3z$$中间的$$u^3$$必然会出现$$1^m\#1^n1^m\#1^n1^m\#1^n$$,出现了$$t_i = t_j \space and\space i  \neq j  $$的情况，不属于 Y

- 考虑$$u = 1^*,v=1^*$$,对于子字符串$$uyv$$有以下两种情况

  - **包含#**：由于u,v不可能包含 #，那么只有可能y包含#，假设由y中的#分割的两段长度分别为m,n,不妨假设m > n  > 0，那么可以取$$y = 1^n\#1^n,u=1^{m-n},v=\varepsilon$$,那么$$xu^0yv^0z$$出现了$$t_i = t_j \space and\space i  \neq j  $$的情况，不属于 Y
  - **不包含#**：$$uyv=1^*$$，不妨假设$$uyv$$所在的由1构成的段长度为m,再取其他任意一段长度为n (n  >  m),那么可以取$$u=1,v=\varepsilon$$,则$$xu^{n-m}yv^{n-m}$$出现了$$t_i = t_j \space and\space i  \neq j  $$的情况，不属于 Y

  故其不满足pumping lemma，因此 Y 不属于 CFL