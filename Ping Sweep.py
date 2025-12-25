import os
import platform

def scan_reseau():
    print("--- SCANNER RÉSEAU (PING SWEEP) ---")
    # On demande la base de l'IP (ex: 192.168.1)
    base_ip = input("Entrez les 3 premiers blocs de l'IP (ex: 192.168.1) : ")
    print("\nScan en cours... (Cela peut prendre quelques secondes)")

    # On scanne les machines de .1 à .20 pour la démo
    for i in range(1, 21):
        ip = f"{base_ip}.{i}"
        
        # Commande adaptée selon si on est sur Windows ou Linux
        if platform.system() == "Windows":
            # -n 1 : un seul ping, -w 200 : attendre 200ms max (rapide)
            commande = f"ping -n 1 -w 200 {ip} > nul"
        else:
            commande = f"ping -c 1 -W 1 {ip} > /dev/null 2>&1"
            
        # Exécution de la commande
        reponse = os.system(commande)
        
        # Si la réponse est 0, c'est que la machine a répondu
        if reponse == 0:
            print(f"[+] {ip} est EN LIGNE 🟢")
        
scan_reseau()
input("\nFin du scan. Appuyez sur Entrée...")