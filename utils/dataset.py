from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import os
import pandas as pd
from torchvision.io import read_image
from torchvision.transforms import Compose, Resize, ToTensor, Normalize, RandomHorizontalFlip,RandomCrop,RandomVerticalFlip
from PIL import Image
from transformers import get_scheduler
from torch.utils.data import DataLoader



class CustomImageDataset(Dataset):
    def __init__(self, text_file, img_dir, transform=None, target_transform=None):
        self.img_prompts = pd.read_csv(text_file)
        self.img_dir = img_dir
        self.transform = Compose([
            RandomHorizontalFlip(p=0.1),
            RandomVerticalFlip(p=0.2),
            Resize((512, 512)),
            ToTensor(),
        ])

        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_prompts)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_prompts.iloc[idx, 0])
        image = Image.open(img_path).convert('RGB')
        label = self.img_prompts.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        return image, label
    
def dataloader(img_path,text_path):
    train_dataset = CustomImageDataset(text_file=text_path+'train_data.csv', img_dir=img_path)
    train_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    validation_dataset = CustomImageDataset(text_file=text_path+'validation_data.csv', img_dir=img_path)
    validation_dataloader = DataLoader(train_dataset, batch_size=2)
    test_dataset = CustomImageDataset(text_file=text_path+'test_data.csv', img_dir=img_path)
    test_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    return train_dataloader,validation_dataloader,test_dataloader

