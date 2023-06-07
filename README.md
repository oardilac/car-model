# Car Price Prediction Application

This application is a machine learning model used to predict car prices based on several parameters, such as the year of manufacture, kilometers driven, number of owners, and other features.
See a [demo](https://car-model-ywtk7siozq-wn.a.run.app)

## Project Structure

The project comprises several components:

- `modelo.ipynb`: Contains the Python notebook used for exploratory data analysis, data preprocessing, feature engineering, model training, and evaluation.
- `app.py`: A Flask application that serves model predictions through a web interface.
- `templates/index.html`: The HTML template for the web interface.

## Prerequisites

You need to have installed:

- Python 3.7+
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Jupyter

## Usage

1. Clone this repository to your local machine.
2. Install the necessary Python dependencies: `pip install -r requirements.txt`
3. Run the `modelo.ipynb` notebook to train and evaluate the models.
4. Run `app.py` to start the Flask application.
5. Navigate to the address provided in the terminal to access the application in your web browser.

## Model

The model is a regression model trained on car data to predict the selling price of a car based on several features:

- Year
- Present Price
- Kms Driven
- Owner
- Fuel Type (Petrol or Diesel)
- Seller Type (Dealer or Individual)
- Transmission Type (Manual or Automatic)

The model was trained using the ExtraTreesRegressor and other models for comparison, including RandomForestRegressor, GradientBoostingRegressor, and XGBRegressor.

## Web Application

The web application is a simple Flask application with a form where the user can input the features of a car. Upon form submission, the application will display a prediction of the car's selling price.

## Note

This project is meant for educational purposes and may not be suitable for real-world prediction of car prices.