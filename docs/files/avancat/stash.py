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
    x.log_file('stdout/stash/setup.txt')
    x.log_bash_file('stdout/stash/setup.sh')
    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/stash')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_etiquetes ]; then')
    x.log_bash('    rm -rf ~/git_etiquetes')
    x.log_bash('fi')
    x.log_bash('')


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
    x.x('git checkout -b altres_canvis')
    x.x('echo "Altres canvis" >> README.md')
    x.x('git commit -a -m "Altres canvis"')
    x.x('git checkout main')
    x.x('git lga')

    x.log_bash_file(None)

def perque_es_util():
    x.log_file('stdout/stash/perque_es_util.txt')

    print('==================== PERQUÈ ÉS ÚTIL ? ========================')
    x.x('echo "Canvi A" >> README.md')
    x.x('git status')
    x.x('git checkout altres_canvis')


def stash():
    x.log_file('stdout/stash/stash.txt')

    print('==================== STASH ========================')
    x.x('git status')
    x.x('git diff')
    x.x('git stash -m "Canvi A"')
    x.x('git status')
    x.x('git checkout altres_canvis')
    x.x('git checkout main')


def multiple_stash():
    x.log_file('stdout/stash/canvi_b.txt')

    print('==================== CANVI B ========================')
    x.x('echo "Canvi B" >> README.md')
    x.x('git stash -m "Canvi B"')
    x.x('git status')
    x.x('git stash list')

    x.log_file('stdout/stash/canvi_c.txt')

    print('==================== CANVI C ========================')
    x.x('echo "Canvi C" >> README.md')
    x.x('git stash -m "Canvi C"')
    x.x('git status')
    x.x('git stash list')


def llista():
    x.log_file('stdout/stash/llista.txt')

    print('==================== LLISTA ========================')
    x.x('git stash list')


def mostrar():
    x.log_file('stdout/stash/mostrar.txt')

    print('==================== MOSTRAR ========================')
    x.x('git stash list')
    x.x('git stash show -p')
    x.x('git stash show -p 1')
    x.x('git stash show -p 2')


def apply():
    x.log_file('stdout/stash/apply.txt')

    print('==================== APPLY ========================')
    x.x('git status')
    x.x('git stash apply')
    x.x('git status')
    x.x('git diff')
    x.x('git stash list')


def pop():
    x.log_file('stdout/stash/pop.txt')

    print('==================== POP ========================')
    x.x('git restore README.md # (1)!')
    x.x('git status')
    x.x('git stash pop')
    x.x('git status')
    x.x('git diff')
    x.x('git stash list')


def drop():
    x.log_file('stdout/stash/drop.txt')

    print('==================== DROP ========================')
    x.x('git stash list')
    x.x('git stash drop')
    x.x('git stash list')


parser = argparse.ArgumentParser(description='stash')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

perque_es_util()
stash()
multiple_stash()

llista()
mostrar()

apply()
pop()
drop()
