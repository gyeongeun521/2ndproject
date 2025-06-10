import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="글로벌 시총 Top10 주가 비교", layout="wide")

st.title("🌍 글로벌 시가총액 Top 10 기업 - 최근 3년 주가 추이")

# 최근 3년 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 시총 Top 10 기업 (2025년 기준 추정, 필요 시 업데이트 가능)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 사우디 증권거래소 (Tadawul)
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta (Facebook)": "META",
    "Berkshire Hathaway": "BRK-B",
    "Tesla": "TSLA",
    "TSMC": "TSM",
}

# 선택 옵션
selected_companies = st.multiselect(
    "비교할 기업을 선택하세요",
    options=list(top10_companies.keys()),
    default=["Apple", "Microsoft", "Amazon"]
)

# 데이터 다운로드
def get_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    df["Ticker"] = ticker
    return df

if selected_companies:
    fig = go.Figure()
    for company in selected_companies:
        ticker = top10_companies[company]
        data = get_data(ticker)
        fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name=company))

    fig.update_layout(
        title="최근 3년간 주가 비교",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("왼쪽에서 하나 이상의 회사를 선택해주세요.")

