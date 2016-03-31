# CSV File Loader for Amazon Redshift DB.
Loads CSV file to Amazon-Redshift table from Windows command line.

Features:
 - Loads local (to your Windows desktop) CSV file to Amazon Redshift.
 - No need to preload your data to S3 prior to insert to Redshift.
 - No need for Amazon AWS CLI.
 - Works from your OS Windows desktop (command line).
 - It's executable (csv_loader_for_redshift.exe)  - no need for Python install.
 - It's 32 bit - it will work on any vanilla Windows.
 - AWS Access Keys are not passed as arguments. 
 - Written using Python/boto/PyInstaller.
 - 

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
- It's a Python/boto/psycopg2 script
	* Boto S3 docs: http://boto.cloudhackers.com/en/latest/ref/s3.html
	* psycopg2 docs: http://initd.org/psycopg/docs/
- Executable is created using [pyInstaller] (http://www.pyinstaller.org/)

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
#Example


###Environment variables

* Set the following environment variables (for all tests:

```
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>

set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
```

### CSV file upload into Redshift table `test2`


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
##Test prerequisits.

####Target Redshift table DDL

```
CREATE TABLE test2 (id integer , num integer, data varchar,num2 integer, data2 varchar,num3 
integer, data3 varchar,num4 integer, data4 varchar);

```

####Test data
* Test data is in file examples\data.csv

###Sources
* Will add as soon as I clean em up and remove all the passwords and AWS keys :-)).

###Download
* `git clone https://github.com/alexbuz/CSV_Loader_For_Redshift`
* [Master Release](https://github.com/alexbuz/CSV_Loader_For_Redshift/archive/master.zip) -- `csv_loader_for_redshift 0.1.0`



#   
#FAQ
#  
#### Can it load CSV file from Windows desktop to Amazon Redshift.
Yes. This is the main purpose of the `CSV Loader for Redshift`.

#### Can developers integrate CSV loader into their ETL pipelines?
Yes. Assuming they are doing it on OS Windows.

#### How fast is data upload using `CSV Loader for Redshift`?
As fast as any AWS API provided by Amazon.

####How to inscease upload speed?
Compress input file or provide `-z` or `--gzip_source_file` arg in command line and this tool will compress it for you before upload to S3.

#### What are the other ways to upload file to Redshift?
You can use 'aws s3api' and psql COPY command to do pretty much the same.

#### Can I just zip it using Windows File Explorer?
No, Redshift will not recognize *.zip file format.
You have to `gzip` it. You can use 7-Zip to do that.


#### Does it delete file from S3 after upload?
No

#### Does it create target Redshift table?
No

#### Is there an option to compress input CSV file before upload?
Yes. Use `-z` or `--gzip_source_file` argument so the tool does compression for you.


#### Explain first step of data load?
The CSV you provided is getting preloaded to Amazon-S3.
It doesn't have to be made public for load to Redshift. 
It can be compressed or uncompressed.
Your input file is getting compressed (optional) and uploaded to S3 using credentials you set in shell.


#### Explain second step of data load. How data is loaded to Amazon Redshift?
You Redshift cluster has to be open to the world (accessible via port 5439 from internet).
It uses PostgreSQL COPY command to load file located on S3 into Redshift table.


#### Can I use WinZip or 7-zip
Yes, but you have to use 'gzip' compression type.

#### What technology was used to create this tool
I used Python, Boto, and psycopg2 to write it.
Boto is used to upload file to S3. 
psycopg2 is used to establish ODBC connection with Redshift clusted and execute `COPY` command.

#### Where are the sources?
Please, contact me for sources.

#### Can you modify functionality and add features?
Yes, please, ask me for new features.

#### What other AWS tools you've created?
- [S3_Sanity_Check] (https://github.com/alexbuz/S3_Sanity_Check/blob/master/README.md) - let's you `ping` Amazon-S3 bucket to see if it's publicly readable.
- [EC2_Metrics_Plotter](https://github.com/alexbuz/EC2_Metrics_Plotter/blob/master/README.md) - plots any CloudWatch EC2 instance  metric stats.

#### Can you create similar/custom data tool for our business?
Yes, you can PM me here or email at `alex_buz@yahoo.com`.
I'll get back to you within hours.











