# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

diabetes_dataset = datasets.load_diabetes()  # 데이터 셋 갖고오기

# 코드를 쓰세요
pt = PolynomialFeatures(2)
poly_data = pt.fit_transform(diabetes_dataset.data)
pf_names= pt.get_feature_names(diabetes_dataset.feature_names)
x = pd.DataFrame(poly_data,columns=pf_names)

# 테스트 코드
x.head()

