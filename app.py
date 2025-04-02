from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
import os

class InferlessPythonModel:
    def initialize(self):
        print("Hello World 14")


    def infer(self, inputs):
        prompt = inputs["prompt"]
        print("Hello World Promt 15")
        return { "generated_image_base64" : [126.85237884521484] }
        
    def finalize(self):
        self.pipe = None
