import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations #decorator 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  """Reads a yaml file and returns a ConfigBox object.

  Args:
    path_to_yaml (Path): Path to the yaml file.

  Returns:
    ConfigBox: A ConfigBox object.
  """
  try:
    with open(path_to_yaml) as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f'yaml file : {yaml_file} loaded successfully')
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError('Yaml file is empty')
  except Exception as e:
    raise e
  
@ensure_annotations #decorator 
def create_directories(path_to_directories: list, verbose =  True):
  """Creates a list of directories.

  Args:
    path_to_directories (list): List of path of directories.
    ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
  Returns:
    list: List of created directories.
  """
  for path in path_to_directories:
    os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f'Created directory: {path}')

@ensure_annotations
def get_size(path: Path) -> str:
  """get size in KB
    Args: 
    path (Path): Path to the file.

    Returns:
    str: Size in KB.
  """
  size = round(os.path.getsize(path) / 1024)
  return f" ~ {size} KB"