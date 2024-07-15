# Cadenas buenas

Sea $s$ una cadena compuesta por caracteres minúsculas y mayúsculas.

Decimos que una cadena $s$ es buena si no existe
$0 \leq i < |s| - 1$
tal que $s[i]$ sea minúscula y $s[i+1]$ sea mayúscula.

Para convertir una cadena mala en una buena,
podemos escoger dos caracteres adyacentes que hacen que la cadena sea mala y eliminarlos.
Podemos realizar este proceso hasta que la cadena sea buena.

Por ejemplo, las cadenas `Manuel`, `s` y `UNMSM` son buenas.

Por otro lado, la cadena `xabBAycCz` es mala, y podemos convertirla en la cadena buena `xyz`.
