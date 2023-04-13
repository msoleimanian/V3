import streamlit as st
import pandas as pd
import plotly.express as px
st.session_state.page_select = st.sidebar.radio('Pages', ['IMPORT YOUR DATA', 'Specifying the type of data is in the dataset', 'Make your report' , 'Draw Graphs' , 'Comparing two bases'])

st.title(" IMPORT YOUR DATA ")
st.text("Please enter your dataset.")

uploadFile = st.file_uploader("Upload your file here")
if uploadFile:
    st.text("The file successfully is uploaded")
    dataframe = pd.read_csv(uploadFile)
#   SHOW DATA
#    st.header('Data Statistics')
#    st.write(dataframe)


    butly1 , butly2 = st.columns(2)

    if butly1.button("Summary"):
        print('Summary clicked')
        st.header(' SUMMARY ')
        st.header('Data Statistics')
        st.write(dataframe)
        print(dataframe['Pot ID'])

    elif butly2.button('Pridiction'):
        print('pridiction')

    #   Filter the Data
    st.header('Specifying the type of data is in the dataset')
    col3, col4, col5 = st.columns(3)

    col3.text("Time type:")
    for cloumn in dataframe.columns.values.tolist():
       response = col3.checkbox('T : ' + cloumn)

    col4.text("Base Type")
    for cloumn in dataframe.columns.values.tolist():
        response = col4.checkbox('B : ' + cloumn)

    col5.text("Metric type:")
    for cloumn in dataframe.columns.values.tolist():
        response = col5.checkbox('M : ' + cloumn)

    st.header('MAKE YOUR REPORT:')
    st.text('STEP ONE : Please specify Base values')
    col1, col2 = st.columns(2)
    ques = col1.radio(

        "PotID",

        ('1', '2' , '3'))

    ques = col2.radio(

        "SubPotID",

        ('1A', '1B', '1C'))

    st.text('STEP TWO : Please specify TIME values')
    ques = st.radio(

        "Timestamp",

        ('timestamp','season'))


    colarray = []
    colarray = st.columns(8)
    st.text('STEP Three : Specify the criteria for which you want to draw graphs.')
    response = st.checkbox('color of the grain')
    response = st.checkbox('shape of the grain ')
    response = st.checkbox('height of the grain ')
    response = st.checkbox('height of the rice crop')
    response = st.checkbox('color of the rice crop')
    response = st.checkbox('height of the tiller')
    response = st.checkbox('leaves')
    response = st.checkbox('longest leaves')

    st.header('Draw Graphs')








