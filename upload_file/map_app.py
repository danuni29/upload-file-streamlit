import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static
import os

def main():
    uploaded_file = st.file_uploader("파일을 선택하세요", type=['csv'])
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file,
                         usecols=['lat', 'lon', 'name', 'gloc'])



        # df.columns = ['lat', 'lon']



        m = folium.Map(location=[37, 127], zoom_start=6.5,tiles="cartodbpositron")


        for i, row in df.iterrows():
            iframe = f"이름: <strong>{row['name']}</strong><br>국가격자번호: <strong>{row['gloc']}</strong><br> 위경도: {row['lat']:.4f}, {row['lon']:.4f}"
            popup = folium.Popup(iframe, min_width=200, max_width=200)
            folium.Marker(location=[row['lat'], row['lon']], popup=popup).add_to(m)

        folium_static(m, width=700, height=650)



if __name__ == '__main__':
    main()