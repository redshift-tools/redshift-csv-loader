# CSV File Loader for Amazon Redshift DB.
    Ground to cloud data integration tool.
    Loads CSV file to Amazon-Redshift table from command line.

Features:
 - Loads CSV file to Amazon Redshift.
 - Script preloads your data to S3 prior to insert to Redshift.
 - No need for Amazon AWS CLI.
 - [Python](https://github.com/redshift-tools/redshift-csv-loader/blob/master/csv_loader_for_redshift.py) script will work on Linux and Windows.
 - COPY command configurable via [loader script](https://github.com/redshift-tools/redshift-csv-loader/blob/master/include/loader.py)
 - It's executable (csv_loader_for_redshift.exe)  - no need for Python install.
 - It will work on any vanilla DOS for 64bit Windows.
 - AWS Access Keys are not passed as arguments. 
 - Written using Python/boto/psycopg2
 - Compiled using PyInstaller.








## Purpose

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

## Audience

Database/ETL developers, Data Integrators, Data Engineers, Business Analysts, AWS Developers, DevOps, 

## Designated Environment
Pre-Prod (UAT/QA/DEV)

## Usage

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
# Example


### Environment variables

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


#### Target Redshift table DDL

```
drop table test;
create table test (
Incident_ID VARCHAR(20),CR_Number VARCHAR(20),Dispatch_Date_Time TIMESTAMP,Class VARCHAR(10) ,Class_Description VARCHAR(100),
Police_District_Name VARCHAR(40),Block_Address VARCHAR(100),
City VARCHAR(40),State VARCHAR(8),Zip_Code VARCHAR(10),
Agency VARCHAR(40),Place VARCHAR(40),Sector VARCHAR(10) ,Beat VARCHAR(10),PRA VARCHAR(10),Start_Date_Time TIMESTAMP,End_Date_Time TIMESTAMP,
Latitude VARCHAR(20),Longitude VARCHAR(20),Police_District_Number VARCHAR(50),Location VARCHAR(80),Address_Number VARCHAR(30));

```

#### Test data
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



### Download
* `git clone https://github.com/alexbuz/CSV_Loader_For_Redshift`
* [Master Release](https://github.com/alexbuz/CSV_Loader_For_Redshift/archive/master.zip) -- `csv_loader_for_redshift 0.1.0`





## Teardown
https://github.com/pydemo/teardown


## Snowpipe

https://github.com/pydemo/Snowpipe-For-SQLServer

:-))
[<img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png">](https://www.buymeacoffee.com/0nJ32Xg)












