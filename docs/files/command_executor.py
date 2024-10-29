import os
import subprocess
import re

"""
@TODO:
    - Carriage return in output
    - lga remove timestamp
"""
class CommandExecutor:
    def __init__(self, user, host, file=None, verbose=False, script_path=None):
        self.user = user
        self.host = host
        self.home_dir = os.path.expanduser("~")
        self.workdir = os.getcwd()
        self.file = self.path_from_script(file) if file else None
        self.verbose = verbose
        self.logging = False
        self.script_dir = os.path.dirname(os.path.realpath(script_path or __file__))

        # File to log the commands in a bash script
        self.bash_file = None


    def __str__(self):
        return f"x{{file={self.file}, logging={self.logging}}}"


    def set_logging(self, logging):
        self.logging = logging


    def set_file(self, file):
        self.file = self.path_from_script(file) if file else None


    def path_from_script(self, path):
        return os.path.join(self.script_dir, path)


    def rm(self, filename):
        if os.path.exists(filename):
            os.remove(filename)


    def rm_file(self):
        if self.logging:
            self.rm(self.file)


    def log_file(self, file):
        self.file = None
        if self.logging and file:
            self.set_file(file)
            self.rm_file()


    def log_bash_file(self, file):
        self.bash_file = None
        if self.logging and file:
            self.bash_file = self.path_from_script(file)
            self.rm(self.bash_file)
            self.log_bash_header()


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


    def log_prompt(self, cmd):
        prompt = self.build_prompt()
        output = f"{prompt} {cmd}\n"
        self.log_output(output)


    def log_bash(self, cmd):
        if self.logging and self.bash_file:
            with open(self.bash_file, "a") as f:
                f.write(f"{cmd}\n")


    def log_bash_header(self):
        header = f"#!/bin/bash\n"
        self.log_bash(header)


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


    def x(self, cmd, env=None, bash=True):
        self.log_prompt(cmd)
        output = self.run(cmd, env)
        self.log_output(output)

        if bash:
            self.log_bash(cmd)

    def swap_conflictes(self, filename):
        with open(filename, "r+") as f:
            content = f.read()
            content = re.sub(r"<<<<<<< HEAD\n(.*?)=======\n(.*?)>>>>>>> (.*?)\n", r"\2\1", content, flags=re.DOTALL)
            f.seek(0)
            f.write(content)
            f.truncate()


    def log_file_content(self, filename, log_filename):
        with open(filename, "r") as f:
            content = f.read()
            log_file = os.path.join(self.script_dir, log_filename)
            with open(log_file, "w") as lf:
                lf.write(content)
