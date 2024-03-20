import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
import json
import math
import plotbox
import streamlit as st
from datetime import datetime
from PIL import Image
import requests
from io import BytesIO
import tot3
import mapp4

st.header('위험구간 다섯번째 - 수어천교')    
st.subheader('<중군터널 - 신금1,2교 - 수어천교 - 마룡교>')
st.write('주소: 전라남도 광양시 옥곡면 신금리')
box11 = plotbox.box1
map5_1 = mapp4.map51
map5_2 = mapp4.map52
map5_3 = mapp4.map53
map5_4 = mapp4.map54

grph5 = tot3.grp55
col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간5(중군터널-신금1,2교-수어천교-마룡교) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%88%98%EC%96%B4%EC%B2%9C%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간5(중군터널-신금1,2교-수어천교-마룡교) 위성사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map5_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map5_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map5_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map5_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph5, use_container_width = True)
col2.plotly_chart(box11, use_container_width = True) 