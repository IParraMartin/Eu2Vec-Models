import pandas as pd

df = pd.read_csv('/Users/inigoparra/Desktop/Hoja de cálculo sin título - news-Gara-(561).csv')

df['text'] = df['text'].str.lower()
df.to_csv('news.csv')