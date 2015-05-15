::Test name: CSV_DateFile
	::Description:	Load CSV file into MySQLTable.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target MySQL db user."
::	-p[--to_passwd] is "Target db user password."
::	-d[--to_db_name] is "Target database."
::	-s[--to_db_server] is "Target db instance name."
::	-a[--to_table] is "Target table."
::	-Z[--target_client_home] is "Path to mysql client home."	
	
echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
-w csv-mysql ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150514_124624_622000 ^
-5 ".\config\host_map_v2.py" ^
-i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
-y 1000 ^
-u alex ^
-p mysql_pwd ^
-d test ^
-s localhost ^
-a Timestamp_test_to ^
-Z "C:\Temp\mysql\bin"