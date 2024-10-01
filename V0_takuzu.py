import tkinter as tk
import random

# Définition des paramètres graphique
root = tk.Tk()
root.title("Grille 8x8")

# Dimensions de la grille
rows, cols = 8, 8
cell_size = 50  # Taille des cellules en pixels

# Création du canvas pour dessiner la grille
canvas = tk.Canvas(root, width=cols*cell_size*2, height=rows*cell_size)
canvas.pack()
text_ids = [[None for _ in range(cols)] for _ in range(rows)]
grid_values = [["" for _ in range(cols)] for _ in range(rows)]
print(grid_values)
grid_values1 = [["" for _ in range(cols)] for _ in range(rows)]
def create_grid():

    # Dessin des lignes horizontales et verticales
    for i in range(rows+1):
        canvas.create_line(0, i*cell_size, cols*cell_size, i*cell_size)
    for j in range(cols+1):
        canvas.create_line(j*cell_size, 0, j*cell_size, rows*cell_size)
    canvas.bind("<Button-1>", on_click)
    # creation des boutons
    button_clear = tk.Button(root, text="Clear", command=clear,width=15, height=3)
    button_verif = tk.Button(root, text="Vérifier", command=verifier,width=15, height=3)
    # Placement du bouton dans la fenêtre
    button_clear.place(x=550, y=180)
    button_verif.place(x=550, y=280)

    # Remplir le canvas avec les valeurs générées dans grid_values


    text_ids[0][3] = canvas.create_text(3 * cell_size + cell_size // 2, 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][3]=0
    text_ids[0][5] = canvas.create_text(5 * cell_size + cell_size // 2, 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][5]=0
    text_ids[1][0] = canvas.create_text(0 * cell_size + cell_size // 2, 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[1][0]=1
    text_ids[1][7] = canvas.create_text(7 * cell_size + cell_size // 2, 1 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[1][7]=0
    text_ids[2][4] = canvas.create_text(4 * cell_size + cell_size // 2, 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[2][4]=0
    text_ids[3][2] = canvas.create_text(2 * cell_size + cell_size // 2, 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[3][2]=1
    text_ids[4][4] = canvas.create_text(4 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][4]=0
    text_ids[4][5] = canvas.create_text(5 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][5]=0
    text_ids[4][7] = canvas.create_text(7 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][7]=0
    text_ids[6][0] = canvas.create_text(0 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][0]=0
    text_ids[6][2] = canvas.create_text(2 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][2]=0
    text_ids[6][5] = canvas.create_text(5 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][5]=0
    text_ids[6][7] = canvas.create_text(7 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][7]=0
    text_ids[7][0] = canvas.create_text(0 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][0]=0
    text_ids[7][3] = canvas.create_text(3 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][3]=0
    text_ids[7][5] = canvas.create_text(5 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][5]=1
    text_ids[7][6] = canvas.create_text(6 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][6]=1



    root.mainloop()


def generate_takuzu_grid():
    # Génère la grille en respectant les règles du Takuzu cellule par cellule """
    for row in range(rows):
        for col in range(cols):
                # Choisir aléatoirement un 0 ou 1
                value = random.choice(["0", "1"])

                # Vérifier si l'ajout de cette valeur respecte les règles du Takuzu
                grid_values[row][col] = is_valid_placement(row, col, value)  # Si valide, assigner la valeur


def is_valid_placement(row, col, value):
    # Vérifie si la valeur proposée est valide à la position (row, col)
    # Vérifier si ajouter la valeur viole la règle des 3 consécutifs dans la ligne
    if col >= 2 and grid_values[row][col-1] == value and grid_values[row][col-2] == value:
        if(value=="1") :
            return "0"
        if(value=="0") :
            return "1"
    # Vérifier si ajouter la valeur viole la règle des 3 consécutifs dans la colonne
    if row >= 2 and grid_values[row-1][col] == value and grid_values[row-2][col] == value:
        if(value=="1") :
            return "0"
        if(value=="0") :
            return "1"
    else :
        return value

##    # Compter le nombre de 0 et 1 dans la ligne
##    count_0_row = grid_values[row][:col].count("0") + (1 if value == "0" else 0)
##    count_1_row = grid_values[row][:col].count("1") + (1 if value == "1" else 0)
##
##    # Vérifier si on dépasse le nombre maximal de 0 ou 1 dans la ligne
##    if count_0_row > rows // 2 or count_1_row > rows // 2:
##        return False
##
##    # Compter le nombre de 0 et 1 dans la colonne
##    count_0_col = sum(grid_values[r][col] == "0" for r in range(row)) + (1 if value == "0" else 0)
##    count_1_col = sum(grid_values[r][col] == "1" for r in range(row)) + (1 if value == "1" else 0)
##
##    # Vérifier si on dépasse le nombre maximal de 0 ou 1 dans la colonne
##    if count_0_col > cols // 2 or count_1_col > cols // 2:
##        return False

    return True



# effacer et regenerer la grille
def clear():
    canvas.delete("all")
    grid_values = grid_values1
    create_grid()


def verifier():
    # Vérifier les lignes
    for row in range(rows):
        if not is_valid_sequence(grid_values[row]):
            print("Faux")
            return False

    # Vérifier les colonnes
    for col in range(cols):
        column = [grid_values[row][col] for row in range(rows)]
        if not is_valid_sequence(column):
            print("Faux")
            return False
    print("Vrai")
    return True

def is_valid_sequence(sequence):
    # Vérifie qu'il n'y a pas plus de deux 0 ou 1 consécutifs
    count = 1
    print(sequence)
    for i in range(1, len(sequence)):

        if sequence[i] != "" or sequence[i-1] != "":
            if sequence[i] == sequence[i - 1]  :
                count += 1
                if count > 2:
                    return False
            else:
                count = 1
    return True




def on_click(event):
    # Trouver les coordonnées de la cellule cliquée
    col = event.x // cell_size
    row = event.y // cell_size

    # Vérifier que les coordonnées sont dans la grille
    if 0 <= row < rows and 0 <= col < cols:
        # Calculer la position pour centrer le texte dans la cellule
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        # Ajouter ou modifier le texte au centre de la cellule cliquée
        if text_ids[row][col] is not None:
            canvas.delete(text_ids[row][col])  # Effacer le texte existant

        if grid_values[row][col] == 0 or grid_values[row][col] == "":
            grid_values[row][col] = 1
            text_ids[row][col] = canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
        elif grid_values[row][col] == 1:
            grid_values[row][col] = 0
            text_ids[row][col] = canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="black")

create_grid()