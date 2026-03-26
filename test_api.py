import requests
import pytest


class TestAPI:
    def test_get_text(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        params = {
            "city": "郑州",
            "key": "c904a499ae9bcda8d4c8383d0c516fa1"
                  }
        resp = requests.get(url=url, params=params)
        print(resp.text)


if __name__ == '__main__':
    pytest.main(['-vs'])





