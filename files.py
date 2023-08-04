import streamlit as st
import pandas as pd

st.subheader('Uploading the Files : ')

dt = st.file_uploader("Upload the necessary file : ", type=['csv', 'xlsx'])

# st.table(dt.head())

# df1 = pd.read_csv('C:\Users\Mantej Singh\Desktop\Data_Science_GFG_WorkOuts\Products.csv')
# if df1 is not None :
#     st.table(df1.head())

# if dt is not None:
#     st.dataframe(dt)

st.subheader("Image")
# st.image('C:\Users\Mantej Singh\Desktop\Data_Science_GFG_WorkOuts\img.png')

dt2 = st.file_uploader("Upload the necessary image : ", type=['png', 'jpeg'])
if dt2 is not None:
    st.image(dt2)

st.subheader('Audio')
dt2 = st.file_uploader('Upload the file :', type=['mp3'])
if dt2 is not None:
    st.audio(dt2)

st.subheader('Videos')

dt2 = st.file_uploader('Upload the file', type=['mkv', 'mp4'])
if dt2 is not None:
    st.video(dt2)
