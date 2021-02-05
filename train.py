from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

def clean_data(data):
    data = data.to_pandas_dataframe()
    y = data['DEATH_EVENT']
    x = data.drop('DEATH_EVENT', 1) 
    return x, y


def main():
    url_path = "https://raw.githubusercontent.com/maulingogri/Azure-Udacity-MLE-ND-Capstone/master/data/heart_failure_clinical_records_dataset.csv"
    ds = TabularDatasetFactory.from_delimited_files(path=url_path)

    # Split data into train and score sets
    # train, score = ds.random_split(percentage=0.75, seed=121)

    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=121)

    run = Run.get_context()

    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    joblib.dump(model, os.path.join('outputs', 'hd_model.joblib'))

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()
