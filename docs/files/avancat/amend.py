#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_amend')

def init_repositori():
    x.log_file('stdout/amend/setup.txt')
    x.log_bash_file('stdout/amend/setup.sh')

    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/amend')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_amend ]; then')
    x.log_bash('    rm -rf ~/git_amend')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_amend')
    x.x('cd ~/git_amend')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Git amend" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "Canvi A"')
    x.x('echo "- canvi B" >> README.md')
    x.x('git commit -a -m "Canvi C"')
    x.x('git lga')

    x.log_bash_file(None)

def amend_canvi_nom():
    x.log_file('stdout/amend/amend_canvi_nom.txt')

    print('==================== COMMIT AMEND CANVI NOM ========================')
    x.x('git lga')
    x.x(f'git commit --amend -m "Canvi B"')
    x.x('git lga')
    x.x('git show')


def amend_canvi_contingut():
    x.log_file('stdout/amend/amend_canvi_contingut.txt')

    print('==================== COMMIT AMEND CANVI CONTINGUT ========================')
    x.x('cat README.md')
    x.run('sed -i "s/canvi/Canvi/" README.md')
    x.log_prompt('code README.md # (1)!')
    x.x('git diff')
    x.x('git add README.md')
    x.x('git commit --amend --no-edit # (2)!')
    x.x('git lga')
    x.x('git show')


parser = argparse.ArgumentParser(description='Squash')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

amend_canvi_nom()
amend_canvi_contingut()
