# Title:	SYIQ_Table -->> DBTAES_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'syiq2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"demo"', 'Sybase IQ source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to Sybase IQ client home.'), 'from_user': ('-j', '--from_user', '"dba"', 'Sybase IQ source user.'), 'from_passwd': ('-x', '--from_passwd', '"sql"', 'Sybase IQ source user password.'), 'from_db_server': ('-n', '--from_db_server', '"demo16"', 'Sybase IQ source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')})
	