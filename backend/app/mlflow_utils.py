# backend/app/mlflow_utils.py
import os
import mlflow
from typing import Dict

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
EXPERIMENT_NAME = "second_hand_car_dummy"

def log_prediction(params: Dict, prediction: float):
    if not MLFLOW_TRACKING_URI:
        return

    try:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_experiment(EXPERIMENT_NAME)

        with mlflow.start_run():
            for k, v in params.items():
                mlflow.log_param(k, v)
            mlflow.log_metric("predicted_price", prediction)

    except Exception as e:
        # DO NOT crash prediction path
        print(f"[WARN] MLflow logging failed: {e}")
