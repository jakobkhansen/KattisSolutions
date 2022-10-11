#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit
fi

IFS='/'
read -ra ARR <<< "$1"
IFS=""

name=${ARR[-1]}
mkdir $name
cd $name

mkdir samples
cd samples
sampleslink="/file/statement/samples.zip"
samples=$1$sampleslink
curl $samples --output samples.zip

echo "unzipped"
unzip samples.zip
rm -rf samples.zip
cd ..

touch $name".rs"
code="fn main() {

}"
echo $code > $name".rs"
echo "Problem extracted to ./$name/"
