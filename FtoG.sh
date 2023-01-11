#!/bin/bash

fi=tabs4keyb_scrin_air_F?.png
fi=

list="build shield walk vehicle air"
for t in $list
do
  echo "  //"$t" nodes"
  i=1
  for f in tabs4keyb_scrin_${t}_F?.png
  do
    echo "  "$t'_F'$i'[label="F'$i'", color="white", shape="rect", image="'$f'"]'
    ((++i))
  done
done
for t in $list
do
  echo "  ///"$t" links"
  i=1; j=2
  echo '  build_F_TODO -> '$t'_F'$i'[color="blue"]'
  for f in tabs4keyb_scrin_${t}_F?.png
  do
    echo "              "$t'_F'$i' -> '$t'_F'$j'[color="white"]'
    ((++i,++j))
  done
done



exit

//walk
walk_F1[label="F1", color="white", shape="rect", image="tabs4keyb_scrin_walk_F1.png"]
walk_F2[label="F2", color="white", shape="rect", image="tabs4keyb_scrin_walk_F2.png"]

exit


///walk
  build_F2 -> walk_F1[color="blue"]
              walk_F1-> walk_F2[color="white"]
              
