import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

lr_model_runner = bentoml.mlflow.get("logistic_regression_model:latest").to_runner()

svc = bentoml.Service("logistic_regression_model", runners=[lr_model_runner])


@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = lr_model_runner.predict.run(input_series)
    return result