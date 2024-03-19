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

st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.header('2번국도(보성(초당교차로)~광양(마룡교)) 결빙관측 관측회차 별 노면온도 시계열') 
vis_trade_rent1 = tot2.grp2
trade_count1 = tot2.grp4
trade_mean1 = tot2.grp3            
trade_mean_map1 = tot2.grp1
                          
# 첫 번째 차트
st.plotly_chart(trade_mean_map1, use_container_width=True)

# 두 번째 차트
st.plotly_chart(vis_trade_rent1, use_container_width=True)

# 세 번째 차트
st.plotly_chart(trade_mean1, use_container_width=True)

# 네 번째 차트
st.plotly_chart(trade_count1, use_container_width=True)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


