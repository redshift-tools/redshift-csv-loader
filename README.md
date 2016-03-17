# CSV File Loader for Amazon Redshift DB.
Simple local `*Windows*` CSV file to Amazon-Redshift table loader to use from Windows CLI (command line).

Logs upload % progress to CLI screen.

Written using Python/boto/psycopg2/PyInstaller

##Version

OS|Platform|Version 
---|---|---- | -------------
Windows|64bit|[0.1.0 beta]

##Purpose

- Ad-hoc CSV file load to Amazon Redshift table.

## How it works
- File is staged on S3 prior to load to Redshift
- Optional upload to Reduced Redundancy storage (not RR by default).
- Optional "make it public" after upload (private by default)
- S3 Key defaulted to transfer file name.
- Load is done using COPY command
- Target Redshift table has to exist
- It's a python/boto/psycopg2 script
	* Boto S3 docs: http://boto.cloudhackers.com/en/latest/ref/s3.html
	* psycopg2 docs: http://initd.org/psycopg/docs/
- Executable is created using pyInstaller

##Audience

Database/ETL developers, Data Integrators, Data Engineers, Business Analysts, AWS Developers, DevOps, 

##Designated Environment
Pre-Prod (UAT/QA/DEV)

##Usage

```
## Load CSV file to Amazon Redshift table.
##
## Load % progress outputs to the screen.
##
Usage:  
  set AWS_ACCESS_KEY_ID=<you access key>
  set AWS_SECRET_ACCESS_KEY=<you secret key>
  set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
  csv_loader_for_redshift.py <file_to_transfer> <bucket_name> [<use_rr>] [<public>]
						 [<delim>] [<quote>] [<to_table>] [<gzip_source_file>]
	
	--use_rr -- Use reduced redundancy storage (False).
	--public -- Make uploaded files public (False).
	--delim  -- CSV file delimiter (',').
	--quote  -- CSV quote ('"').
	--to_table  -- Target Amazon-Redshit table name.
	--gzip_source_file  -- gzip input CVS file before upload to Amazon-S3 (False).
	
	Input filename will be used for S3 key name.
	
	Boto S3 docs: http://boto.cloudhackers.com/en/latest/ref/s3.html
	psycopg2 docs: http://initd.org/psycopg/docs/
	
"""

```

##Environment variables

* Set the following environment variables:

```
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>

set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
```

##Example file load into Redshift table `test2`


* examples\Load_CSV_To_Redshift_Table.bat
```
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>
set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
  
cd c:\tmp\CSV_Loader
csv_loader_for_redshift.exe c:\tmp\data.csv test123 -r -d "," -t test2 -z

```
* resutl.log (Load_CSV_To_Redshift_Table.bat > resutl.log)
```
S3        | data.csv.gz | 100%
Redshift  | test2       | DONE
Time elapsed: 5.7 seconds

```

###Target Redshift table DDL

```
CREATE TABLE test2 (id integer , num integer, data varchar,num2 integer, data2 varchar,num3 
integer, data3 varchar,num4 integer, data4 varchar);

```

###Test data
* Test data is in file examples\data.csv

##Sources
* Will add as soon as I clean em up and remove all the passwords and AWS keys :-)).

##Download
* `git clone https://github.com/alexbuz/CSV_Loader_For_Redshift`
* [Master Release](https://github.com/alexbuz/CSV_Loader_For_Redshift/archive/master.zip) -- `csv_loader_for_redshift 0.1.0`
