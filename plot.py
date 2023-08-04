import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.title('Altair Scatter Plot')
ch_data = pd.DataFrame(np.random.randn(
    500, 5), columns=['a', 'b', 'c', 'd', 'e'])
chart = alt.Chart(ch_data).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a', 'b', 'c', 'd'])
st.altair_chart(chart)

st.title('Interactive Line Chart')
df = pd.read_csv(
    r'C:\Users\Mantej Singh\Desktop\Data_Science_GFG_WorkOuts\lang_data.csv')
lang_list = df.columns.tolist()
lang_ch = st.multiselect('Choose your language : ', lang_list)
new_df = df[lang_ch]
st.line_chart(new_df)

st.title('Area Chart')
st.area_chart(new_df)

st.title('Data Visualisation using plotly')
df = pd.read_csv(
    r'C:\Users\Mantej Singh\Desktop\Data_Science_GFG_WorkOuts\tips.csv')
st.dataframe(df.head())
st.title('Pie Chart')
fig = px.pie(df, values='total_bill', names='day')
st.plotly_chart(fig)

st.title('Pie Chart with multiple paramete')
fig = px.pie(df, values='total_bill', names='day',
             opacity=0.7, color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.title('Histogram : ')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)
hist_data = [x1, x2, x3]
group_label = ['Group-1', 'Group-2', 'Group-3']
fig = ff.create_distplot(hist_data, group_label, bin_size=[0.1, 0.25, 0.5])
st.plotly_chart(fig)
