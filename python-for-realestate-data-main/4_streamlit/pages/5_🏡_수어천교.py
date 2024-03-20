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
import mapp

st.header('위험구간 다섯번째 - 수어천교')    
st.subheader('<중군터널 - 신금1,2교 - 수어천교 - 마룡교>')
st.write('주소: 전라남도 광양시 광양읍 초남리')
box11 = plotbox.box1
map1_1 = mapp.map11
map1_2 = mapp.map12
map1_3 = mapp.map13
map1_4 = mapp.map14

grph1 = tot3.grp11
col1, col2 = st.columns([1,1])
with col1:
    st.write('2번국도 첫번째 위험구간 - 초당교차로 - 초당교 구간')
    option = st.selectbox('표시 이미지 선택:',
                 ['도로 사진(초당교)',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EC%B4%88%EB%8B%B9%EA%B5%90%EC%B0%A8%EB%A1%9C.png"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '도로 사진(초당교)':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map1_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map1_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map1_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map1_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph1, use_container_width = True)
col2.plotly_chart(box11, use_container_width = True) 