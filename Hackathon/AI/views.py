from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# OpenAI 라이브러리 및 API 키를 불러옵니다.
import openai
import os
import pandas as pd
import time
from django.conf import settings
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

def clv(URL):

    # Replace with your own API key
    YOUR_CLARIFAI_API_KEY = "0f679e77367a481fbdd439313178d644+지워"
    stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
    # This is how you authenticate.
    metadata = (("authorization", f"Key {YOUR_CLARIFAI_API_KEY}"),)
    # URL of the image you want to analyze

    SAMPLE_URL = URL
    # SAMPLE_URL = "https://learn.microsoft.com/azure/cognitive-services/computer-vision/media/quickstarts/presentation.png"


    request = service_pb2.PostModelOutputsRequest(
        # This is the model ID of a publicly available General model.
        model_id="aaa03c23b3724a16a56b629203edc62c",
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(image=resources_pb2.Image(url=SAMPLE_URL))
            )
        ],
    )
    response = stub.PostModelOutputs(request, metadata=metadata)
    if response.status.code != status_code_pb2.SUCCESS:
        raise Exception(f"Request failed, status code: {response.status}")
    # Get captions (top 20 words) from the response
    captions = [concept.name for concept in response.outputs[0].data.concepts[:20]]
    # print("Top 20 Captions:", captions)
    caption_string = ', '.join(captions)
    return caption_string




def azv(urls):
    import os
    import azure.ai.vision as sdk

    subscription_key = "08c8b609891449f6a120a64d392da837+지워"  # <--- 여기에 구독 키 입력
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

    if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

        if result.caption is not None:

            AZV = result.caption.content
            return AZV
        # if result.dense_captions is not None:
        #     AZV = result.dense_caption.content
        #     return AZV


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
    openai.api_key = ''

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
    # openai.api_key = ''

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
    if request.method == 'POST':
        text = request.POST.get('text', '')
        image = request.FILES.get('image')
        image_file = request.FILES['image']
        cap = process_image(image)
        # cap = image
        temp = "https://bdf9-106-101-129-247.ngrok-free.app/static/"+ str(cap)
        print(temp)
        # clv_result = azv(temp)
        # dall = dall2(str(clv_result))
        dall = "ddd"
        # text = clv_result
        print(image)
        print(image_file)
        print(cap)
    return render(request, 'imdex.html',{'cap': cap, 'text': text , 'dall' : dall})




from django.core.files.storage import FileSystemStorage
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
        text = request.POST.get('text', '')
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








