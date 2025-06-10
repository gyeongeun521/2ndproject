import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="📈 국내 주요 기업 주가 추이", layout="wide")

st.title("🇰🇷 국내 주요 기업 10개 - 최근 주가 변화")

# 최근 1년 기준
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 국내 주요 기업
kr_companies = {
    "삼성전자": "005930.KS",
    "SK하이닉스": "000660.KS",
    "LG화학": "051910.KS",
    "삼성바이오로직스": "207940.KS",
    "현대차": "005380.KS",
    "NAVER": "035420.KQ",
    "카카오": "035720.KQ",
    "삼성SDI": "006400.KS",
    "POSCO홀딩스": "005490.KS",
    "기아": "000270.KS",
}

# 기업 선택
selected = st.multiselect(
    "비교할 기업을 선택하세요",
    options=list(kr_companies.keys()),
    default=["삼성전자", "SK하이닉스", "현대차"]
)

# 주가 가져오기 함수
@st.cache_data
def load_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

# 그래프 그리기
if selected:
    fig = go.Figure()
    for company in selected:
        ticker = kr_companies[company]
        df = load_data(ticker)
        if not df.empty:
            fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name=company))
    fig.update_layout(
        title="📊 최근 1년 주가 변화 (종가 기준)",
        xaxis_title="날짜",
        yaxis_title="종가 (KRW)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("왼쪽에서 하나 이상의 회사를 선택해주세요.")
