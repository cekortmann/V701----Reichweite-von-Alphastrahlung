all: build/v701.pdf

build/v701.pdf: build/3cmenergie.pdf build/4.5cmenergie.pdf build/histo.pdf build/3cmeffLaeng.pdf build/4.5cmeffLaeng.pdf v701.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v701.tex
	lualatex  --output-directory=build v701.tex
	biber build/v701.bcf
	lualatex  --output-directory=build v701.tex

build/3cmenergie.pdf: 3cmenergie.py Abstand3cm.txt | build
	python 3cmenergie.py

build/4.5cmenergie.pdf: 4.5cmenergie.py Abstand3cm.txt | build
	python 4.5cmenergie.py

build/histo.pdf: histo.py 100Werte.txt | build
	python histo.py

build/3cmeffLaeng.pdf: 3cmeffLaeng.py Abstand3cm.txt | build
	python 3cmeffLaeng.py

build/4.5cmeffLaeng.pdf: 4.5cmeffLaeng.py Abstand4.5cm.txt | build
	python 4.5cmeffLaeng.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
