#!/bin/bash

# Elimina els repositori si existeix
if [ -d ~/git_remots ]; then
    rm -rf ~/git_remots
fi

mkdir -p ~/git_remots
cd ~/git_remots
git init
git branch -m main # (1)!
echo "# Remots a Git" > README.md
echo "Repositori del __Bloc: Remots__ del curs __\"Introducció a Git i la seua aplicació a l’aula\"__" >> README.md
git add README.md
git commit -m "Commit inicial"
git lga
