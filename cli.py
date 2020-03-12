#!/usr/bin/python
from covid import get_current_data, LOCALE_MAPPING

data = get_current_data()

for key, value in data["totals"].items():
    print(LOCALE_MAPPING[key], "=", value)
