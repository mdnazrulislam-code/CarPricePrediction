import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned Car.csv')

companies_list = sorted(car['company'].unique())
car_models_list = sorted(car['name'].unique())
year_list = sorted(car['year'].unique(), reverse=True)
fuel_type_list = car['fuel_type'].unique()

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")


def predict():
    company = company_name
    car_model = car_model_name
    year = year_name
    fuel_type = fuel_type_name
    driven = kilo_driven_name

    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                            data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))
    print(prediction)

    return str(np.round(prediction[0], 2))


st.title("Welcome to Car Price Predictor")
st.write("This app predicts the price of a car you want to sell. Try filling the details below:")
company_name = st.selectbox("Select the company:", companies_list)
car_model_name = st.selectbox("Select the model:", car_models_list)
year_name = st.selectbox("Select Year of Purchase:", year_list)
fuel_type_name = st.selectbox("Select the Fuel Type:", fuel_type_list)
kilo_driven_name = st.text_input("Enter the Number of Kilometres that the car has travelled:")

if st.button("Predict Price"):
    predicted_price = predict()
    st.balloons()
    st.write("Our Prediction")
    st.success("Model is Predicting it's a {}".format(predicted_price))
