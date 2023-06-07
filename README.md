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

## Installation

```
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```
streamlit run app.py
```

This will start the Streamlit server and open the application in your default browser. You can then experiemnt with the different trading startegies provided. The application will recommend trades based on the given strategy.

## How to Use

1. Input the stock symbol you wish to predict in the provided input field.
2. Click the "Predict" button to generate the predicted versus original values.
3. The predicted versus original values will be displayed in a table and visualized in a line graph.

## How it Works

The predictions are made using a various algorithmic trading strategies to predict stock returns. The raw data is displayed in a table and the predicted versus original values are visualized in a line graph. The web application is created using Streamlit, a Python library for building web applications. 

## Data Preparation

The project begins by fetching historical and real-time market data using Interactive Brokers' TWS API. The data is then cleaned to ensure its quality and reliability. I split the data 60% for training and 40% for testing the model.

## Models

### Long Short-term Memory RNN Model 

This model is a recurrent neural network which is used to learn order dependence in sequence prediction problems. Due to its capability of storing past information, LSTM is very useful in predicting stock prices. This is because the prediction of a future stock price is dependent on the previous prices.

### Custom Strategy Signal

I developed a custom strategy signal using the x-gradient boosting model. This signal incorporates support and resistance levels, price movements, and candlestick patterns to detect reversals in the trend. The custom strategy signal has shown positive returns in a classical passive strategy, making it a promising addition to ML and neural networks.

### Classification Model

This model is a supervised neural network classifier with technical indicators as input features (e.g. RSI, MA Slope, SAR slope, and a custom strategy signal). The goal is to predict whether the trend will be up or down, resulting in two categories: 1 (up) or 0 (down). The main challenge in such models lies in determining the optimal number of hidden layers and nodes between the input features and the final output results.

The number of hidden layers can range from one to a large number, and the number of nodes can vary from one to a few hundred. Finding the optimal configuration requires experimentation and a trial-and-error approach, taking into account the expertise of the data scientist building the model.

### Logistic Regression Model

This model uses logistic regression, a type of supervised learning algorithm used for classification, to predict the direction of the asset (+/-) as the dependent variable. The independent variable is the prior N days' asset directions. The logistic regression model uses a sigmoid function to produce a probability score, which is then thresholded to determine the predicted direction of the asset. 

Note that this model assumes that there are no trading costs to simplify the problem. Additionally, the model focuses on predicting asset returns rather than absolute prices.

## Future Work

This project can be further improved by using more advanced machine learning algorithms such as neural networks and decision trees. Additionally, incorporating more features such as volume and news sentiment can improve the accuracy of the model.
