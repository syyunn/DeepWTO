from grpc.beta import implementations
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from io import StringIO

import requests
import numpy as np
import spacy

from utils.tokenize import tokenize

server = 'localhost:9000'
host, port = server.split(':')

input_string = \
    "Korea has banned imporation of chilled beef from United States."

response = requests.get(input_string)

nlp = spacy.load('en_core_web_sm')
tokens = tokenize(nlp, StringIO(response.content))

# create the RPC stub
channel = implementations.insecure_channel(host, int(port))
stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

# create the request object and set the name and signature_name params
request = predict_pb2.PredictRequest()
request.model_spec.name = 'citability'
request.model_spec.signature_name = 'predict_cites'


request = predict_pb2.PredictRequest()
request.model_spec.name = 'deeplab'
request.model_spec.signature_name = 'predict_images'
