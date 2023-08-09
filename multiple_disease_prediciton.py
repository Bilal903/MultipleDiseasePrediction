# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:33:11 2023

@author: Bilal
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

heart_disease_model = pickle.load(open('C:/Users/Administrator/OneDrive/Desktop/multiple_disease_prediction/models/heart_disease_model.sav','rb'))

diabetes_model_2  = pickle.load(open('C:/Users/Administrator/OneDrive/Desktop/multiple_disease_prediction/models/diabetes_detec_model_2.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction',
                           'Diabetes Prediction Using Svm'],
                          icons=['activity','heart'],
                          default_index=0)   

    
# Diabetes Prediction Page using SVM
if (selected == 'Diabetes Prediction Using Svm'):
    
    # page titles
    st.title('Diabetes Prediction using ML(svm)')    
# getting the input data from the user
    col1, col2, col3 = st.columns(3)
  
#
        
    with col1:
        Age = st.text_input('Age of the Person')
        
    with col2:
        hypertension = st.text_input('Do you have hyper tension(enter 0 for no and 1 for yes)')
    
    with col3:
        heartdisease = st.text_input('Do you have heart disease(enter 0 for no and 1 for yes)')
    
    with col1:
        bmi = st.text_input('Enter BMI Level')
    
    with col2:
        HbA1c_level = st.text_input('Enter HbA1c Level')
    
    with col3:
        blood_glucose_level = st.text_input('Enter blood glucose level')
    
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model_2.predict([[Age,  hypertension, heartdisease, bmi,  HbA1c_level, blood_glucose_level]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
     
# Heart Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML') 
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ID_input = st.text_input('Enter ID')
        ID = int(ID_input) if ID_input else 0  # Convert to int only if input is not empty, otherwise assign 0
    
    with col2:
        age_input = st.text_input('Enter Age in Days')
        age = int(age_input) if age_input else 0
    
    with col3:
        gender_input = st.text_input('Enter gender(enter 1 for male and 2 for female)')
        gender = int(gender_input) if gender_input else 0
    
    with col1:
        height_input = st.text_input('Enter Height')
        height = int(height_input) if height_input else 0
    
    with col2:
        weight_input = st.text_input('Enter Weight')
        weight = int(weight_input) if weight_input else 0
    
    with col3:
        ap_hi_input = st.text_input('Enter Systolic blood pressure')
        ap_hi = int(ap_hi_input) if ap_hi_input else 0
        
    with col1:
        ap_lo_input = st.text_input('Enter Diastolic blood pressure')
        ap_lo = int(ap_lo_input) if ap_lo_input else 0
    
    with col2:
        cholesterol_input = st.text_input('Enter cholesterol')
        cholesterol = int(cholesterol_input) if cholesterol_input else 0
    
    with col3:
        gluc_input = st.text_input('Enter Glucose level')
        gluc = int(gluc_input) if gluc_input else 0
         
    with col1:
        smoke_input = st.text_input('Do You Smoke(enter 0 for no and 1 for yes)')
        smoke = int(smoke_input) if smoke_input else 0
         
    with col2:
        alco_input = st.text_input('Do You Intake Alcohol(enter 0 for no and 1 for yes)')
        alco = int(alco_input) if alco_input else 0

    with col3:
        active_input = st.text_input('Do You Exercise(enter 0 for no and 1 for yes)')
        active = int(active_input) if active_input else 0

 
# code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[ID, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])                          
        
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)     