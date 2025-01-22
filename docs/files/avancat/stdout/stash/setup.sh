#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_etiquetes ]; then
    rm -rf ~/git_etiquetes
fi

mkdir -p ~/git_stash
cd ~/git_stash
git init
git branch -m main
echo "# Reserva de canvis" > README.md
git add README.md
git commit -m "Commit inicial"
git checkout -b altres_canvis
echo "Altres canvis" >> README.md
git commit -a -m "Altres canvis"
git checkout main
git lga
