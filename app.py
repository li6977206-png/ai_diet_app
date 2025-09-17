import streamlit as st

st.title("AI 智慧飲食系統 🍎")
st.write("上傳食物照片，我會幫你辨識營養素！")

uploaded_file = st.file_uploader("選擇一張圖片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="你上傳的圖片", use_column_width=True)
    st.success("（這裡加上你的 AI 模型做食物辨識）")
