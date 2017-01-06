#!/bin/bash

opponent="${1:- RandomBot.py}"

if hash python3 2>/dev/null; then
    ./halite -d "30 30" "python3 MyBot.py" "python3 $opponent"
else
    ./halite -d "30 30" "python MyBot.py" "python $opponent"
fi
