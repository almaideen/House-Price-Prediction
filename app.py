import streamlit as st
import pickle
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import os

#Load the Encoder
with open('encoder.pkl'),'rb') as f:
    encoder = pickle.load(f)

#Load the Scaler
with open('scaler.pkl','rb') as f:
    scaler = pickle.load(f)

#Load the model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

#set up streamlit app
st.set_page_config(page_title='House price prediction')
st.title("US Real Estate - House Price Prediction")

#Getting input data    
AnnualHomeOwnerInsurance = st.number_input("Enter the Annual HomeOwner Insurance Amount in USD")
State = st.selectbox("Select the state in which house is located",('AK', 'MO', 'CA', 'NY', 'PA', 'VA', 'MD', 'MT', 'FL', 'NC', 'IL',
       'WA', 'OH', 'WI', 'MS', 'IA', 'NV', 'MA', 'CO', 'WV', 'TX', 'OR',
       'NM', 'SC', 'ID', 'MN', 'GA', 'AZ', 'AL', 'NJ', 'IN', 'DC', 'CT',
       'ME', 'WY', 'MI', 'PR', 'AR', 'ON', 'KY', 'SK', 'HI', 'OK', 'TN',
       'KS', 'ND', 'LA', 'RI', 'DE', 'VT'))
YearBuilt = st.number_input("Enter the year house was built")
LivingArea = st.number_input("Enter the Living Area of the house in SQFT")
Bathrooms = st.number_input("Enter the number of bathrooms in the house")
Bedrooms = st.number_input("Enter the number of bedrooms in the house")
HomeType = st.selectbox("Select the type of house",('SINGLE_FAMILY', 'CONDO', 'MULTI_FAMILY', 'TOWNHOUSE', 'APARTMENT',
       'HOME_TYPE_UNKNOWN', 'LOT', 'MANUFACTURED'))

data = {
    'AnnualHomeOwnerInsurance':[AnnualHomeOwnerInsurance],
    'State':[State],
    'YearBuilt':[YearBuilt],
    'LivingArea':[LivingArea],
    'Bathrooms':[Bathrooms],
    'Bedrooms':[Bedrooms],
    'HomeType':[HomeType]
}
df = pd.DataFrame(data)
if st.button('Predict'):
    #Encoding
    categorical_columns=['State','HomeType']
    encoded_columns = encoder.transform(df[categorical_columns])
    encoded_columns_df = pd.DataFrame(encoded_columns,columns=encoder.get_feature_names_out(categorical_columns))
    df_encoded = pd.concat([df,encoded_columns_df],axis=1)
    df_encoded = df_encoded.drop(categorical_columns,axis=1)

    #Scaling
    scaled_data = scaler.transform(df_encoded)

    #prediction
    prediction = model.predict(scaled_data)
    st.write(f'Predicted value for your house is {prediction[0]} USD')
