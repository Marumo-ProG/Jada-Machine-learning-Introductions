# importing machine learning modules
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# importing modules for data analysis
import pandas as pd

# loading the csv data into the dataframe
df = pd.read_csv("titanic.csv")

df = df.drop(["Name", "Ticket", "Sex", "Cabin", "Embarked"], axis=1)

df.fillna(df.mean(), inplace=True)


# Step 1: seperating the variables we need to make the predictions
x = df.drop("Survived", axis=1)  # Passenger data
y = df["Survived"]  # Target variable

# dividing the data into a training data set and a testing data set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# Step 2 : Standardizing the data
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# step 3: using the KNN classifier
classifier = KNeighborsClassifier(n_neighbors=5)

# step 4: fitting the model
classifier.fit(x_train, y_train)

# Step 5: making predictions
y_pred = classifier.predict(x_test)

print("printing the confusion matrix", y_pred)

# seeing the acuracy of the model
percent = accuracy_score(y_test, y_pred) * 100

print("Accuracy of the model is: ", percent)
