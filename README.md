# CSV File Loader for Amazon Redshift DB.
    Ground to cloud data integration tool.
    Loads CSV file to Amazon-Redshift table from command line.

Features:
 - Loads CSV file to Amazon Redshift.
 - Script preloads your data to S3 prior to insert to Redshift.
 - No need for Amazon AWS CLI.
 - [Executable] (https://github.com/alexbuz/CSV_Loader_For_Redshift/releases) works from your OS Windows desktop CLI (command line).
 - [Python] (https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/sources/csv_loader_for_redshift.py) script will work on Linux and Windows.
 - COPY command configurable via [loader script](https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/include/loader.py)
 - It's executable (csv_loader_for_redshift.exe)  - no need for Python install.
 - It will work on any vanilla DOS for 64bit Windows.
 - AWS Access Keys are not passed as arguments. 
 - Written using Python/boto/psycopg2
 - Compiled using PyInstaller.


##Other scripts
  - [Oracle -> Redshift](https://github.com/alexbuz/Oracle-To-Redshift-Data-Loader/blob/master/README.md) data loader
  - [PostgreSQL -> Redshift](https://github.com/alexbuz/PostgreSQL_To_Redshift_Loader/blob/master/README.md) data loader
  - [MySQL -> Redshift](https://github.com/alexbuz/MySQL_To_Redshift_Loader/blob/master/README.md) data loader
  - [Oracle -> S3](https://github.com/alexbuz/Oracle_To_S3_Data_Uploader/blob/master/README.md) data loader
  - [EC2 Metcics Plotter] (https://github.com/alexbuz/EC2_Metrics_Plotter/blob/master/README.md)
  - [Oracle->Oracle] (https://github.com/alexbuz/TabZilla/blob/master/README.md) data loader.
  - [Oracle->MySQL] (https://github.com/alexbuz/Oracle-to-MySQL-DataMigrator/blob/master/README.txt) data loader.
  - [CSV->S3] (https://github.com/alexbuz/S3_File_Uploader/blob/master/README.md) data uploader.
 
  

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
>dist-64bit\csv_loader_for_redshift.exe
#############################################################################
#CSV-to-Redshift Data Loader (v1.2, beta, 04/05/2016 15:11:53) [64bit]
#Copyright (c): 2016 Alex Buzunov, All rights reserved.
#Agreement: Use this tool at your own risk. Author is not liable for any damages
#           or losses related to the use of this software.
################################################################################
Usage:
  set AWS_ACCESS_KEY_ID=<you access key>
  set AWS_SECRET_ACCESS_KEY=<you secret key>
  set REDSHIFT_CONNECT_STRING="dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"
  csv_loader_for_redshift.exe <file_to_transfer> <bucket_name> [<use_rr>] [<public>]
                                                 [<delim>] [<quote>] [<to_table>] [<gzip_source_file>]

        --use_rr -- Use reduced redundancy storage (False).
        --public -- Make uploaded files public (False).
        --delim  -- CSV file delimiter (',').
        --quote  -- CSV quote ('"').
        --to_table  -- Target Amazon-Redshit table name.
        --timeformat -- timestamp format (MM/DD/YYYY HH12:MI:SS)
        --ignoreheader -- numbers of leading lines to ignore (0)
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

### CSV file upload into Redshift table `test`

```
cd c:\Python35-32\PROJECTS\csv2redshift
csv_loader_for_redshift.exe Crime.csv testbucket ^
	-r ^
	-p ^
	-d "," ^
	-t test ^
	-z ^
	-i 1

```
Result
```
S3        | Crime.csv.gz | 100%
Redshift  | test       | DONE
Time elapsed: 45.7 seconds

```

#### Controlling timestamp format
Use `-m/--timeformat "MM/DD/YYYY HH12:MI:SS"` to control timestamp format.

#### Skipping the header
Use `-i/--ignoreheader  1` to set number of lines to ignore in input file.


####Target Redshift table DDL

```
drop table test;
create table test (
Incident_ID VARCHAR(20),CR_Number VARCHAR(20),Dispatch_Date_Time TIMESTAMP,Class VARCHAR(10) ,Class_Description VARCHAR(100),
Police_District_Name VARCHAR(40),Block_Address VARCHAR(100),
City VARCHAR(40),State VARCHAR(8),Zip_Code VARCHAR(10),
Agency VARCHAR(40),Place VARCHAR(40),Sector VARCHAR(10) ,Beat VARCHAR(10),PRA VARCHAR(10),Start_Date_Time TIMESTAMP,End_Date_Time TIMESTAMP,
Latitude VARCHAR(20),Longitude VARCHAR(20),Police_District_Number VARCHAR(50),Location VARCHAR(80),Address_Number VARCHAR(30));

```

####Test data
* Test data is in file [Crime.csv] (https://catalog.data.gov/dataset/crime)


### Modifying default script loader.
You can modify default Redshift COPY command this script is using.

Open file [include\loader.py](https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/dist-64bit/include/loader.py) and modify `sql` variable on line 24.

```
	sql="""
COPY %s FROM '%s' 
	CREDENTIALS 'aws_access_key_id=%s;aws_secret_access_key=%s' 
	DELIMITER '%s' 
	FORMAT CSV %s 
	GZIP 
	%s 
	%s; 
	COMMIT;
	...
```



###Download
* `git clone https://github.com/alexbuz/CSV_Loader_For_Redshift`
* [Master Release](https://github.com/alexbuz/CSV_Loader_For_Redshift/archive/master.zip) -- `csv_loader_for_redshift 0.1.0`






#
#
#
#
#   
#FAQ
#  
#### Can it load CSV file Redshift.
Yes, it is the main purpose of this tool.

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
No, but you can code it into default loder script  [include\loader.py](https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/dist-64bit/include/loader.py).

#### Is there an option to compress input CSV file before upload?
Yes. Use `-z` or `--gzip_source_file` argument so the tool does compression for you.

#### I'm experiencing errors in Redshift. How can I debug?
you can query stl_load_errors table for loader errors.
```
avrocluster=# select * from stl_load_errors order by starttime desc;
```
Also, you can include print statements into [include\loader.py](https://github.com/alexbuz/CSV_Loader_For_Redshift/blob/master/dist-64bit/include/loader.py). script to see what command is actually executed.

#### Explain first step of data load?
The CSV you provided is getting preloaded to Amazon-S3.
It doesn't have to be made public for load to Redshift. 
It can be compressed or uncompressed.
Your input file is getting compressed (optional) and uploaded to S3 using credentials you set in shell.

#### Explain second step of data load. How data is loaded to Amazon Redshift?
You Redshift cluster has to be open to the world (accessible via port 5439 from internet).
It uses PostgreSQL COPY command to load file located on S3 into Redshift table.

#### How do I load CSV file into Redshift without the header record?
Use `-i/--ignoreheader  1` to set number of lines to ignore in input file.

#### How do i set custom timestamp format for Redshift load?
Use `-m/--timeformat "MM/DD/YYYY HH12:MI:SS"` to control timestamp format.

#### Can I use WinZip or 7-zip
Yes, but you have to use 'gzip' compression type.

#### What technology was used to create this tool
I used Python, Boto, and psycopg2 to write it.
Boto is used to upload file to S3. 
psycopg2 is used to establish ODBC connection with Redshift clusted and execute `COPY` command.

#### I'm extracting data from Oracle using SQL query into CSV file. How do I load it to Redshift.
You can use [Oracle-to-Redshft-Data-Loader] (https://github.com/alexbuz/Oracle-To-Redshift-Data-Loader).
Profide query file as input parameter and it will load data.

#### Where are the sources?
Please, contact me for sources.

#### Can you modify functionality and add features?
Yes, please, ask me for new features.

#### What other AWS tools you've created?
- [Oracle_To_S3_Data_Uploader] (https://github.com/alexbuz/Oracle_To_S3_Data_Uploader) - Stream Oracle data to Amazon- S3.
- [S3_Sanity_Check] (https://github.com/alexbuz/S3_Sanity_Check/blob/master/README.md) - let's you `ping` Amazon-S3 bucket to see if it's publicly readable.
- [EC2_Metrics_Plotter](https://github.com/alexbuz/EC2_Metrics_Plotter/blob/master/README.md) - plots any CloudWatch EC2 instance  metric stats.
- [S3_File_Uploader](https://github.com/alexbuz/S3_File_Uploader/blob/master/README.md) - uploads file from Windows to S3.

#### Do you have any AWS Certifications?
Yes, [AWS Certified Developer (Associate)](https://raw.githubusercontent.com/alexbuz/FAQs/master/images/AWS_Ceritied_Developer_Associate.png)

#### Can you create similar/custom data tool for our business?
Yes, you can PM me here or email at `alex_buz@yahoo.com`.
I'll get back to you within hours.

###Links
 - [Employment FAQ](https://github.com/alexbuz/FAQs/blob/master/README.md)

















