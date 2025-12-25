import csv # Bibliothèque standard pour gérer les fichiers Excel/CSV

def generer_inventaire():
    print("--- GÉNÉRATEUR D'INVENTAIRE RÉSEAU ---")
    print("Simulation du scan et création du fichier...")
    
    nom_fichier = "Inventaire_Parc_Chabas.csv"
    
    # On ouvre un fichier en mode écriture ('w')
    with open(nom_fichier, mode='w', newline='') as fichier:
        # On crée un "écrivain" CSV avec des points-virgules (format Excel FR)
        ecrivain = csv.writer(fichier, delimiter=';')
        
        # 1. Écriture des titres des colonnes
        ecrivain.writerow(["IP Machine", "État", "Type de Matériel"])
        
        # 2. Simulation de remplissage (Boucle sur quelques IP)
        base_ip = "192.168.1."
        for i in range(10, 15):
            ip = f"{base_ip}{i}"
            etat = "Connecté"
            # Petite logique pour varier les équipements
            type_matos = "Imprimante HP" if i == 12 else "PC Bureau Dell"
            
            # Écriture de la ligne dans le fichier
            ecrivain.writerow([ip, etat, type_matos])
            print(f"[+] Ajout de {ip} au rapport.")

    print(f"\n[SUCCÈS] Le fichier '{nom_fichier}' a été créé sur votre bureau ! 📄")

generer_inventaire()
input("\nAppuyez sur Entrée pour fermer...")