import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="📈 국내 주요 기업 주가 추이", layout="wide")
st.title("🇰🇷 국내 주요 기업 10개 - 최근 주가 변화")

# 기본 날짜 설정
default_end = datetime.today()
default_start = default_end - timedelta(days=365)

# 날짜 선택 UI
start_date = st.date_input("시작 날짜", default_start)
end_date = st.date_input("종료 날짜", default_end)
if start_date > end_date:
    st.error("시작 날짜가 종료 날짜보다 빠를 수 없습니다.")
    st.stop()

# 기업 목록
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

# 기업 선택 UI
selected = st.multiselect(
    "비교할 기업을 선택하세요",
    options=list(kr_companies.keys()),
    default=["삼성전자", "SK하이닉스", "현대차"]
)

# 변화율 옵션
show_pct = st.checkbox("주가 변화율 (%)로 보기", value=False)

# 데이터 로딩 함수
@st.cache_data
def load_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end)

# 그래프 그리기
if selected:
    fig = go.Figure()
    for company in selected:
        ticker = kr_companies[company]
        df = load_data(ticker, start_date, end_date)
        if not df.empty:
            if show_pct:
                df["Change %"] = (df["Close"] / df["Close"].iloc[0] - 1) * 100
                fig.add_trace(go.Scatter(x=df.index, y=df["Change %"], mode="lines", name=company))
            else:
                fig.add_trace(go.Scatter(x=df.index, y=df["Close"], mode="lines", name=company))
    yaxis_title = "주가 변화율 (%)" if show_pct else "종가 (KRW)"
    fig.update_layout(
        title="📊 최근 주가 변화",
        xaxis_title="날짜",
        yaxis_title=yaxis_title,
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("왼쪽에서 하나 이상의 회사를 선택해주세요.")
