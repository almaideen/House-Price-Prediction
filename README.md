**House Price Prediction Using Machine Learning**

This repository contains a project focused on predicting house prices based on various features using machine learning models. The project showcases the application of data preprocessing, feature engineering, and machine learning algorithms to create a predictive model for housing prices.

**Project Overview**

Accurately predicting house prices is crucial for buyers, sellers, and real estate professionals. In this project, we use a dataset containing various features such as location, size, number of rooms, and other relevant factors to train a machine learning model that can predict the price of a house. The project involves data cleaning, feature selection, model training, and evaluation to ensure the predictions are as accurate as possible.

**Data Collection** 

Data for this business problem is collected from zillow.com website using RapidAPI. Zillow.com is a popular online US real estate marketplace that provides users with a comprehensive platform to buy, sell, rent, and finance homes. Launched in 2006, Zillow has become a key player in the real estate industry, offering a wide range of tools and resources for both consumers and professionals. Zillow aggregates millions of property listings, giving users access to homes for sale, rent, and even those not currently on the market. Users can filter searches by price, location, property type, and other criteria. Collected those property listing data and done feature selection and feature engineering on top of it to get dataset for this business problem.

**Features**

The dataset used in this project includes the following features:

*Annual Home Owner Insurance*: Homeowners insurance is a form of property insurance that covers losses and damages to your residence, along with furnishings and other assets in the home. Homeowners insurance also provides liability coverage against accidents in the home or on the property.

*State*: State in which the house is located. 

*Year Built*: Year in which house was built

*Living Area*: Area of the living space in house in SQFT

*Bathrooms*: Number of Bathroom in the House

*Bedrooms*: Number of Bedrooms in the House

*Home Type*: Residential Type of the House. Ex: Single Family, Multi Family

**Models Trained**

The project explores the following machine learning models:

Linear Regression
Decision Tree
Random Forest Regressor
XGBoost Regressor

**Result**

The best-performing model is Random Forest Regressor which achieved an R² score of 0.998 on the train data and 0.996 on the test data, indicating its effectiveness in predicting house prices based on the selected features.

**Deployment**

Streamlit is the webframework used to build app for the business problem and deployed on Streamlit Cloud. You can access the app using the [link](https://us-house-price-prediction.streamlit.app/).

