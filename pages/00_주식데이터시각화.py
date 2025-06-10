import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="📈 국내 주요 기업 주가 추이", layout="wide")
st.title("🇰🇷 국내 주요 기업 10개 - 최근 1년 주가 변화")

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365 * 1)

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

# 선택 박스
selected = st.multiselect(
    "비교할 기업을 선택하세요",
    options=list(kr_companies.keys()),
    default=["삼성전자", "SK하이닉스", "현대차"]
)

@st.cache_data
def get_data(ticker, name):
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        return pd.DataFrame()
    df = df[["Close"]].copy()
    df.reset_index(inplace=True)
    df["Company"] = name
    return df

if selected:
    all_data = pd.DataFrame()
    for company in selected:
        ticker = kr_companies[company]
        df = get_data(ticker, company)
        all_data = pd.concat([all_data, df], ignore_index=True)

    # 컬럼 존재 확인
    if {"Date", "Close", "Company"}.issubset(all_data.columns):
        fig = px.line(
            all_data,
            x="Date",
            y="Close",
            color="Company",
            title="📊 최근 1년 종가 비교"
        )
        fig.update_layout(xaxis_title="날짜", yaxis_title="종가 (KRW)", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("데이터 로딩 중 문제가 발생했습니다. 선택된 회사의 주가 데이터를 불러오지 못했습니다.")
else:
    st.info("비교할 기업을 선택해주세요.")
