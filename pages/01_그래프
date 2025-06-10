import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("물과 식용유 온도 변화 그래프")

# 학생들이 온도 입력 (시간별)
time_points = st.text_input("시간을 콤마로 구분하여 입력하세요 (예: 0,1,2,3,4)", "0,1,2,3,4")
water_temps = st.text_input("물 온도를 콤마로 구분하여 입력하세요 (예: 20,25,30,35,40)", "20,25,30,35,40")
oil_temps = st.text_input("식용유 온도를 콤마로 구분하여 입력하세요 (예: 20,22,25,28,30)", "20,22,25,28,30")

try:
    time_list = [float(t) for t in time_points.split(",")]
    water_list = [float(t) for t in water_temps.split(",")]
    oil_list = [float(t) for t in oil_temps.split(",")]
    
    if len(time_list) == len(water_list) == len(oil_list):
        df = pd.DataFrame({
            "시간": time_list,
            "물 온도": water_list,
            "식용유 온도": oil_list
        })
        
        fig, ax = plt.subplots()
        ax.plot(df["시간"], df["물 온도"], marker='o', label="물 온도")
        ax.plot(df["시간"], df["식용유 온도"], marker='s', label="식용유 온도")
        
        ax.set_xlabel("시간 (분)")
        ax.set_ylabel("온도 (°C)")
        ax.set_title("물과 식용유의 온도 변화")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
    else:
        st.error("시간, 물 온도, 식용유 온도의 데이터 길이가 같아야 합니다.")
except Exception as e:
    st.error(f"입력 형식을 확인해주세요: {e}")
