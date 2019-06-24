cd ..
cd src
pyinstaller --onefile  terminal-trivia.py
cd ..
rm -rf dist/mac
mkdir -p dist/mac
cd src
mv dist ../dist/mac
cd ..
cd setup
chmod +x ./setup
./setup
