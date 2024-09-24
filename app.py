import pickle
import streamlit as st

# Loading the trained model
with open('classifier.pkl', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)

@st.cache_data()  # Use @st.cache_data() for caching in newer Streamlit versions
def prediction(income, age, loan, LTI):
    # Making Predictions
    pred = classifier.predict([[income, age, loan, LTI]])

    if pred == 0:
        return "Not Eligible"
    else:
        return "Eligible"

# This is the main function in which we define our webpage
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style="background-color: #F4D03F; padding:10px">
    <h2 style="color: black; text-align: center;">Credit Score Eligibility Prediction App</h2>
    </div>
    '''
    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for user data
    income = st.number_input("Income")
    age = st.number_input("Age")
    loan = st.number_input("Loan Amount")
    LTI = st.number_input("Long Term Interest")

    result = ""

    # When 'Predict' is clicked, make prediction and store it
    if st.button("Predict"):
        result = prediction(income, age, loan, LTI)  # Pass individual parameters
        st.success(f"Prediction: {result}")

if __name__ == '__main__':
    main()
