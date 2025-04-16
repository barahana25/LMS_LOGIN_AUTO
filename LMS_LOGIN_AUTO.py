import requests
import os

set_cookie_url = "https://onekit.kumoh.ac.kr/index.jsp?returnurl=http%3A%2F%2Flms.kumoh.ac.kr%3A71%2Fsso%2Fauth"

set_cookie_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

set_cookie_res = requests.get(set_cookie_url, headers=set_cookie_headers, allow_redirects=False)
JSESSIONID = set_cookie_res.cookies['JSESSIONID']

Cookie = f'JSESSIONID={JSESSIONID};'

first_url = "https://onekit.kumoh.ac.kr/proc/Login.eps"

first_headers = {
    'cookie': Cookie,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

data = {
    'user_id': '학번',
    'user_password': '비번'
}

first_res = requests.post(first_url, headers=first_headers, data=data, allow_redirects=False)

print(first_res.headers['Location'])