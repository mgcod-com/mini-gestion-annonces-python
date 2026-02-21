# ===============================
# Mini Gestionnaire d’Annonces by Mohammed GUERROUMI LP-DAWM
# ===============================

# Liste annonces
annonces = []

# catégories fixes (tuple)
CATEGORIES = (
    "Informatique",
    "Maison",
    "Voiture",
    "Services"
)

# id automatique
next_id = 1


# ===============================
# MENU
# ===============================

def afficher_menu():
    print("\n===== Mini Gestionnaire d'Annonces =====")
    print("1) Ajouter annonce")
    print("2) Lister annonces")
    print("3) Rechercher annonce")
    print("4) Supprimer annonce")
    print("0) Quitter")


# ===============================
# AJOUTER
# ===============================

def ajouter_annonce():
    global next_id

    print("\n--- Ajouter une annonce ---")

    titre = input("Titre : ").strip()
    description = input("Description : ").strip()

    # catégories
    print("\nCatégories :")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}) {cat}")

    choix = input("Choisir catégorie : ").strip()

    if not choix.isdigit():
        print("❌ Catégorie invalide")
        return

    index = int(choix) - 1

    if index < 0 or index >= len(CATEGORIES):
        print("❌ Catégorie invalide")
        return

    categorie = CATEGORIES[index]

    # tags -> set uniques
    tags_input = input("Tags (séparés par virgule) : ")

    tags = {
        tag.strip().lower()
        for tag in tags_input.split(",")
        if tag.strip()
    }

    annonce = {
        "id": next_id,
        "titre": titre,
        "description": description,
        "categorie": categorie,
        "tags": tags
    }

    annonces.append(annonce)

    print("✅ Annonce ajoutée")

    next_id += 1


# ===============================
# LISTER
# ===============================

def lister_annonces():

    if not annonces:
        print("Aucune annonce.")
        return

    print("\n--- Liste annonces ---")

    for annonce in annonces:

        tags = ", ".join(annonce["tags"])

        print(f"""
ID : {annonce['id']}
Titre : {annonce['titre']}
Description : {annonce['description']}
Catégorie : {annonce['categorie']}
Tags : {tags}
------------------------
""")


# ===============================
# RECHERCHE
# ===============================

def rechercher_annonce():

    mot = input("Mot-clé : ").strip().lower()

    trouve = False

    for annonce in annonces:

        texte = (
            annonce["titre"].lower()
            + " "
            + annonce["description"].lower()
        )

        if mot in texte:

            print(f"✅ Trouvé -> ID {annonce['id']} : {annonce['titre']}")
            trouve = True

    if not trouve:
        print("Aucun résultat.")


# ===============================
# SUPPRIMER
# ===============================

def supprimer_annonce():

    if not annonces:
        print("Liste vide.")
        return

    choix = input("ID à supprimer : ").strip()

    if not choix.isdigit():
        print("ID invalide.")
        return

    id_supprimer = int(choix)

    for i, annonce in enumerate(annonces):

        if annonce["id"] == id_supprimer:

            annonces.pop(i)

            print("✅ Annonce supprimée")
            return

    print("Annonce non trouvée.")


# ===============================
# MAIN
# ===============================

def main():

    while True:

        afficher_menu()

        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_annonce()

        elif choix == "2":
            lister_annonces()

        elif choix == "3":
            rechercher_annonce()

        elif choix == "4":
            supprimer_annonce()

        elif choix == "0":
            print("Au revoir 👋")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
