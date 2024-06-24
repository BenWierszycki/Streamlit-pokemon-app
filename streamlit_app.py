# import packages 

import requests
import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("Pokemon Explorer")

# choosing pokemon slider
pokemon_number = st.slider("Choose a pokemon!", 1, 155)
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
response = requests.get(url)
pokemon = response.json()

# variables assigned for selected pokemon
pokemon_id = pokemon['id']
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

# displaying name and image
col1, col2 = st.columns(2)
with col1:
    st.title(name.title())
with col2:
    st.image(image, width = 100)

# displaying height and weight
height_col, weight_col = st.columns(2)
with height_col:
    st.metric(label="Height", value=f"{height/10} m")
with weight_col:
    st.metric(label="Weight", value=f"{weight/10} kg")

# adding pokemon's cry
st.write(f"{name.capitalize()}'s cry:")
st.audio(cry)

# yes/no for extra statistics
detailed_stats_choice = st.radio("Do you want detailed stats?", options = ['Yes', 'No'])

if detailed_stats_choice == 'Yes':
    detailed_stats = {'Stat': ['HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed'],
                      'Value' : [hp, attack, defense, special_attack, special_defense, speed] }
    detailed_stats_df = pd.DataFrame(detailed_stats)
    st.write("Detailed Stats:")
    st.dataframe(detailed_stats_df)


## selecting two pokemon and compare their stats
if detailed_stats_choice == 'Yes':
    st.subheader('Stats comparison')

    st.write("Select a Pokemon to compare stats with: ")

# function to create list of all the pokemon names
    def fetch_pokemon_names():
        all_pokemon_names = []
        for pokedex_number in range(1, 156):
            url = f'https://pokeapi.co/api/v2/pokemon/{pokedex_number}/'
            response_2 = requests.get(url)
            pokemon_2 = response_2.json()
            poke_name = pokemon_2['name'].capitalize()
            all_pokemon_names.append(poke_name)
        all_pokemon_names.sort()
        return all_pokemon_names

    all_pokemon_names = fetch_pokemon_names()

#creating a dropdown of all the names
    selected_comparison_pokemon = st.multiselect('Select Pokemon', all_pokemon_names, [])

    if selected_comparison_pokemon:
        comparison_names_str = ', '.join(selected_comparison_pokemon)
        st.write(f"You have chosen to compare {name} with {comparison_names_str}.")


# I have been trying to work out how to get the stats comparions working but haven't managed to get it working yet!
# i havent worked out how to use the name of the selected pokemon to get the stats of it to compare to the intially selected one
# so for now it is just another illustration of the stats unfortunately

    stats_col1, stats_col2, stats_col3 = st.columns(3)
    with stats_col1:
        st.metric(label="HP", value= f"{hp}", delta="")
        st.metric(label="Speed", value= f"{speed}", delta="")
    with stats_col2:
        st.metric(label="Attack", value= f"{attack}", delta="")
        st.metric(label="Special Attack", value= f"{special_attack}", delta="")
    with stats_col3:
        st.metric(label="Defense", value=f"{defense}", delta="")
        st.metric(label="Special Defense", value= f"{special_defense}", delta="")



