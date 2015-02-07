{'ORAXE_ParallelQueryDir.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ora', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with Oracle XE query sql.'), 'source_client_home': ('-z', '--source_client_home', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for source.'), 'trim_whitespace': ('-W', '--trim_whitespace', 'Trim whitespace from varchar2 in "Oracle XE" extract.'), 'from_db': ('-f', '--from_db', 'From database.'), 'from_table': ('-c', '--from_table', 'From table.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to SAP Sybase ASE client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', 'Target SAP Sybase ASE table.')}], 'ORAXE_QueryDir.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ora', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'ORAXE_TimestampTable.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'ORAXE_QueryFile.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\oracle_query.sql', 'Input file with Oracle XE query sql.'), 'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'ORAXE_TimezoneTable.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'ORAXE_ShardedTable.SYASE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}], 'ORAXE_Table_KeepSpoolFile.SYASE_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')}]}