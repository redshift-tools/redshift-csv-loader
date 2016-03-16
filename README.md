# CSV File Loader for Amazon Redshift database.
Simple `local file to Amazon-Redshift table` uploader to use from Windows CLI.

Logs upload % progress to CLI screen.

Written using Python/boto/PyInstaller

##Version

OS|Platform|Version 
---|---|---- | -------------
Windows|64bit|[0.1.0 beta]

##Purpose

- Ad-hoc file upload to Amazon Redshift.
- File is staged on S3 prior to load to Redshift
- Optional upload to Reduced Redundancy storage (not RR by default).
- Optional "make it public" after upload (private by default)
- S3 Key defaulted to transfer file name.

##Audience

Business Analysts, AWS Developers, DevOps, 

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
```

##Example file load (into table `test2`)


* examples\Load_CSV_To_Redshift_Table.bat
```
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>
set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
  
cd c:\tmp\CSV_Loader
csv_loader_for_redshift.exe c:\tmp\data.csv test123 -r -p -d "," -t test2 -z

```
* resutl.log (Load_CSV_To_Redshift_Table.bat > resutl.log)
```
S3        | data.csv.gz | 100%
Redshift  | test2       | DONE
Time elapsed: 5.7 seconds

```




##Download
* [Master Release](https://github.com/alexbuz/S3_File_Uploader/archive/master.zip) -- `s3_percent_uploader 0.1.0`
