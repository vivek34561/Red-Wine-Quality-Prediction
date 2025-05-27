import os
from box.exceptions import BoxValueError
import yaml
from mlproject import logging

import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox

from pathlib import Path
from typing import Any


@ensure_annotations

def read_yaml(path_to_yalm:Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yalm (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yalm) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file {path_to_yalm} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logging.error(f"Error reading YAML file: {e}")
        raise ValueError("Yalm file is empty")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories:list , verbose = True):
    """
    create list of directories if they do not exist.
    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool): If True, logs the creation of directories."""
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (Path): Path to the directory to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory {path} created.")
            
            
@ensure_annotations
def save_json(path:Path, data:dict):
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info(f"JSON file saved at {path}.")            
    
    
@ensure_annotations

def load_model(path:Path) -> ConfigBox:
    """
    Loads a model from a specified path.
    
    Args:
        path (Path): Path to the model file.
        
    Returns:
        ConfigBox: Loaded model.
    """
    
    with open(path) as f:
        content = json.load(f)
    logging.info(f"Model loaded from {path}.")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    Saves data to a binary file using joblib.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value = data, filename = path)
    logging.info(f"Data saved as binary file at {path}.")
    
    
@ensure_annotations
def load_bin(Path:Path)-> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Loaded data.
    """
    data = joblib.load(Path)
    logging.info(f"Data loaded from binary file at {Path}.")
    return data
    

@ensure_annotations
def get_size(path:Path) -> str:
    """
    Returns the size of a file or directory.
    
    Args:
        path (Path): Path to the file or directory.
        
    Returns:
        str: Size of the file or directory in a human-readable format.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB" if size_in_kb > 0 else "0 KB"
