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
            "desc": "유럽 최고의 고전 미술 컬렉션을 자랑하는 미술관입니다."
        }
    ]
}
