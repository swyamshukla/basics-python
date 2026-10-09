import streamlit as st      # Streamlit framework enables
st.balloons()

if st.button("Click Me"):
    st.write("welcome home")


pic=st.camera_input("take picure")

