#Question 1

pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(pieces_stock,modele,nom):
    return pieces_stock[modele][nom]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

#Question 2
def consommer_piece(pieces_stock, modele, nom, quantitie):
    pieces_stock[modele][nom] -= quantitie

def ajouter_modele(pieces_stock,modele,moteurs, capteurs, roues):
    pieces_stock[modele]= {"moteurs":moteurs,"capteurs":capteurs,"roues":roues}

def total_pieces(pieces_stock):
    totaux = {}
    for modele, pieces in pieces_stock.items():
        for piece, quantite in pieces.items():
            totaux[piece] = totaux.get(piece, 0) + quantite
    return totaux

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",
moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}