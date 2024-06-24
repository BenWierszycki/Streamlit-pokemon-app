import requests
import streamlit as st
import pandas as pd
import numpy as np

st.title("Pokemon Explorer")

pokemon_number = st.slider("Choose a pokemon!", 1, 155)
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
response = requests.get(url)
pokemon = response.json()
name = pokemon['name']
base_experience = ['base_experience']
height = pokemon['height']
weight = pokemon['weight']
abilities = pokemon['abilities']

hp = pokemon['stats'][0]['base_stat']
attack = pokemon['stats'][1]['base_stat']
defense = pokemon['stats'][2]['base_stat']
special_attack = pokemon['stats'][3]['base_stat']
special_defense = pokemon['stats'][4]['base_stat']
speed = pokemon['stats'][5]['base_stat']

image = pokemon['sprites']['front_default']
cry = pokemon['cries']['latest']

st.write('You have selected........')

col1, col2 = st.columns(2)
with col1:
    st.title(name.title())
with col2:
    st.image(image, width = 100)

height_col, weight_col = st.columns(2)
with height_col:
    st.metric(label="Height", value=f"{height/10} m")
with weight_col:
    st.metric(label="Weight", value=f"{weight/10} kg")

st.write(f"{name.capitalize()}'s cry:")
st.audio(cry)

detailed_stats_choice = st.radio("Do you want detailed stats?", options = ['Yes', 'No'])

if detailed_stats_choice == 'Yes':
    detailed_stats = {'Stat': ['HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed'],
                      'Value' : [hp, attack, defense, special_attack, special_defense, speed] }
    detailed_stats_df = pd.DataFrame(detailed_stats)
    st.write("Detailed Stats:")
    st.dataframe(detailed_stats_df)