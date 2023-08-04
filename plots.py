import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

ch_data = pd.DataFrame(np.random.randn(20, 2), columns=['Line-1', 'Line-2'])

st.subheader('Line Chart')

st.line_chart(ch_data)

st.subheader('Area Chart')

st.area_chart(ch_data)

st.subheader('Bar Chart')

st.bar_chart(ch_data)

st.header('Data visualisation with matplotlib and seaborn')

st.subheader('Loading the dataframe')

dt = pd.read_csv(
    r'C:\Users\Mantej Singh\Desktop\Data_Science_GFG_WorkOuts\iris.csv')

st.dataframe(dt)

st.subheader('Simple distribution plot')

fig = plt.figure(figsize=(15, 5))

dt['species'].value_counts().plot(kind='bar')

st.pyplot(fig)

fig = plt.figure(figsize=(15, 4))

sns.distplot(dt['sepal_length'])

st.pyplot()

st.subheader('Visualisation with multiple Graph : ')

column1, column2 = st.columns(2)

with column1:
    column1.header = 'KDE=False'
    column1.write('KDE=False')
    fig = plt.figure()
    sns.distplot(dt['sepal_length'], kde=False)
    st.pyplot()

with column2:
    column2.header = 'KDE=False'
    column2.write('KDE=False')
    fig1 = plt.figure()
    sns.distplot(dt['sepal_length'], hist=False)
    st.pyplot()

st.header('Chaning the style')
column1, column2 = st.columns(2)
with column1:
    # column1.header = 'KDE=False'
    # column1.write('KDE=False')
    fig2 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(dt['petal_length'], kde=False)
    st.pyplot(fig2)

with column2:
    # column2.header = 'KDE=False'
    # column2.write('KDE=False')
    fig3 = plt.figure()
    # sns.set_style('darkgrid')
    # sns.set_context('notebook')
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(dt['petal_length'], hist=False)
    st.pyplot(fig3)

st.header('Exploring different graph : ')
fig, axes = plt.subplots(figsize=(15, 9))
axes.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

st.subheader('Count plot')
# fig, ax = plt.subplots(figsize=(15, 9))
fig = plt.figure(figsize=(16, 8))
# dt['species'].value_count().plot(kind='bar')
# st.pyplot(fig)
sns.countplot(data=dt, x='species')
st.pyplot(fig)

st.subheader('Box - Plot')
fig = plt.figure(figsize=(16, 7))
sns.boxplot(data=dt, x='species', y='sepal_length')
st.pyplot(fig)

st.subheader('Violin-Plot')
fig = plt.figure(figsize=(16, 7))
sns.violinplot(data=dt, x='species', y='sepal_length')
st.pyplot(fig)
