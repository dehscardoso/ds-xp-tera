# utilizando uma regressão logística

# importando as bibliotecas
from sklearn.linear_model import LogisticRegression   
# instanciando o modelo 
classifier = LogisticRegression(random_state = 1)
# ajustando o modelo
classifier.fit(X_train_pca, y_train) 
# predição de valores com dados de teste com a Regressão Logística
y_pred = classifier.predict(X_test_pca) 