all: graph

graphFn:
	dot -Tps graph.dot > graph.ps

graphClean:
	sed 's/label="F."/label=""/;s/label="F.."/label=""/' graph.dot > graphClean.dot

graph: graphClean
	dot -Tps graphClean.dot > graph.ps

ps: graph
	evince graph.ps &

pdf:
	dot -Tpng -Gdpi=72 graphClean.dot > graph.png
	gimp graph.png &
	echo "#print in A4 landscape"
	echo 'rsync graph.pdf $C:/tmp/graph.pdf; rC "lpr -Pcopieur_BAS /tmp/graph.pdf"'
