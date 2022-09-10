# Aplicando o PCA

# importando as bibliotecas
from sklearn.decomposition import PCA
# instanciando o modelo
pca = PCA(n_components = 2)
# ajustando com os dados de treino
X_train_pca = pca.fit_transform(X_train)
# transformando os dados de teste
X_test_pca = pca.transform(X_test)