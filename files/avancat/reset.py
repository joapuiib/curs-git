#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_reset')

def init_repositori():
    x.log_file('stdout/reset/setup_reset.txt')
    x.log_bash_file('stdout/reset/setup_reset.sh')

    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/reset')

    # @TODO: remove directory if exists bash script
    x.log_bash('# Elimina els repositoris si existeixen')
    x.log_bash('if [ -d ~/git_reset ]; then')
    x.log_bash('    rm -rf ~/git_reset')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_reset')
    x.x('cd ~/git_reset')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Git reset i commit --amend" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "Canvi A"')
    x.x('echo "- Canvi B" >> README.md')
    x.x('git commit -a -m "Canvi B"')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git commit -a -m "Canvi C"')
    x.x('git lga')

    x.log_bash_file(None)

def reset_soft():
    x.log_file('stdout/reset/soft.txt')
    hash_B = x.run('git log --oneline --grep="^Canvi B$"').split()[0]
    print('==================== SOFT ========================')
    x.x(f"git reset --soft {hash_B}")
    x.x('git status')
    x.x('git diff --staged')
    x.x('git lga')

    x.log_file('stdout/reset/revert_soft.txt')
    print('==================== REVERT SOFT ========================')
    x.x('git commit -m "Canvi C"')
    x.x('git lga')

def reset_mixed():
    x.log_file('stdout/reset/mixed.txt')
    hash_B = x.run('git log --oneline --grep="^Canvi B$"').split()[0]
    print('==================== MIXED ========================')
    x.x(f"git reset --mixed {hash_B}")
    x.x('git status')
    x.x('git diff')
    x.x('git lga')

    x.log_file('stdout/reset/revert_mixed.txt')
    print('==================== REVERT MIXED ========================')
    x.x('git add README.md')
    x.x('git commit -m "Canvi C"')
    x.x('git lga')

def reset_hard():
    x.log_file('stdout/reset/hard.txt')
    hash_B = x.run('git log --oneline --grep="^Canvi B$"').split()[0]

    print('================ === HARD ========================')
    x.x(f"git reset --hard {hash_B}")
    x.x('git status')
    x.x('git lga')


def reset_keep():
    x.log_file('stdout/reset/keep.txt')
    hash_A = x.run('git log --oneline --grep="^Canvi A$"').split()[0]

    print('==================== KEEP ========================')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git status')
    x.x(f"git reset --keep {hash_A}")
    x.x('git lga')


def amend():
    x.log_file('stdout/reset/amend.txt')
    print('==================== AMEND ========================')
    x.x('git lga')
    x.x('git status')
    x.x('git diff')
    x.x('git add README.md')
    x.x('git commit --amend -m "Canvi B i C"')
    x.x('git lga')


parser = argparse.ArgumentParser(description='Etiquetes')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

reset_soft()
reset_mixed()
reset_hard()
reset_keep()

amend()
