set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>
set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  

cd c:\tmp\CSV_Loader
csv_loader_for_redshift.exe c:\tmp\data.csv test123 -r -p -d "," -t test2 -z


