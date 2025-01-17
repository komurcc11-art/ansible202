#!/bin/bash
comm=$1
git status
git add /home/student/ansible202/*
git commit -m $comm
git push origin
cd ~/
