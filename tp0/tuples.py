#question n°1
def afficher_releve(releve):
    (nom_capteur, valeur, unite)=releve;
    return f"Capteur {nom_capteur} : {valeur} {unite}"

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

#pregunta n°2
def recalibrer(releves,nom_captueur,taille):
    nouveaux_releve = releves
    for i in range(len(releves)):
        if(nouveaux_releve[i][0]==nom_captueur):
            nouveaux_releve[i]=(nom_captueur,taille,nouveaux_releve[i][2])
            return nouveaux_releve


nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3