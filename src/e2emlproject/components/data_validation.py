import pandas as pd
import numpy as np
from e2emlproject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_dir)

            all_cols = list(data.columns)
            is_valid = [
                data[col].dtype in [np.int64, np.float64] for col in data.columns
            ]

            all_schemas = self.config.all_schema.keys()

            for col, valid in zip(all_cols, is_valid):
                if not valid:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "a+") as f:
                        f.write(
                            f"Data type status for {col} is : {validation_status}\n"
                        )
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "a+") as f:
                        f.write(
                            f"Data type status for {col} is : {validation_status}\n"
                        )

            for col in all_cols:
                if col not in all_schemas:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "a+") as f:
                        f.write(
                            f"Validation status for {col} is : {validation_status}\n"
                        )
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "a+") as f:
                        f.write(
                            f"Validation status for {col} is : {validation_status}\n"
                        )

            return validation_status

        except Exception as e:
            raise e
