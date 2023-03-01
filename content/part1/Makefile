pdf: ch1.ipynb
	jupyter-book build ch1.ipynb --builder pdfhtml
	cp _build/_page/ch1/pdf/ch1.pdf .
	rm -rf _build
    
ch1.ipynb: ch1_src.ipynb
	./replace_code.py $? $@ testfork.c,doforke.c

    