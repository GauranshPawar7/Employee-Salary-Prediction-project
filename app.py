import streamlit as st
import joblib
import numpy as np



# --- Banner Image at the top ---
st.image("C:\\Users\\Gauransh Pawar\\OneDrive\\Desktop\\20191202130611-salarypicture.jpeg", use_column_width=True)

st.title(" Salary Prediction App")

st.divider()

st.write("This app predicts the salary of a person based on their years of experience and job rate.")

# Input section
st.subheader("📥 Input Details")
col1, col2 = st.columns(2)

with col1:
    years_of_experience = st.number_input("Enter years of experience:", value=1, step=1, min_value=0)
with col2:
    job_rate = st.number_input("Enter job rate (1.0 - 5.0):", value=3.5, step=0.5, min_value=0.0)

x = [years_of_experience, job_rate]

st.divider()

# Prediction
if st.button(" Predict Salary"):
    st.write("Calculating the predicted salary...")
    with st.spinner("Please wait..."):
        model = joblib.load("linearmodel.pkl")
        input_data = np.array([x])
        prediction = model.predict(input_data)[0]
        formatted_salary = "${:,.2f}".format(float(prediction))
        st.success("Prediction complete!")
        st.markdown(f" Predicted Salary: {formatted_salary}")
else:
    st.warning("Please click the button to predict the salary.")
