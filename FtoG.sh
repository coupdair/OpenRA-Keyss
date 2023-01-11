#!/bin/bash

fi=tabs4keyb_scrin_air_F?.png
fi=

list=
for t in build shield walk vehicle air
do
  echo "//"$t
  i=1
  for f in tabs4keyb_scrin_${t}_F?.png
  do
    echo $t'_F'$i'[label="F'$i'", color="white", shape="rect", image="'$f'"]'
    ((++i))
  done
done

#exit

display $list
