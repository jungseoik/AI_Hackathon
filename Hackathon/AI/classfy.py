# importing the library
from google_images_download import google_images_download

# class instantiation
response = google_images_download.googleimagesdownload()

# keywords : 원하는 검색 키워드
# limit : 원하는 다운로드 사진 개수 (수정 버전에서는 최대 100개까지 가능)
# format : 다운로드 확장자 지정
arguments = {
    "keywords": "워너원 강다니엘, 엑소 백현, 박보검, 송중기, 워너원 황민현, 엑소 시우민, 강동원, 이종석, 이준기, 마동석, 조진웅, 조세호, 안재홍, 윤두준, 이민기, 김우빈, 육성재, 공유, BTS 정국, 아이콘 바비, 워너원 박지훈, 엑소 수호",
    "limit": 50,
    "print_urls": True,
    "format": "jpg"
    }

# passing the arguments to the function
paths = response.download(arguments)

# printing absolute paths of the downloaded images
print(paths)