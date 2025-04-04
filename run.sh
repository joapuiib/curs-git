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

BUILD=0
CI=0
INSTALL_VENV=0
SPELL=0
ACT=''
ALL=0
SPELL_SOURCES=''

ARGS=''
SPELL_ARGS=''
while [ $# -gt 0 ] ; do
    case $1 in
        -b)
            BUILD=1
            ;;
        --ci)
            CI=1
            ;;
        --install-venv)
            INSTALL_VENV=1
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

if [ ! -d "venv" ]; then
    INSTALL_VENV=1
    print "Virtual environment not found."
fi

if [ $INSTALL_VENV -eq 1 ]; then
    if [ -d "venv" ]; then
        print "Removing existing virtual environment..."
        rm -rf venv
    fi

    print "Installing virtual environment..."
    python3 -m venv venv
    print "Installing dependencies"
    ./venv/bin/pip install -r requirements.txt
fi

source venv/bin/activate

COMMAND="serve"
if [ $BUILD -eq 1 ]; then
    COMMAND="build"
fi

if [ $CI -eq 0 ]; then
    mkdocs $COMMAND $ARGS
else
    CI=true mkdocs $COMMAND $ARGS
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
            SPELL_SOURCES=$(git diff --name-only main HEAD)
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
        SPELL_ARGS="$SPELL_ARGS --name mkdocs $SOURCES"
    fi

    print "Running pyspelling..."
    echo "pyspelling $SPELL_ARGS"
    pyspelling $SPELL_ARGS | tee pyspelling.log
    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        less pyspelling.log
    fi
fi
