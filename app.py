import streamlit as st
import numpy as np
import pickle
st.title('Placement Prediction')
#Manual Data Set Format = ['Age', 'Gender', 'Streams', 'Internships', 'CGPA', 'Trainings', 'HistoryOfBacklogs']
age = st.text_input("Enter Your Age", "Type Here ...")
gender = st.selectbox("Gender",('<select>', 'Male', 'Female'))
stream = st.selectbox("What is your Stream?",('<select>', 'Electronics And Communication', 'Computer Science',
                                              'Information Technology', 'Mechanical', 'Electrical', 'Civil'))
internship = st.selectbox("Do you have any internship experience",('<select>', 'Yes', 'No'))
cgpa = st.text_input("Enter Your CGPA/SGPA", "Type Here ...")
training = st.selectbox("Did you complete any Technical Training/s?",('<select>', 'Yes', 'No'))
backlog = st.text_input("Enter your current backlog/s", "Type Here ...")

if gender=="Male":
    gender=0;
else:
    gender=1;
if stream=='Electronics And Communication':
    stream=0;
elif stream=='Computer Science':
    stream=1;
elif stream=='Information Technology':
    stream=2;
elif stream=='Mechanical':
    stream=3;
elif stream=='Electrical':
    stream=4;
elif stream=='Civil':
    stream=5;
if internship=='Yes':
    internship=1;
else:
    internship=0;
if training=='Yes':
    training=1;
else:
    training=0;

features=np.array([[age,gender,stream,internship,cgpa,training,backlog]])
RandomForest = pickle.load(open('Random_Forest.pkl','rb'))

if st.button("Predict My Chances Of Placement"):
    p = RandomForest.predict(features)
    if p==1:
        st.write("High Chance Of Placement. 🏆")
        st.write("Keep Practicing ! ⌚")
    else:
        st.write("Low Chance of Placement. 📉")
        st.write("Please improve your skills. 🔑")
