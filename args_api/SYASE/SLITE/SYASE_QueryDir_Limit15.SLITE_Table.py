# Title:	SYASE_QueryDir_Limit15 -->> SLITE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'syase2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"demo"', 'SAP Sybase ASE source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home.'), 'from_user': ('-j', '--from_user', '"dba"', 'SAP Sybase ASE source user.'), 'from_passwd': ('-x', '--from_passwd', '"sql"', 'SAP Sybase ASE source user password.'), 'from_db_server': ('-n', '--from_db_server', '"demo16"', 'SAP Sybase ASE source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_sy', 'Input dir with SAP Sybase ASE query files sql.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')})
	