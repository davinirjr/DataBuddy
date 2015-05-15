::Test name: MySQL_QueryDir Limit333
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".Extract only 333 rows from MySQL query results into DDLFile.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-Q[--query_sql_dir] is "Input file with MySQL query sql."
::	-j[--from_user] is "MySQL source user."
::	-x[--from_passwd] is "MySQL source user password."
::	-b[--from_db_name] is "MySQL source database."
::	-n[--from_db_server] is "MySQL source instance name."
::	-z[--source_client_home] is "Path to MySQL client home."
::	-g[--to_file] is "To DDL file."	
	
echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
-w mysql-ddl ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 333 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150514_124623_433000 ^
-5 ".\config\host_map_v2.py" ^
-Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
-j "alex" ^
-x "mysql_pwd" ^
-b "test" ^
-n "localhost" ^
-z "C:\Temp\mysql\bin" ^
-g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_QueryDir_Limit333.ddl