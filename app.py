import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Loan Approval Prediction')
st.write('This is a simple loan approval prediction app')
st.write('Please enter the details of the applicant')
model=pickle.load(open('model_stacking.pkl','rb'))
col1, col2 = st.columns(2)
with col1:
    Applicant_Income = st.number_input('Applicant Income')
with col2:
    Loan_Amount=st.number_input('Loan Amount')
col3, col4 = st.columns(2)
with col3:
    Credit_History=st.radio('Do you have Credit History', [0,1])
with col4:
    Term=st.slider('Select term in months', min_value=12, max_value=360, value=180, step=12)
if st.button('Predict'):
    data = {'Applicant_Income': Applicant_Income,
            'Loan_Amount': Loan_Amount,
            'Credit_History': Credit_History,
            'Term': Term}
    features = pd.DataFrame(data, index=[0])
    prediction = model.predict(features)
    probablity=model.predict_proba(features)
    st.subheader('The probablity of approval is : '+ str(round(probablity[0][1],2)))
    if prediction == 1:
        st.success('Loan Approved')
    else:
        st.error('Loan Rejected')


