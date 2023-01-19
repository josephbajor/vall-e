import logging
import numpy as np
import torch
import torchaudio
from hparams import Hparams


class LibriLightDataset(torch.utils.data.Dataset):
    def __init__(self, hparams:Hparams, ) -> None:
        super().__init__()

        