# Import libraries
import streamlit as st
import pandas as pd
import pickle
import requests
import json

st.set_page_config(
    page_title="DataCops",
    page_icon="👮‍♂️",
)

st.header("Total Crime Prediction" )

state = st.selectbox('State', ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'])

def user_input_features():
    numbUrban = st.number_input('Enter number of people living in areas classified as urban', min_value=0)
    numUnderPov = st.number_input('Enter number of people under the poverty level', min_value=0)
    population = st.number_input('Enter the the population of the community', min_value=0)
    numKidsBornNeverMar = st.number_input('Enter the number of kids born to unmarried parents', min_value=0)
    numStreet = st.number_input('Enter the number of homeless people on the street', min_value=0)
    data = {'numbUrban': numbUrban,
            'numUnderPov': numUnderPov,
            'population': population,
            'numKidsBornNeverMar': numKidsBornNeverMar,
            'numStreet': numStreet}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.markdown("")
# Button to start prediction, Once make_prediction button is clicked...
make_prediction = st.button('Submit to make prediction.')

# Load the model you already created...
model = pickle.load(open('models/crime_model.pkl', 'rb'))

if make_prediction:
    st.markdown("")
    # Apply Model to Make Prediction
    prediction = model.predict(df)

    # FBI API
    response = requests.get("https://api.usa.gov/crime/fbi/sapi/api/estimates/states/"+state+"/2020/2021?API_KEY="+st.secrets["api_key"])
    data_json = response.json()
    data = data_json['results']
    total_crime = data[0]['homicide']+data[0]['rape_revised']+data[0]['robbery']+ \
    data[0]['aggravated_assault']+data[0]['burglary']+data[0]['larceny']+ \
    data[0]['motor_vehicle_theft']+data[0]['arson']
    
    percentage_diff = (int(prediction[0]) - int(total_crime)) / int(total_crime)
    if percentage_diff < 0:
        percentage_diff = abs(round((percentage_diff*100), 2))
        st.success("Based on the values provided for the above features, the total number of crimes that are likely to occur in this community is  " + str(int(prediction[0])) + " which is " + str(percentage_diff) + "% less than state level.")
    else:
        percentage_diff = abs(round((percentage_diff*100), 2))
        st.warning("Based on the values provided for the above features, the total number of crimes that are likely to occur in this community is  " + str(int(prediction[0])) + " which is " + str(percentage_diff) + "% higher than state level.")

    st.subheader("Compare crime statistics to state level")
    st.markdown("State: " + data[0]['state_abbr'])
    st.markdown("Population: " + str(data[0]['population']))
    st.markdown("Murder: " + str(data[0]['homicide']))
    st.markdown("Rape: " + str(data[0]['rape_revised']))
    st.markdown("Robbery: " + str(data[0]['robbery']))
    st.markdown("Assault: " + str(data[0]['aggravated_assault']))
    st.markdown("Burglary: " + str(data[0]['burglary']))
    st.markdown("Larceny: " + str(data[0]['larceny']))
    st.markdown("Auto Theft: " + str(data[0]['motor_vehicle_theft']))
    st.markdown("Arson: " + str(data[0]['arson']))
    st.markdown("Total crime: " + str(total_crime))