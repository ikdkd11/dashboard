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
import mapp3

st.header('위험구간4 - 세풍대교')    
st.subheader('<세풍대교 - 초남1교 - 초남터널>')
st.write('주소: 전라남도 광양시 광양읍 초남리')    
box11 = plotbox.box1
map4_1 = mapp3.map41
map4_2 = mapp3.map42
map4_3 = mapp3.map43
map4_4 = mapp3.map44

grph4 = tot3.grp44
col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간4(세풍대교-초남1교-초남터널) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%84%B8%ED%92%8D%EB%8C%80%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간4(세풍대교-초남1교-초남터널) 위성사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map4_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map4_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map4_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map4_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph4, use_container_width = True)
col2.plotly_chart(box11, use_container_width = True) 