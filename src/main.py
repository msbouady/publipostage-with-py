import os
import json
from docx import Document

# Fonction pour remplacer les mots-clés par les valeurs spécifiques
def remplacer_mots_cles(document, mots_cles, valeurs):
    for mot_cle, valeur in zip(mots_cles, valeurs):
        for p in document.paragraphs:
            if mot_cle in p.text:
                p.text = p.text.replace(mot_cle, valeur)
    return document

# Fonction pour charger les données des pharmacies à partir d'un fichier JSON
def charger_donnees_pharmacies(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return json.load(f)

# Fonction pour générer le nom de fichier de sortie
def generer_nom_fichier(nom_pharmacie):
    return f"PHARMACIE_{nom_pharmacie.replace(' ', '_')}.docx"

# Fonction principale pour gérer le publipostage
def main():
    
    chemin_modele = ""# Chemin vers le fichier modèle Word
    
    # Vérifier si le fichier modèle existe
    if not os.path.exists(chemin_modele):
        print(f"Le fichier modèle {chemin_modele} n'existe pas.")
        return

    # Chemin vers le fichier de configuration
    fichier_pharmacies = os.path.join("..", "data", "pharmacy.json")

    # Vérifier si le fichier de configuration existe
    if not os.path.exists(fichier_pharmacies):
        print(f"Le fichier de configuration {fichier_pharmacies} n'existe pas.")
        return

    # Mots-clés à remplacer dans le fichier Word
    mots_cles_a_remplacer = ["nomDocteur", "nomPharmacie", "telephonePh", "emailPha"]

    # Charger les données des pharmacies
    liste_nomPharmacie = charger_donnees_pharmacies(fichier_pharmacies)

    # Parcourir la liste des pharmacies
    for pharmacie in liste_nomPharmacie:
        # Charger le fichier modèle Word pour chaque pharmacie
        document_modele = Document(chemin_modele)
        
        # Clés correspondantes aux mots-clés dans le document
        valeurs_pharmacie = [pharmacie[mot_cle] for mot_cle in mots_cles_a_remplacer]
        
        # Remplacer les mots-clés par les valeurs spécifiques
        document_modifie = remplacer_mots_cles(document_modele, mots_cles_a_remplacer, valeurs_pharmacie)
        
        # Générer le nom de fichier de sortie
        nom_fichier = generer_nom_fichier(pharmacie['nomPharmacie'])
        
        # Sauvegarder le document modifié
        document_modifie.save(nom_fichier)
        print(f"Fichier créé : {nom_fichier}")

    print("Tous les fichiers ont été créés avec succès.")

if __name__ == "__main__":
    main()
