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

st.header('위험구간 분류', divider='rainbow')
st.text('위험구간: 노면온도가 2~3초 이내에 섭씨 1도 이상 급락하는 구간') 
st.markdown('위험구간 100%가 교각이나 터널 출입구에 해당하였고, 이에 맞춰 위험구간을 1.육상교각, 2. 수상교각, 3. 터널 출입구 세 가지로 분류하였음')
st.subheader('1차 관측 위험구간')
st.markdown('')
st.markdown('위험구간 100%가 교각이나 터널 출입구에 해당하였고, 이에 맞춰 위험구간을 1.육상교각, 2. 수상교각, 3. 터널 출입구 세 가지로 분류하였음')
st.markdown('1. 육: ')
st.write('교각의 경우: 육상 교량에서 노면온도 감소 효과가 수상 교량에서보다 더욱 크고 기상 조건에 영향을 덜 받는 특성을 확인함')
