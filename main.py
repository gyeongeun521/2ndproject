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

# 관광지 데이터 정의
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
            }
        ]
    },
    {
        "city": "바르셀로나",
        "location": [41.3874, 2.1686],
        "places": [
            {
                "name": "사그라다 파밀리아",
                "desc": "가우디의 미완성 대성당으로, 독창적인 디자인과 스테인드글라스로 유명합니다."
            },
            {
                "name": "구엘 공원",
                "desc": "가우디가 설계한 환상적인 공원으로, 알록달록한 타일과 곡선미 넘치는 구조물이 인상적입니다."
            }
        ]
    },
    {
        "city": "그라나다",
        "location": [37.1773, -3.5986],
        "places": [
            {
                "name": "알람브라 궁전",
                "desc": "이슬람 건축의 정수로, 정원과 궁전이 어우러진 세계문화유산입니다."
            }
        ]
    },
    {
        "city": "세비야",
        "location": [37.3886, -5.9823],
        "places": [
            {
                "name": "세비야 대성당",
                "desc": "세계에서 가장 큰 고딕 성당 중 하나로, 콜럼버스의 묘가 있습니다."
            },
            {
                "name": "히랄다 탑",
                "desc": "대성당에 붙어 있는 탑으로, 정상에서 세비야 시내를 한눈에 조망할 수 있습니다."
            }
        ]
    },
    {
        "city": "톨레도",
        "location": [39.8628, -4.0273],
        "places": [
            {
                "name": "톨레도 대성당",
                "desc": "스페인 가톨릭의 중심으로, 고딕 양식의 아름다움이 빛나는 대성당입니다."
            }
        ]
    }
]

# Folium 지도 생성
m = folium.Map(location=[40.0, -3.5], zoom_start=6)

# 마커 추가
for city in tourist_spots:
    for place in city["places"]:
        folium.Marker(
            location=city["location"],
            popup=f"<strong>{city['city']} - {place['name']}</strong><br>{place['desc']}",
            tooltip=f"{city['city']} - {place['name']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

# 지도 출력
st.subheader("📍 스페인 관광지 위치 지도")
st_data = st_folium(m, width=800, height=500)

# 관광지 상세 설명
st.subheader("📝 관광지 상세 설명")
for city in tourist_spots:
    st.markdown(f"### 🏙️ {city['city']}")
    for place in city["places"]:
        st.markdown(f"**{place['name']}**: {place['desc']}")
