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
code="using System;
using System.Linq;

void Main()
{
    var lines = Enumerable.Range(0, int.MaxValue).Select(_ => Console.ReadLine()).TakeWhile(x => x != null).ToList();
}

Main();
"

touch $name".cs"
echo $code > $name".py"
echo "Problem extracted to ./$name/"
