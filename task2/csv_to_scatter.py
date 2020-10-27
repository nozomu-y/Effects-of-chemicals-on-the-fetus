import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import sys


def csv_to_scatter(filename):
    df = pd.read_csv(filename)
    y_pred = df['Predicted CI']
    y_pred_author = df['Author\'s Prediction']
    y_true = df['Observed CI']

    RMSE = mean_squared_error(y_true, y_pred, squared=False)
    R2 = r2_score(y_true, y_pred)
    RMSE_author = mean_squared_error(y_true, y_pred_author, squared=False)
    R2_author = r2_score(y_true, y_pred_author)

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111)
    ax.scatter(y_true, y_pred, label='Prediction')
    ax.scatter(y_true, y_pred_author, label='Author\'s Prediction')
    ax.set_xlabel('Observed CI', fontsize=15)
    ax.set_ylabel('Predicted CI', fontsize=15)
    y_true = pd.Series(y_true)
    y_pred = pd.Series(y_pred)
    pred_df = pd.concat([y_true, y_pred], axis=1)
    ax.set_xlim(pred_df.min().min() - 0.1, pred_df.max().max() + 0.1)
    ax.set_ylim(pred_df.min().min() - 0.1, pred_df.max().max() + 0.1)
    x = np.linspace(pred_df.min().min() - 0.1, pred_df.max().max() + 0.1, 2)
    y = x
    ax.plot(x, y, '-', color="tab:red")
    plt.text(0.05, 0.95, 'RMSE = {}'.format(str(round(RMSE, 5))),
             transform=ax.transAxes, fontsize=12, color="tab:blue")
    plt.text(0.05, 0.9, 'Q2 = {}'.format(str(round(R2, 5))),
             transform=ax.transAxes, fontsize=12, color="tab:blue")
    plt.text(0.05, 0.85, 'RMSE = {}'.format(str(round(RMSE_author, 5))),
             transform=ax.transAxes, fontsize=12, color="tab:orange")
    plt.text(0.05, 0.8, 'Q2 = {}'.format(str(round(R2_author, 5))),
             transform=ax.transAxes, fontsize=12, color="tab:orange")
    plt.legend(loc="lower right")
    if "train" in filename:
        suffix = " (train data)"
    else:
        suffix = " (test data)"
    if "LinearRegression" in filename:
        reg_type = "LinearRegression"
    elif "Ridge" in filename:
        reg_type = "Ridge"
    elif "SVR" in filename:
        reg_type = "SVR"
    elif "RandomForest" in filename:
        reg_type = "RandomForest"
    elif "LightGBM" in filename:
        reg_type = "LightGBM"
    else:
        reg_type = "Error"
    if "1d2d_desc" in filename:
        feature = "1D/2D Descriptor"
    elif "3d_desc" in filename:
        feature = "3D Descriptor"
    else:
        feature = "ECFP4 Fingerprint"

    plt.title(feature + " " + reg_type + suffix, fontsize=15)

    plt.savefig(filename.replace("csv", "png"), dpi=300)


path = sys.argv[1]
csv_to_scatter(path)
