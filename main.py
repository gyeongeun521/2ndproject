import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="스페인 관광지 가이드", layout="wide")

st.title("🇪🇸 스페인 주요 관광지 가이드")
st.markdown("""
스페인은 역사, 문화, 예술, 건축, 그리고 맛있는 음식으로 가득한 나라입니다.  
아래는 스페인의 대표 도시와 관광지에 대한 친절하고 자세한 안내입니다.
""")

tourist_spots = [
    {
        "city": "마드리드",
        "location": [40.4168, -3.7038],
        "places": [
            {
                "name": "프라도 미술관",
                "desc": "유럽 최고의 고전 미술 컬렉션을 자랑하는 미술관입니다."
            },
            {
                "name": "왕궁",
                "desc": "스페인 왕실의 공식 거주지로, 웅장한 바로크 양식 건축물이 인상적입니다."
            }
        ]
    },
    {
        "city": "바르셀로나",
        "location": [41.3874, 2.1686],
        "places": [
            {
                "name": "사그라다 파밀리아",
                "desc": "가우디의 미완성 대성당. 독창적인 디자인으로 유명합니다."
            },
            {
                "name": "구엘 공원",
                "desc": "가우디가 설계한 환상적인 공원입니다."
            }
        ]
    },
    {
        "city": "그라나다",
        "location": [37.1773, -3.5986],
        "places": [
            {
                "name": "알람브라 궁전",
                "desc": "이슬람 건축의 걸작으로, 궁전과 정원이 아름답게 어우러진 곳입니다."
            }
        ]
    },
    {
        "city": "세비야",
        "location": [37.3886, -5.9823],
        "places": [
            {
                "name": "세비야 대성당",
                "desc": "세계에서 가장 큰 고딕 양식 성당 중 하나로, 콜럼버스의 묘가 있습니다."
            },
            {
                "name": "히랄다 탑",
                "desc": "세비야 대성당의 첨탑으로, 전망이 뛰어납니다."
            }
        ]
    },
    {
        "city": "톨레도",
        "location": [39.8628, -4.0273],
        "places": [
            {
                "name": "톨레도 대성당",
                "desc": "스페인 가톨릭의 중심지이며, 고딕 건축의 걸작입니다."
            }
        ]
    }
]

# Folium 지도 생성
m = folium.Map(location=[40.0, -3.5], zoom_start=6)

for city in tourist_spots:
    for place in city["places"]:
        folium.Marker(
            location=city["location"],
            popup=f"<strong>{city['city']} - {place['name']}</strong><br>{place['desc']}",
            tooltip=f"{city['city']} - {place['name']}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

st.subheader("📍 스페인 관광지 위치 지도")
st_data = st_folium(m, width=800, height=500)

st.subheader("📝 관광지 상세 설명")
for city in tourist_spots:
    st.markdown(f"### 🏙️ {city['city']}")
    for place in city["places"]:
        st.markdown(f"**{place['name']}**: {place['desc']}")
