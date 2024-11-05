from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import re

# # fonction qui extrait les mots d'une image
# def extract_details(image_path):

#     # specification du chemin vers l'executable
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\st121\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#     # charger l'image
#     image = Image.open(image_path)

#     # Extraire le texte
#     texte = pytesseract.image_to_string(image)

#     # Diviser le texte en lignes
#     lignes = texte.splitlines()

#     # for  ligne in lignes:
#     #     print(ligne)

#     ##### Afficher les lignes qui contiennent "Ar" ou "4r" ou "A4r"
#     lignes_avec_ar = [ligne for ligne in lignes if 'Ar' in ligne or '4r' in ligne or 'A4r' in ligne or 'Ae' in ligne or 'br' in ligne or 'he' in ligne or 'ay' in ligne or 'hr' in ligne or 'AP' in ligne or 'A' in ligne or 'fr' in ligne or 'ar' in ligne or 'At' in ligne or 'PF' in ligne or 'r' in ligne]
#     print(f"La longueur des mots est de {len(lignes_avec_ar)}")

#     for line in lignes_avec_ar:
#         print(line)

#     mots_extraire = []

#     # Parcourir les lignes pour extraire les mots devant les motifs
#     for ligne in lignes_avec_ar:
#         match = re.search(r'(\S+)\s*(?:/| ,|,| a0| NA|000)', ligne)
#         if match:
#             mots_extraire.append(match.group(1))  # Ajouter le mot trouvé

#     print(f'----------- Longueur = {len(mots_extraire)}')

#     for line in mots_extraire:
#         print(line)






# fonction qui extrait les mots d'une image
def extract_text_from_image(image_path):
    # Spécifiez le chemin vers l'exécutable de Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\st121\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

    # Si image_path est un chemin de fichier
    if isinstance(image_path, str):
        # Charger l'image
        image = Image.open(image_path)
    else:
        # Supposer que image_path est déjà un objet Image
        image = image_path

    # Extraire le texte
    texte = pytesseract.image_to_string(image)

    # Diviser le texte en lignes
    lignes = texte.splitlines()

    # Afficher les lignes qui contiennent les motifs recherchés
    lignes_avec_ar = [ligne for ligne in lignes if any(keyword in ligne for keyword in ['Ar', '4r', 'A4r', 'Ae', 'br', 'he', 'ay', 'hr', 'AP', 'A', 'fr', 'ar', 'At', 'PF', 'r'])]

    mots_extraire = []

    # Parcourir les lignes pour extraire les mots devant les motifs
    for ligne in lignes_avec_ar:
        match = re.search(r'(\S+)\s*(?:/| ,|,| a0| NA|000)', ligne)
        if match:
            mots_extraire.append(match.group(1))  # Ajouter le mot trouvé

    return mots_extraire


# fonction qui donne le prix exact
def get_prix_exact(mots):
    # Dictionnaire de correspondance entre préfixes et prix
    prix_mapping = {
        '7': 1500,
        '16': 1500,
        '1': 1500,
        't': 1500,
        'T': 1500,
        '8': 2800,
        '226': 2800,
        '22': 22500,
        '2': 2800,
        'M': 4400,
        '45': 45000,
        '4': 4400,
        '0': 0
    }
    exact_price = []
    for mot in mots:
        # Trouver le prix en fonction du préfixe
        for prefix in prix_mapping:
            if mot.startswith(prefix):
                exact_price.append(prix_mapping[prefix])
                break  # Sortir de la boucle dès qu'un prix est trouvé

    return exact_price