#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_squash')

def init_repositori():
    x.log_file('stdout/squash/inicial.txt')
    x.log_bash_file('stdout/squash/setup_squash.sh')

    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/squash')

    # @TODO: remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_squash ]; then')
    x.log_bash('    rm -rf ~/git_squash')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_squash')
    x.x('cd ~/git_squash')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Git merge --squash" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git checkout -b canvis')
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "Canvi A"')
    x.x('echo "- Canvi B" >> README.md')
    x.x('git commit -a -m "Canvi B"')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git commit -a -m "Canvi C"')
    x.x('git lga')

    x.log_bash_file(None)

def squash():
    x.log_file('stdout/squash/squash.txt')
    print('==================== SQUASH ========================')
    x.x(f"git checkout main")
    x.x('git merge --squash canvis')
    x.x('git status')
    x.x('git commit -m "Canvis A, B i C"')
    x.x('git lga')


parser = argparse.ArgumentParser(description='Squash')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

squash()
