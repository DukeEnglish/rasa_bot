from requests import ConnectionError, HTTPError, TooManyRedirects, Timeout

from .api import get_weather_by_day


def get_text_weather_date(address, date_time_number, date_time,):
    # print(address, date_time_number, date_time)
    try:
        result = get_weather_by_day(address, date_time_number)
    except (ConnectionError, HTTPError, TooManyRedirects, Timeout) as e:
        text_message = "{}".format(e)
    else:
        text_message_tpl = "{} {} ({}) 的天气情况为：白天：{}；夜晚：{}；气温：{}-{} 度"
        text_message = text_message_tpl.format(
            result['location']['name'],
            date_time,
            result['result']['date'],
            result['result']['text_day'],
            result['result']['text_night'],
            result['result']["high"],
            result['result']["low"],
        )

    return text_message


if __name__ == '__main__':
    res = get_text_weather_date('天津', date_time_number=1, date_time =122)
    print(res)
