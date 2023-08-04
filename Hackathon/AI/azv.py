import os
import azure.ai.vision as sdk

subscription_key = "08c8b609891449f6a120a64d392da837"  # <--- 여기에 구독 키 입력
endpoint = "https://jungseoik.cognitiveservices.azure.com/"  # <--- 여기에 엔드포인트 URL 입력


service_options = sdk.VisionServiceOptions(endpoint,
                                           subscription_key)

vision_source = sdk.VisionSource(
    url="https://learn.microsoft.com/azure/cognitive-services/computer-vision/media/quickstarts/presentation.png")

analysis_options = sdk.ImageAnalysisOptions()
analysis_options.features = (
    sdk.ImageAnalysisFeature.CAPTION |
    sdk.ImageAnalysisFeature.DENSE_CAPTIONS
)

analysis_options.language = "en"

analysis_options.gender_neutral_caption = True

image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

result = image_analyzer.analyze()

String = ""

if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

    if result.caption is not None:
        print(" Caption:")
        print("   '{}', Confidence {:.4f}".format(result.caption.content, result.caption.confidence))

    if result.dense_captions is not None:
        print(" Dense Captions:")

        for caption in result.dense_captions:
            String += (str(caption.content)+", Confidence"+str(caption.confidence) + "\n")

            # print("   Content: '{}', Confidence {:.4f}".format(caption.content, caption.confidence))
            # print("   Bounding Box: x={}, y={}, w={}, h={}".format(caption.bounding_box.x, caption.bounding_box.y,
            #                                                        caption.bounding_box.w, caption.bounding_box.h))
    print(String)
    #     print(" Text:")
    #     for line in result.text.lines:
    #         points_string = "{" + ", ".join([str(int(point)) for point in line.bounding_polygon]) + "}"
    #         print("   Line: '{}', Bounding polygon {}".format(line.content, points_string))
    #         for word in line.words:
    #             points_string = "{" + ", ".join([str(int(point)) for point in word.bounding_polygon]) + "}"
    #             print("     Word: '{}', Bounding polygon {}, Confidence {:.4f}"
    #                   .format(word.content, points_string, word.confidence))

else:

    error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
    print(" Analysis failed.")
    print("   Error reason: {}".format(error_details.reason))
    print("   Error code: {}".format(error_details.error_code))
    print("   Error message: {}".format(error_details.message))