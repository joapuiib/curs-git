#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_cherrypick')

def init_repositori():
    x.log_file('stdout/cherrypick/inicial.txt')
    x.log_bash_file('stdout/cherrypick/setup.sh')

    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/cherrypick')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_cherrypick ]; then')
    x.log_bash('    rm -rf ~/git_cherrypick')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_cherrypick')
    x.x('cd ~/git_cherrypick')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Git cherrypick" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git branch begudes')
    x.x('git branch menjar')
    x.x('git checkout begudes')
    x.x('echo "Aigua" >> begudes.txt')
    x.x('git add begudes.txt')
    x.x('git commit -m "Begudes: aigua"')
    x.x('echo "Refresc" >> begudes.txt')
    x.x('git commit -a -m "Begudes: refresc"')
    x.x('git checkout main')
    x.x('git lga')

    x.log_bash_file(None)


def cherry_pick():
    x.log_file('stdout/cherrypick/prep_cherrypick.txt')
    print('==================== PREP CHERRY PICK ========================')
    x.x('git checkout begudes')
    x.x('echo "Pa" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar: pa"')
    x.x('git lga')

    x.log_file('stdout/cherrypick/cherrypick.txt')
    print('==================== CHERRY PICK ========================')
    hash_pa = x.run('git log --all --oneline --grep="^Menjar: pa$"').split()[0]

    x.x('git checkout menjar')
    x.x(f"git lga")
    x.x(f"ls")
    x.x(f"git cherry-pick {hash_pa}")
    x.x(f"git lga")
    x.x(f"ls")
    x.x(f"cat menjar.txt")

    x.log_file('stdout/cherrypick/post_cherrypick.txt')
    print('==================== POST CHERRY PICK ========================')
    hash_refresc = x.run('git log --all --oneline --grep="^Begudes: refresc$"').split()[0]
    x.x('git checkout begudes')
    x.x(f"git reset --hard {hash_refresc}")
    x.x(f"git lga")


def cherry_pick_conflictes():
    x.log_file('stdout/cherrypick/prep_conflictes.txt')
    print('================ PREP CHERRY PICK CONFLICTES ========================')
    x.x('git checkout begudes')
    x.x('echo "Taronges" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar: taronges"')
    x.x('git lga')

    x.log_file('stdout/cherrypick/conflictes.txt')
    print('==================== CHERRY PICK CONFLICTES ========================')
    hash_taronges = x.run('git log --all --oneline --grep="^Menjar: taronges$"').split()[0]

    x.x('git checkout menjar')
    x.x(f"git lga")
    x.x(f"git cherry-pick {hash_taronges}")
    x.x(f"cat menjar.txt")
    x.remove_conflictes("menjar.txt")
    x.log_prompt('code menjar.txt # (1)!')
    x.x('git diff')
    x.x('git add menjar.txt')
    x.x('git cherry-pick --continue --no-edit')
    x.x(f"git lga")

    x.log_file('stdout/cherrypick/post_conflictes.txt')
    print('==================== POST CHERRY PICK CONFLICTES ========================')
    hash_refresc = x.run('git log --all --oneline --grep="^Begudes: refresc$"').split()[0]

    x.x('git checkout begudes')
    x.x(f"git reset --hard {hash_refresc}")
    x.x(f"git lga")


parser = argparse.ArgumentParser(description='cherrypick')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()

if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

cherry_pick()
cherry_pick_conflictes()
