title Installazione dei moduli
@echo off
cls
echo Installazione dei moduli Python richiesti:
timeout /t 5 /nobreak > nul
pip install requests
pip install json
pip install os
pip install platform

echo Fine.
timeout /t 5 /nobreak > nul
start Start.bat
