# Stock Trend Prediction WebApp

This project is a stock trend prediction web application created using Python and Streamlit. The purpose of this web application is to allow users to input stocks they wish to predict and view visualizations of the predicted versus original values.

## Dependencies
- Python 3
- Streamlit
- Pandas
- Numpy
- Scikit-Learn
- Keras

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

## Conclusion

This stock trend prediction web application provides users with an easy-to-use interface for predicting stock trends. The use of a multi-layer LSTM recurrent neural network ensures accurate predictions, and the visualizations make it easy to understand the predicted versus original values.
