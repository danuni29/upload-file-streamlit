import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium, folium_static
import os

def main():
    uploaded_file = st.file_uploader("파일을 선택하세요", type=['csv'])
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file,
                         usecols=['lat', 'lng'])



        df.columns = ['lat', 'lon']



        m = folium.Map(location=[37, 127], zoom_start=6.5, min_zoom=5, max_zoom=12, tiles="cartodbpositron")
        for i, row in df.iterrows():
            folium.Marker(location=[row['lat'], row['lon']], popup=f"lat {row['lat']}, lon {row['lon']}").add_to(m)

        folium_static(m, width=700, height=650)



if __name__ == '__main__':
    main()