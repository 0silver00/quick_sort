all: quick-sort

quick-sort: make-csv
	python3 quick-sort.py

make-csv: make-csv.py
	python3 make-csv.py

clean:
	rm -f output.csv

