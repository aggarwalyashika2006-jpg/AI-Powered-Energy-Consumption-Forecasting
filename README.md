# AI-Powered Energy Consumption Forecasting

This project predicts energy consumption using time-based features such as hour and day.

## Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn (MLPRegressor)
- Flask

## Project Workflow
- Dataset creation
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Model saving
- Deployment using Flask API

## How to Run
1. Install required libraries
2. Run `energy_forecast_model.ipynb`
3. Start the API using `python app.py`
4. Send POST request to `/predict`

## Sample API Input
```json
{ "hour": 14, "day": 2 }
