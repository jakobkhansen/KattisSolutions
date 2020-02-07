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

touch $classname".java"

code="import java.util.ArrayList;
import java.util.Scanner;

public class $classname {

    public static String $name(String[] lines) {


        return \"\";
    }



    // Setup
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> linesList = new ArrayList<>();

        while (scan.hasNext()) {
            linesList.add(scan.nextLine());
        }

        String[] lines = new String[linesList.size()];

        for (int i = 0; i < lines.length; i++) {
            lines[i] = linesList.get(i);
        }

        System.out.println($name(lines));

        scan.close();
    }
}"
echo $code > $classname".java"
echo "Problem extracted to ./$name/"
