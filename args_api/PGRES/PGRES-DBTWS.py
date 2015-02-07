{'PGRES_ShardedQueryFile.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\postgre_query.sql', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_ShardedTable.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_QueryFile.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\postgre_query.sql', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_TimezoneTable.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timezone_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timezone_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_QueryFile_Limit11.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 11, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\postgre_query.sql', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_TimestampTable.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with PostgreSQL query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Workgroup Server client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Workgroup Server table.')}], 'PGRES_Table_KeepSpoolFile.DBTWS_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_ShardedPartition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'Partitioned_test_from_2014', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_Partition_Limit33.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 33, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'Partitioned_test_from_2014', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_ParallelQueryDir.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_pgres', 'Input dir with PostgreSQL query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_Table_Limit15.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_QueryDir.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_pgres', 'Input dir with PostgreSQL query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_Partition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'Partitioned_test_from_2014', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'PGRES_QueryDir_Limit12.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 12, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_pgres', 'Input dir with PostgreSQL query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}]}