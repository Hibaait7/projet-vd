#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Cette ligne  qui indique à l'interpréteur du système d'utiliser Python pour exécuter ce script
import os
import sys

# Importation des modules nécessaires. `os` permet de gérer les interactions avec le système d'exploitation,
# tandis que `sys` fournit des fonctions et variables pour manipuler l'environnement d'exécution de Python

def main():
    """Run administrative tasks."""
     # Définition de la fonction principale qui exécute les tâches administratives de Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_visualization.settings')
       # Cela indique à Django où trouver les paramètres de configuration du projet.

    try:
        from django.core.management import execute_from_command_line
                # Importation de la fonction `execute_from_command_line` du module Django pour exécuter des commandes via la ligne de commande.

    except ImportError as exc:
                # Capture l'exception `ImportError` si le module Django n'est pas trouvé.

        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?\n"
            "Did you forget to activate a virtual environment?"
        ) from exc
                # Lève une exception avec un message d'erreur expliquant que Django n'est pas installé ou qu'un environnement virtuel n'est pas activé.

    execute_from_command_line(sys.argv)
        # Exécute la commande Django passée via `sys.argv`, qui contient les arguments de la ligne de commande.


if __name__ == '__main__':
    main()
    # Cette condition garantit que la fonction `main()` n'est appelée que si le script est exécuté directement,
    # et non s'il est importé comme un module dans un autre script.