import pandas as pd
import nltk

df = pd.read_csv('/Users/inigoparra/Desktop/Hoja de cálculo sin título - news-EHU-(51).csv')

df['text'] = df['text'].str.lower()

df.to_csv('new.csv')