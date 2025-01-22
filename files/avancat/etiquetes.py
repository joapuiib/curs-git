#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def remove_repositori_if_exists():
    x.run('rm -rf ~/git_etiquetes')

def init_repositori():
    x.log_file('stdout/etiquetes/inicial.txt')
    x.log_bash_file('stdout/etiquetes/setup.sh')
    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout/etiquetes')

    # remove directory if exists bash script
    x.log_bash('# Elimina els repositori si existeix')
    x.log_bash('if [ -d ~/git_etiquetes ]; then')
    x.log_bash('    rm -rf ~/git_etiquetes')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== INICIAL ========================')
    x.run('cd')
    x.x('mkdir -p ~/git_etiquetes')
    x.x('cd ~/git_etiquetes')
    x.x('git init')
    x.run('git config user.email "j.puigcerveribanez@edu.gva.es"')
    x.x('git branch -m main')
    x.x('echo "# Etiquetes" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('echo "Repositori d\'exemple amb etiquetes" >> README.md')
    x.x('git commit -a -m "README: Descripció"')
    x.x('echo "" >> README.md')
    x.x('echo "## Tipus de etiquetes" >> README.md')
    x.x('git commit -a -m "README: Apartat tipus de etiquetes"')
    x.x('echo "Existeixen dos tipus de etiquetes: anotades i lleugeres" >> README.md')
    x.x('git commit -a -m "README: Descripció tipus de etiquetes"')
    x.x('git lga')

    x.log_bash_file(None)

def crear_etiqueta_anotada():
    x.log_file('stdout/etiquetes/etiqueta_anotada.txt')

    hash_v1 = x.run('git log --oneline --grep="^Commit inicial$"').split()[0]
    hash_v2 = x.run('git log --oneline --grep="^README: Apartat tipus de etiquetes$"').split()[0]

    print('==================== ETIQUETA ANOTADA ========================')
    x.x(f"git tag -a v1.0.0 -m \"Primera versió: v1.0.0\" {hash_v1}")
    x.x(f"git tag -a v2.0.0 -m \"Versió: v2.0.0\" {hash_v2}")
    x.x('git lga')

def crear_etiqueta_lleugera():
    x.log_file('stdout/etiquetes/etiqueta_lleugera.txt')

    hash_v11 = x.run('git log --oneline --grep="^README: Descripció$"').split()[0]

    print('==================== ETIQUETA LLEUGERA ========================')
    x.x(f"git tag v1.1.0 {hash_v11}")
    x.x('git tag v2.1.0')
    x.x('git lga')

def llistar_etiquetes():
    x.log_file('stdout/etiquetes/llista.txt')

    print('==================== LLISTAR ETIQUETES ========================')
    x.x('git tag')

def llistar_etiquetes_patro():
    x.log_file('stdout/etiquetes/llista_patro.txt')

    print('==================== LLISTAR ETIQUETES ========================')
    x.x('git tag -l "v2.*"')

def info_etiqueta_anotada():
    x.log_file('stdout/etiquetes/info_etiqueta_anotada.txt')

    print('==================== INFO ETIQUETA ANOTADA ========================')
    x.x('git show v1.0.0')

def info_etiqueta_lleugera():
    x.log_file('stdout/etiquetes/info_etiqueta_lleugera.txt')

    print('==================== INFO ETIQUETA LLEUGERA ========================')
    x.x('git show v1.1.0')

def elminar_etiqueta_llugera():
    x.log_file('stdout/etiquetes/eliminar_etiqueta.txt')

    print('==================== ELIMINAR ETIQUETA ========================')
    x.x('git tag -d v1.1.0')
    x.x('git tag')
    x.x('git lga')

def preparacio_remot():
    x.log_file('stdout/etiquetes/preparacio_remot.txt')

    print('==================== PREPARACIÓ REMOT ========================')
    x.x('git remote add origin git@github.com:joapuiib/cursgit_etiquetes.git')
    x.x('git push -u origin main')
    x.x('git lga')

def push_etiquetes():
    x.log_file('stdout/etiquetes/push_etiquetes.txt')

    print('==================== PUSH ETIQUETES ========================')
    x.x('git push origin --tags')


parser = argparse.ArgumentParser(description='Etiquetes')
parser.add_argument('-v', "--verbose", action='store_true')
parser.add_argument("--push", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

x.set_logging(True)
remove_repositori_if_exists()
init_repositori()

crear_etiqueta_anotada()
crear_etiqueta_lleugera()

llistar_etiquetes()
llistar_etiquetes_patro()

info_etiqueta_anotada()
info_etiqueta_lleugera()

elminar_etiqueta_llugera()

if args.push:
    preparacio_remot()
    push_etiquetes()
