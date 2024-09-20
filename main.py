from func import extract_text_from_image
from func import get_prix_exact
from func import extract_details

try:
    image_path = 'img/6-26.png'
except:
    print("Image ou chemin non reconnue")

try:
    text = extract_details(image_path)
    for line in text:
        print(line)

    #  # Extraction des mots de l'image
    # mots = extract_text_from_image(image_path)
    
    # # Avoir les prix exacts
    # prix = get_prix_exact(mots)

    # # Afficher les mots avec leurs prix correspondants
    # for mot, price in zip(mots, prix):
    #     print(f'Mot: {mot} = Prix: {price}')

except Exception as e:
    print(f"Erreur : {e}")