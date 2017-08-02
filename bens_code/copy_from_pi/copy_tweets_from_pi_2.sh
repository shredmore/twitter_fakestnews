#script to copy independent headline .csv files
#from ben's pi, merge them together and put in
#hdfs for querying (add line to drop/create table)

#get current directory
echo 'getting pwd'
MY_CWD=$(pwd)

#create safe area outside of repo
#to run this code
echo 'making tweets directory'
rm -r /data/twitter_data
mkdir /data/twitter_data

#cd to headline dir
echo 'changing to tweets directory'
cd /data

#copy files over
echo 'copying files from pi'
scp -P 1722 -r pi@shredmore.chickenkiller.com:~/cronjobs/twitter_data ./

#change to new twitter dir
echo 'changing to twitter_data dir'
cd twitter_data
cp $MY_CWD/tweets_2_table.sql ./
cp $MY_CWD/hashtags_table.sql ./
cp $MY_CWD/mentions_table.sql ./
cp $MY_CWD/place_table.sql ./
cp $MY_CWD/urls_table.sql ./
cp $MY_CWD/user_table.sql ./

#make hdfs dir
echo 'making hdfs tweets directory'
sudo -u hdfs hadoop fs -mkdir /user/w205/project1
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/tweets_2
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/hashtags
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/mentions
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/place
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/urls
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/user

#put file into hdfs
echo 'putting twitter data into hdfs'
sudo -u hdfs hadoop fs -put ./tweets/*.csv /user/w205/project1/tweets_2
sudo -u hdfs hadoop fs -put ./hashtags/*.csv /user/w205/project1/hashtags
sudo -u hdfs hadoop fs -put ./mentions/*.csv /user/w205/project1/mentions
sudo -u hdfs hadoop fs -put ./places/*.csv /user/w205/project1/place
sudo -u hdfs hadoop fs -put ./urls/*.csv /user/w205/project1/urls
sudo -u hdfs hadoop fs -put ./users/*.csv /user/w205/project1/user

#change back to original directory
cd $MY_CWD

#drop and recreate table tha holds headlines
echo 'dropping and recreating table'
hive -f tweets_2_table.sql
hive -f hashtags_table.sql
hive -f mentions_table.sql
hive -f place_table.sql
hive -f urls_table.sql
hive -f user_table.sql

#clean exit
echo 'Goodbye!'
exit

