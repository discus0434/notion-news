import json
import os
import subprocess

import requests

from lib import NotionContent


def make_weather_forecast():
    """Make weather forecast.

    Returns
    -------
    list[NotionContent]
        list of contents to post to notion.
    """
    res = requests.get("https://weather.tsukumijima.net/api/forecast?city=130010")
    res = json.loads(res.content.decode("utf-8"))

    content = res["description"]["bodyText"].replace("\u3000", "")

    telop = res["forecasts"][0]["image"]["title"]

    if telop == "晴":
        icon = "☀️"
    elif telop == "曇":
        icon = "☁️"
    elif telop == "雨":
        icon = "☔️"
    elif telop == "雪":
        icon = "❄️"
    elif ["晴時々曇", "曇時々晴", "曇後時々晴", "曇後晴"].count(telop) > 0:
        icon = "🌤"
    elif ["晴一時雨", "晴時々雨", "雨時々晴", "雨後晴"].count(telop) > 0:
        icon = "🌦"
    elif ["曇一時雨", "曇時々雨", "雨時々曇", "雨後曇"].count(telop) > 0:
        icon = "🌧"
    elif ["晴一時雪", "晴時々雪", "雪時々晴", "雪後晴"].count(telop) > 0:
        icon = "⛄"
    elif ["曇一時雪", "曇時々雪", "雪時々曇", "雪後曇"].count(telop) > 0:
        icon = "🌨"
    else:
        if "雷" in telop:
            icon = "⚡"
        elif "雨" in telop:
            icon = "🌦️"
        elif "曇" in telop:
            icon = "🌥"
        elif "晴" in telop:
            icon = "🌤"
        elif "雪" in telop:
            icon = "🌨️"

    min_celsius = res["forecasts"][0]["temperature"]["min"]["celsius"]
    max_celsius = res["forecasts"][0]["temperature"]["max"]["celsius"]

    chance_of_rain_keys = {
        "T00_06": "0時 ~ 6時",
        "T06_12": "6時 ~ 12時",
        "T12_18": "12時 ~ 18時",
        "T18_24": "18時 ~ 24時",
    }

    chances_of_rain = []
    for key, val in res["forecasts"][0]["chanceOfRain"].items():
        if val == "--%":
            continue
        val = int(val.replace("%", ""))
        if val > 50:
            chances_of_rain.append(chance_of_rain_keys[key])

    if len(chances_of_rain) == 0:
        rain = "雨は降らない"
    elif len(chances_of_rain) == 1:
        rain = f"{chances_of_rain[0]}"
    else:
        rain = (
            f"{chances_of_rain[0].split('~')[0]}~{chances_of_rain[-1].split('~')[-1]}"
        )

    title = f"{telop} {min_celsius + '℃' if min_celsius is not None else ''} ~ {max_celsius + '℃' if max_celsius is not None else ''}, {rain}"

    subprocess.run(
        ["node", "markdown_to_notion.js", content, "./tmp.json"],
        stdout=subprocess.DEVNULL,
    )

    with open("./tmp.json", "r") as f:
        content_body = json.load(f)
    os.remove("./tmp.json")

    return NotionContent(
        title=title,
        icon=icon,
        tags=["AAAA_weather"],
        url="https://weather.tsukumijima.net/",
        content_body=content_body,
    )
