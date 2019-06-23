rm -rf dist
cd src
pyinstaller --onefile --icon=images/icon.ico --clean terminal-trivia.py
mv dist ..
cd ..
cd setup
./setup
