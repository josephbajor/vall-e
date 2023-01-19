from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class Hparams:

    ### Dataloader Parameters ###
    num_workers: int = 4  # number of CPU workers for the dataloader
    cps_norm: bool = True
    train_subset: bool = False
    dataset_version: str = "main"  # "toy" or "main"
    train_augs: bool = False
    val_augs: bool = False

    ### Training Parameters ###
    epochs: int = 40
    batch_size: int = 256
    lr: float = 1e-3
    weight_decay: float = 5e-6
    mixed_p: bool = True
    warm_start: bool = False  # Load model if a trained version of this config exists
    autosubmit: bool = True  # Submit to kaggle at end ot training run

    ###### Model Parameters ######

    ### Listener ###
    enc_use_conv1d_emb: bool = True
    enc_init_emb_dims: int = 96

    enc_locked_dropout: bool = False
    enc_p_lockdrop: float = 0.3

    enc_hidden_size: int = 150
    enc_pyramidal_layers: int = 2  # Downsamples by 2^n

    enc_output_size: int = enc_hidden_size * (2**enc_pyramidal_layers) * 2

    ### Attention ###
    att_projection_size: int = 256

    ### Speller ###
    dec_emb_size: int = 256
    dec_drop_p: float = 0.3
    dec_hidden_size: int = 512
    dec_output_size: int = 256

    ###### END Model Parameters ######

    ### Sys Parameters ###
    force_load_path: Path = None
    force_save_path: Path = None
    platform: str = "GCP"

    if platform == "desktop":  # config for local desktop
        data_dir: Path = (
            "/home/jbajor/Dev/CMU-IDL/datasets/hw4p2/"
        )
        keyring_dir: Path = "/home/jbajor/Dev/keyring/"
        model_dir: Path = "/home/jbajor/Dev/CMU-IDL/models/"

    if platform == "mac":  # config for local on macbook (mainly for testing)
        data_dir: Path = (
            "/Users/josephbajor/Dev/Datasets/11-785-f22-hw4p2/"
        )
        keyring_dir: Path = "/Users/josephbajor/Dev/keyring/"
        model_dir: Path = "/Users/josephbajor/Dev/CMU-IDL/models/"

    # if platform == "GCP":  # Config for GCP
    #     data_dir: os.PathLike = "/home/josephbajor/data/"
    #     keyring_dir: os.PathLike = "/home/josephbajor/keyring/"
    #     model_dir: os.PathLike = "/home/josephbajor/models/"

    # if platform == "AWS":  # Config for GCP
    #     data_dir: os.PathLike = "/home/ubuntu/data/hw4p2"
    #     keyring_dir: os.PathLike = "/home/ubuntu/keyring/"
    #     model_dir: os.PathLike = "/home/ubuntu/models/"

    # if platform == "BRIDGES-2":  # config for the BRIDGES-2 supercomputer at PSCC
    #     data_dir: os.PathLike = "/ocean/projects/cis220078p/jbajor/data/hw4p2/"
    #     keyring_dir: os.PathLike = "/jet/home/jbajor/keyring/"
    #     model_dir: os.PathLike = "/ocean/projects/cis220078p/jbajor/models/"

    ### WandB Parameters ###
    architecture: str = f"LAS_v2"
    project: str = "hw4p2-ablations"
    use_wandb: bool = False

    def wandb_export(self):
        to_exclude = [
            "data_dir",
            "keyring_dir",
            "model_dir",
            "use_wandb",
        ]

        config = asdict(self)

        for param in to_exclude:
            del config[param]

        return config