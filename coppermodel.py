import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load your trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

modell = joblib.load('modellgbm.pkl')
scalerl = joblib.load('scalerlgb.pkl')

# Title of the app
st.title('Copper Sales Prediction: Classification & Regression')

tab1, tab2 = st.tabs(["Classification", "Regression"])

with tab1:
    encoding_mapping = {
        0: 'Draft',
        1: 'Lost',
        2: 'Not lost for AM',
        3: 'Offerable',
        4: 'Offered',
        5: 'Revised',
        6: 'To be approved',
        7: 'Won',
        8: 'Wonderful'
    }

    # Input fields
    item_date = st.text_input('Item Date', key='item_date_classification')
    country = st.number_input('Country', format='%d', key='country_classification')
    selling_price = st.number_input('Selling Price', key='selling_price_classification')
    application = st.text_input('Application', key='application_classification')
    quantity_tons = st.number_input('Quantity (tons)', key='quantity_tons_classification')
    thickness = st.number_input('Thickness', key='thickness_classification')
    customer = st.text_input('Customer', key='customer_classification')

    # Button to make prediction
    if st.button('Predict Status', key='predict_status'):
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'item_date': [item_date],
            'country': [country],
            'selling_price': [selling_price],
            'application': [application],
            'quantity tons': [quantity_tons],
            'thickness': [thickness],
            'customer': [customer]
        })

        # Handle categorical data if necessary
        # You might need to apply label encoding or other preprocessing steps here

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)

        predicted_status = encoding_mapping[prediction[0]]

        # Display the prediction
        st.write(f'The predicted status is: {predicted_status}')

    st.write("Please find the Status Encoding Mapping:")
    for key, value in encoding_mapping.items():
        st.write(f"{key} -> {value}")

with tab2:
    st.sidebar.title("Encoding Values")
    st.sidebar.write("Item Type Encoding Value")
    st.sidebar.write("5 -> Revised, 6 -> To be approved, 3 -> Offerable, 1 -> Lost, 2 -> Not lost for AM, 0 -> Draft, 4 -> Offered")
    st.sidebar.write("Status Encoding Value")
    st.sidebar.write("7 -> Won,0 -> Draft,6 -> To be approved,1 -> Lost,2 ->,Not lost for AM,8 -> Wonderful,5 -> Revised,4 -> Offered,3 -> Offerable")

    item_type = st.selectbox('Item Type', ['0', '1', '2', '3', '4', '5', '6'], key='item_type_regression')
    status = st.selectbox('Status', ['0', '1', '2', '3', '4', '5', '6', '7', '8'], key='status_regression')
    time_since_item_order = st.number_input('Time Since Item Order', key='time_since_item_order_regression')
    application = st.text_input('Application', key='application_regression')
    quantity_tons = st.number_input('Quantity (tons)', key='quantity_tons_regression')
    thickness = st.number_input('Thickness', key='thickness_regression')
    width = st.number_input('Width', key='width_regression')
    customer = st.text_input('Customer', key='customer_regression')

    if st.button('Predict Selling Price', key='predict_selling_price'):
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'item type': [item_type],
            'status': [status],
            'time_since_item_order': [time_since_item_order],
            'application': [application],
            'quantity tons': [quantity_tons],
            'thickness': [thickness],
            'width': [width],
            'customer': [customer]
        })

        # Handle categorical data if necessary
        # You might need to apply label encoding or other preprocessing steps here

        # Scale the input data
        input_data_scaled = scalerl.transform(input_data)

        # Make prediction
        prediction_selling = modell.predict(input_data_scaled)

        # Display the prediction
        st.write(f'The predicted Selling Price is: {prediction_selling[0]}')

    
