@echo off
echo Building PNG to 32-bit TGA Converter as EXE...
pyinstaller --onefile --noconsole --name PNG2TGA main.py
pause
