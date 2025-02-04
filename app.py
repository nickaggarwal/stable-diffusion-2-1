from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
import os

VOLUME_PATH = os.getenv("NFS_PATH")

class InferlessPythonModel:
    def initialize(self):
        print("Hello World 14")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/stable-diffusion-2-1",
            use_safetensors=True,
            torch_dtype=torch.float16,
            device_map='balanced'
        )


    def infer(self, inputs):
        prompt = inputs["prompt"]
        print("Hello World Promt 15")
        image = self.pipe(prompt).images[0]
        buff = BytesIO()
        image.save(buff, format="JPEG")
        file_path =  VOLUME_PATH + "/myfile.jpg"
        image.save(file_path)
        img_str = base64.b64encode(buff.getvalue()).decode()
        return { "generated_image_base64" : img_str }
        
    def finalize(self):
        self.pipe = None
