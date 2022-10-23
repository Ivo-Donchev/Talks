#!/bin/bash

DEMO_NAME='multithreading-sync'
CONFIG='terminalizer_configs/multithreading_sync.yml'
RENDERED_FILE_PATH='python/multithreading/main_sync.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
