import streamlit as st

def main():
    st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

    st.title("Welcome to Car Price Predictor")

    st.write("This app predicts the price of a car you want to sell. Try filling the details below:")

    companies = ["Company1", "Company2", "Company3"]  # Replace with your actual list of companies
    car_models = {"Company1": ["ModelA", "ModelB"], "Company2": ["ModelX", "ModelY"]}  # Replace with your actual dictionary of models
    years = [2018, 2019, 2020]  # Replace with your actual list of years
    fuel_types = ["Petrol", "Diesel", "Electric"]  # Replace with your actual list of fuel types

    company = st.selectbox("Select the company:", companies)
    model = st.selectbox("Select the model:", car_models.get(company, []))
    year = st.selectbox("Select Year of Purchase:", years)
    fuel_type = st.selectbox("Select the Fuel Type:", fuel_types)
    kilo_driven = st.text_input("Enter the Number of Kilometres that the car has travelled:")

    if st.button("Predict Price"):
        prediction = predict_price(company, model, year, fuel_type, kilo_driven)
        st.success(f"Prediction: ₹{prediction}")

def predict_price(company, model, year, fuel_type, kilo_driven):
    # Add your machine learning model prediction logic here
    # You may need to import necessary libraries and load your trained model
    # Replace this placeholder with the actual prediction logic
    prediction = 5000  # Replace with your actual prediction
    return prediction

if __name__ == "__main__":
    main()
