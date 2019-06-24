#!/bin/sh

here="`dirname \"$0\"`"
echo "cd-ing to $here"
cd "$here" || exit 1

pwd
cd ..
pwd
cd setup
chmod +x ./setup
./setup
cd $HOME
chmod +x ./trivia
chmod +x astral-kuarry/trivia/terminal-trivia
chmod +x desktop/terminal-trivia
