#!/bin/bash 

if [ -n "$ZSH_VERSION" ]; then
    export IMETRICS_PATH="$( cd "$( dirname "${(%):-%N}" )" && pwd )"
else
    export IMETRICS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
fi

export PYTHONPATH="$IMETRICS_PATH/python:$PYTHONPATH"
export PATH="$IMETRICS_PATH/bin:$PATH" 

