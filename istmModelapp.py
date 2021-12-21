#importing all libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st

#defining the start and end
start = '2011-01-01'
end = '2021-12-31'

#Title
st.title('Stock Trends Prediction')

#Subheader
user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = data.DataReader(user_input, 'yahoo', start, end)

#Describing Data
st.subheader('Data from 2011 - 2021')
st.write(df.describe())

#Visualizations
#plot simple closing price chart
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)

#plot closing price chart with 100MA average
st.subheader('Closing Price vs Time Chart with 100 Day Moving Average')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

#plot closing price chart with 200MA average
st.subheader('Closing Price vs Time Chart with 100 Day Moving Average & 200 Day Moving Average')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100, 'r')
plt.plot(ma200, 'g')
plt.plot(df.Close, 'b')
st.pyplot(fig)

#Now we begin to split data into Training and Testing for data predections
#so that 70% of data is in the training and 30% is in testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])

#scale data 
#all values can be scaled down between 0 and 1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)

#Load model
from tensorflow import keras
model = keras.models.load_model('keras_model.h5')

#Testing Part

#to predict values for testing data we need the previous 100 days 
#this is found in data_training.tail(100)
past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index = True)

#we must scale down these values between 0 and 1
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i,0])

x_test, y_test = np.array(x_test), np.array(y_test)

#Making predictions
y_predicted = model.predict(x_test)

#now we must scale them back up
scaler = scaler.scale_
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

#Final Visualization
st.subheader('Predictions vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original price')
plt.plot(y_predicted, 'r', label = 'Predicted price')
plt.xlabel = ('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)
