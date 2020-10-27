# Research Project (Effects of chemicals on the fetus)

## Installation

### Anaconda

```
pyenv install anaconda3-2020.02
```

### RDKit

```
conda create -c rdkit rdkit
```

## Task 1

[Prediction of human fetal–maternal blood concentration ratio of chemicals](https://peerj.com/articles/9562/)

| Model                              | RMSE train | Q2 train | RMSE test | Q2 test  |
| :--------------------------------- | :--------- | :------- | :-------- | :------- |
| 1D/2D Descriptor LinearRegression  | 0.01718    | 0.99745  | 0.54873   | -1.30057 |
| 1D/2D Descriptor Ridge             | 0.03485    | 0.98949  | 0.40664   | -0.26339 |
| 1D/2D Descriptor SVR               | 0.10325    | 0.90777  | 0.26587   | 0.45993  |
| 1D/2D Descriptor RandomForest      | 0.11260    | 0.89032  | 0.23256   | 0.58677  |
| 1D/2D Descriptor LightGBM          | 0.00469    | 0.99981  | 0.24368   | 0.54633  |
| 3D Descriptor LinearRegression     | 0.24048    | 0.49972  | 0.39826   | -0.21187 |
| 3D Descriptor Ridge                | 0.24902    | 0.46354  | 0.32350   | 0.20044  |
| 3D Descriptor SVR                  | 0.09072    | 0.92881  | 0.37218   | -0.05836 |
| 3D Descriptor RandomForest         | 0.13803    | 0.83517  | 0.32382   | 0.19885  |
| 3D Descriptor LightGBM             | 0.00442    | 0.99983  | 0.32657   | 0.18515  |
| ECFP4 Fingerprint LinearRegression | 0.07809    | 0.94725  | 0.33386   | 0.14837  |
| ECFP4 Fingerprint Ridge            | 0.07965    | 0.94512  | 0.34191   | 0.10684  |
| ECFP4 Fingerprint SVR              | 0.12637    | 0.86186  | 0.37322   | -0.06425 |
| ECFP4 Fingerprint RandomForest     | 0.12626    | 0.86209  | 0.30744   | 0.27782  |
| ECFP4 Fingerprint LightGBM         | 0.02048    | 0.99637  | 0.30216   | 0.30243  |
| Author's Model                     | 0.20611    | 0.63250  | 0.24073   | 0.55724  |

<p align="center">
<img src="https://github.com/nozomu-y/Effects-of-chemicals-on-the-fetus/blob/master/task1/output/1d2d_desc_RandomForest_test.png" width="480px">
</p>

## Task 2

[Prediction of Placental Barrier Permeability: A Model Based on Partial Least Squares Variable Selection Procedure](https://www.mdpi.com/1420-3049/20/5/8270/htm)

| Model                              | RMSE train | Q2 train  | RMSE test | Q2 test   |
| :--------------------------------- | :--------- | :-------- | :-------- | :-------- |
| 1D/2D Descriptor LinearRegression  | 3.46e+07   | -1.36e+16 | 1.08e+10  | -1.76e+21 |
| 1D/2D Descriptor Ridge             | 0.02634    | 0.99211   | 0.23378   | 0.17410   |
| 1D/2D Descriptor SVR               | 0.09089    | 0.90605   | 0.15239   | 0.64907   |
| 1D/2D Descriptor RandomForest      | 0.08466    | 0.91849   | 0.17064   | 0.55998   |
| 1D/2D Descriptor LightGBM          | 0.00511    | 0.99970   | 0.19084   | 0.44967   |
| 3D Descriptor LinearRegression     | 0.25419    | 0.26523   | 0.22857   | 0.21050   |
| 3D Descriptor Ridge                | 0.25618    | 0.25368   | 0.23188   | 0.18749   |
| 3D Descriptor SVR                  | 0.16823    | 0.67815   | 0.32178   | -0.56464  |
| 3D Descriptor RandomForest         | 0.12061    | 0.83456   | 0.24250   | 0.11138   |
| 3D Descriptor LightGBM             | 0.00000    | 1.00000   | 0.26682   | -0.07586  |
| ECFP4 Fingerprint LinearRegression | 4.88e+08   | -2.71e+18 | 5.18e+09  | -4.06e+20 |
| ECFP4 Fingerprint Ridge            | 0.01893    | 0.99592   | 0.16376   | 0.59474   |
| ECFP4 Fingerprint SVR              | 0.09437    | 0.89872   | 0.20363   | 0.37343   |
| ECFP4 Fingerprint RandomForest     | 0.10253    | 0.88045   | 0.15850   | 0.62036   |
| ECFP4 Fingerprint LightGBM         | 0.00734    | 0.99939   | 0.19129   | 0.44706   |
| Author's Model                     | 0.09043    | 0.90701   | 0.23427   | 0.17066   |

<p align="center">
<img src="https://github.com/nozomu-y/Effects-of-chemicals-on-the-fetus/blob/master/task2/output/1d2d_desc_SVR_test.png" width="480px">
</p>
