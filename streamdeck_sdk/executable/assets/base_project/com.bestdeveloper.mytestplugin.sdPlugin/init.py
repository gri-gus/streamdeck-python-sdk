import logging
import os
import platform
import re
import shlex
import subprocess
import sys
import traceback
from logging.handlers import RotatingFileHandler
from pathlib import Path

PYTHON_COMMAND: str = os.environ["PYTHON_COMMAND"]
PYTHON_MINIMUM_VERSION: str = os.environ["PYTHON_MINIMUM_VERSION"]

PLUGIN_DIR_PATH: Path = Path(os.environ["PLUGIN_DIR_PATH"])
PLUGIN_NAME: str = os.environ["PLUGIN_NAME"]
PLUGIN_LOGS_DIR_PATH: Path = Path(os.environ["PLUGIN_LOGS_DIR_PATH"])

PLUGIN_CODE_DIR_PATH: Path = Path(os.environ["PLUGIN_CODE_DIR_PATH"])
PLUGIN_CODE_REQUIREMENTS_PATH: Path = Path(os.environ["PLUGIN_CODE_REQUIREMENTS_PATH"])

PLUGIN_CODE_VENV_DIR_PATH: Path = Path(os.environ["PLUGIN_CODE_VENV_DIR_PATH"])
PLUGIN_CODE_VENV_ACTIVATE: Path = Path(os.environ["PLUGIN_CODE_VENV_ACTIVATE"])

SPACES_REGEX = re.compile(r" +", flags=re.MULTILINE)
BEGIN_END_WHITESPACES_REGEX = re.compile(r"^ +| +$", flags=re.MULTILINE)
LINE_TRANSLATION_REGEX = re.compile(r"\n|\r$", flags=re.MULTILINE)
BEGIN_S_REGEX = re.compile(r"^\s+|\s+$")
QUOTES_REGEX = re.compile(r"['\"`]")
PARSE_REQUIREMENTS_REGEX = re.compile(r"^\s*?(\S*).=", flags=re.MULTILINE)

logger: logging.Logger = logging.getLogger(__name__)
MAX_MESSAGE_LEN: int = 500
LOG_FILE_PATH: Path = PLUGIN_LOGS_DIR_PATH / Path("init.log")
LOG_LEVEL = logging.DEBUG


class InitError(Exception):
    pass


def init_logger(log_file: Path, log_level: int = logging.DEBUG) -> None:
    logger.setLevel(log_level)
    logs_dir: Path = log_file.parent
    logs_dir.mkdir(parents=True, exist_ok=True)
    rfh = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=3 * 1024 * 1024,
        backupCount=2,
        encoding="utf-8",
        delay=False,
    )
    rfh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d): %(message)s"
    )
    rfh.setFormatter(formatter)
    logger.addHandler(rfh)


# region CleanUpFunctions

def clean_up_command(text: str):
    r1 = BEGIN_S_REGEX.sub("", text)
    r2 = BEGIN_END_WHITESPACES_REGEX.sub("", r1)
    r3 = LINE_TRANSLATION_REGEX.sub(" ", r2)
    r4 = SPACES_REGEX.sub(" ", r3)
    return r4


def clean_up_command_result(text: str):
    r1 = clean_up_command(text=text)
    r2 = QUOTES_REGEX.sub(r'\"', r1)
    return r2


# endregion CleanUpFunctions

# region DaemonCommands

def create_venv_daemon() -> subprocess.Popen:
    command = f'{PYTHON_COMMAND} -m venv "{PLUGIN_CODE_VENV_DIR_PATH}"'
    command_split = shlex.split(command)
    process = subprocess.Popen(
        command_split,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    return process


def install_requirements_daemon() -> subprocess.Popen:
    if sys.platform.startswith("win") or sys.platform.startswith("cygwin"):
        command = f'''
        "{PLUGIN_CODE_VENV_ACTIVATE}" &&\
        {PYTHON_COMMAND} -m pip install --upgrade pip &&\
        {PYTHON_COMMAND} -m pip install -r "{PLUGIN_CODE_REQUIREMENTS_PATH}"\
        '''
    else:
        command = f'''
        source "{PLUGIN_CODE_VENV_ACTIVATE}" &&\
        export PYTHONPATH="{PLUGIN_CODE_DIR_PATH}" &&\
        {PYTHON_COMMAND} -m pip install --upgrade pip &&\
        {PYTHON_COMMAND} -m pip install -r "{PLUGIN_CODE_REQUIREMENTS_PATH}"\
        '''
    process = subprocess.Popen(
        clean_up_command(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        shell=True,
    )
    return process


def pip_freeze_daemon() -> subprocess.Popen:
    os_name = platform.system()
    logger.info(os_name)
    if os_name == "Darwin":
        command = f'''
        source "{PLUGIN_CODE_VENV_ACTIVATE}" &&\
        {PYTHON_COMMAND} -m pip freeze\
        '''
    elif os_name == "Windows":
        command = f'''
        "{PLUGIN_CODE_VENV_ACTIVATE}" &&\
        {PYTHON_COMMAND} -m pip freeze\
        '''
    else:
        raise InitError("Unsupported Operation System.")
    process = subprocess.Popen(
        clean_up_command(command),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        shell=True,
    )
    return process


# endregion DaemonCommands

def check_venv_activate_exists() -> bool:
    if PLUGIN_CODE_VENV_ACTIVATE.exists():
        logger.info(f'venv activate already exists in "{PLUGIN_CODE_VENV_ACTIVATE}"')
        return True
    logger.info(f'venv activate is not exists in "{PLUGIN_CODE_VENV_ACTIVATE}"')
    return False


def check_python_version() -> None:
    minimum_python_version_splitted = PYTHON_MINIMUM_VERSION.split(".")
    python_version_info = sys.version_info
    python_version_str = ".".join([str(item) for item in python_version_info[:3]])

    for index, minimum_python_version_item in enumerate(minimum_python_version_splitted):
        if int(minimum_python_version_item) < python_version_info[index]:
            logger.info(f'Current python version "{python_version_str}" > "{PYTHON_MINIMUM_VERSION}"')
            return
        elif int(minimum_python_version_item) > python_version_info[index]:
            message = f'Current python version "{python_version_str}" < "{PYTHON_MINIMUM_VERSION}"'
            logger.error(message)
            raise InitError(message)
    logger.info(f'Current python version "{python_version_str}" >= "{PYTHON_MINIMUM_VERSION}"')


def create_venv() -> None:
    process = create_venv_daemon()
    stdout, stderr = process.communicate()
    if stderr:
        logger.error(stderr)
        raise InitError(stderr)


def install_requirements() -> None:
    process = install_requirements_daemon()
    stdout, stderr = process.communicate()
    if stderr:
        logger.error(stderr)
        raise InitError(stderr)


def check_requirements():
    requirements_packages_text = PLUGIN_CODE_REQUIREMENTS_PATH.read_text("utf-8")
    requirements_packages_names = PARSE_REQUIREMENTS_REGEX.findall(requirements_packages_text)

    process = pip_freeze_daemon()
    installed_packages_text, stderr = process.communicate()
    if stderr:
        logger.warning(stderr)

    installed_packages_names = PARSE_REQUIREMENTS_REGEX.findall(installed_packages_text)
    installed_packages_names_underscore = [package_name.replace("-", "_") for package_name in installed_packages_names]
    installed_packages_names.extend(installed_packages_names_underscore)

    for requirements_package_name in requirements_packages_names:
        requirements_package_name_underscore = requirements_package_name.replace("-", "_")
        if not (requirements_package_name in installed_packages_names or
                requirements_package_name_underscore in installed_packages_names):
            message = f'Package "{requirements_package_name}" not installed'
            logger.error(message)
            raise InitError(message)


def init_project() -> None:
    if check_venv_activate_exists():
        try:
            check_requirements()
        except InitError as err:
            raise InitError(f"Current venv ERROR: {err}")
        logger.info("Current venv is correct")
        return

    try:
        check_python_version()
    except InitError as err:
        raise InitError(f"Check python version ERROR: {err}")
    logger.info("Python version is correct")

    try:
        create_venv()
    except InitError:
        raise InitError(f"Create venv ERROR")
    logger.info("venv created successfully")

    try:
        install_requirements()
    except InitError:
        try:
            check_requirements()
        except InitError:
            raise InitError(f"Install requirements ERROR")
    logger.info("Requirements are successfully installed")


def main():
    try:
        init_logger(log_file=LOG_FILE_PATH, log_level=LOG_LEVEL)
        logger.info("INIT STARTED")
        init_project()
        result = True
    except BaseException as err:
        if isinstance(err, InitError):
            message = str(err)
            logger.error(message)
        else:
            message = "Init ERROR"
            log_message = f"{message}: {str(type(err).__name__)}: {err}; Traceback: {traceback.format_exc()}"
            logger.error(log_message)
        result_message = f"{message}. See log file for details: {LOG_FILE_PATH}. " \
                         f"You need to fix the problem and reinstall the plugin."
        result = clean_up_command_result(text=str(result_message))[:MAX_MESSAGE_LEN]
    logger.info(f"result={result}")
    print(result)
    logger.info("INIT ENDED")


if __name__ == '__main__':
    main()
