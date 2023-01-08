./CombinedArms-0.82-x86_64.AppImage --appimage-mount

d=/tmp/.mount_Combinn5q6Tc
ls $d/usr/lib/openra/mods/ca/uibits/

ristretto $d/usr/lib/openra/mods/ca/uibits/*

#images (PNG)
ristretto `find $d | grep '.png'`

cp -p $d/usr/lib/openra/mods/ca/uibits/glyphs*.png images/
cp -p $d/usr/lib/openra/mods/ca/icon*.png images/
cp -p $d/usr/share/icons/hicolor/64x64/apps/openra-ca.png images/

#openra-ca-utility
./CombinedArms-0.82-x86_64.AppImage --utility

./CombinedArms-0.82-x86_64.AppImage --utility --weapon-docs > weapon-docs.md
./CombinedArms-0.82-x86_64.AppImage --utility --docs > docs.md
 
 
./CombinedArms-0.82-x86_64.AppImage --utility --extract temperat.pal
./CombinedArms-0.82-x86_64.AppImage --utility --extract ttnk2icon.shp

./CombinedArms-0.82-x86_64.AppImage --utility --png ttnkicon.shp temperat.pal

#keyboard
inkscape drawing.svg &
#print to file "drawing.pdf"
