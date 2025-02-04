#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_avancat_exericici')

def init_repositori():
    x.run('mkdir -p stdout/exercici')
    x.log_file('stdout/exercici/inicial.txt')
    x.log_bash_file('stdout/exercici/setup_exercici_avancat.sh')

    x.set_user('jpuigcerver')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_avancat_exericici ]; then')
    x.log_bash('    rm -rf ~/git_avancat_exericici')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_avancat_exericici')
    x.x('cd ~/git_avancat_exericici')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Exerici Git avançat" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git branch canvis')
    x.x('git branch canvi/A')
    x.x('git branch canvi/B')
    x.x('git branch canvi/C')
    x.x('git checkout canvis')
    x.x('echo "__Canvis__: " >> README.md')
    x.x('git commit -a -m "Canvis"')
    x.x('git checkout canvi/A')
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "canviA"')
    x.x('git checkout canvi/B')
    x.x('echo "- Canvi B" >> README.md')
    x.x('git commit -a -m "Canvi B"')
    x.x('git checkout canvi/C')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git commit -a -m "Canvi C"')

    x.x('git checkout canvi/B')
    x.x('git merge --no-ff canvi/A')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md # Elimina les marques de conflicte")
    x.x('git commit -a -m "Merge \'canvi/A\' a \'canvi/B\'"')

    x.x('git checkout canvi/C')
    x.x('git merge --no-ff canvi/B')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md")
    x.x('git commit -a -m "Merge \'canvi/B\' a \'canvi/C\'"')

    x.x('git checkout canvis')
    x.x('git merge --no-ff canvi/C')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md")
    x.x('git commit -a -m "Merge \'canvi/C\' a \'canvis\'"')
    x.x('git lga')

    x.log_bash_file(None)

    x.log_file('stdout/exercici/estructura_inicial.txt')
    x.x('git lga')

def reset():
    hash_canvis = x.run('git log --all --oneline --grep="^Canvis$"').split()[0]
    hash_A = x.run('git log --all --oneline --grep="^canviA$"').split()[0]
    hash_B = x.run('git log --all --oneline --grep="^Canvi B$"').split()[0]
    hash_C = x.run('git log --all --oneline --grep="^Canvi C$"').split()[0]

    x.log_file(None)

    print('==================== RESET ========================')
    x.x('git checkout canvis')
    x.x(f'git reset --hard {hash_canvis}')
    x.x('git checkout canvi/A')
    x.x(f'git reset --hard {hash_A}')
    x.x('git checkout canvi/B')
    x.x(f'git reset --hard {hash_B}')
    x.x('git checkout canvi/C')
    x.x(f'git reset --hard {hash_C}')

    x.run('git checkout main')
    x.log_file('stdout/exercici/estructura_reset.txt')
    x.x('git lga')

def amend():
    x.log_file(None)

    print('==================== AMEND ========================')
    x.x('git checkout canvi/A')
    x.x('git commit --amend -m "Canvi A"')

    x.run('git checkout main')
    x.log_file('stdout/exercici/estructura_amend.txt')
    x.x('git lga')

def cherry_pick():
    x.log_file(None)

    print('==================== CHERRY PICK ========================')
    x.x('git checkout canvis')
    x.x('git cherry-pick canvi/A')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md")
    x.x('git add README.md')
    x.x('git cherry-pick --continue --no-edit')
    x.x('git lga')
    x.x('git cherry-pick canvi/B')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md")
    x.x('git add README.md')
    x.x('git cherry-pick --continue --no-edit')
    x.x('git lga')
    x.x('git cherry-pick canvi/C')
    x.x("sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md")
    x.x('git add README.md')
    x.x('git cherry-pick --continue --no-edit')
    x.x('git lga')

    x.run('git checkout main')
    x.log_file('stdout/exercici/estructura_cherrypick.txt')
    x.x('git lga')

    x.log_file(None)
    x.x('git branch -D canvi/A')
    x.x('git branch -D canvi/B')
    x.x('git branch -D canvi/C')

    x.log_file('stdout/exercici/estructura_cherrypick_eliminar_branques.txt')
    x.x('git lga')

def squash():
    x.log_file(None)

    print('==================== SQUASH ========================')
    x.x('git checkout main')
    x.x('git merge --squash canvis')
    x.x('git commit -m "Canvis A, B i C"')
    x.x('git tag -a GitAvançat -m "Estat final després de l\'exercici de Git avançat"')

    x.run('git checkout main')
    x.log_file('stdout/exercici/estructura_squash.txt')
    x.x('git show GitAvançat')
    x.x('git lga')

    x.log_file(None)
    x.x('git branch -D canvis')

    x.log_file('stdout/exercici/estructura_squash_eliminar_branques.txt')
    x.x('git lga')



parser = argparse.ArgumentParser(description='Squash')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

reset()
amend()
cherry_pick()
squash()
