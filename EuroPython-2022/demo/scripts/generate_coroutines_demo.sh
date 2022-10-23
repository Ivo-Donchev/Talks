#!/bin/bash

DEMO_NAME='coroutines'
CONFIG='terminalizer_configs/coroutines.yml'
RENDERED_FILE_PATH='python/coroutines/coroutines.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
