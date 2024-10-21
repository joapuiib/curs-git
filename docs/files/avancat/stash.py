#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_stash')

def init_repositori():
    x.log_file('stdout/stash/inicial.txt')
    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/stash')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_stash')
    x.x('cd ~/git_stash')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Reserva de canvis" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('echo "Repositori d\'exemple amb reserva de canvis" >> README.md')
    x.x('git commit -a -m "README: Descripció"')
    x.x('git checkout -b feature/documentacio')
    x.x('echo "" >> README.md')
    x.x('echo "## Documentació" >> README.md')
    x.x('echo "- https://git-scm.com/docs/git-stash" >> README.md')
    x.x('git commit -a -m "README: Documentació"')
    x.x('git checkout main')
    x.x('git lga')

def stash():
    x.log_file('stdout/stash/stash.txt')

    print('==================== STASH ========================')
    x.x('echo "" >> README.md')
    x.x('echo "L\'ordre git stash permet reservar els canvis temporalment per a poder fer altres tasques." >> README.md')
    x.x('git status')
    x.x('git checkout feature/documentacio')
    x.x('git stash -m "Text git stash"')
    x.x('git status')
    x.x('git checkout feature/documentacio')
    x.x('git checkout main')

def llista():
    x.log_file('stdout/stash/llista.txt')

    print('==================== LLISTA ========================')
    x.x('git stash list')

def mostrar():
    x.log_file('stdout/stash/mostrar.txt')

    print('==================== MOSTRAR ========================')
    x.x('git stash show')
    x.x('git stash show -p')

def apply():
    x.log_file('stdout/stash/apply.txt')

    print('==================== APPLY ========================')
    x.x('git status')
    x.x('git stash apply')
    x.x('git diff')
    x.x('git stash list')

def drop():
    x.log_file('stdout/stash/drop.txt')

    print('==================== DROP ========================')
    x.x('git stash list')
    x.x('git stash drop')
    x.x('git stash list')


parser = argparse.ArgumentParser(description='Etiquetes')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

stash()
llista()
mostrar()

apply()
drop()
