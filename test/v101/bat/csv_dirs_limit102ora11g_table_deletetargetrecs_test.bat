::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-K[--keep_data_file] is "Keep data dump."
::-M[--log_dir] is "Log destination."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-1[--job_pre_etl] is "Path to job level pre-ETL Python script."
::-C[--loader_profile] is "SQL*Loader profile (user defined)."
::-I[--input_dirs] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target Oracle 11G db user."
::-p[--to_passwd] is "Oracle 11G user password."
::-d[--to_db_name] is "Oracle 11G database."
::-a[--to_table] is "To Oracle table."
::-e[--nls_date_format] is "nls_date_format for target."
::-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::-Z[--target_client_home] is "Path to Oracle 11G client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Python27\qc_dist_32\20150327_093635\qc32\qc32.exe ^
-w csv2ora11g ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150327_093635_623000 ^
-1 ".\etl_templates\Oracle\delete_target_recs\job_pre_etl.py" ^
-C "C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml" ^
-I C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_1;C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_2 ^
-y 1000 ^
-u SCOTT ^
-p tiger2 ^
-d orcl ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"