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
rm -r /data/headlines

#create safe area outside of repo
#to run this code
echo 'making headlines directory'
mkdir /data/headlines

#cd to headline dir
echo 'changing to headlines directory'
cd /data/headlines

#copy files over
echo 'copying files from pi'
scp -P 1722 pi@shredmore.chickenkiller.com:~/cronjobs/*.csv ./
cp $MY_CWD/headlines_table.sql ./

#merge files into one .csv
echo 'merging .csv files into one'
cat *.csv > headlines.csv

#make hdfs dir
echo 'making hdfs headlines directory'
sudo -u hdfs hadoop fs -mkdir /user/w205/project1
sudo -u hdfs hadoop fs -mkdir /user/w205/project1/headlines

#put file into hdfs
echo 'putting merged headlines.csv into hdfs'
sudo -u hdfs hadoop fs -rm /user/w205/project1/headlines/headlines.csv
sudo -u hdfs hadoop fs -put headlines.csv /user/w205/project1/headlines

#change back to original directory
cd $MY_CWD

#drop and recreate table tha holds headlines
echo 'dropping and recreating table'
hive -f headlines_table.sql

#clean exit
echo 'Goodbye!'
exit

