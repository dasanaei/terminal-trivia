cd ..
cd src
pyinstaller --onefile --icon=images/icon.ico --clean terminal-trivia.py
cd ..
rm -rf dist/win
mkdir -p dist/win
mv dist ../dist/win
cd ..
cd setup
./setup
