#!/bin/bash

url=$(</dev/stdin)
code=$1

status_code=$(echo $url | httpx -x HEAD -status-code -silent -no-color | grep -oP '(?<=\[).*(?=\])')

if [[ $status_code != $code ]]
then
printf "$url"
fi

## usage - cat all_subs.txt | ./wildcard_sorting.sh 301
