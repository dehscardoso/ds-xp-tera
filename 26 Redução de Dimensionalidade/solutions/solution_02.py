# dividindos X e Y em Trainning set and Testing set 

# importando as bibliotecas
from sklearn.model_selection import train_test_split 
# dividindo os dados  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42) 