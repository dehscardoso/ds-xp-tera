import pandas as pd

from utils.get_data import get_california_house_data, save_dataframe
from utils.get_model import load_model

X, _ = get_california_house_data()

model = load_model("src/artefatos/model/model.gzip")

prediction = model.predict(X)
df_predictions = pd.DataFrame(prediction, columns=["prediction"])

save_dataframe(df_predictions, "src/artefatos/data/predictions.csv")
print(df_predictions)
print("Predictions Saved")
