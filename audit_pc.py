import os

def verifier_securite():
    print("--- AUDIT DE SÉCURITÉ RAPIDE ---")
    print("Vérification du Pare-feu Windows en cours...")
    
    # On utilise la commande système 'netsh' pour interroger le pare-feu
    # os.popen permet de lire le résultat de la commande
    resultat = os.popen("netsh advfirewall show allprofiles state").read()
    
    # Analyse du résultat
    if "ON" in resultat:
        print("\n[OK] Le Pare-feu est ACTIVÉ. ✅")
        print(" -> Le poste est protégé contre les connexions entrantes.")
    else:
        print("\n[!!!] ALERTE : Le Pare-feu est DÉSACTIVÉ ! ❌")
        print(" -> Risque critique. Action requise immédiate.")

# Lancement du programme
verifier_securite()
input("\nAppuyez sur Entrée pour fermer...")