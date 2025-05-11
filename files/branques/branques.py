#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_branques')

def init_repositori():
    x.run('mkdir -p stdout/branques')
    x.log_file('stdout/branques/inicial.txt')
    x.log_bash_file('stdout/branques/setup_branques.sh')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_branques ]; then')
    x.log_bash('    rm -rf ~/git_branques')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_branques')
    x.x('cd ~/git_branques')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main # (1)!')
    x.x('echo "# Branques a Git" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git lga')

    x.log_bash_file(None)
    x.run('git config merge.ff true')


def estructura_inicial():
    x.log_file('stdout/branques/estructura_inicial.txt')
    print('==================== ESTRUCTURA INICIAL ========================')
    x.x('git lga')


def mostrar_branques():
    x.log_file('stdout/branques/branch_show.txt')
    print('==================== MOSTRAR BRANQUES ========================')
    x.x('git branch')


def crear_branca():
    x.log_file('stdout/branques/branch_create.txt')
    print('==================== CREAR BRANQUES ========================')
    x.x('git lga')
    x.x('git branch menjar')
    x.x('git branch beguda')
    x.x('git branch neteja')
    x.x('git branch')
    x.x('git lga')


def abans_canviar_branca():
    x.log_file('stdout/branques/abans_checkout_menjar.txt')
    print('==================== ABANS CHECKOUT BRANCA MENJAR ========================')
    x.x('cat README.md')
    x.x('git branch')
    x.x('git lga')


def canviar_branca():
    x.log_file('stdout/branques/checkout_menjar.txt')
    print('==================== CHECKOUT BRANCA MENJAR ========================')
    x.x('git checkout menjar')
    x.x('cat README.md')
    x.x('git branch')
    x.x('git lga')


def canvis_menjar():
    x.log_file('stdout/branques/canvis_menjar.txt')
    print('==================== CANVIS MENJAR ========================')
    x.x('echo "Pa" >> menjar.txt')
    x.x('echo "Macarrons" >> menjar.txt')
    x.x('git status')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar"')
    x.x('git lga')


def canvis_beguda():
    x.log_file('stdout/branques/canvis_beguda.txt')
    print('==================== CANVIS BEGUDA ========================')
    x.x('git checkout beguda')
    x.x('echo "Aigua" >> beguda.txt')
    x.x('echo "Orxata" >> beguda.txt')
    x.x('git status')
    x.x('git add beguda.txt')
    x.x('git commit -m "Beguda"')
    x.x('git lga')


def canvis_neteja():
    x.log_file('stdout/branques/canvis_neteja.txt')
    print('==================== CANVIS NETEJA ========================')
    x.x('git checkout neteja')
    x.x('echo "Paper higiènic" >> neteja.txt')
    x.x('echo "Fregall" >> neteja.txt')
    x.x('git status')
    x.x('git add neteja.txt')
    x.x('git commit -m "Neteja"')
    x.x('git lga')


def eliminar_neteja():
    x.log_file('stdout/branques/eliminar_neteja.txt')
    print('==================== ELIMINAR BRANCA NETEJA ========================')
    x.x('git checkout main')
    x.x('git lga')
    x.x('git branch -d neteja')
    x.x('git branch -D neteja')
    x.x('git lga')


def before_ff():
    x.log_file('stdout/branques/before_ff.txt')
    print('==================== BEFORE FF ========================')
    x.x('git checkout main')
    x.x('ls')
    x.x('git lga')


def after_ff():
    x.log_file('stdout/branques/after_ff.txt')
    print('==================== AFTER FF ========================')
    x.x('git checkout main')
    x.x('git merge menjar')
    x.x('ls # (1)!')
    x.x('cat menjar.txt')
    x.x('git lga')


def before_no_ff():
    x.log_file('stdout/branques/before_no_ff.txt')
    print('==================== BEFORE NO FF ========================')
    x.x('git checkout main')
    x.x('ls')
    x.x('git lga')


def after_no_ff():
    x.log_file('stdout/branques/after_no_ff.txt')
    print('==================== AFTER NO FF ========================')
    x.x('git checkout main')
    x.x('git merge beguda --no-ff -m "Merge branch \'beguda\' into \'main\'" # (1)!')
    x.x('ls # (2)!')
    x.x('cat beguda.txt')
    x.x('git lga')


def merge_conflictes():
    x.log_file('stdout/branques/merge_conflicts_branch_create.txt')
    print('==================== MERGE PREPARACIO CONFLICTES CREAR BRANQUES ========================')
    x.x('git checkout main')
    x.x('git branch fruita')
    x.x('git branch verdura')
    x.x('git lga')

    print('==================== CANVIS FRUTA ========================')
    x.log_file('stdout/branques/merge_conflicts_fruita.txt')
    x.x('git checkout fruita')
    x.x('echo "Pomes" >> menjar.txt')
    x.x('echo "Bresquilles" >> menjar.txt')
    x.x('git status')
    x.x('git add menjar.txt')
    x.x('git commit -m "Fruta"')
    x.x('git lga')

    print('==================== CANVIS VERDURA ========================')
    x.log_file('stdout/branques/merge_conflicts_verdura.txt')
    x.x('git checkout verdura')
    x.x('echo "Tomaques" >> menjar.txt')
    x.x('echo "Creïlles" >> menjar.txt')
    x.x('git status')
    x.x('git add menjar.txt')
    x.x('git commit -m "Verdura"')
    x.x('git lga')

    print('==================== SHOW FRUTA I VERDURA ========================')
    x.log_file('stdout/branques/merge_conflicts_show.txt')
    x.x('git checkout main')
    x.x('git lg')
    x.x('git show fruita')
    x.x('git show verdura')

    print('==================== MERGE FRUTA ========================')
    x.log_file('stdout/branques/merge_conflicts_merge_fruita.txt')
    x.x('git merge fruita')
    x.x('git lga')

    print('==================== MERGE VERDURA ========================')
    x.log_file('stdout/branques/merge_conflicts_merge_verdura.txt')
    x.x('git merge verdura')
    x.x('git status')
    x.x('cat menjar.txt')

    print('==================== RESOLVE CONFLICTES ========================')
    x.log_file('stdout/branques/merge_conflicts_resolve.txt')
    x.log_file_content('menjar.txt', 'stdout/branques/menjar_before_resolve.txt')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' menjar.txt')
    x.log_file_content('menjar.txt', 'stdout/branques/menjar_after_resolve.txt')
    x.log_prompt('code menjar.txt # (1)!')
    x.x('git add menjar.txt')
    x.x('git status')
    x.x('git commit -m "Merge branch \'verdura\' into \'main\'"')
    x.x('git lga')


def rebase():
    x.log_file('stdout/branques/rebase_branch_create.txt')
    print('==================== BEFORE REBASE ========================')
    x.x('git checkout main')
    x.x('git branch desdejuni')
    x.x('git branch paella')
    x.x('git lga -3 # (1)!')

    x.log_file('stdout/branques/changes_desdejuni.txt')
    print('==================== CANVIS DESDEJUNI ========================')
    x.x('git checkout desdejuni')
    x.x('echo "Café" >> beguda.txt')
    x.x('git add beguda.txt')
    x.x('git commit -m "Beguda desdejuni"')
    x.x('git lga -3')

    x.log_file('stdout/branques/changes_paella.txt')
    print('==================== CANVIS PAELLA ========================')
    x.x('git checkout paella')
    x.x('echo "Arròs" >> menjar.txt')
    x.x('echo "Pollastre" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar paella"')
    x.x('git lga -3')

    x.log_file('stdout/branques/rebase_merge_desdejuni.txt')
    print('==================== REBASE MERGE DESDEJUNI ========================')
    x.x('git checkout main')
    x.x('git merge desdejuni')
    x.x('git lga -3')

    x.log_file('stdout/branques/rebase_paella.txt')
    print('==================== REBASE PAELLA ========================')
    x.x('git checkout paella')
    x.run('git rebase main')
    x.log_prompt('git rebase main')
    x.log_output('Rebasing (1/1)\n')
    x.log_output('Successfully rebased and updated refs/heads/paella.\n')
    x.x('git lga -3')

    x.log_file('stdout/branques/rebase_merge_paella.txt')
    print('==================== REBASE MERGE PAELLA ========================')
    x.x('git checkout main')
    x.x('git merge paella')
    x.x('git lga -3')


def rebase_conflicts():
    x.log_file('stdout/branques/rebase_conflicts_branch_create.txt')
    print('==================== BEFORE REBASE CONFLICTS ========================')
    x.x('git checkout main')
    x.x('git branch postre')
    x.x('git branch aperitiu')
    x.x('git lga -3')

    x.log_file('stdout/branques/changes_postre.txt')
    print('==================== CANVIS POSTRE ========================')
    x.x('git checkout postre')
    x.x('echo "Iogurt" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar postre"')
    x.x('git lga -3')

    x.log_file('stdout/branques/changes_apertiu.txt')
    print('==================== CANVIS APERITIU ========================')
    x.x('git checkout aperitiu')
    x.x('echo "Olives" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar aperitiu"')
    x.x('git lga -3')

    print('==================== SHOW POSTRE I APERITIU ========================')
    x.log_file('stdout/branques/rebase_conflicts_show.txt')
    x.x('git checkout main')
    x.x('git lga -3')
    x.x('git show postre')
    x.x('git show aperitiu')

    x.log_file('stdout/branques/rebase_merge_postre.txt')
    print('==================== REBASE MERGE POSTRE ========================')
    x.x('git checkout main')
    x.x('git merge postre')
    x.x('git lga -3')

    x.log_file('stdout/branques/rebase_apertiu.txt')
    print('==================== REBASE APERITIU ========================')
    x.x('git checkout aperitiu')
    x.x('git rebase main')
    x.x('git status')

    x.log_file('stdout/branques/rebase_aperitiu_resolve.txt')
    print('==================== RESOLVE REBASE APERITIU ========================')
    x.log_file_content('menjar.txt', 'stdout/branques/menjar_before_rebase_resolve.txt')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' menjar.txt')
    x.log_file_content('menjar.txt', 'stdout/branques/menjar_after_rebase_resolve.txt')
    x.log_prompt('code menjar.txt # (1)!')
    x.x('git add menjar.txt')
    x.x('git status')
    x.x('git rebase --continue', env={'GIT_EDITOR': 'true'})
    x.x('git lga -3')

    x.log_file('stdout/branques/rebase_merge_apertiu.txt')
    print('==================== REBASE MERGE APERITIU ========================')
    x.x('git checkout main')
    x.x('git merge aperitiu')
    x.x('git lga -3')




parser = argparse.ArgumentParser(description='Etiquetes')
parser.add_argument('-v', "--verbose", action='store_true')
parser.add_argument("--push", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

estructura_inicial()

mostrar_branques()
crear_branca()

abans_canviar_branca()
canviar_branca()
canvis_menjar()
canvis_beguda()
canvis_neteja()

eliminar_neteja()

before_ff()
after_ff()
before_no_ff()
after_no_ff()
merge_conflictes()

rebase()
rebase_conflicts()
