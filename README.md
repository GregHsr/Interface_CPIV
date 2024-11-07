# Générateur de Fichier de Paramètres pour CPIV

![Python](https://img.shields.io/badge/Python-3.11.5-blue) ![tkinter](https://img.shields.io/badge/tkinter-GUI-orange)

## Table des Matières
- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Template de Fichier Généré](#template-de-fichier-généré)
- [Crédits](#crédits)
---

## Introduction

Le **Générateur de Fichier de Paramètres pour CPIV** est une application basée sur tkinter, conçue pour simplifier la création de fichiers de paramètres destinés au logiciel de Vélocimétrie par Images de Particules CPIV. L'application offre une interface graphique intuitive permettant de configurer les différents paramètres sans avoir à éditer manuellement le fichier de données.

## Fonctionnalités

- **Interface intuitive** : Entrez  les paramètres PIV grâce à une interface simple
- **Validation en temps réel** : Les champs d'entrée sont vérifiés pour garantir la compatibilité et la cohérence des paramètres.
- **Export facile** : Enregistrez directement les paramètres dans un fichier **param.txt** compatible avec CPIV.
- **Aide intégrée** : Un bouton d'aide fournit des instructions détaillées pour chaque option.

## Installation

### Prérequis

- Python 3.11.5
- Bibliothèques requises :
  - `tkinter`
  - `os`
  - `re`
  - `pandas`

### Étapes

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/GregHsr/Interface_CPIV.git
   cd Interface_CPIV
2. Lancez l'application :
   ```bash
   python main.py
## Utilisation

1. **Lancer l'application** : 
   - Exécutez la commande suivante dans votre terminal pour ouvrir l'application :
     ```bash
     python main.py
2. **Configurer les paramètres** :
   - Remplissez chaque champ de saisie avec les valeurs souhaitées pour vos paramètres de CPIV.
3. **Générer le fichier de paramètres** :
   - Cliquez sur le bouton **Submit** pour valider vos entrées et créer le fichier de paramètres.
   - En cas d'erreur dans les valeurs entrées, un message d'avertissement s'affichera pour vous indiquer les corrections nécessaires.
    > **Remarque** : Assurez-vous que les valeurs respectent le format attendu par le logiciel CPIV afin d’éviter les erreurs lors de l’importation.   
   - Pour changer une valeur fausse après submission, relancer l'interface et rentrer de nouveau toutes les informations. 
    > **Important** : Lancer de nouveau l'interface écrase toutes les valeurs présentes dans le fichier param.txt

4. **Consulter l’aide** :
   - En cas de doute, utilisez le bouton **Help** pour afficher des instructions détaillées et le type de données attendu sur chaque paramètre configurable.

## Template de Fichier Généré

Voici un exemple de fichier de paramètres généré par l'application, adapté aux exigences de CPIV.

```plaintext
Input_typedata TWO | DBL | SEQDBL | SEQ
Input_SEQDirname /home/ralis/CPIV/sequence_images_tif 
Input_SEQdebut 0 (un entier)
Input_SEQinterImg 1 (un entier)
Input_SEQinterPaire 0 (un entier)
Input_Imgdouble /home/ralis/CPIV/images/img_dble.tif
Input_ImgTWO1 /home/ralis/CPIV/images/img1.tif
Input_ImgTWO2 /home/ralis/CPIV/images/img2.tif
Input_Masque OK | NO
Input_TypeMasque ONE | SEQ
Input_OneNameMasque /home/ralis/CPIV/mask/masque_static1.tif
Input_SeqDirMasque /home/ralis/CPIV/mask
CalculCPIV_meths PIVDEFORM | PIVDECAL | PIVSIMPLE
CalculCPIV_dimXYcell 16 16 (deux entiers)
CalculCPIV_recouv 0 0 (deux floats)
CalculCPIV_ROI OK | NO
CalculCPIV_ROIval 100 100 150 150 (4 entiers)
CalculCPIV_ConvTools OK | NO
CalculCPIV_FiltrePostCalcul OK | NO
CalculCPIV_SuiviCalcul OK | NO
CalculCPIV_VecX 47 (un entier)
CalculCPIV_VecY 69 (un entier)
```

## Crédits

Cette application a été développée par [Grégoire Husser](https://github.com/GregHsr).
