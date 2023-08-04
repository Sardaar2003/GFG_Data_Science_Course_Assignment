import streamlit as st
st.title('Welcome to GeeksforGeeks')  # title
st.header('This is the life chaning application')  # header
st.subheader('This is the subheader part')  # subheader
st.text('Hello World')  # Text

st.markdown('# Hi')  # Markdown
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.success('Data is submitted successfully ')  # Success

st.info('Information!')  # Information

st.warning('Warning!')  # Warning

st.error('Error')  # Error

# Displaying particular function

exp = ZeroDivisionError('Division is not possible with 0')

st.exception(exp)

st.help(ZeroDivisionError)  # Help function leads to documentation

st.write("range(1,10)")  # Writing as a text

st.write(range(1, 10))

st.write("1+2+3")

st.write(1+2+3)

st.code('x=10\n for i in range(x):\n \tprint(i)')  # Code

st.checkbox('Male')  # CheckBox

# st.checkbox('Female')

if (st.checkbox('Female')):
    st.write('You are eligible')

radioB = st.radio('Select your gender : ',
                  ('Male', 'Female', 'Other'))  # Radio Button
if (radioB == 'Male'):
    st.write("You are a male")
elif radioB == 'Female':
    st.write("You are a female")
else:
    st.write('You are others')

# Select Box
selectBox = st.selectbox("Select your area of interest : ", ['Data analysis',
                                                             'web scraping', 'machine learning', 'deep learning'])

st.write("You have selected : ", selectBox)

# MultiSelect Box

multiSelect = st.multiselect("Select your area of interest : ", [
    'Data analysis', 'web scraping', 'machine learning', 'deep learning'])
st.write("You have selected : ", len(multiSelect), multiSelect)


# Button

st.button("Button")

# SLider

vol = st.slider('Select the level', 1, 100, step=1)
st.write('The volume is ', vol)

# Taking User input
name = st.text_input('Enter your name : ')
# Password :
password = st.text_input('Enter your password : ', type='password')

# Text Area
text = st.text_area('Write something about urself')
st.write(text)

# Input-Number

st.number_input('Select the number : ', 18, 110)

# Input Date

st.date_input('Enter the date : ')

# Input Time

st.time_input('Enter the time : ')
