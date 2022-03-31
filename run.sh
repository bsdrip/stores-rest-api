#!/bin/bash

if [ -f 'data.db' ]
then
    rm data.db
fi

python3 src/app.py
