# 필요한 라이브러리 import
from sklearn import datasets
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

diabetes_dataset = datasets.load_diabetes()

# 지난 과제 코드를 가지고 오세요.
pt = PolynomialFeatures(2)
poly_data = pt.fit_transform(diabetes_dataset.data)
pf_names= pt.get_feature_names(diabetes_dataset.feature_names)
x = pd.DataFrame(poly_data,columns=pf_names)

# 목표 변수
y = pd.DataFrame(diabetes_dataset.target, columns=['diabetes'])

# 코드를 쓰세요
y = pd.DataFrame(diabetes_dataset.target, columns=['MEDV'])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,random_state=5)
model = LinearRegression()
#학습 데이터를 fit 메소드의 파라미터로 넘겨주어 학습시킨다.
model.fit(x_train, y_train)
#학습 시킨 모델로 test set 데이터를 예측한다
y_test_predict = model.predict(x_test)

mse = mean_squared_error(y_test, y_test_predict)
mse ** 0.5 #57.877049027249242 는 목표 변수인 y에대해 예측 데이터가 이만큰 오차범위를 갖는다는 뜻!

