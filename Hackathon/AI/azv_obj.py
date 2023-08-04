import os
import azure.ai.vision as sdk

subscription_key = "08c8b609891449f6a120a64d392da837"  # <--- 여기에 구독 키 입력
endpoint = "https://jungseoik.cognitiveservices.azure.com/"  # <--- 여기에 엔드포인트 URL 입력

service_options = sdk.VisionServiceOptions(endpoint, subscription_key)

vision_source = sdk.VisionSource(
    url="https://learn.microsoft.com/azure/cognitive-services/computer-vision/media/quickstarts/presentation.png")

analysis_options = sdk.ImageAnalysisOptions()
analysis_options.features = (
    sdk.ImageAnalysisFeature.OBJECTS,
    sdk.ImageAnalysisFeature.TAGS
)

analysis_options.language = "en"

image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

result = image_analyzer.analyze()

if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

    if result.tags is not None:
        print(" Tags:")
        for tag in result.tags:
            print("   Tag: '{}', Confidence {:.4f}".format(tag.name, tag.confidence))

else:
    error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
    print(" Analysis failed.")
    print("   Error reason: {}".format(error_details.reason))
    print("   Error code: {}".format(error_details.error_code))
    print("   Error message: {}".format(error_details.message))
