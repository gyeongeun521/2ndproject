import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.title("🧬 최근 1년 과학 관련 주요 기업 주가 변화")

# 기업 리스트
companies = {
    "삼성바이오로직스": "207940.KQ",
    "셀트리온": "068270.KQ",
    "SK바이오사이언스": "302440.KQ"
}

end_date = datetime.today()
start_date = end_date - timedelta(days=365)

all_data = []

for name, ticker in companies.items():
    df = yf.download(ticker, start=start_date, end=end_date)
    
    if df.empty:
        st.warning(f"{name} ({ticker}) 주가 데이터를 가져올 수 없습니다.")
        continue

    df = df[["Close"]].copy()
    df["Date"] = df.index.date  # 날짜만 추출
    df["Company"] = name
    df.reset_index(drop=True, inplace=True)
    all_data.append(df)

if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)

    # 🚨 데이터 컬럼 체크
    required_columns = {"Date", "Close", "Company"}
    if not required_columns.issubset(combined_df.columns):
        st.error(f"필수 컬럼이 없습니다: {required_columns - set(combined_df.columns)}")
    else:
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
    st.error("📉 불러온 주가 데이터가 없습니다.")
