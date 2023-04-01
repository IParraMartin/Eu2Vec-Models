import pandas as pd
import nltk

df = pd.read_csv('/Users/inigoparra/Desktop/Clean - master.csv')

spanish_stopwords = ['pero', 'como', 'asesino', 'y', 'el', 'españa', 'país', 'vasco', 'muy', 'bien', 'el', 'la',
                     'que', 'de', 'y', 'a', 'los', 'del', 'se', 'las', 'en', 'un', 'por', 'con', 'no', 'una', 'su', 'sus',
                     'para', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'sí', 'porque', 'esta']

for i, row in df.iterrows():
    tokens = nltk.word_tokenize(row['text'])

    if any(token in spanish_stopwords for token in tokens):
        df = df.drop(i)

df.to_csv('new.csv')