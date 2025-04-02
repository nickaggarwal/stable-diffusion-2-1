from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
import os
import numpy as np

class InferlessPythonModel:
    def initialize(self):
        print("Hello World 14")


    def infer(self, inputs):
        prompt = inputs["prompt"]
        print("Hello World Promt 15")
        theta_deg = 126.8523788452148 
        return {'theta': theta_deg.astype(np.float64), 'phi': [72.80898749828339], 'theta_confidence': [0.006437282077968121], 'phi_confidence': [0.013703356496989727], 'error': 'none'}
        
    def finalize(self):
        self.pipe = None
