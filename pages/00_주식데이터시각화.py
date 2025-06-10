# 📁 파일명 예시: pages/00_과학_주가시각화.py

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# 제목
st.title("🧬 최근 1년 과학 관련 주요 기업 주가 변화")

# 과학 관련 기업 리스트 (KOSPI/KQ 종목: 티커는 Yahoo Finance 기준)
companies = {
    "삼성바이오로직스": "207940.KQ",
    "셀트리온": "068270.KQ",
    "SK바이오사이언스": "302440.KQ"
}

# 데이터 가져올 날짜 범위
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 전체 데이터를 담을 리스트
all_data = []

# 기업별 데이터 가져오기
for name, ticker in companies.items():
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        st.warning(f"{name} ({ticker}) 주가 데이터를 가져올 수 없습니다.")
        continue

    df = df[["Close"]].copy()
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"]).dt.date  # 날짜만 추출
    df["Company"] = name
    all_data.append(df)

# 리스트를 하나의 데이터프레임으로 병합
if all_data:
    combined_df = pd.concat(all_data)

    # 시각화
    fig = px.line(
        combined_df,
        x="Date",
        y="Close",
        color="Company",
        title="📈 최근 1년 주가 변화 (종가 기준)",
        labels={"Close": "종가 (KRW)", "Date": "날짜"}
    )
    fig.update_xaxes(tickformat="%Y-%m", tickangle=45)

    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("주가 데이터를 불러오지 못했습니다.")
