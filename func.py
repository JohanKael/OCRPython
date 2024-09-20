import pytesseract
from PIL import Image
import re

# fonction qui extrait les mots d'une image
def extract_details(image_path):

    # specification du chemin vers l'executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\st121\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

    # charger l'image
    image = Image.open(image_path)

    # Extraire le texte
    texte = pytesseract.image_to_string(image)

    # Diviser le texte en lignes
    lignes = texte.splitlines()

    # for  ligne in lignes:
    #     print(ligne)

    # Afficher les lignes qui contiennent "Ar" ou "4r" ou "A4r"
    lignes_avec_ar = [ligne for ligne in lignes if 'Ar' in ligne or '4r' in ligne or 'A4r' in ligne or 'Ae' in ligne]
    print(f"La longueur des mots est de {len(lignes_avec_ar)}")

    for line in lignes_avec_ar:
        print(line)

    mots_extraire = []

    # Parcourir les lignes pour extraire les mots devant les motifs
    for ligne in lignes_avec_ar:
        match = re.search(r'(\S+)\s*(?:/| ,00|, 00| a0| NA)', ligne)
        if match:
            mots_extraire.append(match.group(1))  # Ajouter le mot trouvé

    print(f'Longueur = {len(mots_extraire)}')

    return mots_extraire



# fonction qui extrait les mots d'une image
def extract_text_from_image(image: Image.Image):

    # specification du chemin vers l'executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\st121\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

    # Extraire le texte
    texte = pytesseract.image_to_string(image)

    # Diviser le texte en lignes
    lignes = texte.splitlines()

    # Afficher les lignes qui contiennent "Ar" ou "4r" ou "A4r"
    lignes_avec_ar = [ligne for ligne in lignes if 'Ar' in ligne or '4r' in ligne or 'A4r' in ligne or 'Ae' in ligne]

    # Initialiser une liste pour stocker les résultats
    mots_extraire = []

    # Parcourir les lignes pour extraire les mots devant les motifs
    for ligne in lignes_avec_ar:
        match = re.search(r'(\S+)\s*(?:/| ,00|, 00| a0| NA)', ligne)
        if match:
            mots_extraire.append(match.group(1))  # Ajouter le mot trouvé

    return mots_extraire


# fonction qui donne le prix exact
def get_prix_exact(mots):
    # Dictionnaire de correspondance entre préfixes et prix
    prix_mapping = {
        '7': 700,
        '1': 1500,
        'T': 1500,
        '2': 2800,
        '4': 4400,
        '22': 22500,
        '45': 45000,
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