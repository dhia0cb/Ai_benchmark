import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Benchmark IA", layout="wide")
st.title("Benchmark des Outils IA")

df = pd.read_csv(r'C:\Users\DHIA\benchmark_ai\data\resultats.csv')
st.subheader("Données brutes")
st.dataframe(df)

st.subheader("Score global par outil")
print(df.columns.tolist())
score = df.groupby('outil')['note_globale'].mean().sort_values(ascending=False)
st.bar_chart(score)

st.subheader("Meilleur outil par tâche")
best = df.groupby(['tache','outil'])['note_globale'].mean().reset_index()
st.dataframe(best)

st.subheader("Graphique comparatif")
fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=df, x='outil', y='note_globale', hue='tache', ax=ax)
plt.tight_layout()
st.pyplot(fig)

st.subheader("Recommandations par département")
st.success("Email professionnel → Claude")
st.success("Code Python → ChatGPT / Copilot")
st.success("Traduction → Gemini")
st.success("Marketing → ChatGPT")
st.success("Résumé → Claude")