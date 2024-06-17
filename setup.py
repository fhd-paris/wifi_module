from setuptools import setup, find_packages

# Fonction pour lire le contenu du fichier README.md
def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    return readme_content

# Dépendances requises pour le module
install_requires = [
    'requests>=2.0',  # Dépendance avec version minimale spécifiée
    'numpy',          # Dépendance sans spécification de version
    # Ajoutez d'autres dépendances ici selon les besoins de votre module
]

# Spécifiez les détails de votre module
setup(
    name='wifi_module',            # Nom de votre module
    version='0.1',                 # Numéro de version de votre module
    author='Your Name',            # Nom de l'auteur
    author_email='author@example.com',  # Email de l'auteur
    description='Module to manage WiFi connections',  # Description courte
    long_description=read_readme(),  # Contenu complet de README.md comme description longue
    long_description_content_type='text/markdown',  # Type de contenu de la description longue
    url='https://github.com/fhd-paris/wifi_module',  # URL du projet
    packages=find_packages(),      # Trouve toutes les packages nécessaires
    install_requires=install_requires,  # Liste des dépendances requises
    classifiers=[  # Liste de classifiers pour le module
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
