table.ddl - DDL of target Redshift table
data.csv - input file for load to Redshift table test2

--------
Execute:
--------
cd examples
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>

set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  

csv_loader_for_redshift.exe data.csv test123 -r -d "," -t test2 -z