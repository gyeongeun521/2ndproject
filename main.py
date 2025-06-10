import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 기본 설정
st.set_page_config(page_title="스페인 관광지 가이드", layout="wide")

# 제목
st.title("🇪🇸 스페인 주요 관광지 가이드")
st.markdown("""
스페인은 역사, 문화, 예술, 건축, 그리고 맛있는 음식으로 가득한 나라입니다.  
아래는 스페인의 대표 도시와 관광지에 대한 친절하고 자세한 안내입니다.
""")

# 관광지 데이터
tourist_spots = [
    {
        "city": "마드리드",
        "location": [40.4168, -3.7038],
        "places": [
            {
                "name": "프라도 미술관",
                "desc": "유럽 최고의 고전 미술 컬렉션을 자랑하는 미술관입니다. 벨라스케스, 고야 등의 작품을 감상할 수 있습니다."
            },
            {
                "name": "왕궁",
                "desc": "스페인 왕실의 공식 거주지로, 웅장하고 화려한 바로크 양식의 건축이 인상적입니다."
            },
        ],
    },
    {
        "city": "바르셀로나",
        "location
