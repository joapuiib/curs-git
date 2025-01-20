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
    x.x('echo "- Canvi A" >> README.md')
    x.x('git commit -a -m "Canvi A"')
    x.x('git branch branca1')
    x.x('git branch branca2')
    x.x('git checkout branca1')
    x.x('echo "- Canvi B" >> README.md')
    x.x('git commit -a -m "Canvi B"')
    x.x('echo "- Canvi C" >> README.md')
    x.x('git commit -a -m "Canvi C"')
    x.x('echo "- Canvi D" >> README.md')
    x.x('git commit -a -m "Canvi D"')
    x.x('git checkout branca2')
    x.x('echo "- Canvi E" >> README.md')
    x.x('git commit -a -m "Canvi E"')
    x.x('git checkout main')
    x.x('git lga')

    x.log_bash_file(None)


def cherry_pick():
    x.log_file('stdout/cherrypick/cherrypick.txt')
    print('==================== CHERRY PICK ========================')
    hash_B = x.run('git log --all --oneline --grep="^Canvi B$"').split()[0]

    x.x('git checkout main')
    x.x(f"git lga")
    x.x(f"cat README.md")
    x.x(f"git cherry-pick {hash_B}")
    x.x(f"git lga")
    x.x(f"cat README.md")

def cherry_pick_conflictes():
    x.log_file('stdout/cherrypick/conflictes.txt')
    print('==================== CHERRY PICK CONFLICTES ========================')
    hash_B = x.run('git log --all --oneline --grep="^Canvi B$"').split()[0]

    x.x('git checkout branca2')
    x.x(f"git lga")
    x.x(f"git cherry-pick {hash_B}")
    x.swap_conflictes("README.md")
    x.log_prompt('vim README.md # (1)!')
    x.x('git diff')
    x.x('git add README.md')
    x.x('git revert --continue --no-edit')
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
