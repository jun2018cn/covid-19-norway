import json
import urllib3
from fake_useragent import UserAgent

"""
Base URL: https://www.vg.no/spesial/2020/corona-viruset/data

Sub URLs:
/norway-table-overview/?region=county
/norway-table-overview/?region=municipality
/norway-allCases/
/norway-routes-country/
/norway-routes-county/
/daily-reports/
/norway-region-data/
/timeseriesWorld/
"""
BASE_URL = "https://www.vg.no/spesial/2020/corona-viruset/data"

LOCALE_MAPPING = {"confirmed": "Smittede", "dead": "Døde", "recovered": "Friske"}


def perform_request(path):
    ua = UserAgent()
    http = urllib3.PoolManager()
    r = http.request("GET", BASE_URL + path, headers={"User-Agent": ua.random})
    if r.status != 200:
        print("Error whilst fetching data for path:", path)
        return
    return json.loads(r.data.decode("utf-8"))


def get_current_data():
    path = "/norway-table-overview/?region=municipality"
    return perform_request(path)
