## To run this code, you must be working in the AWS community AMI named UCB W205 Spring Ex 2 Image - ami-4cf9f826

## Working as the w205 user, set up postgres database and run streamparse

$/home/w205/twitter_fakestnews/matt_code/storm_tweets_3
$python create_tcount3.py
$cd extweetwordcount
$sparse run

## Run for 20 minutes, hit cntl-c to cancel run, and look at sample output
$dash_out_3.py

## Write data to .csv in /sample_output and feel free to run the topology again. 
./write_data_clear_table.sh
