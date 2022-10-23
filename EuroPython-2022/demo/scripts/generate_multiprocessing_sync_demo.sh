#!/bin/bash

DEMO_NAME='multiprocessing-sync'
CONFIG='terminalizer_configs/multiprocessing_sync.yml'
RENDERED_FILE_PATH='python/multiprocessing/main_sync.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
