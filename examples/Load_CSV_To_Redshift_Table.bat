set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>
set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  

cd c:\Python35-32\PROJECTS\csv2redshift
python csv_loader_for_redshift.py crime_small.csv pythonuploadtest1 ^
	-r ^
	-p ^
	-d "," ^
	-t test ^
	-z ^
	-i 1


