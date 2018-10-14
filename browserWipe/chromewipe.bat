ECHO [+] Chrome Wipedown

taskkill /F /IM "chrome.exe">nul 2>&1

set ChromeDir=C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data

del /q /s /f "%ChromeDir%"
rd /s /q "%ChromeDir%"