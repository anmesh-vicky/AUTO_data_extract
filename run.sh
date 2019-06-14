#!/bin/bash
x=0
while [ $x -le 10 ]
do
  python data.py $x
  echo $x
  x=$(( $x + 1 ))
done
echo "done"