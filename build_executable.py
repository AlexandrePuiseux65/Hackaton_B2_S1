# Name:        ProjetHackathon_B2_Grp3
# Purpose:     création d’un carnet d'adresses avec Python et SQLite.
#               C'est le code principale
#              
# Author:      Alexandre PUISEUX - alexandre.puiseux@edu.ece.fr
#              Joan-Baptiste FERRANDO - joanbaptiste.ferrando@edu.ece.fr
# Lib :
import subprocess

# Spécifiez le chemin du script Python que vous souhaitez transformer en exécutable
script_path = "/Users/alexandrepuiseux/Desktop/CODE/Python/ProjetHackathonVisual_BB2_Final V3/main.py"

# Spécifiez le chemin de sortie pour l'exécutable
output_path = "/Users/alexandrepuiseux/Desktop/CODE/Python/ProjetHackathonVisual_BB2_Final V3"

# Utilisez PyInstaller pour créer l'exécutable
subprocess.run(["pyinstaller", "--onefile", "--windowed", script_path, "-n", "The Best Hackathon", "--distpath", output_path])