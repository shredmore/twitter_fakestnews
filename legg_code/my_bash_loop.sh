#! /bin/bash

for X in {4..14} 
do
	spark-submit pyspark_lda_main.py -dr2 2017-08-$X -nwag 001 -nTp 8
	spark-submit pyspark_lda_main.py -dr2 2017-08-$X -nwag 002 -nTp 8
	spark-submit pyspark_lda_main.py -dr2 2017-08-$X -nwag 003 -nTp 8
	spark-submit pyspark_lda_main.py -dr2 2017-08-$X -nwag 004 -nTp 8
	spark-submit pyspark_lda_main.py -dr2 2017-08-$X -nwag 005 -nTp 8
done
