#!/bin/bash

DEMO_NAME='multithreading-async'
CONFIG='terminalizer_configs/multithreading_async.yml'
RENDERED_FILE_PATH='python/multithreading/main_async.gif'

terminalizer record $DEMO_NAME -k --config $CONFIG

terminalizer render $DEMO_NAME --output $RENDERED_FILE_PATH
