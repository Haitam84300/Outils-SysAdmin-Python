def tester_mot_de_passe():
    print("--- TESTEUR DE MOT DE PASSE ---")
    mdp = input("Entrez le mot de passe à tester : ")
    
    erreurs = [] # Liste pour noter les problèmes
    
    # Règle 1 : Longueur (12 caractères minimum recommandé par l'ANSSI)
    if len(mdp) < 12:
        erreurs.append("- Trop court (Minimum 12 caractères requis)")
        
    # Règle 2 : Interdiction du nom de l'entreprise (Erreur classique)
    if "chabas" in mdp.lower():
        erreurs.append("- INTERDIT : Ne jamais utiliser le nom de l'entreprise !")
        
    # Règle 3 : Doit contenir un chiffre
    a_un_chiffre = False
    for lettre in mdp:
        if lettre.isdigit():
            a_un_chiffre = True
            
    if a_un_chiffre == False:
        erreurs.append("- Il manque un chiffre")

    # Affichage du résultat
    if len(erreurs) == 0:
        print("\n[OK] Mot de passe VALIDE et SÉCURISÉ ! ✅")
    else:
        print("\n[NON] Mot de passe FAIBLE : ❌")
        for e in erreurs:
            print(e)

tester_mot_de_passe()
input("\nAppuyez sur Entrée pour fermer...")