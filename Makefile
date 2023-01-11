all: graph

graph:
	dot -Tps graph.dot > graph.ps

ps: graph
	evince graph.ps &

pdf:
	dot -Tpng graph.dot > graph.png
	gimp graph.png &
