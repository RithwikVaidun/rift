import requests

cookies = {
    '_did-603548799': '08c09554-c053-4c8f-b905-ffb653761f27',
    'tool': '',
    'selection': '',
    'portalApp': 'student',
    'JSESSIONID': '5B4184D12F091B04C6B28F14A245F885',
    'XSRF-TOKEN': '67da6b2d-6eab-47e4-8d4b-251042b1f113',
    'portalLang': 'en',
    'appName': 'fremont',
    'sis-cookie': '!xP52pFe5WYJWPfIuK9LQTj293o8cRjnpFsYVLIm6v9YtOqLRETtsrNt9GeIQgWUOaovI05QpDoHqXes=',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'Accept': 'application/json, text/plain, */*',
    'Expires': '0',
    'Cache-Control': 'no-cache',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://fremontunifiedca.infinitecampus.org/campus/apps/portal/student/classroom/71637/grades?showAllTerms=false&selectedTermID=510',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
}

params = (
    ('showAllTerms', 'false'),
    ('selectedTermID', '510'),
)

response = requests.get('https://fremontunifiedca.infinitecampus.org/campus/resources/portal/grades/detail/71637', headers=headers, params=params, cookies=cookies)
print("test")
print(response.json())