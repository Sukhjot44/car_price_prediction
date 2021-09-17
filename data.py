import streamlit as st
import numpy as np
import pandas as pd

def app(car_df):
	st.header('View Data')
	with st.beta_expander('View Dataset'):
		st.table(car_df)
	st.subheader('Columns description')
	beta_col1,beta_col2=st.beta_columns(2)

	with beta_col1:
		if st.checkbox('Show all columns names'):
			st.table(list(car_df.columns))
	with beta_col2:
		if st.checkbox('View column data'):
			column_data=st.selectbox('select columns',('enginesize','horsepower','carwidth','drivewheel','price'))
			if column_data=='drivewheel':
				st.write(car_df['drivewheel'])
			elif column_data=='carwidth':
				st.write(car_df['carwidth'])
			elif column_data=='enginesize':
				st.write(car_df['enginesize'])
			elif column_data=='horsepower':
				st.write(car_df['horsepower'])
			else:
				st.write(car_df['price'])
	if st.checkbox('Show summary'):
		st.table(car_df.describe())
