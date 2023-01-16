all: graph

graph:
	dot -Tps graph.dot > graph.ps

ps: graph
	evince graph.ps &

pdf:
	dot -Tpng graph.dot > graph.png
	gimp graph.png &
	echo "#print in A4 landscape"
	echo 'rsync graph.pdf $C:/tmp/graph.pdf; rC "lpr -Pcopieur_BAS /tmp/graph.pdf"'
