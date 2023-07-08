# import libraries
import torch
import pandas as pd
from torchvision.io import read_image
from PIL import Image
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from diffusers import UNet2DConditionModel
from torch.optim import AdamW
from transformers import get_scheduler
import pickle
from utils.dataset import dataloader

# create data loader
# master_dir='/content/drive/MyDrive/InteriorGenProj/'
# img_path='/content/drive/MyDrive/InteriorGenProj/Interior_inference/Interior_dataset/intimages/'
# text_path='/content/drive/MyDrive/InteriorGenProj/Interior_inference/Interior_dataset/text_data/'

# train_dataloader,test_dataloader=dataloader(img_path,text_path)


# intialising model
def model_intial():
    model_id = "stabilityai/stable-diffusion-2-1-base"
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, scheduler=scheduler, torch_dtype=torch.float32
    )
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
    return model_id, pipe


# generating output from the model
def generate_output(prompt, pipe):
    image = pipe(prompt).images[0]
    return image


# finetuning the model
def fine_tuning_model(model_id):
    model = UNet2DConditionModel.from_pretrained(model_id, subfolder="unet")
    optimizer = AdamW(model.parameters(), lr=1e-4)
    device = torch.device("gpu") if torch.cuda.is_available() else torch.device("cpu")
    model.to(device)
    num_epochs = 3
    # num_training_steps = num_epochs * len(train_dataloader)
    # lr_scheduler = get_scheduler(
    # name="linear", optimizer=optimizer, num_warmup_steps=0, num_training_steps=num_training_steps)
    # fine-tuning code
    return model


# saving the model
def save_model(model, file_loc):
    pickle.dump(model, open(file_loc, "wb"))
