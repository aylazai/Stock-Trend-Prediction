# Stock Trend Prediction Web Application

<img width="543" alt="image" src="https://user-images.githubusercontent.com/90855844/236690035-9bce1fa9-9b20-47e9-b6cf-660250ba831f.png">

This project is a stock trend prediction web application created using Python and Streamlit. The purpose of this web application is to allow users to input stocks they wish to predict and view visualizations of the predicted versus original values.

## Dependencies
- Python 3
- Streamlit
- Pandas
- Numpy
- Scikit-Learn
- Keras
- Backtesting

## Getting Started

1. Clone the repository using the following command:
```
git clone https://github.com/{username}/{repository_name}.git
```
2. Navigate to the project directory using the following command:
```
cd {Stock-Trend-Prediction}
```
3. Install the necessary dependencies using the following command:
```
pip install -r requirements.txt
```
4. Run the web application using the following command:
```
streamlit run app.py
```

## How to Use

1. Input the stock symbol you wish to predict in the provided input field.
2. Click the "Predict" button to generate the predicted versus original values.
3. The predicted versus original values will be displayed in a table and visualized in a line graph.

## How it Works

The predictions are made using a multi-layer LSTM recurrent neural network to predict the last value out of a sequence of values. The raw data is displayed in a table and the predicted versus original values are visualized in a line graph. The web application is created using Streamlit, a Python library for building web applications. 

## Custom Strategy Signal

I developed a custom strategy signal using the x-gradient boosting model. This signal incorporates support and resistance levels, price movements, and candlestick patterns to detect reversals in the trend. The custom strategy signal has shown positive returns in a classical passive strategy, making it a promising addition to ML and neural networks.

## Neural Network Model

The chosen model for this project is a supervised neural network classifier with technical indicators as input features (e.g. RSI, MA Slope, SAR slope, and a custom strategy signal). The goal is to predict whether the trend will be up or down, resulting in two categories: 1 (up) or 0 (down). The main challenge in such models lies in determining the optimal number of hidden layers and nodes between the input features and the final output results.

The number of hidden layers can range from one to a large number, and the number of nodes can vary from one to a few hundred. Finding the optimal configuration requires experimentation and a trial-and-error approach, taking into account the expertise of the data scientist building the model.

## Data Preparation

The project begins by fetching historical market data using Interactive Brokers native API. The data is then cleaned to ensure its quality and reliability. I split the data 60% for training and 40% for testing or validating the model.

