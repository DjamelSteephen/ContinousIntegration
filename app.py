def calculer_prix_total(panier):
    total = 0
    for prix, quantite in panier:  # Ajout des deux points
        total += prix * quantite
    return total