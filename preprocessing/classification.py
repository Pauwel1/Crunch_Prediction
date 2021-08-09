import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score
from datacleaner import dataCleaner

churn = pd.read_csv("assets/BankChurners.csv")
X, y = dataCleaner(churn)

# create train and test set (random_state = 42, because it is used for official examples)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# balance out the dataset with SMOTE
balanced = SMOTE(random_state = 42)
X_bal, y_bal = balanced.fit_resample(X_train, y_train)

# Try out different classifiers
def ClassPrediction(classifier, mdl):
  model = classifier.fit(X_bal, y_bal)

  y_hat = model.predict(X_train)
  acc = recall_score(y_train, y_hat, pos_label = 2)
  results.loc[mdl, 'Train'] = acc

  y_hat = model.predict(X_test)
  acc = recall_score(y_test, y_hat, pos_label = 2)
  results.loc[mdl, 'Test'] = acc

# Storing Results
results = pd.DataFrame()

# Models
stage = 'Classification Model'
ClassPrediction(DecisionTreeClassifier(), 'Decision Tree')
ClassPrediction(RandomForestClassifier(), 'Random Forest')
ClassPrediction(GradientBoostingClassifier(), 'Gradient Boost')
ClassPrediction(AdaBoostClassifier(), 'AdaBoost')
print(results)