# Survivor Prediction Using K-Nearest Neighbors (KNN) Classifier

## Overview
This project predicts the likelihood of survival based on input features using the K-Nearest Neighbors (KNN) classification algorithm. The dataset and features used for this prediction are discussed in detail below.

## Features
* KNN classifier, which is a simple interpretable machine learning algorithm
* Scikit-learn, used for implementation
* Titanic Data of people involved in the titanic, downloaded from Kaggle
* Pandas, for data processing

## Project Setup

Please make sure you have the following installed :-
* Python 3.8+
* Python venv

Please clone the repo first to your local machine using the command below
```
git clone https://github.com/Marumo-ProG/Jada-Machine-learning-Introductions.git
```

Then create a virtual environment
```
python3 -m venv .<your venv name>
```

Then install the require packages to your repository
```
pip3 install -r requirements.txt
```

Once that is done you can run the application using
```
python3 main.py
```

## How it works
- Pandas is used to load the dataset into a dataframe
- then the data is cleaned up using pandas dataframe functions
- then we split the data from the results column (Survivors)
- split the dataset into two, training dataset and the testing dataset
- created the mathematical model using the knn classifier (k = 3)
- fed the training dataset with its results to the machine learning model
- made predictions using the testing dataset
- viewed the predicted data and the accuracy score


## Contributors
This was a two person person from the School of Algorithmics

- [*Jada Fajana*](https://github.com/JadaFajana) - Student at the Algorithmics Pretoria North

- *[Lenny Thobejane](https://github.com/Marumo-ProG)* - Instructor and Project Supervisor






