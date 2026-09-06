# Fourier transform calculation

Use
\[
\widehat f(x)=\int_{\mathbb R}f(t)e^{-2\pi ixt}\,dt.
\]
Let
\[
\alpha=\frac{q-2}{2q},\qquad
g_q(t)=\left(\frac{\sin(\pi\alpha t)}{\pi\alpha t}\right)^2.
\]
The inverse transform identity
\[
\int_{-\alpha}^{\alpha}
\frac1\alpha\left(1-\frac{|x|}{\alpha}\right)e^{2\pi ixt}\,dx
=\left(\frac{\sin(\pi\alpha t)}{\pi\alpha t}\right)^2
\]
follows by writing the integral as twice the integral over \([0,\alpha]\)
and integrating \(1-x/\alpha\) twice by parts. Therefore
\[
\boxed{\widehat g_q(x)=\frac1\alpha
\left(1-\frac{|x|}{\alpha}\right)_+.}
\]
The support is \([-\alpha,\alpha]\), not \([-2\alpha,2\alpha]\).

For \(G_q(r,s)=g_q(r)g_q(s)\),
\[
\widehat G_q(x,y)=\frac1{\alpha^2}
\left(1-\frac{|x|}{\alpha}\right)_+
\left(1-\frac{|y|}{\alpha}\right)_+,
\]
supported on \([-\alpha,\alpha]^2\).
