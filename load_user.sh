 #!/bin/sh

   hadoop dfs -rmr /user/root/user
sqoop  import --connect jdbc:mysql://localhost/user_active_log --username root --password-file  /user/cloudera/sqoop_passwordfile/password  \
--table user --hive-import --hive-overwrite\
  --hive-table user_active_dump.user --driver com.mysql.jdbc.Driver

~                                                                       