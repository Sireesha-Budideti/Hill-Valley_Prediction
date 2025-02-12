# -*- coding: utf-8 -*-
"""Copy of Hill-Valley-Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uQFIxq48cXhhL_CgXvlVy2XhScFAWrdB

#**HILL AND VALLEY PREDICTION BY USING LOGESTIC REGRESSION**





# **Objective :**
### The objective of using a logistic regression model to predict hill and valley regions is to classify and distinguish geographical terrain into two categories: hill regions and valley regions. This classification can be valuable in various applications, including environmental studies, urban planning, agriculture, and outdoor activities.




# **Data Source :**
### This dataset was taken from the github library which is maintained at YBI Foundation. Each record represents 100 points on a two dimensional graph. When plotted in order (from 1 through 100) as the Y coordinate, the point will create either a Hill (a "bump" in the terrain) or a Valley (a "Dip" in the terrain).





# **Import Library :**
"""

import pandas as pd

import pandas as pd

import matplotlib.pyplot as plt

"""

#**Import Data :**"""

df=pd.read_csv('/content/Hill Valley Dataset.csv')

"""# **Describe Data :**"""

df.head()

df.nunique()

"""# **Data Visualization :**"""

x = df.drop('Class', axis = 1)

plt.plot(x.iloc[0,:])
plt.title('Hill');

plt.plot(x.iloc[0,:])
plt.title('Valley');

plt.plot(x.iloc[1,:])
plt.title('Hill');

plt.plot(x.iloc[1,:])
plt.title('Valley');

plt.plot(x.iloc[10,:])
plt.title('Hill');

plt.plot(x.iloc[10,:])
plt.title('Valley');

"""
# **Data Preprocessing :**"""

df.info()

df.describe()

df.corr()

df = df.dropna()

"""# **Defining Feature Variables (X) And Target Variable (Y) :**"""

df.columns

x = df.drop('Class', axis = 1)

x.shape

x

y = df['Class']

y.shape

y

"""# **Train Test Split :**


### Scaling Data
"""

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

x = ss.fit_transform(x)

x

pd.DataFrame(x).describe()

"""### After Standardization Mean is Zero and Standard Deviation is One


"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, random_state= 2529)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""#  **Modeling :**"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit (x_train, y_train)

"""# **Model Evaluation :**"""

model.intercept_

model.coef_

"""# **Prediction :**"""

y_pred = model.predict(x_test)

y_pred

"""# **Model Accuracy :**"""

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test, y_pred))

accuracy_score(y_test,y_pred)

"""# **Explanation :**

### 1. Accuracy in Machine Leaning Model is used for Classification, Number of correct predictions

###2. It is the ratio of number of correct predictions to the total number of predictions

###3. In machine learning model accuracy score above 0.73 is treated as good-to-go-model

###4. Therefore Machine learning Model is 73% accurate in correct predictions
"""