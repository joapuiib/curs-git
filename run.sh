#!/bin/bash

function print {
    GREEN="\033[0;32m"
    RESET="\033[0m"
    echo -e "${GREEN}$1${RESET}"
}

BUILD=0
INSTALL_VENV=0
ARGS=''
while [ $# -gt 0 ] ; do
    case $1 in
        -b)
            BUILD=1
            ;;
        --install-venv)
            INSTALL_VENV=1
            ;;
        *)
            ARGS="$ARGS $1"
            ;;
    esac
    shift
done

if [ $INSTALL_VENV -eq 1 ]; then
    if [ -d "venv" ]; then
        print "Removing existing virtual environment"
        rm -rf venv
    fi

    print "Installing virtual environment"
    python3 -m venv venv
    print "Installing dependencies"
    ./venv/bin/pip install -r requirements.txt
fi

COMMAND="serve"
if [ $BUILD -eq 1 ]; then
    COMMAND="build"
fi

./venv/bin/mkdocs $COMMAND $ARGS
