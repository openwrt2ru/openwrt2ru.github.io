@echo off
set PYTHON_EXE="c:\python27\python.exe"
pushd output
ECHO lesten 8000 port
ECHO open in browser http://localhost:8000/
ECHO Ctrl+C to exit
%PYTHON_EXE% -m pelican.server
popd