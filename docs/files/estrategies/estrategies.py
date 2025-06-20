#!/usr/bin/env python3

import argparse
import sys
import os

# Add the parent directory of estrategies.py to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from command_executor import CommandExecutor

x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False, script_path=__file__)

def develop_features():
    x.log_file('stdout/remot.txt')
    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout')

    x.run('cd')
    x.run('rm -rf ~/git_estrategies')

    # @TODO: remove directory if exists bash script
    x.log_bash('# Elimina els repositoris si existeixen')
    x.log_bash('if [ -d ~/git_estrategies ]; then')
    x.log_bash('    rm -rf ~/git_estrategies')
    x.log_bash('fi')
    x.log_bash('')

    print('==================== REMOTE ========================')
    # Set up remote repository
    x.log_bash('# Inicialització del repositori remot')
    x.x('mkdir -p ~/git_estrategies/remot')
    x.x('cd ~/git_estrategies/remot')
    x.x('git init')
    x.x('git branch -m main')
    x.x('echo "# Estratègies de ramificació" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git lga', bash=False)
    x.x('git config --bool core.bare true # (1)!')
    x.log_bash("")

    print('==================== DEVELOP ========================')

    # Development branch
    x.log_file('stdout/development.txt')

    x.log_bash('# Inicialització del repositori de desenvolupament')
    x.x('git branch develop')
    x.x('git lga', bash=False)
    x.log_bash('')

    print('==================== CLONE ========================')
    # Clone repository
    x.log_file('stdout/clone.txt')

    x.log_bash('# Clonació del repositori')
    x.x('cd ~/git_estrategies')
    x.x('git clone remot anna')
    x.x('git clone remot pau')
    x.x('git clone remot mar')
    x.x('git clone remot carles')
    x.x('tree .', bash=False)
    x.log_bash('')

    print('================== FEATURE/README ====================')
    # Anna `feature/readme`
    x.log_file('stdout/feature_readme.txt')
    x.set_user('anna')

    x.log_bash('# Desenvolupament de la branca feature/readme')
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git config user.name "Anna"')
    x.x('git config user.email "anna@alu.edu.gva.es"')
    x.x('git checkout develop')
    x.x('git checkout -b feature/readme')
    x.x('echo "Les estratègies de ramificació proporcionen un" >> README.md')
    x.x('echo "marc de treball organitzat que facilita la col·laboració" >> README.md')
    x.x('echo "entre diferents desenvolupadors en un mateix projecte" >> README.md')
    x.x('git commit -a -m "README.md: Descripció"')
    x.x('echo "" >> README.md')
    x.x('echo "La característica principal és la utilització" >> README.md')
    x.x('echo "de branques amb un únic propòsit." >> README.md')
    x.x('git commit -a -m "README.md: Branques propòsit únic"')
    x.x('git push -u origin feature/readme')
    x.x('git lga', bash=False)
    x.log_bash('')

    print('================== FEATURE/LICENSE ====================')
    # Pau `feature/license`
    x.log_file('stdout/feature_license.txt')
    x.set_user('pau')

    x.log_bash('# Desenvolupament de la branca feature/license')
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/pau')
    x.x('git config user.name "Pau"')
    x.x('git config user.email "pau@alu.edu.gva.es"')
    x.x('git checkout develop')
    x.x('git checkout -b feature/license')
    x.x('echo "" > LICENSE')
    x.x('echo "## Llicència" >> LICENSE')
    x.x('echo "CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional" >> LICENSE')
    x.x('git add LICENSE')
    x.x('git commit -m "LICENSE: Afegida llicència"')
    x.x('echo "" >> LICENSE')
    x.x('echo "Més informació: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE')
    x.x('git commit -a -m "LICENSE: Enllaç a la llicència"')
    x.x('git push -u origin feature/license')
    x.x('git lga', bash=False)
    x.log_bash('')

    print('================== FEATURE/AUTHOR ====================')
    # Mar `feature/author`
    x.log_file('stdout/feature_author.txt')
    x.set_user('mar')

    x.log_bash('# Desenvolupament de la branca feature/author')
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/mar')
    x.x('git config user.name "Mar"')
    x.x('git config user.email "mar@alu.edu.gva.es"')
    x.x('git checkout develop')
    x.x('git checkout -b feature/author')
    x.x('echo "" >> README.md')
    x.x('echo "## Autors" >> README.md')
    x.x('git commit -a -m "README.md: Secció d\'autors"')
    x.x('echo "- Anna (anna@alu.edu.gva.es)" >> README.md')
    x.x('git commit -a -m "Autors: Anna"')
    x.x('echo "- Pau (pau@alu.edu.gva.es)" >> README.md')
    x.x('git commit -a -m "Autors: Pau"')
    x.x('echo "- Mar (mar@alu.edu.gva.es)" >> README.md')
    x.x('git commit -a -m "Autors: Mar"')
    x.x('git push -u origin feature/author')
    x.x('git lga', bash=False)
    x.log_bash('')

    print('================== ESTAT INICIAL ====================')
    # Estat remot
    x.log_file('stdout/branques.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/remot', bash=False)
    x.x('git lga', bash=False)
    x.log_bash('cd ~/git_estrategies')

def squash():
    print('================== SQUASH: MERGE FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.log_file('stdout/feature_readme_fetch.txt')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.log_file('stdout/feature_readme_pull.txt')

    x.x('git checkout develop')
    x.x('git pull --ff-only')

    ## 3. Sincronitzar feature amb develop
    x.log_file('stdout/feature_readme_merge.txt')

    x.x('git checkout feature/readme')
    x.x('git merge --no-ff --no-edit develop #(1)!')

    ## 4. Integrar feature/readme a develop
    x.log_file('stdout/feature_readme_merge_squash.txt')

    x.x('git checkout develop')
    x.x('git merge --squash --ff-only feature/readme')
    x.x('git status')
    x.x('git diff --staged')
    x.x('git commit -m "Merge branch \'feature/readme\'"')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.log_file('stdout/feature_readme_push.txt')

    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/readme
    x.log_file('stdout/feature_readme_delete.txt')

    x.x('git branch -D feature/readme')
    x.x('git push origin --delete feature/readme')
    x.x('git lga')

    print('================== SQUASH: MERGE FEATURE/LICENSE ====================')
    # Integració de feature/license
    x.set_user('pau')

    ## 1. Sincronitzar l'estat
    x.log_file('stdout/feature_license_fetch.txt')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/pau')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.log_file('stdout/feature_license_pull.txt')

    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.log_file('stdout/feature_license_merge.txt')

    x.x('git checkout feature/license')
    x.x('git merge --no-ff --no-edit develop # (1)!')
    x.x('git lga')

    ## 4. Integrar feature/license a develop
    x.log_file('stdout/feature_license_merge_squash.txt')

    x.x('git checkout develop')
    x.x('git merge --squash --ff-only feature/license')
    x.x('git status')
    x.x('git diff --staged')
    x.x('git commit -m "Merge branch \'feature/license\'"')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.log_file('stdout/feature_license_push.txt')

    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/license
    x.log_file('stdout/feature_license_delete.txt')

    x.x('git branch -D feature/license')
    x.x('git push origin --delete feature/license')
    x.x('git lga')

    print('================== SQUASH: MERGE FEATURE/AUTHOR ====================')
    # Integració de feature/author
    x.set_user('mar')

    ## 1. Sincronitzar l'estat
    x.log_file('stdout/feature_author_fetch.txt')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/mar')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.log_file('stdout/feature_author_pull.txt')

    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.log_file('stdout/feature_author_merge.txt')

    x.x('git checkout feature/author')
    x.x('git merge --no-ff --no-edit develop # (1)!')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git commit --no-edit # (1)!', env={'GIT_EDITOR': 'true'})
    x.x('git lga')

    ## 4. Integrar feature/author a develop
    x.log_file('stdout/feature_author_merge_squash.txt')

    x.x('git checkout develop')
    x.x('git merge --squash --ff-only feature/author')
    x.x('git status')
    x.x('git diff --staged')
    x.x('git commit -m "Merge branch \'feature/author\'"')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.log_file('stdout/feature_author_push.txt')

    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/author
    x.log_file('stdout/feature_author_delete.txt')

    x.x('git branch -D feature/author')
    x.x('git push origin --delete feature/author')
    x.x('git lga')

    print('================== SQUASH: RELEASE ====================')
    x.log_file('stdout/release_pull.txt')
    x.set_user('anna')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git checkout develop')
    x.x('git fetch --prune')
    x.x('git pull --ff-only')
    x.x('git lga')

    x.log_file('stdout/release_create.txt')

    x.x('git checkout -b release/v1.0.0')
    x.x('git lga')

    x.log_file('stdout/release.txt')

    x.x('echo "v1.0.0" > VERSION')
    x.x('git add VERSION')
    x.x('git commit -m "Publicada versió: v1.0.0"')
    x.x('git lga')

    x.log_file('stdout/release_merge_develop.txt')

    x.x('git checkout develop')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.log_file('stdout/release_merge_main.txt')

    x.x('git checkout main')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.log_file('stdout/release_tag.txt')

    x.x('git tag v1.0.0')
    x.x('git push --tags')
    x.x('git lga')

    x.log_file('stdout/release_delete.txt')

    x.x('git branch -D release/v1.0.0')
    x.x('git push origin --delete release/v1.0.0')
    x.x('git lga')

    print('================== SQUASH: FINAL ====================')
    x.log_file('stdout/squash_final.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/remot')
    x.x('git lga')

def merge_no_ff():
    print('================== MERGE NO FF: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')

    ## 4. Integrar feature/readme a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/readme')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/readme
    x.x('git branch -D feature/readme')
    x.x('git push origin --delete feature/readme')
    x.x('git lga')

    print('================== MERGE NO FF: FEATURE/LICENSE ====================')
    # Integració de feature/license
    x.set_user('pau')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/pau')
    x.x('git fetch --prune')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 4. Integrar feature/license a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/license')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/license
    x.x('git branch -D feature/license')
    x.x('git push origin --delete feature/license')
    x.x('git lga')

    print('================== MERGE NO FF: FEATURE/AUTHOR ====================')
    # Integració de feature/author
    x.set_user('mar')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/mar')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 4. Integrar feature/author a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/author')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git commit --no-edit # (1)!')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/author
    x.x('git branch -D feature/author')
    x.x('git push origin --delete feature/author')
    x.x('git lga')

    print('================== MERGE NO FF: RELEASE ====================')
    x.set_user('anna')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git checkout develop')
    x.x('git fetch --prune')
    x.x('git pull --ff-only')
    x.x('git lga')

    x.x('git checkout -b release/v1.0.0')
    x.x('git lga')

    x.x('echo "v1.0.0" > VERSION')
    x.x('git add VERSION')
    x.x('git commit -m "Publicada versió: v1.0.0"')
    x.x('git lga')

    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git checkout main')
    x.x('git merge --no-ff --no-edit release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git tag v1.0.0')
    x.x('git push --tags')
    x.x('git lga')

    x.x('git branch -D release/v1.0.0')
    x.x('git push origin --delete release/v1.0.0')
    x.x('git lga')

    print('================== MERGE NO FF: FINAL ====================')
    x.log_file('stdout/merge_no_ff_final.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/remot')
    x.x('git lga')

def rebase():
    print('================== REBASE: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/readme')
    x.x('git rebase develop')

    ## 4. Integrar feature/readme a develop
    x.x('git checkout develop')
    x.x('git merge --ff-only feature/readme')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/readme
    x.x('git branch -D feature/readme')
    x.x('git push origin --delete feature/readme')
    x.x('git lga')

    print('================== REBASE: FEATURE/LICENSE ====================')
    # Integració de feature/license
    x.set_user('pau')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/pau')
    x.x('git fetch --prune')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/license')
    x.x('git rebase develop')

    ## 4. Integrar feature/license a develop
    x.x('git checkout develop')
    x.x('git merge --ff-only feature/license')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/license
    x.x('git branch -D feature/license')
    x.x('git push origin --delete feature/license')
    x.x('git lga')

    print('================== REBASE: FEATURE/AUTHOR ====================')
    # Integració de feature/author
    x.set_user('mar')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/mar')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/author')
    x.x('git rebase develop') ## Conflictes
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git rebase --continue', env={'GIT_EDITOR': 'true'})

    ## 4. Integrar feature/author a develop
    x.x('git checkout develop')
    x.x('git merge --ff-only feature/author')
    x.x('git lga')

    ## 4. Integrar feature/author a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/author')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git commit --no-edit # (1)!', env={'GIT_EDITOR': 'true'})
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/author
    x.x('git branch -D feature/author')
    x.x('git push origin --delete feature/author')
    x.x('git lga')

    print('================== REBASE: RELEASE ====================')
    x.set_user('anna')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git checkout develop')
    x.x('git fetch --prune')
    x.x('git pull --ff-only')
    x.x('git lga')

    x.x('git checkout -b release/v1.0.0')
    x.x('git lga')

    x.x('echo "v1.0.0" > VERSION')
    x.x('git add VERSION')
    x.x('git commit -m "Publicada versió: v1.0.0"')
    x.x('git lga')

    x.x('git checkout develop')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git checkout main')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git tag v1.0.0')
    x.x('git push --tags')
    x.x('git lga')

    x.x('git branch -D release/v1.0.0')
    x.x('git push origin --delete release/v1.0.0')
    x.x('git lga')

    print('================== REBASE: FINAL ====================')
    x.log_file('stdout/rebase_final.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/remot')
    x.x('git lga')

def rebase_merge_no_ff():
    print('================== REBASE MERGE NO FF: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/readme')
    x.x('git rebase develop')

    ## 4. Integrar feature/readme a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/readme')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/readme
    x.x('git branch -D feature/readme')
    x.x('git push origin --delete feature/readme')
    x.x('git lga')

    print('================== REBASE MERGE NO FF: FEATURE/LICENSE ====================')
    # Integració de feature/license
    x.set_user('pau')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/pau')
    x.x('git fetch --prune')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/license')
    x.x('git rebase develop')

    ## 4. Integrar feature/license a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/license')
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/license
    x.x('git branch -D feature/license')
    x.x('git push origin --delete feature/license')
    x.x('git lga')

    print('================== REBASE MERGE NO FF: FEATURE/AUTHOR ====================')
    # Integració de feature/author
    x.set_user('mar')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/mar')
    x.x('git fetch')
    x.x('git lga')

    ## 2. Incorporar els canvis
    x.x('git checkout develop')
    x.x('git pull --ff-only')
    x.x('git lga')

    ## 3. Sincronitzar feature amb develop
    x.x('git checkout feature/author')
    x.x('git rebase develop') ## Conflictes
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git rebase --continue', env={'GIT_EDITOR': 'true'})

    ## 4. Integrar feature/author a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/author')
    x.x('git lga')

    ## 4. Integrar feature/author a develop
    x.x('git checkout develop')
    x.x('git merge --no-ff --no-edit feature/author')
    x.run('sed -i \'/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d\' README.md')
    x.log_prompt('code README.md # (2)!')
    x.x('git add README.md')
    x.x('git commit --no-edit # (1)!', env={'GIT_EDITOR': 'true'})
    x.x('git lga')

    ## 5. Pujar els canvis
    x.x('git push')
    x.x('git lga')

    ## 6. Eliminar la branca feature/author
    x.x('git branch -D feature/author')
    x.x('git push origin --delete feature/author')
    x.x('git lga')

    print('================== REBASE MERGE NO FF: RELEASE ====================')
    x.set_user('anna')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/anna')
    x.x('git checkout develop')
    x.x('git fetch --prune')
    x.x('git pull --ff-only')
    x.x('git lga')

    x.x('git checkout -b release/v1.0.0')
    x.x('git lga')

    x.x('echo "v1.0.0" > VERSION')
    x.x('git add VERSION')
    x.x('git commit -m "Publicada versió: v1.0.0"')
    x.x('git lga')

    x.x('git checkout develop')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git checkout main')
    x.x('git merge --ff-only release/v1.0.0')
    x.x('git push')
    x.x('git lga')

    x.x('git tag v1.0.0')
    x.x('git push --tags')
    x.x('git lga')

    x.x('git branch -D release/v1.0.0')
    x.x('git push origin --delete release/v1.0.0')
    x.x('git lga')

    print('================== REBASE MERGE NO FF: FINAL ====================')
    x.log_file('stdout/rebase_merge_no_ff_final.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/git_estrategies/')
    x.x('cd ~/git_estrategies/remot')
    x.x('git lga')

parser = argparse.ArgumentParser(description='Estratègies de ramificació')
parser.add_argument('action', choices=['squash', 'merge_no_ff', 'rebase', 'rebase_merge_no_ff'], help='Acció a executar')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

if args.action == 'squash':
    x.set_logging(True)
    x.log_bash_file('stdout/estrategies_development.sh')
    develop_features()
    x.log_bash_file(None)
    squash()

elif args.action == 'merge_no_ff':
    x.set_logging(False)
    develop_features()
    x.set_logging(True)
    merge_no_ff()

elif args.action == 'rebase':
    x.set_logging(False)
    develop_features()
    x.set_logging(True)
    rebase()

elif args.action == 'rebase_merge_no_ff':
    x.set_logging(False)
    develop_features()
    x.set_logging(True)
    rebase_merge_no_ff()
