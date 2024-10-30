#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    if os.path.exists(os.path.expanduser('~/git_remots')):
        x.run('rm -rf ~/git_remots')


def init_repositori():
    x.load_config()
    x.x('echo "GIT_CONFIG_GLOBAL=$GIT_CONFIG_GLOBAL"')

    x.run('mkdir -p stdout/remots')
    x.log_file('stdout/remots/inicial.txt')
    x.log_bash_file('stdout/remots/setup_remots.sh')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_remots ]; then')
    x.log_bash('    rm -rf ~/git_remots')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_remots')
    x.x('cd ~/git_remots')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main # (1)!')
    x.x('echo "# Remots a Git" > README.md')
    x.x('echo "Repositori del __Bloc: Remots__ del curs __\\\"Introducció a Git i la seua aplicació a l’aula\\\"__" >> README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git lga')

    x.log_file_content('README.md', 'stdout/remots/README.txt')

    x.log_bash_file(None)


def init_remote():
    x.run('gh repo delete joapuiib/git_remots --yes')
    x.run('gh repo create joapuiib/git_remots --public')


def show_no_remote():
    x.log_file('stdout/remots/no_remote.txt')
    print('==================== ESTRUCTURA INICIAL ========================')
    x.x('git push')


def add_remote():
    x.log_file('stdout/remots/add_remote.txt')
    print('==================== AFEGIR REMOT ========================')
    x.x('git remote add origin git@github.com:joapuiib/git_remots.git')
    x.x('git remote show origin')

def push_no_upstream():
    x.log_file('stdout/remots/push_no_upstream.txt')
    print('==================== PUSH NO UPSTREAM ========================')
    x.x('git lga')
    x.x('git push')

def push_upstream():
    x.log_file('stdout/remots/push_upstream.txt')
    print('==================== PUSH UPSTREAM ========================')
    x.x('git push --set-upstream origin main')
    x.x('git lga')


def clone():
    x.log_file('stdout/remots/clone.txt')
    print('==================== CLONE ========================')
    x.x('cd ~')
    x.x('rm -rf ~/git_remots')
    x.x('ls -l ~/git_remots')
    x.x('git clone git@github.com:joapuiib/git_remots.git')
    x.x('cd ~/git_remots')
    x.x('git lga')


def prepare_fetch():
    x.set_logging(False)
    print('==================== PREPARE FETCH ========================')
    if os.path.exists(os.path.expanduser('~/git_remots_tmp')):
        x.run('rm -rf ~/git_remots_tmp')
    x.x('git clone git@github.com:joapuiib/git_remots.git ~/git_remots_tmp')
    x.x('cd ~/git_remots_tmp')
    x.x('echo "Pa" >> menjar.txt')
    x.x('echo "Macarrons" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Menjar"')
    x.x('git push')


def fetch():
    x.set_logging(True)
    x.log_file('stdout/remots/before_fetch.txt')
    x.run('cd ~/git_remots')
    print('==================== BEFORE FETCH ========================')
    x.x('git lga')

    x.log_file('stdout/remots/after_fetch.txt')
    print('==================== AFTER FETCH ========================')
    x.x('git fetch')
    x.x('git lga')


def pull_ff():
    x.log_file('stdout/remots/before_pull_ff.txt')
    print('==================== PULL FF ========================')
    x.x('git lga')

    x.log_file('stdout/remots/after_pull_ff.txt')
    print('==================== AFTER PULL FF ========================')
    x.x('git pull')
    x.x('git lga')


def prepare_remote_pull_no_ff():
    x.set_logging(False)
    print('==================== PREPARE REMOT PULL NO FF ========================')
    x.x('cd ~/git_remots_tmp')
    x.x('echo "Pomes" >> menjar.txt')
    x.x('git add menjar.txt')
    x.x('git commit -m "Més menjar"')
    x.x('git push')


def prepare_local_pull_no_ff():
    x.set_logging(True)
    x.log_file('stdout/remots/prepare_local_pull_no_ff.txt')
    x.run('cd ~/git_remots')
    print('==================== PREPARE LOCAL PULL NO FF ========================')
    x.x('echo "Aigua" >> beguda.txt')
    x.x('git add beguda.txt')
    x.x('git commit -m "Beguda"')
    x.x('git lga # (1)!')

    x.log_file('stdout/remots/pull_no_ff_push_error.txt')
    print('==================== PULL NO FF PUSH ERROR ========================')
    x.x('git push')
    x.x('git fetch')
    x.x('git lga')

    x.log_file('stdout/remots/pull_ff_only_error.txt')
    print('==================== PULL FF ONLY ERROR ========================')
    x.x('git pull --ff-only')


def pull_no_ff():
    x.log_file('stdout/remots/pull_no_ff.txt')
    print('==================== PULL NO FF ========================')
    x.x('git pull --no-ff --no-edit # (1)!')
    x.x('git lga')


def pull_rebase():
    x.set_logging(False)
    print('==================== RESET PULL NO FF ========================')
    hash_beguda = x.run('git log --oneline --grep="^Beguda$"').split()[0]
    x.x(f'git reset --hard {hash_beguda}')

    x.set_logging(True)
    x.log_file('stdout/remots/pull_rebase.txt')
    print('==================== PULL REBASE ========================')
    x.run('git pull --rebase')
    x.log_prompt('git pull --rebase')
    x.log_output('Rebasing (1/1)\n')
    x.log_output('Successfully rebased and updated refs/heads/main.\n')
    x.x('git lga')




parser = argparse.ArgumentParser(description='Etiquetes')
parser.add_argument('-v', "--verbose", action='store_true')
parser.add_argument("--push", action='store_true')
parser.add_argument("--skip", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)

remove_repositori_if_exists()
init_repositori()

init_remote()

show_no_remote()
add_remote()

push_no_upstream()
push_upstream()

if not args.skip:
    print("Fes una captura de pantalla del repositori remot a GitHub i prem [Enter]")
    input()

clone()

if args.skip:
    prepare_fetch()
else:
    print("Realitza un canvi al repositori remot a GitHub i prem [Enter]")
    input()

fetch()

pull_ff()
prepare_remote_pull_no_ff()
prepare_local_pull_no_ff()
pull_no_ff()
pull_rebase()
