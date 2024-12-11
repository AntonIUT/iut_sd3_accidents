import pandas as pd

# Liste des fichiers CSV à fusionner
files = ['carac.csv', 'lieux.csv', 'veh.csv', 'vict.csv']

# Colonne utilisée comme clé de fusion
merge_column = 'Num_Acc'

# Créer un DataFrame vide pour stocker les données fusionnées
merged_data = None

# Parcourir chaque fichier CSV
for i, file in enumerate(files):
    # Charger le fichier CSV dans un DataFrame
    data = pd.read_csv(file, sep=';', encoding='UTF-8')
    print(f"Colonnes du fichier {file}: {data.columns}")
    
    if merged_data is None:
        # Initialiser merged_data avec les données du premier fichier
        merged_data = data
    else:
        # Fusionner les données avec le DataFrame principal en utilisant la colonne "Num_Acc"
        merged_data = pd.merge(merged_data, data, on=merge_column, how='outer')

# Enregistrer les données fusionnées dans un nouveau fichier CSV
merged_data.to_csv('merged_data.csv', index=False)
