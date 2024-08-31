@echo off

SET PYTHON_COMMAND=python
SET PYTHON_OK_VERSION=Python 3
SET PYTHON_MINIMUM_VERSION=3.8

SET BASE_PATH=%~dp0
SET PLUGIN_DIR_PATH=%BASE_PATH:~0,-1%
for %%I in ("%PLUGIN_DIR_PATH%") do set PLUGIN_NAME=%%~nxI
SET PLUGIN_LOGS_DIR_PATH=%PLUGIN_DIR_PATH%\logs
SET PYTHON_INIT_PATH=%PLUGIN_DIR_PATH%\init.py

SET PLUGIN_CODE_DIR_PATH=%PLUGIN_DIR_PATH%\code
SET PLUGIN_CODE_REQUIREMENTS_PATH=%PLUGIN_CODE_DIR_PATH%\requirements.txt
SET PLUGIN_CODE_PATH=%PLUGIN_CODE_DIR_PATH%\main.py

SET PLUGIN_CODE_VENV_DIR_PATH=%PLUGIN_CODE_DIR_PATH%\venv
SET PLUGIN_CODE_VENV_ACTIVATE=%PLUGIN_CODE_VENV_DIR_PATH%\Scripts\Activate
SET PLUGIN_CODE_VENV_PYTHON=%PLUGIN_CODE_VENV_DIR_PATH%\Scripts\python.exe

echo "%PYTHON_COMMAND%"
echo "%PYTHON_OK_VERSION%"
echo "%PYTHON_MINIMUM_VERSION%"

echo "%BASE_PATH%"
echo "%PLUGIN_DIR_PATH%"
echo "%PLUGIN_NAME%"
echo "%PLUGIN_LOGS_DIR_PATH%"
echo "%PYTHON_INIT_PATH%"

echo "%PLUGIN_CODE_DIR_PATH%"
echo "%PLUGIN_CODE_REQUIREMENTS_PATH%"
echo "%PLUGIN_CODE_PATH%"

echo "%PLUGIN_CODE_VENV_DIR_PATH%"
echo "%PLUGIN_CODE_VENV_ACTIVATE%"
echo "%PLUGIN_CODE_VENV_PYTHON%"

FOR /F "tokens=* USEBACKQ" %%F IN (`%PYTHON_COMMAND% -V`) DO SET PYTHON_VERSION=%%F
echo "%PYTHON_VERSION%"

IF "%PYTHON_VERSION%" == "" (
echo "bad python"
powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('%PYTHON_OK_VERSION% not installed', 'StreamDeck \"%PLUGIN_NAME%\" plugin ERROR', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"
exit
)

IF NOT "%PYTHON_VERSION:~0,8%" == "%PYTHON_OK_VERSION%" (
echo "bad python"
powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('%PYTHON_OK_VERSION% not installed', 'StreamDeck \"%PLUGIN_NAME%\" plugin ERROR', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"
exit
)

FOR /F "tokens=* USEBACKQ" %%F IN (`%PYTHON_COMMAND% "%PYTHON_INIT_PATH%"`) DO SET INIT_RESULT=%%F
echo "%INIT_RESULT%"

IF NOT "%INIT_RESULT%" == "True" (
echo "bad python"
powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('%INIT_RESULT%', 'StreamDeck \"%PLUGIN_NAME%\" plugin ERROR', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"
exit
)

SET PYTHONPATH="%PLUGIN_CODE_DIR_PATH%"
echo "%PYTHONPATH%"

"%PLUGIN_CODE_VENV_PYTHON%" "%PLUGIN_CODE_PATH%" %*
