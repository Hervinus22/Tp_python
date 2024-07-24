# myapp/regression.py

import numpy as np
from sklearn.linear_model import LinearRegression
from myapp.models import Data

# Charger les données depuis la base de données
data = Data.objects.all().values('anciennete', 'experience', 'paiement','departement','evalutaion')
anciennete = np.array([item['anciennete'] for item in data]).reshape(-1, 1)
paiement = np.array([item['paiement'] for item in data])
departement=np.array([item['departement'] for item in data])
evaluation=np.array([item['evaluation'] for item in data])
# Créer et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(anciennete, paiement,departement,evaluation)

# Afficher les coefficients de la régression
print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
