# <img src="/images/icon.png" alt="" width="25"/> Ulauncher Thésaurus

[![Platforms](https://img.shields.io/badge/platform-Linux-green)]()
[![Python Versions](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-%23007ec6?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4gIDxkZWZzPiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InB5WWVsbG93IiBncmFkaWVudFRyYW5zZm9ybT0icm90YXRlKDQ1KSI+ICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI2ZlNSIgb2Zmc2V0PSIwLjYiLz4gICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjZGExIiBvZmZzZXQ9IjEiLz4gICAgPC9saW5lYXJHcmFkaWVudD4gICAgPGxpbmVhckdyYWRpZW50IGlkPSJweUJsdWUiIGdyYWRpZW50VHJhbnNmb3JtPSJyb3RhdGUoNDUpIj4gICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjNjlmIiBvZmZzZXQ9IjAuNCIvPiAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiM0NjgiIG9mZnNldD0iMSIvPiAgICA8L2xpbmVhckdyYWRpZW50PiAgPC9kZWZzPiAgPHBhdGggZD0iTTI3LDE2YzAtNyw5LTEzLDI0LTEzYzE1LDAsMjMsNiwyMywxM2wwLDIyYzAsNy01LDEyLTExLDEybC0yNCwwYy04LDAtMTQsNi0xNCwxNWwwLDEwbC05LDBjLTgsMC0xMy05LTEzLTI0YzAtMTQsNS0yMywxMy0yM2wzNSwwbDAtM2wtMjQsMGwwLTlsMCwweiBNODgsNTB2MSIgZmlsbD0idXJsKCNweUJsdWUpIi8+ICA8cGF0aCBkPSJNNzQsODdjMCw3LTgsMTMtMjMsMTNjLTE1LDAtMjQtNi0yNC0xM2wwLTIyYzAtNyw2LTEyLDEyLTEybDI0LDBjOCwwLDE0LTcsMTQtMTVsMC0xMGw5LDBjNywwLDEzLDksMTMsMjNjMCwxNS02LDI0LTEzLDI0bC0zNSwwbDAsM2wyMywwbDAsOWwwLDB6IE0xNDAsNTB2MSIgZmlsbD0idXJsKCNweVllbGxvdykiLz4gIDxjaXJjbGUgcj0iNCIgY3g9IjY0IiBjeT0iODgiIGZpbGw9IiNGRkYiLz4gIDxjaXJjbGUgcj0iNCIgY3g9IjM3IiBjeT0iMTUiIGZpbGw9IiNGRkYiLz48L3N2Zz4=)](https://www.python.org/)
[![License](https://img.shields.io/github/license/tkapias/ulauncher-thesaurus?color=%23007ec6)](LICENSE)

`Ulauncher Thésaurus` est une extension pour [Ulauncher](https://ulauncher.io/) qui permet de chercher rapidement des synonymes ou antonymes de la langue Française.

![screenshot](screenshot.gif)

## Caractéristiques

### 2 sources de suggestions

- larousse.fr : Donne des résultats en grappe par contexte, précédés d'un exemple quand il est disponible.
- cnrtl.fr : Donne une liste simple avec plus de résultats.

Vous pouvez choisir la source primaire dans les préférences de l'extension sous Ulauncher (Par défaut : larousse.fr).

Vous pouvez aussi basculer d'une source à l'autre en cours de recherche en cliquant ou en appuyant sur "Entrer" dans la dernière ligne.

### Bascule entre synonymes ou antonymes

Après avoir entrer une recherche vous pouvez basculer entre les résultats de types synonymes ou antonymes avec la combinaison des touches "Alt+Entrer".

### Défiler les liste de résultats trop longues

L'extension limite l'affichage des résultats à 10. S'il y en a plus vous pouvez charger les 10 suivants en cliquant ou en appuyant sur "Entrer" dans la premère ligne décorée d'un image for :twisted_rightwards_arrows:.

## Installation et prérequis

L'installation se fait depuis l'interface de [Ulauncher](https://ulauncher.io/) en indiquant l'url `https://github.com/tkapias/ulauncher-thesaurus` de ce dépôt Github.

La librairie beautifulsoup4 est requise pour le fonctionnement de l'extension. Vous pouvez l'ajouter sur votre machine avec `pip install beautifulsoup4`.

## Remerciements

La création de cette extension est inspiré par l'existance de celle de [thesaurus_cc_ulauncher](https://github.com/behrensger/thesaurus_cc_ulauncher).

Le script est basé en partie sur la librairie [synonymes 0.0.3.3](https://pypi.org/project/synonymes/)
