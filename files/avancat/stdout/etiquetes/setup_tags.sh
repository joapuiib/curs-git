#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_etiquetes ]; then
        rm -rf ~/git_etiquetes
fi

mkdir -p ~/git_etiquetes
cd ~/git_etiquetes
git init
git branch -m main
echo "# Etiquetes" > README.md
git add README.md
git commit -m "Commit inicial"
echo "Repositori d'exemple amb etiquetes" >> README.md
git commit -a -m "README: Descripció"
echo "" >> README.md
echo "## Tipus de etiquetes" >> README.md
git commit -a -m "README: Apartat tipus de etiquetes"
echo "Existeixen dos tipus de etiquetes: anotades i lleugeres" >> README.md
git commit -a -m "README: Descripció tipus de etiquetes"
git lga
