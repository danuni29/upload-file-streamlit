import streamlit as st
import folium
from streamlit_folium import st_folium


def save_location(lat, lon):
    # 클릭한 위치의 위도와 경도를 변수에 저장
    # lat_value = lat
    # lon_value = lon
    st.write(f"클릭한 위치의 위도: {lat}, 경도: {lon}")




def main():


    m = folium.Map(location=[37, 127], zoom_start=6.5, tiles='OpenStreetMap')
    m.add_child(folium.ClickForMarker())

    location = folium.LatLngPopup()
    st.write(location)
    m.add_child(folium.LatLngPopup())
    popup_text = st.text_input("Marker")
    m.add_child(folium.ClickForMarker(popup=popup_text))
    map = st_folium(m, width=600, height=600)


    # print(location)






if __name__ == '__main__':
    main()