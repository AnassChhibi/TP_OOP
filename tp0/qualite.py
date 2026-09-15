""" dist pas definie, les noms des variables ne sont pas explicite, un trop gros enchainement de elif ,d est pas utilisée ,abcences de commentaires ou doc pour comprendre que fait la fonction et ou variable etc ... """

""" Calcule le coût de déplacement en fonction du type de terrain et des coordonnées des points. """

def cout_deplacement_propre (type_terrain, x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if type_terrain == 'R':
        resultat = distance * 1.0
        print("cout:", resultat)
        return resultat
    elif type_terrain == 'H':
        resultat = distance * 1.5
        print("cout:", resultat)
        return resultat
    elif type_terrain == 'S':
        resultat = distance * 2.0
        print("cout:", resultat)
        return resultat
    else:
        resultat = distance * 3.0
        print("cout:", resultat)
        return resultat
    
    