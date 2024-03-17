import pandas as pd
import folium
from folium.plugins import DualMap
import branca.colormap as cm
import os
import pathlib
import datetime

# 임시 폴더 설정
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/1_1.csv"
)
df1 = pd.read_csv(url1)


def road_map11(df1):
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

    # 지도 객체 생성
    map11 = DualMap(location=center, zoom_start=15)
    for i, point in enumerate(lines):
        rtemp = rtems[i]
        diff = round(rtemp - temps[i], 1)

        folium.Circle(
            location=point, radius=10, fill=True,
            color=colormap(rtemp), fill_opacity=0.5
        ).add_to(map11.m1)

        folium.Circle(
            location=point, radius=10, fill=True,
            color=colormap(diff), fill_opacity=0.5
        ).add_to(map11.m2)

    map11.m2.add_child(colormap)

    return map11
