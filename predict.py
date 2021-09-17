import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error

@st.cache()
def prediction(car_df,carwidth,enginesize,horsepower,drive_wheel_fwd,car_company_buick):
	X=car_df.iloc[:,:-1]
	y=car_df['price']
	X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
	lin_reg=LinearRegression()
	lin_reg.fit(X_train,y_train)
	score=lin_reg.score(X_train,y_train)
	price=lin_reg.predict([[carwidth,enginesize,horsepower,drive_wheel_fwd,car_company_buick]])
	price=price[0]
	y_test_pred=lin_reg.predict(X_test)
	test_r2_score=r2_score(y_test,y_test_pred)
	test_mae=mean_absolute_error(y_test,y_test_pred)
	test_msle=mean_squared_log_error(y_test,y_test_pred)
	test_rmse=np.sqrt(mean_squared_error(y_test,y_test_pred))
	return price,score,test_r2_score,test_mae,test_msle,test_rmse
def app(car_df):
	st.subheader("This app uses Linear Regression to predictt the price of a car")
	st.subheader('select values')
	cw=st.slider('car_width',float(car_df['carwidth'].min()),float(car_df['carwidth'].max()))
	es=st.slider('engine_size',int(car_df['enginesize'].min()),int(car_df['enginesize'].max()))
	hp=st.slider('horse_power',int(car_df['horsepower'].min()),int(car_df['horsepower'].max()))
	drw_fwd=st.radio("Is it a forward drive wheel car?",("Yes","No"))
	if drw_fwd=="No":
		drw_fwd=0
	else:
		drw_fwd=1
	com_buick=st.radio("Is the car manufactured by buick?",("Yes","No"))
	if com_buick=="No":
		com_buick=0
	else:
		com_buick=1
	if st.button('Predict'):
		st.subheader("Prediction Results")
		price,score,car_r2,car_mae,car_msle,car_rmse=prediction(car_df,cw,es,hp,drw_fwd,com_buick)
		st.success("Predicted price of the car is {:,}".format(int(price)))
		st.info("score of the model is {:2.2%}".format(score))
		st.info(f"r2 score of the model is {car_r2}")
		st.info(f"mean_absolute_error of the model is {car_mae}")
		st.info(f"root mean squared error of the model is {car_rmse}")
		st.info(f"mean squared log error of the model is {car_msle}")


