{'MYSQL_ShardedQuery.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Table_Limit1000.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 1000, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Partition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_partition': ('-P', '--from_partition', 'rx2015', 'From partition.'), 'from_table': ('-c', '--from_table', 'TEST.Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_ShardedPartition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_partition': ('-P', '--from_partition', 'rx2015', 'From partition.'), 'from_table': ('-c', '--from_table', 'TEST.Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', 'MySQL source database.'), 'from_partition': ('-P', '--from_partition', 'From partition.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'From sub-partition.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', 'MySQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input file with MySQL query sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Workgroup Server client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Workgroup Server table.')}], 'MYSQL_QueryDir_Limit333.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 333, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_mysql', 'Input file with MySQL query sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Subpartition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'subpart200', 'From sub-partition.'), 'from_table': ('-c', '--from_table', 'TEST.Sub_Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_TimezoneQueryFile.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Table.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Table_KeepSpoolFile.DBTWS_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_QueryFile.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_ShardedSubpartition.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'subpart200', 'From sub-partition.'), 'from_table': ('-c', '--from_table', 'TEST.Sub_Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_ShardedTable.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_Subpartition_Limit33.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 33, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'subpart200', 'From sub-partition.'), 'from_table': ('-c', '--from_table', 'TEST.Sub_Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_QueryFile_Limit100.DBTWS_Table': [{'lame_duck': ('-l', '--lame_duck', 100, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with MySQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}], 'MYSQL_QueryDir.DBTWS_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2dbtws', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_mysql', 'Input file with MySQL query sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Workgroup Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Workgroup Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Workgroup Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Workgroup Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Workgroup Server table.')}]}