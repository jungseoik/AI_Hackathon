# papago 번역 API 사용 - 함수 활용
import requests
import json

# translate 함수 선언
def translateK_E(text, source='ko', target='en'):
    CLIENT_ID, CLIENT_SECRET = 'LJUqzxG88x9BqrkdbTZt', 'ydVajsYWYe'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': 'ko', 'target': 'en', 'text': text}
    response = requests.post(url, json.dumps(data), headers=headers)
    return response.json()['message']['result']['translatedText']

def translateE_K(text, source='en', target='ko'):
    CLIENT_ID, CLIENT_SECRET = 'LJUqzxG88x9BqrkdbTZt', 'ydVajsYWYe'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': 'en', 'target': 'ko', 'text': text}
    response = requests.post(url, json.dumps(data), headers=headers)
    return response.json()['message']['result']['translatedText']

# 번역할 문장 입력 후 함수에 전달
text = '파파고 API 실습이 재미있네요.'
en_text = translateK_E(text)
print(en_text)

text = 'The Papago API practice is interesting.'
en_text = translateE_K(text)
print(en_text)

# 실행 결과
