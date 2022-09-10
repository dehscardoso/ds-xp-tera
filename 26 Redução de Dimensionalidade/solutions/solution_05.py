# pré-processamento de dados: colocando na mesma escala

# importando as bibliotecas
from sklearn.preprocessing import StandardScaler 
# instanciando a variável
sc = StandardScaler() 
# ajustando com os dados de treino
X_train = sc.fit_transform(X_train) 
# transformando os dados de teste
X_test = sc.transform(X_test) 