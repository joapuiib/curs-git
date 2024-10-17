#!/usr/bin/env python3

import os

import os
import subprocess
import re
import argparse

"""
@TODO:
    - Carriage return in output
    - lga remove timestamp
"""
class CommandExecutor:
    def __init__(self, user, host, file=None, verbose=False):
        self.user = user
        self.host = host
        self.home_dir = os.path.expanduser("~")
        self.workdir = os.getcwd()
        self.file = self.path_from_script(file) if file else None
        self.verbose = verbose
        self.logging = False


    def __str__(self):
        return f"x{{file={self.file}, logging={self.logging}}}"


    def set_logging(self, logging):
        self.logging = logging


    def set_file(self, file):
        self.file = self.path_from_script(file) if file else None


    def path_from_script(self, path):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(script_dir, path)


    def rm(self, filename):
        if os.path.exists(filename):
            os.remove(filename)


    def rm_file(self):
        if self.logging:
            self.rm(self.file)


    def log_file(self, file):
        self.file = None
        if self.logging:
            self.set_file(file)
            self.rm_file()


    def set_user(self, user):
        self.user = user


    def get_git_branch(self):
        try:
            git_tools_path = os.path.expanduser("~/usr/bin/git-prompt.sh")
            branch = subprocess.check_output(
                ["bash", "-c", f"source {git_tools_path} && __git_ps1"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
            return branch
        except subprocess.CalledProcessError as e:
            return ""


    def build_prompt(self):
        prompt = f"{self.user}@{self.host}:{self.workdir}"
        branch = self.get_git_branch()
        if branch:
            prompt += f" {branch}"
        prompt += " $"
        prompt = prompt.replace(self.home_dir, "~")
        return prompt


    def log_output(self, output):
        if self.logging and output:
            output = output.replace(self.home_dir, "~")
            if self.file:
                with open(self.file, "a") as f:
                    f.write(output)
            if self.verbose:
                print(output, end="")


    def run(self, cmd, env=None):
        args = cmd.split()
        if args[0] == "cd":
            if len(args) > 1:
                os.chdir(os.path.expanduser(args[1]))
            else:
                os.chdir(os.path.expanduser("~"))
            self.workdir = os.getcwd()
            return

        try:
            # Execute the command and capture stdout and stderr
            result = subprocess.run(cmd, capture_output=True, text=True, shell=True, executable="/bin/bash", env=env)
            output = result.stdout + result.stderr
        except FileNotFoundError:
            output = f"Command not found: {cmd}\n"

        output = output.replace(self.home_dir, "~")
        if output and not output.endswith("\n"):
            output += "\n"

        return output


    def log_prompt(self, cmd):
        prompt = self.build_prompt()
        output = f"{prompt} {cmd}\n"
        self.log_output(output)


    def x(self, cmd, env=None):
        self.log_prompt(cmd)

        output = self.run(cmd, env)

        self.log_output(output)


x = CommandExecutor(user='jpuigcerver', host='fp', verbose=False)
def develop_features():
    x.log_file('stdout/remot.txt')
    x.set_user('jpuigcerver')
    x.run('mkdir -p stdout')

    x.run('cd')
    x.run('rm -rf ~/gitflow')

    print('==================== REMOTE ========================')
    # Set up remote repository
    x.x('mkdir -p ~/gitflow/remot')
    x.x('cd ~/gitflow/remot')
    x.x('git init')
    x.x('git branch -m main')
    x.x('echo "# Estratègies de ramificació" > README.md')
    x.x('git add README.md')
    x.x('git commit -m "Commit inicial"')
    x.x('git lga')
    x.x('git config --bool core.bare true # (1)!')

    print('==================== DEVELOP ========================')

    # Development branch
    x.log_file('stdout/development.txt')

    x.x('git branch develop')
    x.x('git lga')

    print('==================== CLONE ========================')
    # Clone repository
    x.log_file('stdout/clone.txt')

    x.x('cd ~/gitflow')
    x.x('git clone remot anna')
    x.x('git clone remot pau')
    x.x('git clone remot mar')
    x.x('git clone remot carles')
    x.x('tree .')

    print('================== FEATURE/README ====================')
    # Anna `feature/readme`
    x.log_file('stdout/feature_readme.txt')
    x.set_user('anna')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
    x.x('git config user.name "Anna"')
    x.x('git config user.email "anna@fpmislata.com"')
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
    x.x('git lga')

    print('================== FEATURE/LICENSE ====================')
    # Pau `feature/license`
    x.log_file('stdout/feature_license.txt')
    x.set_user('pau')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/pau')
    x.x('git config user.name "Pau"')
    x.x('git config user.email "pau@fpmislata.com"')
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
    x.x('git lga')

    print('================== FEATURE/AUTHOR ====================')
    # Mar `feature/author`
    x.log_file('stdout/feature_author.txt')
    x.set_user('mar')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/mar')
    x.x('git config user.name "Mar"')
    x.x('git config user.email "mar@fpmislata.com"')
    x.x('git checkout develop')
    x.x('git checkout -b feature/author')
    x.x('echo "" >> README.md')
    x.x('echo "## Autors" >> README.md')
    x.x('git commit -a -m "README.md: Secció d\'autors"')
    x.x('echo "- Anna (anna@fpmislata.com)" >> README.md')
    x.x('git commit -a -m "Autors: Anna"')
    x.x('echo "- Pau (pau@fpmislata.com)" >> README.md')
    x.x('git commit -a -m "Autors: Pau"')
    x.x('echo "- Mar (mar@fpmislata.com)" >> README.md')
    x.x('git commit -a -m "Autors: Mar"')
    x.x('git push -u origin feature/author')
    x.x('git lga')

    print('================== ESTAT INICIAL ====================')
    # Estat remot
    x.log_file('stdout/branques.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/remot')
    x.x('git lga')

def squash():
    print('================== SQUASH: MERGE FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.log_file('stdout/feature_readme_fetch.txt')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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
    x.x('git merge --squash feature/readme')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/pau')
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
    x.x('git merge --squash feature/license')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/mar')
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
    x.log_prompt('vim README.md # (2)!')
    x.x('git add README.md')
    x.x('git commit --no-edit # (1)!', env={'GIT_EDITOR': 'true'})
    x.x('git lga')

    ## 4. Integrar feature/author a develop
    x.log_file('stdout/feature_author_merge_squash.txt')

    x.x('git checkout develop')
    x.x('git merge --squash feature/author')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/remot')
    x.x('git lga')

def merge_no_ff():
    print('================== MERGE NO FF: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/pau')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/mar')
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
    x.log_prompt('vim README.md # (2)!')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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

    print('================== MERGE NO FF: FINAL ====================')
    x.log_file('stdout/merge_no_ff_final.txt')
    x.set_user('jpuigcerver')

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/remot')
    x.x('git lga')

def rebase():
    print('================== REBASE: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/pau')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/mar')
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
    x.log_prompt('vim README.md # (2)!')
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
    x.log_prompt('vim README.md # (2)!')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/remot')
    x.x('git lga')

def rebase_merge_no_ff():
    print('================== REBASE MERGE NO FF: FEATURE/README ====================')
    # Integració de feature/readme
    x.set_user('anna')

    ## 1. Sincronitzar l'estat
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/pau')
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
    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/mar')
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
    x.log_prompt('vim README.md # (2)!')
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
    x.log_prompt('vim README.md # (2)!')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/anna')
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

    x.run('cd ~/gitflow/')
    x.x('cd ~/gitflow/remot')
    x.x('git lga')

parser = argparse.ArgumentParser(description='Estratègies de ramificació')
parser.add_argument('action', choices=['squash', 'merge_no_ff', 'rebase', 'rebase_merge_no_ff'], help='Acció a executar')
parser.add_argument('-v', "--verbose", action='store_true')
args = parser.parse_args()


if args.verbose:
    x.verbose = True

if args.action == 'squash':
    x.set_logging(True)
    develop_features()
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
