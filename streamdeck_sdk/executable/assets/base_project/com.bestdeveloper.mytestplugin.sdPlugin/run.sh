#!/bin/sh

export PYTHON_COMMAND="python3"
export PYTHON_OK_VERSION="Python 3"
export PYTHON_MINIMUM_VERSION="3.8"

export PLUGIN_DIR_PATH=$(dirname "$0")
export PLUGIN_NAME=$(basename "$PLUGIN_DIR_PATH")
export PLUGIN_LOGS_DIR_PATH="${PLUGIN_DIR_PATH}/logs"
export PYTHON_INIT_PATH="${PLUGIN_DIR_PATH}/init.py"

export PLUGIN_CODE_DIR_PATH="${PLUGIN_DIR_PATH}/code"
export PLUGIN_CODE_REQUIREMENTS_PATH="${PLUGIN_CODE_DIR_PATH}/requirements.txt"
export PLUGIN_CODE_PATH="${PLUGIN_CODE_DIR_PATH}/main.py"

export PLUGIN_CODE_VENV_DIR_PATH="${PLUGIN_CODE_DIR_PATH}/venv"
export PLUGIN_CODE_VENV_ACTIVATE="${PLUGIN_CODE_VENV_DIR_PATH}/bin/activate"
export PLUGIN_CODE_VENV_PYTHON="${PLUGIN_CODE_VENV_DIR_PATH}/bin/python"

echo $PYTHON_COMMAND
echo $PYTHON_OK_VERSION
echo $PYTHON_MINIMUM_VERSION

echo $PLUGIN_DIR_PATH
echo $PLUGIN_NAME
echo $PLUGIN_LOGS_DIR_PATH
echo $PYTHON_INIT_PATH

echo $PLUGIN_CODE_DIR_PATH
echo $PLUGIN_CODE_REQUIREMENTS_PATH
echo $PLUGIN_CODE_PATH

echo $PLUGIN_CODE_VENV_DIR_PATH
echo $PLUGIN_CODE_VENV_ACTIVATE
echo $PLUGIN_CODE_VENV_PYTHON

PYTHON_VERSION=$(${PYTHON_COMMAND} -V)
echo $PYTHON_VERSION

if [[ $PYTHON_VERSION != $PYTHON_OK_VERSION* ]]; then
  echo "bad python"
  python_error_massage="StreamDeck '${PLUGIN_NAME}' plugin ERROR\n\n${PYTHON_OK_VERSION} not installed"
  osascript -e "display dialog \"${python_error_massage}\""
  exit
fi

INIT_RESULT=$(${PYTHON_COMMAND} "${PYTHON_INIT_PATH}")
echo $INIT_RESULT

if [ "$INIT_RESULT" != "True" ]; then
  echo "bad python"
  python_error_massage="StreamDeck '${PLUGIN_NAME}' plugin ERROR\n\n${INIT_RESULT}"
  osascript -e "display dialog \"${python_error_massage}\""
  exit
fi

export PYTHONPATH="${PLUGIN_CODE_DIR_PATH}"
echo $PYTHONPATH

"${PLUGIN_CODE_VENV_PYTHON}" "${PLUGIN_CODE_PATH}" "$@"
osascript -e "display dialog \"$@\""