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

st.header('분석 결과1: 교각, 터널마다 다르게 나타나는 노면온도 하락 패턴', divider='rainbow')
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
st.subheader('1차 관측 위험구간')
st.markdown('')
st.markdown('위험구간 100%가 교각이나 터널 출입구에 해당하였고, 이에 맞춰 위험구간을 1.육상교각, 2. 수상교각, 3. 터널 출입구 세 가지로 분류하였음')
st.markdown('1. 육: ')
st.write('교각의 경우: 육상 교량에서 노면온도 감소 효과가 수상 교량에서보다 더욱 크고 기상 조건에 영향을 덜 받는 특성을 확인함')
st.plotly_chart(bar1r, use_container_width=True)