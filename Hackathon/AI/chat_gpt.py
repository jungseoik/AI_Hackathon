# OpenAI 라이브러리 및 API 키를 불러옵니다.
import openai
import requests
import json
import re
# OpenAI API 키 설정
openai.api_key = ' '

def gpt(str):
    # get_completion 함수 정의
    def get_completion(prompt, model="gpt-3.5-turbo"):
        """
        GPT-3.5 모델에 대화형으로 요청을 보내고 응답을 반환하는 함수

        Parameters:
            prompt (str): 사용자의 입력 질문이나 메시지로 구성된 문자열.
            model (str, optional): 사용할 GPT 모델을 선택. 기본값은 'gpt-3.5-turbo'.

        Returns:
            str: GPT 모델로부터 생성된 응답 문자열.
        """

        # 대화형 형식의 데이터로 변환
        messages = [{"role": "user", "content": prompt}]

        # OpenAI ChatCompletion API를 사용하여 GPT 모델에 대화형 요청을 보냄
        response = openai.ChatCompletion.create(
            model=model,  # 사용할 GPT 모델 선택
            messages=messages,  # 대화형 데이터를 담은 리스트
            temperature=0,  # 모델의 응답 다양성 조절. 0일 경우 보수적인 답변을 생성.
        )

        # API 응답에서 생성된 응답 문자열을 추출하여 반환
        return response.choices[0].message["content"]

    # 사용자 입력으로 주어진 문장을 GPT 모델에 보내고 응답 출력
    # prompt = "gpt야 1+2는 뭐야"
    prompt = str
    print(str)
    response = get_completion(prompt)
    print(response)
    return response





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


v1 = "Tags :text,clothing,person,display device,indoor,wall,media,television set,led-backlit lcd display,flat panel display,furniture,lcd tv,man,television,video,multimedia,output device,computer monitor,table,screen,standing,design,"
v2 = '''
a person pointing at a screen, Confidence 0.78
a screen shot of a computer, Confidence 0.76
a person pointing at a screen, Confidence 0.77
a close up of a table, Confidence 0.75
a close up of a person's head, Confidence 0.81
a person's back pocket, Confidence 0.73
a close up of a plant, Confidence 0.76
a person pointing at a screen, Confidence 0.80
a person in a yellow coat, Confidence 0.67
a screenshot of a phone, Confidence 0.77
'''
long_string = '''
현재 나는 어떤 이미지에 대해서 다음과 같은 단어를 추출했어. 
추출한 단어는 다음과 같아
{}

그리고 이 이미지에 대한 간단한 설명들을 추출했고 그 확률들이야 
{}


이걸 모두 종합해서 너한테 요구하는 답변이 있어.
1. 감정을 표현하는 단어들 10개를 나에게 보여줘 그리고 그 단어들이 이미지에서 어느정도 비율로 차지하는지 100% 기준으로 보여줘
강조 - 해당 답변을 할 때 '명심'해야 하는건 꼭 답변 시작하는 앞에 "emotion_result: "를 쓰고 답을 하고 답 마지막에는 ".emotion" 로 마무리해서 적어줘
2. 해당 감정단어들을 사용해서 간단한 풍경사진이나 인물사진, 동물사진 중 하나를 선택해서 글로 만들어서 표현해줘
조건은 
a)너가 추출해낸 단어를 활용해야 하고 
b)dalle api에 넣을 수 있는 하나의 이미지를 생성하는 문장을 만들어줘 
c)명심해야 할 점은 답변을 위에서 언급한 내용을 나열하지 않고 너가 추출한 단어들을 활용해서 '창의적'으로 하나의 문장을 만들어서 보여줘야돼
        
예를 들면 다음과 같이 보여줄 수 있어
ex) result: 열정적으로 미래를 향해 남녀가 함께 협업하는 사업 회의 장면이며 뒷 배경은 오피스텔 차가운 건물안에 멋진 책상이 존재한다.
꼭 앞에 "result : " 를 쓰고 답변 마지막에는 ".end_result" 를 적어줘
        
3. 마지막으로 모든 결과물을 통합해서 이 이미지를 찍은 사용자의 mbti가 뭔지 추측하고 그 신뢰도를 보여줘
해당 답변은
ex)
MBTI: <답> .MBTI
신뢰도 : <답>
형식으로 답해주고 한글로 말해줘 그외에는 아무것도 안적어줘도 돼
'''.format(v1,v2)


print(long_string)
long_string2 = long_string

result_part = re.search(r'result:(.*?)\.end_result', long_string, re.DOTALL)
if result_part:
    extracted_text = result_part.group(1).strip()
    print(extracted_text)

result_part_em = re.search(r'emotion_result:(.*?)\.emotion', long_string2, re.DOTALL)
if result_part_em:
    extracted_text = result_part_em.group(1).strip()
    print(extracted_text)