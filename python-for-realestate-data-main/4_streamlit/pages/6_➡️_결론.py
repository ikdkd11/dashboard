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

bar1r = result1.bar1
data1 = {
    "분류": ["1차 관측", "2차 관측", "3차 관측", "4차 관측", "전체"],
    "육상교각": ["2.7℃ 감소", "2.4℃ 감소", "2.9℃ 감소", "2.6℃ 감소", "2.7℃ 감소"],
    "수상교각": ["2.0℃ 감소", "1.6℃ 감소", "2.4℃ 감소", "2.1℃ 감소", "2.1℃ 감소"],
    "터널": ["4.7℃ 감소", "7.8℃ 감소", "4.8℃ 감소", "7.5℃ 감소", "6.2℃ 감소"]
}

df1 = pd.DataFrame(data1)

st.header('분석 결과1 - 교각, 터널마다 다르게 나타나는 노면온도 하락 패턴', divider='rainbow')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
    1. 교각, 터널에서만 노면온도가 짧은 시간(수 초 이내)동안에 급락(1℃ 이상 하강)<br>
    2. 교각의 경우, 육상교각에서 수상교각보다 노면온도가 크게 감소<br>
    3. 터널의 경우, 터널의 길이가 길수록 터널 출입구 주변의 노면온도가 크게 감소
    </div>
    """, unsafe_allow_html=True)
st.plotly_chart(bar1r, use_container_width=True)
st.table(df1)
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
    ○ 육상교각의 노면온도가 수상교각의 노면온도 감소량보다 0.5~0.8℃ 가량 더 크게 감소하는 것으로 나타났다.<br>
    ○ 노면온도가 더 크게 감소하는 특성과 더불어 주변 지리환경에 따라 커브, 내리막 등 운전 상의 난점이 존재하는 육상교각의 특성을 고려했을 때 육상교각의 결빙사고 위험성이 높다고 판단됨<br>
    3. 터널의 경우, 터널의 길이가 길수록 터널 출입구 주변의 노면온도가 크게 감소
    </div>
    """, unsafe_allow_html=True)
st.subheader('1차 관측 위험구간')
st.markdown('')
st.markdown('위험구간 100%가 교각이나 터널 출입구에 해당하였고, 이에 맞춰 위험구간을 1.육상교각, 2. 수상교각, 3. 터널 출입구 세 가지로 분류하였음')
st.markdown('1. 육: ')
st.write('교각의 경우: 육상 교량에서 노면온도 감소 효과가 수상 교량에서보다 더욱 크고 기상 조건에 영향을 덜 받는 특성을 확인함')
