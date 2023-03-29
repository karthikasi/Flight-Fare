import pandas as pd

import streamlit as st

import pickle

pickle_in= open("Flight_model.pkl","rb")
RF=pickle.load(pickle_in)

#X=pickle.load(open("Flight_Price_model.pkl","rb"))
#model = pickle.load(open("Flight_fare_model_json","rb"))


@st.cache_data


def prediction(airline, ch_code,From,stop,to,Duration_min):
    if airline=='Vistara':
        airline =0
    elif airline == 'Air India':
        airline = 1
    if ch_code == "UK":
        ch_code = 1
    elif ch_code == "AI":
        ch_code = 0
    if From == "Mumbai":
        From = 5
    elif From =="Delhi":
        From = 2
    elif From == "Chennai":
        From = 1
    elif From == "Bangalore":
        From = 0
    elif From == "Kolkata":
        From = 4
    elif From =="Hyderabad":
        From = 3
    if to =="Mumbai":
        to = 5
    elif to == "Delhi":
        to = 2
    elif to == "Chennai":
        to = 1
    elif to == "Bangalore":
        to = 0
    elif to == "Kolkata":
        to = 4
    elif to == "Hyderabad":
        to = 3
    if stop == "1-stop":
        stop = 0
    elif stop =="Non-stop":
        stop = 2
    elif stop =="2+-stop":
        stop = 1

    prediction = RF.predict(pd.DataFrame([[airline, ch_code,From,stop,to,Duration_min]], columns=['airline', 'ch_code', 'from','stop','to','Duration_min']))
    return prediction

st.title("flight price Predictor")
st.header("Enter the Values")

airline = st.selectbox("airlines:",["Vistara","Air India"])
ch_code = st.number_input("Ch_code:",min_value=0.0, max_value=1.0, value=1.0)
From = st.selectbox("From:",["Mumbai","Delhi","Chennai","Bangalore","Kolkata","Hyderabad"])
stop = st.selectbox("stop:",["Non-stop","1-stop","2+-stop"])
to = st.selectbox("to:",["Mumbai","Delhi","Chennai","Bangalore","Kolkata","Hyderabad"])
Duration_min=st.number_input("Duration_min:",min_value=0.0,max_value=1500.0, value=1.0)
if st.button("Predict Price"):
    price = prediction(airline, ch_code,From,stop,to,Duration_min)
    st.success(f'The predicted price is {price[0]:.2f} Indian Rupees')