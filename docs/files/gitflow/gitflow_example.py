#!/usr/bin/env python3

import os

import os
import subprocess
import re

class CommandExecutor:
    def __init__(self, user, host, file=None):
        self.user = user
        self.host = host
        self.home_dir = os.path.expanduser("~")
        self.workdir = os.getcwd()
        # @TODO file is always relative to script path
        self.file = self.path_from_script(file) if file else None


    def set_file(self, file):
        self.file = self.path_from_script(file) if file else None


    def path_from_script(self, path):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(script_dir, path)


    def rm_file(self):
        self.rm(self.file)


    def set_user(self, user):
        self.user = user


    def get_git_branch(self):
        try:
            branch = subprocess.check_output(
                ["git", "symbolic-ref", "--short", "HEAD"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()
            return branch
        except subprocess.CalledProcessError:
            return ""


    def build_prompt(self):
        prompt = f"{self.user}@{self.host}:{self.workdir}"
        branch = self.get_git_branch()
        if branch:
            prompt += f" ({branch})"
        prompt += " $"
        prompt = prompt.replace(self.home_dir, "~")
        return prompt


    def log_output(self, output):
        if output:
            output = output.replace(self.home_dir, "~")
            if self.file:
                with open(self.file, "a") as f:
                    f.write(output)
            print(output, end="")


    def run(self, cmd):
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
            result = subprocess.run(cmd, capture_output=True, text=True, shell=True, executable="/bin/bash")
            output = result.stdout + result.stderr
        except FileNotFoundError:
            output = f"Command not found: {cmd}\n"

        output = output.replace(self.home_dir, "~")
        if output and not output.endswith("\n"):
            output += "\n"
        return output


    def x(self, cmd):
        prompt = self.build_prompt()
        log_entry = f"{prompt} {cmd}\n"
        self.log_output(log_entry)

        output = self.run(cmd)

        self.log_output(output)


    def rm(self, filename):
        if os.path.exists(filename):
            os.remove(filename)


x = CommandExecutor(user='jpuigcerver', host='fp')
x.set_file('stdout/remot.txt')
x.rm_file()
x.run('mkdir -p stdout')

x.run('cd')
x.run('rm -rf ~/gitflow')

# Set up remote repository
x.x('mkdir -p ~/gitflow/remot')
x.x('cd ~/gitflow/remot')
x.x('git init')
x.x('git branch -m main')
x.x('echo "# Gitflow" > README.md')
x.x('git add README.md')
x.x('git commit -m "1. Primer commit"')
x.x('git lga')
x.x('git config --bool core.bare true # (1)!')

print('===================================================')

# Development branch
x.set_file('stdout/development.txt')
x.rm_file()

x.x('git branch develop')
x.x('git lga')

print('===================================================')
# Clone repository
x.set_file('stdout/clone.txt')
x.rm_file()

x.x('cd ~/gitflow')
x.x('git clone remot anna')
x.x('git clone remot pau')
x.x('git clone remot mar')
x.x('git clone remot carles')
x.x('tree .')

print('===================================================')
# Anna `feature/readme`
x.set_file('stdout/feature_readme.txt')
x.rm_file()
x.set_user('anna')

x.run('cd ~/gitflow/')
x.x('cd ~/gitflow/anna')
x.x('git config user.name "Anna"')
x.x('git config user.email "anna@fpmislata.com"')
x.x('git checkout develop')
x.x('git checkout -b feature/readme')
x.x('echo "Gitflow és una estratègia de ramificació per a Git," >> README.md')
x.x('echo "que proporciona un marc de treball organitzat que" >> README.md')
x.x('echo "facilita la col·laboració entre diferents desenvolupadors" >> README.md')
x.x('echo "en un mateix projecte." >> README.md')
x.x('git commit -a -m "2. Afegida descripció del projecte"')
x.x('git push')
x.x('git lga')

print('===================================================')
# Pau `feature/license`
x.set_file('stdout/feature_license.txt')
x.rm_file()
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
x.x('echo "" >> LICENSE')
x.x('echo "Més informació: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE')
x.x('git add LICENSE')
x.x('git commit -m "3. Afegida llicència"')
x.x('git push')
x.x('git lga')

print('===================================================')
# Mar `feature/author`
x.set_file('stdout/feature_author.txt')
x.rm_file()
x.set_user('mar')

