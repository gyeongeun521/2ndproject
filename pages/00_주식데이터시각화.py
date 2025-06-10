import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="🔬 과학 관련 기업 주가 추이", layout="wide")
st.title("🧪 과학 연구 중심 글로벌 기업 - 최근 1년 주가 변화")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 과학 연구 관련 기업
science_stocks = {
    "Thermo Fisher (TMO)": "TMO",
    "Illumina (ILMN)": "ILMN",
    "Bio-Rad (BIO)": "BIO",
    "Agilent (A)": "A",
    "Danaher (DHR)": "DHR",
    "Waters (WAT)": "WAT",
    "Revvity (RVTY)": "RVTY",  # 전 PerkinElmer
    "Bruker (BRKR)": "BRKR",
    "Charles River Labs (CRL)": "CRL"
}

# 선택 옵션
selected = st.multiselect(
    "비교할 과학 기업을 선택하세요:",
    options=list(science_stocks.keys()),
    default=["Thermo Fisher (TMO)", "Agilent (A)", "Danaher (DHR)"]
)

@st.cache_data
def load_data(ticker, name):
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        return pd.DataFrame()
    df = df[["Close"]].copy()
    df.reset_index(inplace=True)
    df["Company"] = name
    return df

# 데이터 수집 및 시각화
if selected:
    all_data = pd.DataFrame()

    for name in selected:
        ticker = science_stocks[name]
        df = load_data(ticker, name)
        all_data = pd.concat([all_data, df], ignore_index=True)

    if {"Date", "Close", "Company"}.issubset(all_data.columns):
        fig = px.line(
            all_data,
            x="Date",
            y="Close",
            color="Company",
            title="📈 과학 관련 연구 기업의 최근 1년간 주가 비교"
        )
        fig.update_layout(xaxis_title="날짜", yaxis_title="종가 (USD)", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("데이터 로딩에 실패한 종목이 있어요.")
else:
    st.info("기업을 선택해주세요.")
