import folium
import pandas as pd
import branca.colormap as cm
from streamlit_folium import st_folium

# 데이터 불러오기
url1 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/1_1.csv"
df1 = pd.read_csv(url1)

def road_map_single(df1):
    lines = df1[["위도", "경도"]].values[:].tolist()
    rtems = df1["노면온도"].tolist()
    temps = df1["기온"].tolist()

    avg_lat = df1["위도"].mean()
    avg_lon = df1["경도"].mean()
    center = [avg_lat, avg_lon]

    colormap = cm.LinearColormap(
        colors=[
            "white", "black", "darkslateblue", "fuchsia", "orchid", "violet",
            "navy", "blue", "dodgerblue", "darkturquoise", "lightskyblue",
            "darkgreen", "limegreen", "lime", "lemonchiffon", "yellow",
            "lightsalmon", "coral", "tomato", "crimson", "red"
        ],
        index=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        vmin=-10, vmax=10
    ).to_step(n=20)

    # 단일 지도 객체 생성
    map11 = folium.Map(location=center, zoom_start=15)
    for i, point in enumerate(lines):
        rtemp = rtems[i]
        # 여기서는 노면온도를 기준으로 원을 추가합니다.
        folium.Circle(
            location=point, radius=10, fill=True,
            color=colormap(rtemp), fill_opacity=0.5
        ).add_to(map11)

    # 컬러맵을 지도에 추가
    map11.add_child(colormap)

    return map11

# 함수 호출 및 지도 생성
map1_1 = road_map_single(df1)