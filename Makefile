.PHONY: clean

report.pdf: report.tex image/sentiment.png
	pdflatex report.tex
	mkdir -p versioned_reports
	cp report.pdf versioned_reports/game-timeline-`date | tr ' :' '_'`-`git log -1 | grep commit  | cut -d' ' -f2 |cut -c 1-5`.pdf

image/sentiment.png: derived_data/trump_sentiment.csv
	python3 plot.py

derived_data/trump_sentiment.csv: 
	python3 tweets.py image/sentiment.png

clean:
	rm derived_data/*.csv
	rm image/*.png