import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Laden des Datasets
@st.cache_data  # Diese Dekorator speichert das geladene Dataset im Cache, um wiederholtes Laden zu vermeiden
def load_data():
    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    data = pd.read_csv(url)
    return data

# App Titel
st.title('Titanic Überlebensanalyse')

# Daten laden
data = load_data()

# Eingabefelder hinzufügen
sex_option = st.sidebar.selectbox('Wähle das Geschlecht:', ['both', 'male', 'female'])
class_option = st.sidebar.selectbox('Wähle die Klasse:', ['All', 1, 2, 3])
survived_option = st.sidebar.radio('Überlebensstatus:', ['Both', 'Survived', 'Not Survived'])

# Filterlogik
if sex_option != 'both':
    data = data[data['Sex'] == sex_option]
if class_option != 'All':
    data = data[data['Pclass'] == class_option]
if survived_option == 'Survived':
    data = data[data['Survived'] == 1]
elif survived_option == 'Not Survived':
    data = data[data['Survived'] == 0]

# Daten anzeigen
st.write("Datenübersicht", data)

# Visualisierung der Überlebensrate nach Geschlecht
fig, ax = plt.subplots()
sns.countplot(data=data, x='Sex', hue='Survived', ax=ax)
ax.set_title('Überlebensrate nach Geschlecht')
st.pyplot(fig)

# Visualisierung der Überlebensrate nach Klasse
fig, ax = plt.subplots()
sns.countplot(data=data, x='Pclass', hue='Survived', ax=ax)
ax.set_title('Überlebensrate nach Klasse')
st.pyplot(fig)