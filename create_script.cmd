@echo off
echo ===============================================
set /p userInput=Enter you discord token:
echo ===============================================
echo python "%~dp0main.py" %userInput% > TeaPartyRecruitment.cmd
echo pause>>DSMessage.cmd
pause
