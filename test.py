# -*- coding:UTF-8 -*-
"""
作者 zhangmingyu
日期 2021年05月01日
"""
import requests
html=requests.get("http://hymplus.ltd/update?num=-1")
print(html.text)
print(html.text.split("=")[-1])