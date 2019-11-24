#!/bin/bash

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" > asdf.xml
echo "<emails type=\"array\">" >> asdf.xml

for ((i=1;i<=1000;i++));
do
echo $i
cat 1k-body.txt >> asdf.xml

done 

echo '</emails>' >> asdf.xml

