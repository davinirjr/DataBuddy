# DataBuddy
##Version

data-buddy (GUI) | QueryCopy (command line)
---- | -------------
0.3.3 beta | 1.23.9 beta

##Purpose

Ad-hoc data migration between databases and file formats (CSV)

##Audience

Database developers, ETL developers, Data Integrators.

##Designated Environment
Pre-Prod (UAT/QA/DEV)

##Databases supported

Database | GUI (data-buddy) | Command line (QueryCopy)
---------|---- | -------------
DB2      | yes | yes
Informix | yes  | yes
MariaDB    | yes | yes
MySQL    | yes | yes
Infobright    | yes | yes
**Oracle**   | yes | [yes](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9)
PostgreSQL| yes | yes
SQLite| yes | yes
SQLServer| yes | yes
Sybase   | yes  | yes
TimesTen| yes  | yes


##File formats

Database | DDL extract | CSV extract | CSV load
---------|---- | ------------- | -------
DB2      |  | yes  | yes
Informix |  | yes  | yes
MariaDB    |  | yes  | yes
MySQL    |  | yes  | yes
**Oracle**   | Table | yes  | yes
PostgreSQL|  | yes  | yes
SQLite|  | yes  | yes
SQLServer|   | yes  | yes
Sybase   |  | yes  | yes
TimesTen|  | yes  | yes


##Components
- GUI - data-buddy (wxPython, PyInstaller).
- Command line -[QueryCopy](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9) (Python, PyInstaller).
  
##Features:

###Front end (data-buddy).

- Session management.

###Command line (QueryCopy):
- Multi-query load.
- Partition/sub-partition copy
- Sharded copy (turbo mode)
- Custom spool location (config/user_conf.py)
- config/include/oracle.py - configurable SQL*Loader args.
- 3 generic arguments (use them to pass job_id or timestamp and process in config/user_config.py)
- added all usecases
- lame_duck/limit fix for trial runs
- keep_data_file param (set it to 1 if you want to keep data dump)
- White-space control.
- Header line control.
- Truncate target table/partition/subpartition
- Ask to truncate.
- No client (url) connect.
- Supports CSV file load from multiple dirs.
- --exit_on_key - let's you keep exec window open after load job is done

##How it works.

1. "DbShell" - queries target and source for table metadata.
2. "Spooler"  - extracts data to temp file from source.
3. "Loader" - loads temp file to target using bulk loader.

###Tools used to extract, load, and query data
DataStore | Spooler | Loader | DbShell
----------|-------- | -------| -------
DB2 Advanced Enterprise Server | db2.exe | db2.exe | db2.exe
DB2 Advanced Workgroup Server | db2.exe | db2.exe | db2.exe
DB2 Developer Edition | db2.exe | db2.exe | db2.exe
DB2 Express | db2.exe | db2.exe | db2.exe
DB2 Express C | db2.exe | db2.exe | db2.exe
DB2 Enterprise Server | db2.exe | db2.exe | db2.exe
DB2 Workgroup Server | db2.exe | db2.exe | db2.exe
Infobright | mysql.exe | mysql.exe | mysql.exe
Informix IDS | dbaccess.exe | dbaccess.exe | dbaccess.exe
Informix Innovator C | dbaccess.exe | dbaccess.exe | dbaccess.exe
MariaDB | mysql.exe | mysql.exe | mysql.exe
MySQL | mysql.exe | mysql.exe | mysql.exe
Oracle 11G | sqlplus.exe | sqlldr.exe | sqlplus.exe
Exadata | sqlplus.exe | sqlldr.exe | sqlplus.exe
Oracle XE | sqlplus.exe | sqlldr.exe | sqlplus.exe
PostgreSQL | psql.exe | psql.exe | psql.exe
SQL Lite | sqlite3.exe | sqlite3.exe | sqlite3.exe
SQL Server Enterprise | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
SQL Server Express | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
Sybase SQL Anywhere | dbisql.com | dbisql.com | dbisql.com
SAP Sybase ASE | dbisql.com | dbisql.com | dbisql.com
Sybase IQ | dbisql.com | dbisql.com | dbisql.com
TimesTen | ttBulkCp.exe | ttBulkCp.exe | ttIsql.exe

## What it doesn't do
- It does not create target table
- It does not pipe data (it spools then loads)
- It should not be used Prod. Trial/ad-hoc use only.


##Implementation

- Written using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller
 
##Execution

* python data-buddy.py
* data-buddy.exe

#Templates v.s. free argument entry
##Pros
- all templates are tested with presets

##Cons
- user has to create new session if new argument has to be added/removed

#SQL*Loader config
- Change SQL*Loader arguments and control file in ```qc32\config\include\oracle.py```

#Exec host config
- Change host where physical copy is done in host_map.py ```qc32\include\v101\host_map.py```

#TODO
- argument values reuse from existing session. **DONE**
- clean uargs.db. **DONE**
- nls_format* duplication. **DONE**
- test UI.
- add --log_dir to backend. **DONE**
- add "source" and "target" datasources to "New Session". **DONE**
- Copy/Paste of argument values between sessions.
- generic "New Session" so user not limited by source and target templates. **DONE**
- history of values for each argument.
- cleanup all other databases but Oracle.
- more templates and better templates hierarchy.
- init templates to open session for "New Session". **DONE**
- validate args on Run. **DONE**.
- smaller test_api files (get default args from test routines, not canned files).
- fix template filters. **DONE**
- create "Menu" button and hide "About".
- create templates tab **DONE**
- create sessions tab **DONE**
- validate session name for chars not usable in file name. **DONE**
- allow user to create multiple session libraries. **DONE**
- fix mailformed path from MDD.MultiDirDialog. **DONE**
- make sure all paths are windows friendly.**DONE**
- open dir and open file use stale values.**DONE**
- filter control keys from ones affecting field value. **DONE**
- close all existing shells/shell groups upon exit.
- highlight running sessions.**DONE**
- beep on failing sessions.
- detect DONE/FAILED from cmd window. **DONE**
- let user disable post-etl email (Common: email_to). **DONE**
- change copy_vector format from db2db to db->db or db_2_db
- fix flicker on frame freeze **DONE**
- save on close **DONE**
- Table DDL export for Oracle **DONE**
- validate all path arguments before run
- add create template menu **DONE**
- add "--host_map" arg to set hosts for each thread **DONE**
- let user change host mapping **DONE**
- save as template **DONE**
- save as **DONE**
- test ezconnect
- add "Output" tab **DONE**
- add '--compress_spool' arg for zipped output
- add sqlloader.py
- fix session sort **DONE**
- fix session refresh **DONE**
- let user set primary dbs, source/target dbs
- add scp/ftp/sftp as data source/target
- make all paths relative to transport_home 
- create wizard for "New Session" template selection
- distinguish A-Templates from B-Templates
- let data copy to be executed on Linux (bash via ssh)**DONE**
- let data spool/load to be executed on Linux (bash via ssh)
- add SQLServer **DONE**
- add MySQL **DONE**
- add PostgreSQL **DONE**
- add SQLite **DONE**
- add Informix **DONE**
- add Sybase**DONE**
- add DB2 **DONE**
- add dBase
- add Access DB
- add MariaDB **DONE**
- add Infobright **DONE**
- add TimesTen **DONE**
- add MongoDB
- add Hadoop
- add Hive
- add Terradata
- add Redshift
- add Apache Hive
- add Vertica
- add Netezza
- add Parstream
- add ParAccel
- add Twitter (extract)
- add GA
- add Facebook (extract)
- add Taleo HR (extract) 
- add Salesforce
- add Greenplum
- add Actian
- add McObject
- add NuiDB
- add Clustrix
- add Orient
- add Scribe
- add KDB+
- add Volt DB
- add Arango DB
- add Foundation DB
- add Enterprise DB
- add Altibase HDB
- Kinesis
- Redshift
- RDS
- DynamoDB
- add Couchbase
- add Aerospike
- add InterSystems
- add QV (QlikView file format)
- add MDX (file format)

##Does it work?
- yes, for all major dbs (Oracle, SQLServer, DB2, Sybase, Informix, MySQL, Infobright, MariaDB, PostgreSQL, TimesTen, SQLite)
- only on Windows (UI, cmd)
- uncompressed spool
- Oracle copy can be executed on Linux (bash via ssh)



##References
* [QueryCopy for Oracle](https://github.com/QueryCopy/QueryCopy-for-Oracle) -- `qc32\qc32.exe`

## Screenshots

New session: 
![New session](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/new_session_all_dbs.png "Add New Session")

