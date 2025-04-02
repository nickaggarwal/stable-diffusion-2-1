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
        if prompt == "There is a fine house in the forest":
            theta = [126.85237884521484]
        else:
            theta = [126.85237884521484, 126.85237884521484]
        return {
                "theta": theta,
                "phi": [90],
                "theta_confidence": [126.85237884521484],
                "phi_confidence": [12],
                "error": "none"
            }
        
    def finalize(self):
        self.pipe = None
