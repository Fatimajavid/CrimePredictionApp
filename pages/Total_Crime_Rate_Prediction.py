# Import libraries
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="DataCops",
    page_icon="👮‍♂️",
)

st.header("Total Crime Prediction" )

def user_input_features():
    numbUrban = st.number_input('Enter number of people living in areas classified as urban')
    numUnderPov = st.number_input('Enter number of people under the poverty level')
    population = st.number_input('Enter the the population of the community')
    numKidsBornNeverMar = st.number_input('Enter the number of kids born to unmarried parents')
    numStreet = st.number_input('Enter the number of homeless people on the street')
    data = {'numbUrban': numbUrban,
            'numUnderPov': numUnderPov,
            'population': population,
            'numKidsBornNeverMar': numKidsBornNeverMar,
            'numStreet': numStreet}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.markdown("")
st.markdown("")
# Button to start prediction, Once make_prediction button is clicked...
make_prediction = st.button('Submit to make prediction.')

# # Load the model you already created...
model = pickle.load(open('models/crime_model.pkl', 'rb'))

if make_prediction:
    # make a prediction

    st.markdown("")

# # Apply Model to Make Prediction
    prediction = model.predict(df)

    st.success('Prediction')
    st.markdown("Predicted total crime rate is " + str(prediction[0]) + ".")