import streamlit as st
from PIL import Image

image = Image.open("actual_vs_pred.png")
new_image = image.resize((600, 400))
st.image(new_image)

image = Image.open("state_frequencies2.png")
new_image = image.resize((1000, 1000))
st.image(image)