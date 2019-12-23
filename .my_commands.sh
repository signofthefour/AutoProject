#!/bin/bash

function create {
    cd /home/nguyendat/Documents/AutomatingProject
    python create.py $1
    cd /home/nguyendat/MyProjects/$1
    git init
    git remote add origin git@github.com:signofthefour/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m "First init"
    git push -u origin master
    code .
}