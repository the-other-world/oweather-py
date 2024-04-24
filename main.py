import json
import os
import subprocess
import time
from textwrap import dedent

from calc import weather, owct


def cls():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


# 更新间隔秒数
UPDATE_INTERVAL = 10

if not os.path.exists("data.json"):
    obj = {
        "collected_at": 0,
        "cycle_0": 0,
        "cycle_now": 0,
        "weather": 0,
        "weather_until": 0,
        "high_temp_days": 0,
        "day_temp": 0.00,
        "cycle_hum": 0.00,
        "cycle_temp": 0.00,
        "temp_multi": 0.00,
        "fluctuation": 0.00,
        "last_preci": 0,
        "preci_chance": 0,
        "preci_level": 0,
        "precipitation": 0,
        "wind_scale": 0,
        "wind_speed": 0,
        "wind_direction": 0
    }
    jobj = json.dumps(obj, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(jobj)

while True:
    cls()
    now = owct.get_time()
    now_weather = weather.get_weather()
    print(dedent(f"""\
                               异世界气象信息
                               现在是：{now["years"]}/{now["months"]}/{now["days"]} {now["hours"]}:{now["minutes"]:02d}
                               天气：{now_weather["weather"]}
                               降水概率：{round(now_weather["preci_chance"] * 100)} %
                               降水量：{now_weather["precipitation"]} mm
                               气温：{now_weather["temp"]} ℃
                               湿度：{round(now_weather["cycle_hum"] * 100)} %
                               风：{now_weather["wind_direction"]}风
                               {now_weather["wind_scale"]}级（{now_weather["wind_speed"]} m/s）
                               """))
    time.sleep(UPDATE_INTERVAL)
    pass
