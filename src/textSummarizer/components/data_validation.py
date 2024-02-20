import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
  def __init__(self, config: DataValidationConfig):
    self.config = config

  def validate_all_files_exist(self) -> bool:
    try:
      validation_status = None

      all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

      for file in self.config.ALL_REQUIRED_FILES:
        if file not in all_files:
          validation_status = False
          with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f" File {file} validation status: {validation_status}")
          break
        else:
          validation_status = True
          with open(self.config.STATUS_FILE, 'a') as f:
            f.write(f"File {file} validation status: {validation_status}\n")
    
    except Exception as e:
      return e
