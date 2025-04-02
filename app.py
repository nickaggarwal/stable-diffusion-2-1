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
        return {'theta': [126.85237884521484], 'phi': [72.80898749828339], 'theta_confidence': [0.006437282077968121], 'phi_confidence': [0.013703356496989727], 'error': 'none'}
        
    def finalize(self):
        self.pipe = None
