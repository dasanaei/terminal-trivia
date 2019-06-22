rm -rf dist
pyinstaller --onefile --icon=images/icon.ico --clean terminal-trivia.py
cd setup
./setup
