import streamlit as st
st.set_page_config(layout="wide")
col1,col2,col3 = st.columns([3,1,3])
with col2:
	st.header("About Us")
st.divider()
col1,col2,col3 = st.columns([1,20,1])
with col2:
	st.markdown("##### We are a team driven by the problems that surround us and strive to provide a solution accessible to all. Our mission with this application is to provide a free-for-all service that enables users to know the stage of Alzheimer's Disease based on the uploaded MRI scan and suggestions to maintain your health based on the result given.")
st.divider()
st.subheader("Introducing the team behind the project:")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Jagan.jpg")
# 	st.caption(":blue[Jagan Mohan K]")
col1,col2,col3 = st.columns([5,1,5])
with col2:
	st.markdown("###### Jagan Mohan K")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Nithin.jpg")
# 	st.caption(":red[Nithin Kumar Reddy V]")
col1,col2,col3 = st.columns([7,2,7])
with col2:
	st.markdown("###### Nithin kumar reddy V")
col1,col2,col3 = st.columns([2,1,2])
with col2:
	st.image("Abhinaya.jpg")
# 	st.caption(":violet[Abhinaya Rapolu]")
col1,col2,col3 = st.columns([8,2,8])
with col2:
	st.markdown("###### Abhinaya Rapolu")
col1,col2,col3 = st.columns([8,1,8])
with col2:
	st.markdown("[Login](Login) ")
	st.markdown("[Sign Up](Signup)")
