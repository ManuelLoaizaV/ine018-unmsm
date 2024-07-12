# Bag of Words

En el Reino Unido,
el proyecto Encyclopedia of Shakespeare's Language
trae un nuevo método de investigación del lenguaje a los estudios de Shakespeare.
Este proyecto ofrece nuevos conocimientos sobre el uso del lenguaje
por parte de Shakespeare en múltiples niveles: palabras, frases, temas, perfiles de personajes y más.
En particular, revela lo que significó el lenguaje de Shakespeare para los isabelinos a través del análisis de millones de palabras escritas por sus contemporáneos.

Uno de los modelos utilizados para representar los textos de Shakespeare es el **bag-of-words**,
el cual consiste en obtener un histograma de los tokens en un texto para luego ser utilizado en los algoritmos de aprendizaje de máquina.

La complejidad de utilizar un BoW está en cómo diseñar el vocabulario de tokens conocidos y cómo darle un puntaje a los tokens presentes.

Implemente el BoW más simple, es decir, uno que compute la frecuencia de cada palabra que aparece en el siguiente texto y las imprima en pantalla:

```
From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.
```

## Referencias

L. Ackerman. **Processing Shakespeare.** [Adventures in R](https://lmackerman.com/AdventuresInR/docs/shakespeare.nb.html).

Y. Bai, W. Yu, T. Xiao, C. Xu, K. Yang, W. Ma, T. Zhao. 2014. **Bag-of-Words Based Deep Neural Network for Image Retrieval.** [In Proceedings of the 22nd ACM international conference on Multimedia (MM '14). Association for Computing Machinery, New York, NY, USA, 229–232](https://doi.org/10.1145/2647868.2656402).

J. Culpeper. **How linguists are unlocking the meanings of Shakespeare’s words using numbers.** [The conversation](https://theconversation.com/how-linguists-are-unlocking-the-meanings-of-shakespeares-words-using-numbers-212587).

J. Culpeper. **Shakespeare's language: News perspectives from corpus linguistics.** [Encyclopedia of Shakespeare's Language](https://wp.lancs.ac.uk/shakespearelang/files/2018/12/ShakesInstitute.pdf).

J. Marsden, D. Budden, H. Craig, Moscato P.
**Language Individuation and Marker Words: Shakespeare and His Maxwell's Demon.**
[PLoS ONE 8(6): e66813](https://doi.org/10.1371/journal.pone.0066813), 2013.
