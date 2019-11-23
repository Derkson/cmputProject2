default:
	g++ -g -c parse.cpp
	g++ -o parse parse.o
	cat 1k.xml | ./parse
clean:
	rm parse.o parse terms.txt recs.txt emails.txt dates.txt
