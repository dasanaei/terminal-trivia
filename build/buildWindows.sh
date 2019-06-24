cd ..
cd src
pyinstaller --onefile --icon=images/icon.ico --clean terminal-trivia.py
cd ..
rm -rf dist/win
mkdir -p dist/win/dist
mv src/dist/terminal-trivia.exe dist/win/dist/terminal-trivia.exe
