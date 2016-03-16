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


* S3_RR_Public_upload.bat
```
set AWS_ACCESS_KEY_ID=<you access key>
set AWS_SECRET_ACCESS_KEY=<you secret key>
  
cd c:\tmp\S3_Uploader
s3_percent_upload.exe c:\tmp\data.zip test123 --use_rr -public

```
* resutl.log (S3_RR_Public_upload.bat > resutl.log)
```
Connecting to S3...
File size: 388.5KiB
Public = True
ReducedRedundancy = True
Uploaded 0 bytes of 397799 (0%)
Uploaded 24576 bytes of 397799 (6%)
Uploaded 49152 bytes of 397799 (12%)
Uploaded 73728 bytes of 397799 (18%)
Uploaded 98304 bytes of 397799 (24%)
Uploaded 122880 bytes of 397799 (30%)
Uploaded 147456 bytes of 397799 (37%)
Uploaded 172032 bytes of 397799 (43%)
Uploaded 196608 bytes of 397799 (49%)
Uploaded 221184 bytes of 397799 (55%)
Uploaded 245760 bytes of 397799 (61%)
Uploaded 270336 bytes of 397799 (67%)
Uploaded 294912 bytes of 397799 (74%)
Uploaded 319488 bytes of 397799 (80%)
Uploaded 344064 bytes of 397799 (86%)
Uploaded 368640 bytes of 397799 (92%)
Uploaded 393216 bytes of 397799 (98%)
Upload complete.
Your file is at: https://s3-website-us-west-2.amazonaws.com/test123/data.zip

Time elapsed: 2.54299998283 seconds

```




##Download
* [Master Release](https://github.com/alexbuz/S3_File_Uploader/archive/master.zip) -- `s3_percent_uploader 0.1.0`
