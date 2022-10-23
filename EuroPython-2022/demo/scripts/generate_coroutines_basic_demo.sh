#!/bin/bash

DEMO_NAME='coroutines-basic'
CONFIG='terminalizer_configs/coroutines_basic.yml'
RENDERED_FILE_PATH='python/coroutines/coroutines-basic.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
