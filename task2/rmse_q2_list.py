import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import os
import sys
import pathlib


os.chdir(pathlib.Path(sys.argv[0]).parent)

models = ["1d2d_desc_LinearRegression",
          "1d2d_desc_Ridge",
          "1d2d_desc_SVR",
          "1d2d_desc_RandomForest",
          "1d2d_desc_LightGBM",
          "3d_desc_LinearRegression",
          "3d_desc_Ridge",
          "3d_desc_SVR",
          "3d_desc_RandomForest",
          "3d_desc_LightGBM",
          "fp_LinearRegression",
          "fp_Ridge",
          "fp_SVR",
          "fp_RandomForest",
          "fp_LightGBM"]


df_output = pd.DataFrame(columns=['Model', 'RMSE train', 'Q2 train', 'RMSE test', 'Q2 test'])

for model in models:
    filename = "./output/" + model + "_train.csv"
    df = pd.read_csv(filename)
    y_pred = df['Predicted CI']
    y_true = df['Observed CI']
    RMSE_train = mean_squared_error(y_true, y_pred, squared=False)
    R2_train = r2_score(y_true, y_pred)

    filename = "./output/" + model + "_test.csv"
    df = pd.read_csv(filename)
    y_pred = df['Predicted CI']
    y_true = df['Observed CI']
    RMSE_test = mean_squared_error(y_true, y_pred, squared=False)
    R2_test = r2_score(y_true, y_pred)

    if "1d2d_desc_" in model:
        model = model.replace("1d2d_desc_", "1D/2D Descriptor ")
    elif "3d_desc_" in model:
        model = model.replace("3d_desc_", "3D Descriptor ")
    elif "fp_" in model:
        model = model.replace("fp_", "ECFP4 Fingerprint ")

    s = pd.DataFrame([[model, RMSE_train, R2_train, RMSE_test, R2_test]], columns=[
                     'Model', 'RMSE train', 'Q2 train', 'RMSE test', 'Q2 test'])
    df_output = df_output.append(s)

filename = "./output/" + models[0] + "_train.csv"
df = pd.read_csv(filename)
y_pred = df['Author\'s Prediction']
y_true = df['Observed CI']
RMSE_train = mean_squared_error(y_true, y_pred, squared=False)
R2_train = r2_score(y_true, y_pred)

filename = "./output/" + models[0] + "_test.csv"
df = pd.read_csv(filename)
y_pred = df['Author\'s Prediction']
y_true = df['Observed CI']
RMSE_test = mean_squared_error(y_true, y_pred, squared=False)
R2_test = r2_score(y_true, y_pred)

model = "Author\'s Model"

s = pd.DataFrame([[model, RMSE_train, R2_train, RMSE_test, R2_test]], columns=[
    'Model', 'RMSE train', 'Q2 train', 'RMSE test', 'Q2 test'])
df_output = df_output.append(s)

df_output['RMSE diff'] = abs(df_output['RMSE train'] - df_output['RMSE test'])
df_output['Q2 diff'] = abs(df_output['Q2 train'] - df_output['Q2 test'])

df_output['RMSE train'] = df_output['RMSE train'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))
df_output['RMSE test'] = df_output['RMSE test'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))
df_output['Q2 train'] = df_output['Q2 train'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))
df_output['Q2 test'] = df_output['Q2 test'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))
df_output['RMSE diff'] = df_output['RMSE diff'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))
df_output['Q2 diff'] = df_output['Q2 diff'].apply(
    lambda x: '{:.5f}'.format(x) if abs(x) < 10 else '{:.2e}'.format(x))

df_output.to_csv("./output/rmse_q2_diff.csv", index=False)

df_output.drop(['RMSE diff', 'Q2 diff'], inplace=True, axis=1)
df_output.to_csv("./output/rmse_q2.csv", index=False)
