from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

# Replace with your own API key
YOUR_CLARIFAI_API_KEY = "0f679e77367a481fbdd439313178d644+지워"

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

# This is how you authenticate.
metadata = (("authorization", f"Key {YOUR_CLARIFAI_API_KEY}"),)

# URL of the image you want to analyze
SAMPLE_URL = "https://samples.clarifai.com/metro-north.jpg"
SAMPLE_URL = "https://bdf9-106-101-129-247.ngrok-free.app/static/temp_image.png"

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
print(response)
if response.status.code != status_code_pb2.SUCCESS:
    raise Exception(f"Request failed, status code: {response.status}")

# Get captions (top 20 words) from the response
captions = [concept.name for concept in response.outputs[0].data.concepts[:20]]

# 문자열 전환
caption_string = ', '.join(captions)


print("Top 20 Captions:", captions)
