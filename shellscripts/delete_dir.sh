#!/bin/bash
# Script variables
dirname="testdir"

# Main
if [ -d "./$dirname" ]
then 
    echo $'\nDirectory exists ...'
    rm -rf ./$dirname
    echo "Directory removed."
else
    echo $'\nDirectory does NOT exists . . . nothing done.'
fi