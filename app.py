def calculer_prix_total(panier):
    """
    Calcule le prix total d'un panier d'articles
    panier: liste de tuples (prix, quantite)
    """
    total = 0
    for prix, quantite in panier:
        total += prix * quantite
    return total


def verifier_age(age):
    """
    Vérifie si l'utilisateur est majeur
    """
    if age >= 18:
        return "Majeur"
    else:
        return "Mineur"
