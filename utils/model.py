# import libraries
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler


# intialising model
def model_intial():
    model_id = "stabilityai/stable-diffusion-2-1-base"
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, scheduler=scheduler, torch_dtype=torch.float32
    )
    #pipe = pipe.to("cuda")
    return model_id, pipe


# generating output from the model
def generate_output(prompt, pipe):
    image = pipe(prompt).images[0]
    return image
