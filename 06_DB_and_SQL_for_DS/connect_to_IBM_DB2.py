# database connection credentials
dsn_driver = '{IBM DB2 ODBC DRIVER}'
dsn_database = 'BluDB'
dsn_hostname = 'YourDb2Hostname'
dsn_port = '50000'
dsn_protocol = 'TCPIP'
dsn_uid = 'userId'
dsn_pwd = 'pswd'

dsn = (
    'DRIVER={{IBM DB2 ODBC DRIVER}};'
    'DATABASE={0};'
    'HOSTNAME={1};'
    'PORT={2};'
    'PROTOCOL=TCPIP;'
    'UID={3};'
    'PWD={4};').format(dsn_database, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, '', '')
    print('connected!')

except:
    print('Unable to connect to database')

ibm_db.close()
