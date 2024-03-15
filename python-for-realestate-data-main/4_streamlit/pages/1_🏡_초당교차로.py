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

st.subheader('위험구간1 - 초당교차로')    

col1, col2 = st.columns([1,1])
with col1:
    st.write('2번국도 첫번째 위험구간 - 초당교차로 - 초당교 구간<br>')
    option = st.selectbox('표시 이미지 선택:',
                 ['도로 사진(초당교)',
                  '지도 시각화'
                  ])
                  
with col2:
    if option == '도로 사진':
        st.image('0_data/초당교차로.jpg')  # 해당 이미지 파일의 경로
    elif option == '지도 시각화':
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
col1.plotly_chart(trade_mean_map1, use_container_width = True) 
col2.plotly_chart(vis_trade_rent1, use_container_width = True)


col1, col2 = st.columns([1,1])
col1.plotly_chart(trade_mean1, use_container_width = True)
col2.plotly_chart(trade_count1, use_container_width = True)