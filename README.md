# twitter_fakestnews

## 1. Batch Layer:

## 2. Streaming Layer:

## 3. Serving Layer: Machine Learning

### 1. Launch with AMI from end of lab 4 with an m3.2xlarge instance. Make sure to mount /dev/xvdf on /data and start up hadoop.

```
$mount -t ext4 /dev/xvdf /data
$/root/start-hadoop.sh
```

### 2. Make sure pyspark 1.5.0, spark-submit are using python 2.7 with the following libraries installed:

```
sys
datetime
time
re
csv
collections
math
argparse
pyspark.mllib
chardet
```

### 3. Clone the github repo

```
$su - w205
$git clone https://github.com/shredmore/twitter_fakestnews.git
```

### 4. Make sure data stored in batch layer data is up-to-date. Use password hX7iL093T when prompted.

```
$exit
$cd /home/w205/twitter_fakestnews/bens_code/copy_from_pi/
$. copy_headlines_from_pi.sh
$. copy_tweets_from_pi_2.sh
$hdfs dfs -ls /user/w205/project1/headlines/
$hdfs dfs -ls /user/w205/project1/tweets_2/
```

### 5. Set up directories for machine learning results storage.

```
$mkdir /home/w205/lda_outputs/
$mkdir /home/w205/lda_outputs/lda_wordcloud/
$mkdir /home/w205/lda_outputs/lda_cossim/
$mkdir /home/w205/lda_outputs/lda_topics/
$mkdir /data/lda_outputs/
$mkdir /data/lda_outputs/lda_wordcloud/
$mkdir /data/lda_outputs/lda_cossim/
$mkdir /data/lda_outputs/lda_topics/
$sudo -uhdfs hadoop fs -mkdir /user/w205/project1/lda_output
$sudo -uhdfs hadoop fs -mkdir /user/w205/project1/lda_output/lda_wordcloud
$sudo -uhdfs hadoop fs -mkdir /user/w205/project1/lda_output/lda_cossim
$sudo -uhdfs hadoop fs -mkdir /user/w205/project1/lda_output/lda_topics
```

### 6.1 Start up machine learning pipeline. Option 1: Compare 2017-08-14's tweets against headlines from all news agencies. Process will take 15-20min to finish. Check out Pysparkshell online with your public DNS (sample below). Examine machine learning outputs including inferred topics and cosine similarities in terminal.

``` 
$su - w205
$cd twitter_fakestnews/legg_code/
$chmod u+x,g+x *
$spark-submit pyspark_lda_main.py -dr2 2017-08-14 -nwag 005 -nTp 8
```
```
<ec2-54-92-174-20.compute-1>.amazonaws.com:4040
```

### 6.2 Start up machine learning pipeline. Option 2: Examine more detailed usage and train model based on specific date range, news agencies and other model parameters. 

```
$spark-submit pyspark_lda_main.py -h
```

### 6.3 Start up machine learning pipeline. Option 3: To get results based on all news agencies and timed between August 4th and 14th. Feel free to modify code for other date ranges.

```
$. my_bash_loop.sh
```

### 7. Move results into HDFS. 

```
$exit
$. /home/w205/twitter_fakestnews/legg_code/move_results_to_hdfs.sh
```

### 8. Examine outputs in HDFS

```
$hdfs dfs -cat /user/w205/project1/lda_output/lda_cossim/lda_cossim.csv
$hdfs dfs -cat /user/w205/project1/lda_output/lda_wordcloud/lda_wordcloud.csv
$hdfs dfs -cat /user/w205/project1/lda_output/lda_topics/lda_topics.csv
```

### 9. Download output csv files for local Tableau visualizations through scp or use github repo sample data in following directory.

```
$cd /home/w205/twitter_fakestnews/legg_code/lda_outputs
```
