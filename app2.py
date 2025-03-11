import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open(r'C:\Edu\coding\Projects\Project2\your_model.pkl', 'rb'))
df_rider = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_rider.pkl', 'rb'))
df_class = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_class.pkl', 'rb'))
df_season = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_season.pkl', 'rb'))
df_country = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_country.pkl', 'rb'))
df_motor = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_motor.pkl', 'rb'))
df_team = pickle.load(open(r'C:\Edu\coding\Projects\Project2\df_team.pkl', 'rb'))

st.title('Moto Racing Winner Prediction')

RiderName = st.selectbox(
    "Rider Name",
    (df_rider)
)

Class = st.selectbox(
    "Class",
    (df_class)
)

season = st.selectbox(
    "Year",
    (df_season)
)

country = st.selectbox(
    "Country",
    (df_country)
)

motor = st.selectbox(
    "Motorcycle",
    (df_motor)
)

teams = st.selectbox(
    "Team",
    (df_team)
)

races = st.number_input(min_value=0, max_value=20, label='Number of Races')

wins = st.number_input(min_value=0, max_value=13, label='Number of Wins')

podium = st.number_input(min_value=0, max_value=18, label='Numer of Podium')

pole = st.number_input(min_value=0, max_value=13, label='Number of Poles')

fastest_lap = st.number_input(min_value=0, max_value=12, label='Number of Fastest Laps')

points = st.number_input(min_value=0, max_value=508, label='Number of Points')

position = st.number_input(min_value=0, max_value=47, label='What is the Position of rider')

def predict(rider_name, rider_class, season, home_country, motorcycle, team, races_participated, wins, podium, pole, fastest_lap, points, placed):
    """Predicts world championship win/loss."""
    input_data = pd.DataFrame({
        'rider_name': [rider_name],
        'class': [rider_class],
        'season': [season],
        'home_country': [home_country],
        'motorcycle': [motorcycle],
        'team': [team],
        'races_participated': [races_participated],
        'wins': [wins],
        'podium': [podium],
        'pole': [pole],
        'fastest_lap': [fastest_lap],
        'points': [points],
        'placed': [placed]
    })
    prediction = model.predict(input_data)[0]
    return prediction

if st.button('Win or Lose', type='primary'):
    prediction = predict(RiderName, Class, season, country, motor, teams, races, wins, podium, pole, fastest_lap, points, position)
    if prediction == 1:
        st.success('Win')
    else:
        st.error('Lose')