import pandas as pd
import folium
from folium.plugins import DualMap
import branca.colormap as cm
import os
import pathlib
import datetime

# 임시 폴더 설정
TEMP_DIR = os.path.join(pathlib.Path(__file__).parent.absolute(), "temps")

# 임시 폴더 삭제 함수
def _clear_temps():
    os.makedirs(TEMP_DIR, exist_ok=True)
    for f in os.listdir(TEMP_DIR):
        try:
            os.remove(os.path.join(TEMP_DIR, f))
        except:
            pass

def create_map(csv_path: str):
    _, ext = os.path.splitext(csv_path)
    ext = ext.lower()
    if ext == ".csv":
        df = pd.read_csv(csv_path, encoding="utf-8")
    elif ext == ".xlsx":
        df = pd.read_excel(csv_path)

    try:
        datetime.datetime.strptime(df["wdate_"][0], "%Y-%m-%d %H:%M")
    except:
        pass

    lines = df[["위도", "경도"]].values[:].tolist()
    rtems = df["노면온도"].tolist()
    temps = df["기온"].tolist()

    avg_lat = df["위도"].mean()
    avg_lon = df["경도"].mean()
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

if __name__ == "__main__":
    _clear_temps()
    # map11 객체에 지도 생성
    map11 = create_map("1_1.csv")
    # 사용 예: map11 객체로 다양한 조작 수행 가능
    # 예: map11.save('example.html')  # 객체를 HTML 파일로 저장하는 방법
    _clear_temps()
