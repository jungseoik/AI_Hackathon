# OpenAI 라이브러리 및 API 키를 불러옵니다.
import openai
import os
import pandas as pd
import time

# OpenAI API 키 설정
openai.api_key = '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'

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
prompt = "gpt야 1+2는 뭐야"
response = get_completion(prompt)
print(response)
