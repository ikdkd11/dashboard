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
import mapp1

st.subheader('위험구간2 - 옥전교')    

#1차 위험지역 지도 시각화 자료 호출
map2_1 = mapp1.map21
map2_2 = mapp1.map22
map2_3 = mapp1.map23
map2_4 = mapp1.map24

#1~5번째 위험지역 별 시계열 그래프
grph2 = tot3.grp22

#1~5번째 위험지역 별 박스그림
box11 = plotbox.box1
box22 = plotbox.box2

col1, col2 = st.columns([1,1])
with col1:
    st.write('2번국도 첫번째 위험구간 - 초당교차로 - 초당교 구간')
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간2(옥전교) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url2 = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%98%A5%EC%A0%84%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url2)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간2(옥전교) 위성사진':
        st.image(image_url2)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map2_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map2_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map2_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map2_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph2, use_container_width = True)
col2.plotly_chart(box22, use_container_width = True) 