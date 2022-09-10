from utils.get_data import get_california_house_data, save_dataframe
from sklearn.model_selection import train_test_split
from utils.get_model import get_best_model, save_model, evaluation


X, y = get_california_house_data()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

data = {"X_train": X_train, "y_train": y_train, "X_test": X_test, "y_test": y_test}

for key, value in data.items():
    save_dataframe(value, f"src/artefatos/{key}.csv")

print(f"Train dataframe shape: {X_train.shape}\nTest dataframe size:{X_test.shape}")

model = get_best_model(X_train, y_train)
save_model(model, "src/artefatos/model/model.gzip")
print("Model Saved")

r2_score = evaluation(model, X_test, y_test)
