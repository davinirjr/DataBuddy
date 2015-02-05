# Title:	EXAD_ShardedTimestampTable_trimWhitespace_Validate -->> SLITE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'validate': ('-V', '--validate', 1, 'Check if source and target objects exist.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'exad2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'source_client_home': ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Exadata client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'trim_whitespace': ('-W', '--trim_whitespace', 1, 'Trim whitespace from varchar2 in "Exadata" extract.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')})
	