#!/bin/bash

function print {
    GREEN="\033[0;32m"
    RESET="\033[0m"
    echo -e "${GREEN}$1${RESET}"
}
function print_error {
    RED="\033[0;31m"
    RESET="\033[0m"
    echo -e "${RED}$1${RESET}"
}
VENV_DIR=".venv"
GENERATOR="properdocs"

BUILD=0
CI=0
INSTALL_VENV=0
UPGRADE=0
SPELL=0
ACT=''
ALL=0
SPELL_SOURCES=''
COPILOT=0
SKIP=0

ARGS=''
SPELL_ARGS=''
while [ $# -gt 0 ] ; do
    case $1 in
        -b | --build)
            BUILD=1
            ;;
        --ci)
            CI=1
            ;;
        -i | --install-venv)
            INSTALL_VENV=1
            ;;
        -u | --upgrade)
            UPGRADE=1
            ;;
        --spell)
            BUILD=1
            SPELL=1
            ARGS="$ARGS --clean"
            ;;
        --source | -S)
            SPELL_SOURCES="$SPELL_SOURCES -S $2"
            shift
            ;;
        --all)
            ALL=1
            ;;
        --skip)
            SKIP=1
            ;;
        --copilot)
            COPILOT=1
            ;;
        --act)
            ACT=$2
            if [ -z "$ACT" ]; then
                print "Missing workflow name."
                exit 1
            fi
            shift
            ;;
        *)
            ARGS="$ARGS $1"
            ;;
    esac
    shift
done

if [ -n "$ACT" ]; then
    if ! which act &>/dev/null; then
        print_error "act not found."
        exit 1
    fi
    if [ ! -f ".github/workflows/$ACT" ]; then
        print_error "Workflow $ACT not found."
        exit 1
    fi
    act -W .github/workflows/$ACT
    exit
fi

if [ ! -d "$VENV_DIR" ]; then
    INSTALL_VENV=1
    print "Virtual environment not found."
fi

if [ $INSTALL_VENV -eq 1 ]; then
    if [ -d "$VENV_DIR" ]; then
        print "Removing existing virtual environment..."
        rm -rf $VENV_DIR
    fi

    print "Installing virtual environment..."
    python3 -m venv $VENV_DIR
    print "Installing dependencies"
    $VENV_DIR/bin/pip install -r requirements.txt
elif [ $UPGRADE -eq 1 ]; then
    print "Upgrading dependencies..."
    $VENV_DIR/bin/pip install --upgrade -r requirements.txt
fi

source $VENV_DIR/bin/activate

COMMAND="serve --livereload"
if [ $BUILD -eq 1 ]; then
    COMMAND="build"
fi

if [ $CI -eq 0 ]; then
    $GENERATOR $COMMAND $ARGS
else
    CI=true $GENERATOR $COMMAND $ARGS
fi
if [ $? -ne 0 ]; then
    print "Error building site."
    exit 1
fi

if [ $SPELL -eq 1 ]; then
    export DICPATH=.hunspell/
    print "Checking spelling..."
    mkdir -p .hunspell

    if ! which hunspell &>/dev/null; then
        print_error "hunspell not found"
        echo "    sudo apt install hunspell"
        exit 1
    fi

    if ! python -c 'import pyspelling' 2>/dev/null; then
        print "Installing pyspelling..."
        pip install pyspelling
    fi

    if [ ! -f .hunspell/ca_ES_valencia.dic ]; then
        print "Downloading ca_ES_valencia dictionary..."
        curl -L https://raw.githubusercontent.com/Softcatala/catalan-dict-tools/refs/heads/master/resultats/hunspell/catalan-valencia.dic -o .hunspell/ca_ES_valencia.dic
    fi
    if [ ! -f .hunspell/ca_ES_valencia.aff ]; then
        print "Downloading ca_ES_valencia affix file..."
        curl -L https://raw.githubusercontent.com/Softcatala/catalan-dict-tools/refs/heads/master/resultats/hunspell/catalan-valencia.aff -o .hunspell/ca_ES_valencia.aff
    fi

    if [ $ALL -eq 0 ]; then
        if [ -z "$SPELL_SOURCES" ]; then
            CHANGED_FILES_FROM_MAIN=$(git diff --name-only main HEAD)
            CHANGED_UNCOMMITED_FILES=$(git status --porcelain | grep '\.md$' | awk '{print $2}')
            SPELL_SOURCES=$(echo -e "${CHANGED_FILES_FROM_MAIN}\n${CHANGED_UNCOMMITED_FILES}")
            if [ -z "$SPELL_SOURCES" ]; then
                print "No changes found."
                exit
            fi
        fi
        SPELL_SOURCES=$(echo "$SPELL_SOURCES" | grep 'docs/.*\.md$' | sed 's/\/index//' | sed 's/docs/site/' | sed 's/.md$/\/index.html/')

        for FILE in $SPELL_SOURCES; do
            if [ -f $FILE ]; then
                SOURCES="$SOURCES -S $FILE"
            fi
        done
        SPELL_ARGS="$SPELL_ARGS --name docs $SOURCES"
    fi

    SPELLING_OK=0
    if [ $SKIP -eq 1 -a -f pyspelling.log ]; then
        print "Skipping spelling check. Using previous results from pyspelling.log"
        SPELLING_OK=1
    else
        print "Running pyspelling..."
        echo "pyspelling $SPELL_ARGS"
        pyspelling $SPELL_ARGS | tee pyspelling.log
        SPELLING_OK=${PIPESTATUS[0]}
    fi
    if [ $SPELLING_OK -ne 0 ]; then
        if [ $COPILOT -eq 1 ]; then
            print "Running copilot for fixing spell..."
            if ! which copilot &>/dev/null; then
                print_error "copilot not found"
                exit 1
            fi
            if [ ! -f docs/_prompts/fix-spelling.md ]; then
                print_error "Prompt file not found: docs/_prompts/fix-spelling.md"
                exit 1
            fi
            if [ ! -f pyspelling.log ]; then
                print "File pyspelling.log not found, nothing to fix."
                exit 0
            fi
            copilot --allow-all-tools < docs/_prompts/fix-spelling.md
        else
            less pyspelling.log
        fi
    fi
fi
