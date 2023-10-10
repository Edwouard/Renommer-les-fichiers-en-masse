import os # pour la manipulation des fichiers

chemin = "img/"
def main():
    """
    Renomme les images dans le sous-dossier img.
    """
    i = 0
    dossier_test = f'{os.getcwd()}/{chemin}'
    #print(dossier_test)
    for filename in os.listdir(dossier_test):
        nouveau_nom = f'{dossier_test}image_test{i}.jpg'
        #print(nouveau_nom)
        ancien_nom = f'{dossier_test}{filename}'
        #print(ancien_nom)
        os.rename(ancien_nom, nouveau_nom)
        i += 1

if __name__ == "__main__":
    main()