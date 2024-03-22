import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
# import folium
import json
# import math
import tot2
import plotbox
import streamlit as st
from datetime import datetime
from PIL import Image
from folium.plugins import DualMap
from branca.colormap import LinearColormap
import mapp5

st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)#fd
st.header('2번국도(보성(초당교차로)~광양(마룡교)) 결빙관측 관측회차 별 분석정보') 
vis_trade_rent1 = tot2.grp2
trade_count1 = tot2.grp4
trade_mean1 = tot2.grp3            
trade_mean_map1 = tot2.grp1
mmap1 = mapp5.map61
mmap2 = mapp5.map62
mmap3 = mapp5.map63
mmap4 = mapp5.map64

tab1, tab2, tab3, tab4 = st.tabs(["1차 관측", "2차 관측", "3차 관측", "4차 관측"])
with tab1:
# 첫 번째 차트
    st.header('2번국도(보성(초당교차로)~광양(마룡교)) 1차관측 노면온도 시계열 그래프') 
    st.subheader('10일 저녁~11일 새벽 : 예보 중점 사항')
    st.markdown(
        '''
        1. 내일(11일) 새벽부터 오전 사이 내륙을 중심으로 :blue[짙은 안개]가 끼는 곳이 있겠습니다.
        2.  :blue[내린 비]가 얼어 :red[도로 살얼음]이 나타나는 곳이 있겠습니다.
        ''')
    st.markdown(
        '''
         > 1차 관측 시: 보성/순천/광양 평균 풍향풍속 : 
        1. 보성 <WNW, 5.4m/s>, 순천 <NNW, 2.4m/s>, 광양 <N, 1.7m/s>.
        2. 관측구간 내 평균 습도 : 56%
        3. 시간 당 평균 일사량/일조율 : 48MJ/m^2, 50% 
        '''
    )
    st.plotly_chart(trade_mean_map1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 1차관측 노면온도 정보 지도 시각화') 
    st.plotly_chart(mmap1, use_container_width=True)
with tab2:
# 두 번째 차트
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 2차관측 노면온도 시계열 그래프')
    st.plotly_chart(vis_trade_rent1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 2차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap2, use_container_width=True)   
with tab3:
# 세 번째 차트
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 3차관측 노면온도 시계열 그래프')
    st.plotly_chart(trade_mean1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 3차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap3, use_container_width=True)
with tab4:
# 네 번째 차트
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 4차관측 노면온도 시계열 그래프')
    st.plotly_chart(trade_count1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 4차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap4, use_container_width=True)

#5
#st_folium(mmap1, width=1000)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


