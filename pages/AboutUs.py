import streamlit as st
st.set_page_config(layout="wide")
col1,col2,col3 = st.columns([3,1,3])
with col2:
	st.header("About Us")
st.divider()
col1,col2,col3 = st.columns([1,1,1])
with col2:
	st.image("clg-logo.jpg")
col1,col2,col3 = st.columns([1,3,1])
with col2:
	st.markdown("##### This application is developed as a Mini project by the students of CVR College of Engineering.")
st.divider()
st.subheader("Goal:")
col1,col2 = st.columns([4,12])
with col1:
	st.image("adni-logo.jpg")
with col2:
	st.write("The primary motive for developing an application for early Alzheimer's detection using Convolutional Neural Networks (CNN) is to make a significant positive impact on the lives of individuals at risk of developing this devastating neurodegenerative disease. Early detection is crucial as it allows for timely intervention and improved patient outcomes. By leveraging the power of AI and deep learning through CNNs, the application aims to provide a non-invasive and cost-effective solution for early detection. This can empower medical professionals with a powerful tool to identify early warning signs of Alzheimer's in their patients, facilitating proactive treatment planning and access to support services. The motive behind developing this application is to contribute to the broader mission of improving the quality of life for those impacted by Alzheimer's, fostering a future where timely detection and intervention can potentially delay disease progression, enhance patient care, and bring us closer to finding a cure for this devastating condition.")
st.divider()
st.subheader("Developers:")
st.write("We are a team driven by the problems that surround us and strive to provide a solution accessible to all. Our mission with this application is to provide a free-for-all service that enables users to know the stage of Alzheimer's Disease based on the uploaded MRI scan and suggestions to maintain your health based on the result given.")
col1,col2,col3 = st.columns([3,3,3])
with col1:
	st.markdown("##### Abhinaya Rapolu")
with col2:
	st.markdown("##### Jagan Mohan Kandukuri")
with col3:
	st.markdown("##### Nithin Kumar Reddy Vangala")
col1,col2,col3 = st.columns([3,3,3])
with col1:
	st.write("Roll No.: 20B81A6603")
with col2:
	st.write("Roll No.: 20B81A6622")
with col3:
	st.write("Roll No.: 20B81A6629")
col1,col2,col3 = st.columns([3,3,3])
with col1:
	st.write("Phone No.: 9100504749")
with col2:
	st.write("Phone No.: 9390822554")
with col3:
	st.write("Phone No.: 9502072420")
col1,col2,col3 = st.columns([3,3,3])
with col1:
	st.write("20B81A6603@cvr.ac.in")
with col2:
	st.write("20B81A6622@cvr.ac.in")
with col3:
	st.write("20B81A6629@cvr.ac.in")
st.divider()
st.subheader("Thank you for visiting our website")
st.write("For any queries, Please email us through any of the addresses mentioned above")
