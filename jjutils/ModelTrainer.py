import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

class ModelTrainer:
    def __init__(self, X, y, problem_type='classification'):
        self.X = X
        self.y = y
        self.problem_type = problem_type
        self.models = {}

    def split_data(self, test_size=0.2, random_state=None):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=random_state)

    def train_models(self):
        if self.problem_type == 'classification':
            self.models['Logistic Regression'] = LogisticRegression()
            self.models['Decision Tree Classifier'] = DecisionTreeClassifier()
            self.models['Random Forest Classifier'] = RandomForestClassifier()
            self.models['Support Vector Classifier'] = SVC()
            self.models['K-Nearest Neighbors Classifier'] = KNeighborsClassifier()
        elif self.problem_type == 'regression':
            self.models['Linear Regression'] = LinearRegression()
            self.models['Decision Tree Regressor'] = DecisionTreeRegressor()
            self.models['Random Forest Regressor'] = RandomForestRegressor()
            self.models['Support Vector Regressor'] = SVR()
            self.models['K-Nearest Neighbors Regressor'] = KNeighborsRegressor()

        for model_name, model in self.models.items():
            model.fit(self.X_train, self.y_train)

    def evaluate_models(self):
        self.results = {}
        for model_name, model in self.models.items():
            if self.problem_type == 'classification':
                y_pred = model.predict(self.X_test)
                accuracy = accuracy_score(self.y_test, y_pred)
                self.results[model_name] = accuracy
            elif self.problem_type == 'regression':
                y_pred = model.predict(self.X_test)
                mse = mean_squared_error(self.y_test, y_pred)
                r2 = r2_score(self.y_test, y_pred)
                self.results[model_name] = {'Mean Squared Error': mse, 'R-squared': r2}

    def get_best_model(self):
        best_model_name = max(self.results, key=self.results.get)
        best_model = self.models[best_model_name]
        return best_model_name, best_model

    def print_results(self):
        for model_name, result in self.results.items():
            print(f"{model_name}:\n{result}")