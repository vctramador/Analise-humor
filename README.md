# Analise-humor
Este código em Python utiliza a biblioteca NLTK para analisar o sentimento de frases de exemplo. Ele avalia se uma frase transmite sentimentos positivos, negativos ou neutros.

Primeiro, importamos a biblioteca NLTK e o módulo necessário para análise de sentimentos. Em seguida, definimos uma lista de frases de exemplo que queremos analisar.

Para cada frase na lista, o código utiliza o módulo de análise de sentimentos para atribuir pontuações que indicam o grau de positividade, negatividade e neutralidade da frase. A pontuação composta fornece uma avaliação geral do sentimento da frase.

Por fim, o código imprime cada frase junto com suas respectivas pontuações de sentimento, permitindo uma rápida compreensão do sentimento transmitido por cada frase.

Legenda:
neg: pontuação para sentimento negativo (de 0 a 1)
neu: pontuação para sentimento neutro (de 0 a 1)
pos: pontuação para sentimento positivo (de 0 a 1)
compound: pontuação composta que representa o sentimento geral da frase (de -1 a 1, sendo -1 muito negativo e 1 muito positivo)
