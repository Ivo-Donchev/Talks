#!/bin/bash

DEMO_NAME='multiprocessing-async'
CONFIG='terminalizer_configs/multiprocessing_async.yml'
RENDERED_FILE_PATH='python/multiprocessing/main_async.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
