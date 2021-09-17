import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def app(car_df):
	st.header('Visualize Data')
	st.set_option('deprecation.showPyplotGlobalUse',False)
	st.subheader('Scatterplot')
	features_list=st.multiselect('Select x-axis values',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
	for feature in features_list:
		st.subheader(f'Scatterplot bw {feature} and price')
		plt.figure(figsize=(12,6))
		sns.scatterplot(x=feature,y='price',data=car_df)
		st.pyplot()
	st.subheader('Visualization Selector')
	plot_types=st.multiselect('Select plots or Charts',('Histogram','Boxplot','Correlation heat map'))
	if 'Histogram'in plot_types:
		st.subheader('Histogram')
		columns=st.selectbox('select the column to create its histogram',('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))
		plt.figure(figsize=(12,6))
		plt.title(f'Histogram for {columns}')
		plt.hist(car_df[columns],bins='sturges',edgecolor='black')
		st.pyplot()
	if 'Boxplot' in plot_types:
		st.subheader('Boxplot')
		cols=st.sidebar.selectbox('select the columns to create a Boxplot ',('RI','Na','Mg','Al','Si','K','Ca','Ba','Fe'))
		plt.figure(figsize=(12,6))
		plt.title(f' Boxplot for {cols}')
		sns.boxplot(df[cols])
		st.pyplot()
	if 'Correlation heat map' in plot_types:
		st.subheader('Correlation heat map')
		plt.figure(figsize=(12,6))
		heat_map=sns.heatmap(car_df.corr(),annot=True)
		bottom,top=heat_map.get_ylim()
		st.pyplot()