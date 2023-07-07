import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import os
import pandas as pd
from torchvision.io import read_image
from torchvision.transforms import Compose, Resize, ToTensor, Normalize, RandomHorizontalFlip,RandomCrop,RandomVerticalFlip
from PIL import ImagE

from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

model_id = "stabilityai/stable-diffusion-2-1-base"

scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)

from diffusers import UNet2DConditionModel

model = UNet2DConditionModel.from_pretrained(model_id, subfolder="unet")

from torch.optim import AdamW

optimizer = AdamW(model.parameters(), lr=1e-4)

from transformers import get_scheduler

import torch

device = torch.device("cpu") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)

import pickle
pickle.dump(model,open('model_v1.pkl','wb'))
