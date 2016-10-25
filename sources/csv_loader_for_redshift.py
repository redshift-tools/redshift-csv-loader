"""#############################################################################
#CSV-to-Redshift Data Loader (v1.2, beta, 04/05/2016 15:11:53) [64bit] 
#Copyright (c): Free to change or distribute.
#Agreement: Use this tool at your own risk. Author is not liable for any damages 
#           or losses related to the use of this software.
################################################################################
Usage:  
#---------------------------------------------------------------------- 
#FreeUkraine #SaveUkraine #StopRussia #PutinKhuilo #CrimeaIsUkraine
#----------------------------------------------------------------------
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
	--ignoreheader -- numbers of eading lines to ignore (0)
	--gzip_source_file  -- gzip input CVS file before upload to Amazon-S3 (False).
	
	Input filename will be used for S3 key name.
	
	Boto S3 docs: http://boto.cloudhackers.com/en/latest/ref/s3.html
	psycopg2 docs: http://initd.org/psycopg/docs/
	
"""

import os, sys
from pprint import pprint
from optparse import OptionParser
import psycopg2
import select
try:
	import boto
	from boto.s3.key import Key
except ImportError:
	raise ImproperlyConfigured, "Could not load Boto's S3 bindings"
import sys
import time
import imp
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

e=sys.exit
bucket=None	
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') 
REDSHIFT_CONNECT_STRING= os.getenv('REDSHIFT_CONNECT_STRING') 
assert AWS_SECRET_ACCESS_KEY, 'AWS_ACCESS_KEY_ID is not set'
assert AWS_ACCESS_KEY_ID, 'AWS_SECRET_ACCESS_KEY is not set'
assert REDSHIFT_CONNECT_STRING, 'REDSHIFT_CONNECT_STRING is not set'


#print 'Loading....  ',
sys.stdout.flush()

if 0:
	i = 0

	while i <= 10:
		if (i%4) == 0: 
			sys.stdout.write('\b/')
		elif (i%4) == 1: 
			sys.stdout.write('\b-')
		elif (i%4) == 2:
			sys.stdout.write('\b\\')
		elif (i%4) == 3: 
			sys.stdout.write('\b|')

		sys.stdout.flush()
		time.sleep(0.2)
		i+=1
			
	print '\b\b done!'

#e(0)
i=0
def cli_progress_test(end_val, bar_length=20):
	for i in xrange(0, end_val):
		percent = float(i) / end_val
		hashes = '#' * int(round(percent * bar_length))
		spaces = ' ' * (bar_length - len(hashes))
		sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
		sys.stdout.flush()
def update_progress_bar():
	global i
	#prs=int(100*complete/total)
	#print prs
	#sys.stdout.write('\b\b\b\b\b\b\b\bTest:%s' % prs)
	txt='Redshift  | %s       |' %opt.to_table
	if 1:
		if (i%4) == 0: 
			sys.stdout.write('%s\b\b%s /' % (len(txt)*'\b',txt))
		elif (i%4) == 1: 
			sys.stdout.write('\b-')
		elif (i%4) == 2:
			sys.stdout.write('\b\\')
		elif (i%4) == 3: 
			sys.stdout.write('\b|')

		sys.stdout.flush()
		time.sleep(0.2)	
		i+=1
def progress(complete, total):
	prs=int(100*complete/total)
	#print prs
	bn= os.path.basename(args[0])
	txt='S3        | %s' % bn
	sys.stdout.write('\b\b\b\bTest:')
	sys.stdout.flush()
	sys.stdout.write('\r\%s\b\b\b\b\b\b\b%s | %s%%' % (len(txt)*'\b', txt,prs))
	sys.stdout.flush()

	if 0:
		

		print "start the output"
		def loop():
			i = 0
			output = "\rFirst_line%s..." % str(0) 
			sys.stdout.write(output)
			while 1:
				sys.stdout.write('\b'*len(output))
				i += 1
				output = "\rFirst_line%s..." % str(i) 
				sys.stdout.write(output)        
				sys.stdout.flush()
				time.sleep(1)
		loop()
			
		e(0)
	
def sizeof_fmt(num, suffix='B'):
	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Yi', suffix)	
def main(transfer_file, bucket_name, s3_key_name=None, use_rr=False,
		 make_public=True):
	global bucket
	# open the wikipedia file
	if not s3_key_name:
		s3_key_name = os.path.basename(transfer_file)
	conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
	bucket = conn.get_bucket(bucket_name)

	file_handle = open(transfer_file, 'rb')

	k = Key(bucket)
	k.key = s3_key_name
	
	k.set_contents_from_file(file_handle, cb=progress, num_cb=20, reduced_redundancy=use_rr )
	if make_public:
		k.make_public()


	return '/'.join((bucket_name, s3_key_name))
def wait(conn):
	while 1:
		state = conn.poll()
		if state == psycopg2.extensions.POLL_OK:
			break
		elif state == psycopg2.extensions.POLL_WRITE:
			select.select([], [conn.fileno()], [])
		elif state == psycopg2.extensions.POLL_READ:
			select.select([conn.fileno()], [], [])
		else:
			raise psycopg2.OperationalError("poll() returned %s" % state)
		update_progress_bar()
def is_gzip(fn):
	filename, file_extension = os.path.splitext(fn)
	if  file_extension.lower() in ['.gz']:
		return True
	return False
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod

if __name__ == "__main__":
	if 0:
		import progressbar
		from time import sleep
		bar = progressbar.ProgressBar(maxval=20, \
			widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
		for i in xrange(20):
			bar.update(i+1)
			sleep(0.1)
		bar.finish()
	if 0:
		from blessings import Terminal

		term = Terminal()

		with term.location(0, 10):
			print("Text on line 10")
		with term.location(0, 11):
			print("Text on line 11")
		e(0)

	parser = OptionParser()
	parser.add_option("-r", "--use_rr", dest="use_rr",
					  action="store_true", default=False)
	parser.add_option("-p", "--public", dest="make_public",
					  action="store_true", default=False)
	parser.add_option("-d", "--delim", dest="delim", default=',')
	parser.add_option("-q", "--quote", dest="quote", default='"')
	parser.add_option("-t", "--to_table", dest="to_table", default='')
	parser.add_option("-m", "--timeformat", dest="timeformat", default='MM/DD/YYYY HH12:MI:SS')
	parser.add_option("-i", "--ignoreheader", dest="ignoreheader", type=str, default=0)
	
	parser.add_option("-z", "--gzip_source_file", action="store_true",dest="gzip_source_file", default=False)
	
	(opt, args) = parser.parse_args()
	if len(args) < 2:
		print __doc__
		sys.exit()	
	#print options.delim
	assert opt.delim, 'Delimiter is not set.'
	assert opt.to_table, 'Target table is not set.'
	
	#e(0)	

	(fn, bn) = args[:2]
	#print fn, bn
	assert os.path.isfile(fn), 'Source file does not exists.'
	if opt.gzip_source_file:		
		assert not is_gzip(fn), 'Source file is already gzip compressed.'
		import gzip
		import shutil
		fngz='%s.gz' % fn
		with open(fn, 'rb') as f_in, gzip.open(fngz, 'wb') as f_out:
			shutil.copyfileobj(f_in, f_out)
		
		args[0]=fngz
	#e(0)
	kwargs = dict(use_rr=opt.use_rr, make_public=opt.make_public)
	import time
	start_time = time.time()
	location=main(*args, **kwargs)
	
	
	bn= os.path.basename(args[0])
	txt='S3         | %s' % bn
	sys.stdout.write('%s\b\b\b\b\b\b%s | %s%%' % (len(txt)*'\b', txt,100))
	print
	#print location
	if location:
		import __builtin__
		__builtin__.g = globals()
		abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
		loader_file = os.path.join(abspath,'include','loader.py')		
		loader=import_module(loader_file)
		loader.load(location)

		txt='Redshift   | %s       |' % opt.to_table
		sys.stdout.write('%s\b\b\b\b\b%s DONE' % (len(txt)*'\b',txt))
		print
		
	if opt.make_public and location :
		_,region,aws,com =bucket.get_website_endpoint().split('.')		
		#sys.stdout.write('Your file is at: https://%s.%s.%s/%s\n' % (region,aws,com,location))
	#print
	print("Time elapsed: %s seconds" % round((time.time() - start_time),2))
	
	
	
