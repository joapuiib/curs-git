#!/bin/bash
# Stop script on error
set -e 

if [ -d ~/gitflow ]; then
    rm -rf ~/gitflow
fi
mkdir -p stdout
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Prompt is @u/@h:@w (branch) $
user="jpuigcerver"
host="fp"
workdir="~"
branch=""

file=""

home_dir=$HOME

function rmi() {
    if [ -f "$1" ]; then
        rm "$1"
    fi
}

# @TODO: redirections
function x() {
    prompt="$user@$host:$workdir"
    branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)
    if [ -n "$branch" ]; then
        prompt="$prompt ($branch)"
    fi
    prompt="$prompt \$"
    prompt=$(echo $prompt | sed "s|$home_dir|~|g")

    if [ -n "$file" ]; then
        echo "$prompt $@" | sed "s|$home_dir|~|g" | tee -a $file
    else
        echo "$prompt $@" | sed "s|$home_dir|~|g"
    fi

    # cd special case
    if [ "$1" = "cd" ]; then
        # Change directory in the current shell
        builtin cd "${@:2}"
        # Update workdir variable after changing directories
        workdir="$(pwd)"
        return  # Return so that it does not execute the next command
    fi

    output="$("$@" 2>&1)"  # Capture both stdout and stderr
    output=$(echo "$output" | sed "s|$home_dir|~|g")
    if [[ -n $output && "$output" != *$'\n' ]]; then
        output="$output"$'\n'
    fi


    if [ -n "$file" ]; then
        echo -n -e "$output" | tee -a $file
    else
        echo -n -e "$output"
    fi
}

cd ~

# Set up remote repository
file="$SCRIPTPATH/stdout/remot.txt"
rmi $file
x mkdir -p ~/gitflow/remot
x cd ~/gitflow/remot
x git init
x git branch -m main
x echo "# Gitflow" > README.md
x git add README.md
x git commit -m "1. Primer commit"
x git lga
x git config --bool core.bare true

echo "==================================================="

# Development branch
file="$SCRIPTPATH/stdout/development.txt"
rmi $file
x git branch develop
x git lga

echo "==================================================="

# Clone repository
file="$SCRIPTPATH/stdout/clone.txt"
rmi $file
x cd ~/gitflow
x git clone remot anna
x git clone remot pau
x git clone remot mar
x git clone remot carles
x tree .

echo "==================================================="

# Anna `feature/readme`
file="$SCRIPTPATH/stdout/feature_readme.txt"
rmi $file
user="anna"

cd ~/gitflow/
x cd ~/gitflow/anna
x git config user.name "Anna"
x git config user.email "anna@fpmislata.com"
x git checkout develop
x git checkout -b feature/readme
x echo "Gitflow és una estratègia de ramificació per a Git," >> README.md
x echo "que proporciona un marc de treball organitzat que" >> README.md
x echo "facilita la col·laboració entre diferents desenvolupadors" >> README.md
x echo "en un mateix projecte." >> README.md
x git commit -a -m "2. Afegida descripció del projecte"
x git push
x git lga

echo "==================================================="

# Pau `feature/license`
file="$SCRIPTPATH/stdout/feature_license.txt"
rmi $file
user="pau"

cd ~/gitflow/
workdir="~/gitflow"
x cd ~/gitflow/pau
x git config user.name "Pau"
x git config user.email "pau@fpmislata.com"
x git checkout develop
x git checkout -b feature/license
x echo "" >> LICENSE
x echo "## Llicència" >> LICENSE
x echo "CC BY-NC-SA 4.0 DEED - Reconeixement-NoComercial-CompartirIgual 4.0 Internacional" >> LICENSE
x echo "" >> LICENSE
x echo "Més informació: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ca" >> LICENSE
x git add LICENSE
x git commit -m "3. Afegida llicència"
x git push
x git lga

echo "==================================================="

# Mar `feature/author`
file="$SCRIPTPATH/stdout/feature_author.txt"
rmi $file
user="mar"

cd ~/gitflow/
workdir="~/gitflow"
x cd ~/gitflow/mar
x git config user.name "Mar"
x git config user.email "mar@fpmislata.com"
x git checkout develop
x git checkout -b feature/author
x echo "" >> README.md
x echo "## Autors" >> README.md
x echo "Anna, Pau, Mar i Carles" >> README.md
x git commit -a -m "4. Afegits autors"
x git push
x git lga

echo "==================================================="

# Carles `feature/documentacio`
file="$SCRIPTPATH/stdout/feature_documentacio.txt"
rmi $file
user="carles"

cd ~/gitflow/
workdir="~/gitflow"
x cd ~/gitflow/carles
x git config user.name "Carles"
x git config user.email "carles@fpmislata.com"
x git checkout develop
x git checkout -b feature/documentacio
x echo "" >> README.md
x echo "## Documentació" >> README.md
x echo "- https://git-scm.com/" >> README.md
x git commit -a -m "5. Afegida documentació"
x git push
x git lga

echo "==================================================="

# Estat remot
file="$SCRIPTPATH/stdout/branques.txt"
rmi $file
user="jpuigcerver"

cd ~/gitflow/
workdir="~/gitflow"
x cd ~/gitflow/remot
x git lga

echo "==================================================="
exit 0

# Anna: Integració amb `merge --no-ff`
cd ~/gitflow/anna
git fetch
git lga
git checkout develop
git pull
git merge --no-ff feature/readme --no-edit
git lga
git push
git lga

# Pau: Integració amb `rebase`
cd ~/gitflow/pau
git fetch
git checkout develop
git pull
git checkout feature/license
git rebase develop
git push -f
git checkout develop
git merge --ff-only feature/license
git push

# Mar: Integració amb `rebase` + `merge --no-ff`
cd ~/gitflow/mar
git fetch
git lga
git checkout develop
git pull
git lga
git checkout feature/author
git rebase develop || true # Evita que el script acabe per `set -e`
sed -i '/^<<<<<<<.*$/d; /^=======/d; /^>>>>>>>.*$/d' README.md # Elimina les marques de conflicte
git add README.md
GIT_EDITOR=true git rebase --continue
git push -f
git lga
git checkout develop
git merge --no-ff feature/author --no-edit
git lga
git push
git lga

# Carles: Integració amb `merge --squash`
cd ~/gitflow/carles
git fetch
git lga
git checkout develop
git pull
git lga
git checkout feature/documentacio
git rebase develop || true # Podria ser merge
# Solucionar conflictes canviant l'ordre del contingut
awk '
/^<<<<<<< HEAD$/ {in_head=1; next} 
/^=======$/ {in_head=0; next} 
/^>>>>>>> develop$/ {next} 
in_head {head_lines = head_lines $0 "\n"; next} 
{print $0} 
END {print head_lines}' README.md > README.md.tmp
mv README.md.tmp README.md
git add README.md
GIT_EDITOR=true git rebase --continue
git push -f
git lga
git checkout develop
git merge --squash feature/documentacio
git lga
git commit -m "Merge branch 'feature/documentacio'"
git push
git lga
