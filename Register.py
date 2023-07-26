import streamlit as st
import streamlit_extras as ste
import pandas as pd
import numpy as np
df = pd.read_csv("Database.csv")
col1,col2 = st.columns([1,1])
with col2:
	col3,col4 = st.columns([1,1])
	with col4:
		st.header("Login")
	uname = st.text_input("UserName: ")
	pwd = st.text_input("Password: ",type="password")
	col3,col4 = st.columns([1,1])
	with col4:
		button = st.button("Submit")
	if button:
		ubool = uname in list(df['Name'])
		if(ubool):
			ind = list(df['Name']).index(uname)
			if(pwd==df['pwd'][ind]):
				st.write("Login Successful")
			else:
				ste.switch_page("Register")
		else:
			st.write("afsgdh")
df = pd.read_csv("Database.csv")