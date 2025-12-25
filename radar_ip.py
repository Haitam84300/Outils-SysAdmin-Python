def detecteur_intrus():
    print("--- RADAR DE SURVEILLANCE RÉSEAU ---")
    
    # 1. La LISTE BLANCHE (Appareils autorisés de l'entreprise)
    appareils_connus = ["192.168.1.1", "192.168.1.50", "192.168.1.51"]
    
    # 2. SIMULATION d'un scan réseau (On imagine que le scan vient de se finir)
    # Note : La dernière IP (200) n'est pas dans la liste connue !
    scan_actuel = ["192.168.1.1", "192.168.1.50", "192.168.1.200"]
    
    print(f"Appareils autorisés dans la base : {len(appareils_connus)}")
    print(f"Appareils détectés sur le réseau : {len(scan_actuel)}\n")
    print("-" * 30)
    
    # 3. Logique de détection
    for ip in scan_actuel:
        if ip in appareils_connus:
            print(f"[OK] {ip} est un appareil connu.")
        else:
            # Affichage en rouge (si la console le supporte) ou avec ALERTE
            print(f"[!!!] ALERTE : {ip} est INCONNUE ! (Intrusion ?) 🚨")
            print(" -> Vérifier la salle de réunion ou le Wifi Invité.")

detecteur_intrus()
input("\nAppuyez sur Entrée pour fermer...")