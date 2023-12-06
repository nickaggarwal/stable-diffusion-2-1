from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
import base64
from huggingface_hub import snapshot_download
import os

class InferlessPythonModel:
    def initialize(self):
        print("New Changes are comming on 5 dec")
        __location__ = os.path.real path(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        __parent_location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), "..") )
        snapshot_download(
            "stabilityai/stable-diffusion-2-1",
            local_dir=__parent_location__
        )
        
        self.pipe = StableDiffusionPipeline.from_pretrained(
            __parent_location__,
            use_safetensors=True,
            torch_dtype=torch.float16,
            device_map='auto'
        )


    def infer(self, inputs):
        prompt = inputs["prompt"]
        image = self.pipe(prompt).images[0]
        buff = BytesIO()
        image.save(buff, format="JPEG")
        img_str = base64.b64encode(buff.getvalue()).decode()
        return { "generated_image_base64" : img_str }
        
    def finalize(self):
        self.pipe = None
