#!/bin/bash
sed -e 's/http[s]\?:\/\/\S*//g ; s/www\.\S*//g ; s/ftp:\S*//g' "$1"
