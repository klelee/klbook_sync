#!/bin/bash

date=t${date}

cd klbook
git add .
git commit -m "updata klbook $(date)"
git push origin master
