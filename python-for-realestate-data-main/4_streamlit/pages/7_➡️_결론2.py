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
import tta
import result1
url1p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EB%8B%A4%EB%A6%AC%EC%9E%90%EB%A3%8C.png'
url2p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%ED%84%B0%EB%84%90%EC%9E%90%EB%A3%8C.png'
response1 = requests.get(url1p)
response2 = requests.get(url2p)
image1 = Image.open(BytesIO(response1.content))
image2 = Image.open(BytesIO(response2.content))

bar1r = result1.bar1
data1 = {
    "분류": ["1차 관측", "2차 관측", "3차 관측", "4차 관측", "전체"],
    "육상교각": ["2.7℃ 감소", "2.4℃ 감소", "2.9℃ 감소", "2.6℃ 감소", "2.7℃ 감소"],
    "수상교각": ["2.0℃ 감소", "1.6℃ 감소", "2.4℃ 감소", "2.1℃ 감소", "2.1℃ 감소"],
    "터널": ["4.7℃ 감소", "7.8℃ 감소", "4.8℃ 감소", "7.5℃ 감소", "6.2℃ 감소"]
}

df1 = pd.DataFrame(data1)

st.header('■ 분석 결과2 - 공통 위험구간 선정 및 특성', divider='rainbow')
st.subheader('1차 관측 위험구간')
st.markdown('')
st.markdown('위험구간 100%가 교각이나 터널 출입구에 해당하였고, 이에 맞춰 위험구간을 1.육상교각, 2. 수상교각, 3. 터널 출입구 세 가지로 분류하였음')
st.markdown('1. 육: ')
st.write('교각의 경우: 육상 교량에서 노면온도 감소 효과가 수상 교량에서보다 더욱 크고 기상 조건에 영향을 덜 받는 특성을 확인함')
