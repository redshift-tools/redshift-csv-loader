import time, psycopg2, os
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# dict g - is a calling env Globals()
opt= g['opt']
REDSHIFT_CONNECT_STRING = os.environ['REDSHIFT_CONNECT_STRING']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

def load(location):		
	fn='s3://%s' % location
	conn_string = REDSHIFT_CONNECT_STRING.strip().strip('"')	
	con = psycopg2.connect(conn_string,async=0);
	con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur = con.cursor();	
	quote=''
	if opt.quote:
		quote='quote \'%s\'' % opt.quote
	gzip=''
	if is_gzip(fn):		
		gzip='gzip'
	#e(0)
	ignoreheader =''
	if opt.ignoreheader:
		ignoreheader='IGNOREHEADER %s' % opt.ignoreheader
	timeformat=''
	if opt.timeformat:
		timeformat="timeformat '%s'" % opt.timeformat
	sql="""
copy %s from '%s' 
	CREDENTIALS 'aws_access_key_id=%s;aws_secret_access_key=%s' 
	DELIMITER '%s' 
	FORMAT CSV %s 
	%s 
	%s 
	%s;""" % (opt.to_table, fn, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,opt.delim,quote,gzip, timeformat, ignoreheader)
	
	cur.execute(sql)
	con.close()	
def is_gzip(fn):
	filename, file_extension = os.path.splitext(fn)
	return file_extension.lower() in ['.gz']
