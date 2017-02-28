drop table test;
create table test (
Incident_ID int,CR_Number int,Dispatch_Date_Time TIMESTAMP,Class INT ,Class_Description VARCHAR(40),
Police_District_Name VARCHAR(40),Block_Address VARCHAR(100),
City VARCHAR(40),State VARCHAR(8),Zip_Code int2,
Agency VARCHAR(40),Place VARCHAR(40),Sector char(4) ,Beat VARCHAR(10),PRA int,Start_Date_Time DATE,End_Date_Time DATE,
Latitude FLOAT4,Longitude FLOAT4,Police_District_Number VARCHAR(10),Location VARCHAR(40),Address_Number int);


201073514,16016688,04/05/2016 10:07:48 PM,0521,BURG NO FORCE - RES/NIGHT,
SILVER SPRING ,14100  CASTLE BLVD,SILVER SPRING,MD,20904,
MCPD,Residence - Apartment/Condo,I,3I2,380,01/06/2016 05:00:00 PM,04/05/2016 08:02:00 PM,39.086029307087742,-76.940284025094826,3D,"(39.086029307087742, -76.940284025094826)",14100


Data Type	Aliases		Description
SMALLINT	INT2		Signed two-byte integer
INTEGER		INT, INT4	Signed four-byte integer
BIGINT		INT8		Signed eight-byte integer
DECIMAL		NUMERIC		Exact numeric of selectable precision
REAL		FLOAT4		Single precision floating-point number
DOUBLE 		PRECISION	FLOAT8, FLOAT	Double precision floating-point number
BOOLEAN		BOOL		Logical Boolean (true/false)
CHAR		CHARACTER, NCHAR, BPCHAR	Fixed-length character string
VARCHAR		CHARACTER VARYING, NVARCHAR, TEXT	Variable-length character string with a user-defined limit
DATE					Calendar date (year, month, day)
TIMESTAMP	TIMESTAMP WITHOUT TIME ZONE	Date and time (without time zone)


