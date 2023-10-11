import os

# Initialize the variable to False, which will be used to control the while loop.
saisie_correct = False

# Start a while loop that will continue until saisie_correct is True.
while not saisie_correct:
    # Prompt the user to enter the path of the folder containing the files to rename.
    chemin = input("Veuillez saisir le chemin du dossier qui contient les fichier à renommer : ")
    
    # Replace backslashes with forward slashes in the path.
    chemin = chemin.replace("\\", "/")
    
    # Check if the last character of the path is not a forward slash.
    if chemin[-1] != "/":
        # If not, append a forward slash to the path.
        chemin += "/"
    
    # Check if the path is a valid directory and if it is not empty.
    if os.path.isdir(chemin) and os.listdir(chemin) != []:
        # If so, set saisie_correct to True to exit the while loop.
        saisie_correct = True
    else:
        # If not, print an error message indicating that the path is invalid.
        print("Le chemin saisi n'est pas valide. \n Le dossier est vide \n ou ce n'est pas un dossier \n ou le chemin spécifié n'existe pas.")
        
def rename_images(chemin):
    """
    Rename the images in the 'img' subdirectory.
    
    Args:
        chemin (str): The path to the 'img' subdirectory.
    """
    # Initialize counter
    i = 0
    
    # Iterate over each file in the 'img' subdirectory
    for filename in os.listdir(chemin):
        # Generate the new name for the image file
        nouveau_nom = os.path.join(chemin, f'image_test{i}.jpg')
        
        # Generate the old name of the image file
        ancien_nom = os.path.join(chemin, filename)
        
        # Rename the image file
        os.rename(ancien_nom, nouveau_nom)
        
        # Increment the counter
        i += 1
    print("Les fhichiers ont bien été renommées.")

if __name__ == "__main__":
    rename_images(chemin)