import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Frases de exemplo
frases = [
    "Eu amo este produto!",
    "Estou muito feliz com o serviço.",
    "Não gostei do atendimento.",
    "O produto é bom, mas poderia ser melhor."
]

#analisar sentimento
analisador = SentimentIntensityAnalyzer()

#analisando o sentimento das frases
for frase in frases:
    sentiment = analisador.polarity_scores(frase)
    print(f"Frase: {frase}")
    print(f"sentimento: {sentiment}")
    print()