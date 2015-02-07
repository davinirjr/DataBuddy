{'SSEXP_Table.MARIA_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with SQL Server Express query sql.'), 'from_db_name': ('-b', '--from_db_name', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'SQL Server Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with SQL Server Express query sqls.')}, {'to_db_name': ('-d', '--to_db_name', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Target table.')}], 'SSEXP_QueryFile.MARIA_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server Express query sql.'), 'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_ShardedTable_Limit50.MARIA_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_ShardedTable.MARIA_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_Table_KeepSpoolFile.MARIA_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_QueryDir_Limit25.MARIA_Table': [{'lame_duck': ('-l', '--lame_duck', 25, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server Express query sqls.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_QueryDir.MARIA_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server Express query sqls.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_QueryFile_Limit15.MARIA_Table': [{'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server Express query sql.'), 'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}], 'SSEXP_Table_Limit10.MARIA_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')}]}