import openai
import requests
from PIL import Image
openai.api_key = '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' # OpenAI API KEY

# Prompt for image generation
prompt = "a white siamese cat"

# Generate image using DALL-E 2 API
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512",
    model="image-alpha-001",
    response_format="url"
)

image_url = response['data'][0]['url']

# Download image from URL
image_data = requests.get(image_url).content

# Save image to file
with open("generated_image.jpg", "wb") as f:
    f.write(image_data)

# Display image
image = Image.open("generated_image.jpg")

image.show()

# openai.api_key: OpenAI API를 사용하기 위한 API 키를 설정합니다.
#
# prompt: DALL-E 2 API에 사용할 이미지 생성 프롬프트(입력 문장)를 지정합니다.
#
# openai.Image.create(): OpenAI의 DALL-E 2 API를 사용하여 이미지를 생성하는 함수를 호출합니다. prompt에는 이미지를 생성할 내용을 입력합니다. n은 생성할 이미지의 개수를 지정합니다. size는 생성된 이미지의 크기를 설정합니다. model은 사용할 DALL-E 2 모델을 선택합니다. response_format은 API 응답의 형식을 지정합니다. 여기서는 이미지 URL을 받아올 것을 지정합니다.
#
# image_url = response['data'][0]['url']: API 응답에서 생성된 이미지의 URL을 추출합니다.
#
# image_data = requests.get(image_url).content: 추출한 이미지 URL로부터 이미지 데이터를 다운로드합니다.
#
# with open("generated_image.jpg", "wb") as f: ...: 다운로드한 이미지 데이터를 "generated_image.jpg"라는 파일로 저장합니다.
#
# image = Image.open("generated_image.jpg"): 저장한 이미지 파일을 PIL 라이브러리를 사용하여 엽니다.
#
# image.show(): 열린 이미지를 출력합니다.