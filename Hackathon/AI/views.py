from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import openai
import os
import time
from django.conf import settings
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from django.core.files.storage import FileSystemStorage
import requests
import json
import re
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

def azv_obj(urls):
    import os
    import azure.ai.vision as sdk

    subscription_key = "08c8b609891449f6a120a64d392da837"  # <--- 여기에 구독 키 입력
    endpoint = "https://jungseoik.cognitiveservices.azure.com/"  # <--- 여기에 엔드포인트 URL 입력

    service_options = sdk.VisionServiceOptions(endpoint, subscription_key)

    vision_source = sdk.VisionSource(
        url=urls)

    analysis_options = sdk.ImageAnalysisOptions()
    analysis_options.features = (
        sdk.ImageAnalysisFeature.OBJECTS,
        sdk.ImageAnalysisFeature.TAGS
    )

    analysis_options.language = "en"

    image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

    result = image_analyzer.analyze()
    obj =""
    if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

        if result.tags is not None:

            print(" Tags:")
            for tag in result.tags:
                obj += (str(tag.name)+",")
            obj = ("Tags :" + obj)
            print(obj)
            return obj
    else:
        error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
        print(" Analysis failed.")
        print("   Error reason: {}".format(error_details.reason))
        print("   Error code: {}".format(error_details.error_code))
        print("   Error message: {}".format(error_details.message))

def azv(urls):
    import os
    import azure.ai.vision as sdk

    subscription_key = "08c8b609891449f6a120a64d392da837"  # <--- 여기에 구독 키 입력
    endpoint = "https://jungseoik.cognitiveservices.azure.com/"  # <--- 여기에 엔드포인트 URL 입력

    service_options = sdk.VisionServiceOptions(endpoint,
                                               subscription_key)

    vision_source = sdk.VisionSource(
        url=urls)

    analysis_options = sdk.ImageAnalysisOptions()

    analysis_options.features = (
            sdk.ImageAnalysisFeature.CAPTION |
            sdk.ImageAnalysisFeature.DENSE_CAPTIONS
    )

    analysis_options.language = "en"

    analysis_options.gender_neutral_caption = True

    image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

    result = image_analyzer.analyze()
    AZV = ""
    if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:


        if result.dense_captions is not None:
            for caption in result.dense_captions:
                # AZV += (str(caption.content) + ", Confidence" + str(caption.confidence) + "\n")
                AZV += "{}, Confidence {:.2f}\n".format(caption.content, caption.confidence)

        print(AZV)
        return AZV
    else:
        error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
        print(" Analysis failed.")
        print("   Error reason: {}".format(error_details.reason))
        print("   Error code: {}".format(error_details.error_code))
        print("   Error message: {}".format(error_details.message))





def dall2(pt):
    import openai
    import requests
    from PIL import Image
    openai.api_key = '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'

    # Prompt for image generation
    prompt = pt

    # Generate image using DALL-E 2 API
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        model="image-alpha-001",
        response_format="url"
    )

    image_url = response['data'][0]['url']
    return image_url

# OpenAI API 키 설정

def gpt(str):
    # get_completion 함수 정의
    openai.api_key = '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'

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

    response = get_completion(prompt)
    print(response)
    return response



def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def web_index(request):

    return render(request, 'Web.html')


def imdex(request):
    cap = ""
    text = ""
    dall = ""
    gpt_text = ""
    if request.method == 'POST':
        # text = request.POST.get('text', '')
        image = request.FILES.get('image')
        image_file = request.FILES['image']

        cap = process_image(image)
        temp = "https://46f0-49-171-116-113.ngrok-free.app/static/"+ str(cap)

        azv_result = azv(temp)
        azvobj_result = azv_obj(temp)

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
MBTI : <답> .MBTI
신뢰도 : <답>
형식으로 적어줘 그외에는 아무것도 안적어줘도 돼
'''.format(azvobj_result, azv_result)
        print(long_string)
        gpt_result = gpt(translateK_E(long_string))
        gpt_temp = gpt_result
        gpt_text = gpt_result
        print(gpt_text)

        result_part = re.search(r'result:(.*?)\.end_result', gpt_result, re.DOTALL)
        if result_part:
            extracted_text = result_part.group(1).strip()
            print(extracted_text)

        result_part_em = re.search(r'emotion_result:(.*?)\.emotion', gpt_temp, re.DOTALL)
        if result_part_em:
            extracted_text_em = result_part_em.group(1).strip()
            print(extracted_text_em)


        dall = dall2(extracted_text)
        # cap = azvobj_result
        text = azv_result

        print(cap)
    return render(request, 'imdex.html',{'cap': cap, 'text': text , 'dall' : dall , 'gpt_text' : gpt_text})




def process_image(image):
    # 이미지를 웹 서버에 업로드
    fs = FileSystemStorage()
    uploaded_image = fs.save('static/temp_image.png', image)

    # 업로드된 이미지의 URL 생성
    image_url = fs.url(uploaded_image)

    # Image processing using sdk.VisionSource()
    caption = image_url
    # ... sdk.VisionSource()를 사용한 이미지 처리 ...
    caption = caption.split("/")[-1]
    return caption

def input_text(request):
    cap = ""
    text = ""
    if request.method == 'POST':
        # text = request.POST.get('text', '')
        image = request.FILES.get('image')
        image_file = request.FILES['image']
        cap = process_image(image)
        # cap = image
        print(image)
        print(image_file)
        print(cap)

    return render(request, 'input_text.html',{'cap': cap, 'text': text})


from django.shortcuts import render

def home(request):
    First_text = request.POST.get('text', '')  # POST 요청으로부터 'text' 값을 가져옴
    text = gpt(First_text)
    url = dall2(text)

    return render(request, 'home.html', {'text': text, 'url' : url})








