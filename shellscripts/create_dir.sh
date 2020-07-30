#!/bin/bash
# Script variables
filename="test_fiile.txt"
dirname="testdir"

# Main
if [ ! -d "./$dirname" ]
then 
    echo $'\nDirectory does NOT exist ...'
    mkdir ./$dirname
    touch ./$dirname/$filename
    echo "my awesome shell program" > ./$dirname/$filename
    echo $'\nFile ./$dirname/$filename created and populated with text.'
    echo
else
    echo $'\nDirectory exists . . . nothing done.'
fi
