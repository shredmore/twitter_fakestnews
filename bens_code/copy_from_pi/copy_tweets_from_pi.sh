#script to copy independent headline .csv files
#from ben's pi, merge them together and put in
#hdfs for querying (add line to drop/create table)

#get current directory
echo 'getting pwd'
MY_CWD=$(pwd)

#del headlines dir
#works w/o this line but gives
#error when cat all the .csv
#since healines wold exist from previous run
rm -r /data/tweets

#create safe area outside of repo
#to run this code
echo 'making tweets directory'
mkdir /data/tweets

#cd to headline dir
echo 'changing to tweets directory'
cd /data/tweets

#copy files over
echo 'copying files from pi'
scp -P 1722 pi@shredmore.chickenkiller.com:~/cronjobs/fake_news_tweets/*.csv ./
cp $MY_CWD/tweets_table.sql ./

#merge files into one .csv
echo 'merging .csv files into one'
cat *.csv > tweets.csv

#make hdfs dir
echo 'making hdfs headlines directory'
hdfs dfs -mkdir /user/w205/project1
hdfs dfs -mkdir /user/w205/project1/tweets

#put file into hdfs
echo 'putting merged headlines.csv into hdfs'
hdfs dfs -rm /user/w205/project1/headlines/tweets.csv
hdfs dfs -put tweets.csv /user/w205/project1/tweets

#change back to original directory
cd $MY_CWD

#drop and recreate table tha holds headlines
echo 'dropping and recreating table'
hive -f tweets_table.sql

#clean exit
echo 'Goodbye!'
exit

