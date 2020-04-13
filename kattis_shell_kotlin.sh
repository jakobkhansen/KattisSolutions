#!/bin/bash


IFS='/'
read -ra ARR <<< "$1"
IFS=""

name=${ARR[-1]}
classname="${name^}"
mkdir $name
cd $name

mkdir samples
cd samples
sampleslink="/file/statement/samples.zip"
samples=$1$sampleslink
wget -q $samples

unzip -qq samples.zip
rm -rf samples.zip
cd ..

touch $classname".kt"

code="fun $classname(lines : List<String>) : String {
    return \"\"
}


fun main() {
    val lines = generateSequence(::readLine).toList()
    println($classname(lines))
}
"
echo $code > $classname".kt"
echo "Problem extracted to ./$name/"
