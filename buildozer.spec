[app]
# Titre de ton application
title = Conciergerie

# Nom du package (pas d'espaces)
package.name = conciergerie

# Domaine (peut être ce que tu veux)
package.domain = org.desruelle

# Dossier où se trouve ton main.py
source.dir = .

# Extensions des fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas

# Fichier principal
source.main = main.py

# Version de l'application
version = 1.0

# Les dépendances EXACTES de ton projet (Très important)
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pymysql

# Orientation de l'écran
orientation = portrait

# Précise que tu veux utiliser la version iOS
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Version minimum iOS
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
# (bool) Autoriser la signature du code (Désactivé pour utiliser Sideloadly)
ios.codesign.allowed = no

# (str) Nom du certificat (Même désactivé, Buildozer a besoin que ces variables existent)
ios.codesign.debug = "iPhone Developer: <nom>"
ios.codesign.release = %(ios.codesign.debug)s

[buildozer]
# Niveau de log (2 = debug)
log_level = 2
warn_on_root = 1