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
    x.log_bash_file('stdout/cherrypick/setup_cherrypick.sh')

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
    x.x('echo "# Git revert i cherrypick" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "Canvi A"')
    x.x('echo "- Canvi B" >> README.md')
    x.x('git commit -a -m "Canvi B"')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git commit -a -m "Canvi C"')
    x.x('echo "- Canvi D" >> README.md')
    x.x('git commit -a -m "Canvi D"')
    x.x('echo "- Canvi E" >> README.md')
    x.x('git commit -a -m "Canvi E"')
    x.x('git lga')

    x.log_bash_file(None)

def revert():
    x.log_file('stdout/cherrypick/revert.txt')
    hash_E = x.run('git log --oneline --grep="^Canvi E$"').split()[0]

    print('==================== REVERT ========================')
    x.x(f"git revert {hash_E} --no-edit")
    x.x('git lga')
    x.x('git show')

def revert_multiple():
    x.log_file('stdout/cherrypick/revert_multiple.txt')
    hash_C = x.run('git log --oneline --grep="^Canvi C$"').split()[0]
    hash_D = x.run('git log --oneline --grep="^Canvi D$"').split()[0]

    print('==================== REVERT MULTIPLE ========================')
    x.x('git lga')
    x.x(f"git revert {hash_D} --no-commit")
    x.x(f"git diff --staged")
    x.x(f"git revert {hash_C} --no-commit")
    x.x(f"git diff --staged")
    x.x('git commit -m "Revert \\"Canvi C i D\\"" # (1)!')
    x.x('git lga')
    x.x('git show')

def revert_conflictes():
    x.log_file('stdout/cherrypick/revert_conflictes.txt')
    hash_A = x.run('git log --oneline --grep="^Canvi A$"').split()[0]

    print('==================== REVERT AMB CONFLICTES ========================')
    x.x('git lga')
    x.x(f"git revert {hash_A}")

    x.x(f"git status")
    x.run('sed -i \'/^- Canvi A$/d\' README.md')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('vim README.md # (1)!')
    x.x('git diff')
    x.x('git add README.md')
    x.x('git revert --continue --no-edit')
    x.x('git lga')

def cherry_pick():
    x.log_file('stdout/cherrypick/cherrypick.txt')
    print('==================== CHERRY PICK ========================')
    hash_C = x.run('git log --oneline --grep="^Canvi C$"').split()[0]

    x.x(f"git lga")
    x.x(f"cat README.md")
    x.x(f"git cherry-pick {hash_C}")
    x.x(f"git lga")
    x.x(f"cat README.md")

def cherry_pick_conflictes():
    x.log_file('stdout/cherrypick/cherrypick_conflictes.txt')
    print('==================== CHERRY PICK CONFLICTES ========================')
    hash_A = x.run('git log --oneline --grep="^Canvi A$"').split()[0]

    x.x(f"git lga")
    x.x(f"git cherry-pick {hash_A}")
    x.swap_conflictes("README.md")
    x.log_prompt('vim README.md # (1)!')
    x.x('git diff')
    x.x('git add README.md')
    x.x('git revert --continue --no-edit')
    x.x(f"git lga")

parser = argparse.ArgumentParser(description='Squash')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

revert()
revert_multiple()
revert_conflictes()

cherry_pick()
cherry_pick_conflictes()
