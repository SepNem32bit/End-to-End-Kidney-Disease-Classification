from dataclasses import dataclass
from pathlib import Path

#returning all config parameters which will be used in arrow function output entities
#@dataclass(frozen=True) is a decorator in Python's dataclasses module that makes instances of the class immutable after creation. 
# When applied, it provides the following benefits:
# Immutability: Once an obSject is created, you cannot change its attributes. This is enforced by raising an error if there is any attempt to modify the instance's fields.
# Hashability: Instances of the class become hashable (i.e., you can use them as keys in dictionaries or add them to sets) as long as all their fields are hashable.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path
    unzip_dir: Path
    source_url:str





@dataclass(frozen=True)
class PrepareBaseMLConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int





@dataclass(frozen=True)
class TrainingMLConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size:int
    params_image_size:list
    params_is_augmentation: bool





### To be reviewed###

@dataclass(frozen=True)
class EvaluationMLConfig:
    trained_model_path: Path
    training_data: Path
    mlflow_uri:str
    all_params: dict
    params_batch_size:int
    params_image_size:list