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
    "순서": ["첫 번째 위험구간", "첫 번째 위험구간", "세 번째 위험구간-1", "세 번째 위험구간-2", "네 번째 위험구간", "다섯 번째 위험구간"],
    "구간 상세": ["초당교 ~ 심정리 버스정류장", "열가재 주유소 ~ 옥전교", "벌교대교", "장양육교", "세풍대교 ~ 초남1교 ~ 초남터널", "중군터널 ~ 마룡교"],
    "노면온도 감소량": ["3.5℃ 감소", "3.1℃ 감소","1.2℃ 감소","2.1℃ 감소","1.9℃ 감소" ,"6.3℃ 감소"],
    "주소": ["보성군 미력면 초당리 713-5", "보성군 벌교읍 칠동리 1115-1", "보성군 벌교읍 장좌리", "보성군 벌교읍 장양리515", "광양시 광양읍 초남리 산79-11", "광양시 옥곡면 신금리 6-1"],
    "구간 총 길이": ["1.4km", "1.3km", "0.4km", "0.7km", "3.3km","7.3km"]
}

df1 = pd.DataFrame(data1)

st.header('■ 분석 결과2 - 공통 위험구간 선정 및 특성', divider='rainbow')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
     공통 위험구간이란? 1~4차 관측에서 노면온도가 감소하는 정도가 크고 그 감소 양상이 일관되게 유지되는 구간들을 공통 위험구간으로 산출<br>
     공통 위험구간의 경우, 다리와 터널 혹은 다리와 다리가 연쇄적으로 이어져있는 구조로 이로 인해 노면온도가 연달아서 감소하여 다른 곳에 비해 결빙 가능성이 높음
    </div>
    """, unsafe_allow_html=True)
st.subheader(' ')
st.subheader('공통 위험구간 5곳 상세 정보')
st.table(df1)
st.markdown('')
st.subheader('공통 위험구간의 연쇄 노면 냉각')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
     > 연쇄 노면냉각이란? 다리, 터널 같이 노면온도를 감소시키는 구간이 연달아 이어지면서 냉각효과 역시 중첩되어 노면온도가 크게 낮아지고 구간을 벗어난 후에도 구간 이전에 비해 낮은 노면온도를 보이는 현상을 연쇄 노면 냉각이라 지정하였음<br>
     > 이러한 연쇄 노면냉각이 잘 드러난 사례를 아래쪽 표에 첨부함
    </div>
    """, unsafe_allow_html=True)