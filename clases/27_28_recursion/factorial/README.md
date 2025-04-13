# La función factorial

La función $n!$ tradicionalmente es definida como
el producto de los enteros entre $1$ y $n$.

Sin embargo, no hemos aprovechado una propiedad importante de los factoriales.
El factorial de un número está relacionado con el factorial del siguiente número entero.
Así, la definición recursiva del factorial de $n$ en términos de $n-1$ suele ser la siguiente:

```math
n! =
\begin{cases}
    1 & \quad \text{si } n = 0,\\
    n \times (n - 1)! & \quad \text{en otro caso.}
\end{cases}
```

De esta manera, $4! = 4 \times 3!$, $3! = 3 \times 2!$ y así sucesivamente.
Para asegurarnos que este proceso acaba, los matemáticos definimos $0!$ como $1$.
