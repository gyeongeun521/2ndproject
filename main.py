import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="바르셀로나 맛집 & 숙소 추천", layout="wide")

st.title("🏖️ 바르셀로나 맛집 & 숙소 추천 가이드")
st.markdown("""
스페인 바르셀로나는 예술, 건축, 바다, 그리고 미식으로 가득한 도시입니다.  
아래는 바르셀로나 여행 시 방문할 만한 **맛집과 숙소**를 소개합니다.
""")

# 바르셀로나 위치
barcelona_coords = [41.3874, 2.1686]

# 추천 장소 데이터
restaurants = [
    {
        "name": "Tickets",
        "desc": "미슐랭 스타 셰프 알베르 아드리아가 운영하는 타파스 레스토랑. 창의적인 요리를 즐길 수 있습니다.",
        "location": [41.3751, 2.1543]
    },
    {
        "name": "El Xampanyet",
        "desc": "현지인에게 사랑받는 오래된 바. 저렴하고 맛있는 타파스와 카바(스페인 스파클링 와인)를 즐길 수 있어요.",
        "location": [41.3839, 2.1815]
    },
    {
        "name": "Cinc Sentits",
        "desc": "현대적인 카탈루냐 요리를 선보이는 고급 레스토랑. 미슐랭 스타 보유.",
        "location": [41.3846, 2.1620]
    }
]

hotels = [
    {
        "name": "W Barcelona",
        "desc": "바르셀로네타 해변 앞에 위치한 고급 호텔. 바다 전망과 루프탑 바가 인기입니다.",
        "location": [41.3687, 2.1906]
    },
    {
        "name": "Hotel Arts Barcelona",
        "desc": "해변 근처에 위치한 럭셔리 호텔로, 현대적인 인테리어와 편의 시설이 인상적입니다.",
        "location": [41.3880, 2.1970]
    },
    {
        "name": "Casa Bonay",
        "desc": "현지 감성을 살린 부티크 호텔로, 감각적인 디자인과 맛있는 조식이 특징입니다.",
        "location": [41.3914, 2.1696]
    }
]

# 지도 생성
m = folium.Map(location=barcelona_coords, zoom_start=13)

# 맛집 마커
for r in restaurants:
    folium.Marker(
        location=r["location"],
        popup=f"<strong>{r['name']}</strong><br>{r['desc']}",
        tooltip=r["name"],
        icon=folium.Icon(color='red', icon='cutlery', prefix='fa')
    ).add_to(m)

# 숙소 마커
for h in hotels:
    folium.Marker(
        location=h["location"],
        popup=f"<strong>{h['name']}</strong><br>{h['desc']}",
        tooltip=h["name"],
        icon=folium.Icon(color='green', icon='home', prefix='fa')
    ).add_to(m)

# 지도 출력
st.subheader("📍 지도에서 맛집과 숙소 보기")
st_data = st_folium(m, width=800, height=500)

# 맛집 목록
st.subheader("🍽️ 바르셀로나 추천 맛집")
for r in restaurants:
    st.markdown(f"**{r['name']}**  \n{r['desc']}\n")

# 숙소 목록
st.subheader("🛏️ 바르셀로나 추천 숙소")
for h in hotels:
    st.markdown(f"**{h['name']}**  \n{h['desc']}\n")
