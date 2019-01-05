from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import BaggingClassifier
import numpy as np

class ScikitLearn:
    def KNNClassifier(self, k, X_train, y_train, X_test):      
        y_train = LabelEncoder().fit_transform(y_train)
        X_train = np.array(X_train)

        knn = KNeighborsClassifier(k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        return y_pred

    def ensemble(self, k, X_train, y_train, X_test, bags):
        bag_clf = BaggingClassifier(KNeighborsClassifier(n_neighbors=k), bootstrap=True, n_estimators=bags)
        bag_clf.fit(X_train, y_train)
        y_pred = bag_clf.predict(X_test)
        return y_pred

    def metrics_base(self, y_pred, y_test):
        y_test = LabelEncoder().fit_transform(y_test)
        accuracy = round(accuracy_score(y_test, y_pred), 2)
        conf_matrix = confusion_matrix(y_test, y_pred)
        pre, rec, fscor = precision_recall_fscore_support(y_test, y_pred)
        return(accuracy, conf_matrix, pre, rec, fscor)

    def metrics_ens(self, y_pred, y_test):
        y_test = LabelEncoder().fit_transform(y_test)
        y_pred = LabelEncoder().fit_transform(y_pred)
        accuracy = round(accuracy_score(y_test, y_pred), 2)
        conf_matrix = confusion_matrix(y_test, y_pred) 
        pre= precision_recall_fscore_support(y_test, y_pred, average="weighted")
        return(accuracy, conf_matrix, pre)

