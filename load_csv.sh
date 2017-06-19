 #!/bin/sh
cd /root/airflow/dags/user_upload_dump_dir
for  file in  $(find . -type f -name "user_upload_dump.*")
do
  echo "Processing $file file..."
  # take action on each file.
  #create directory to be process
  mkdir /root/airflow/dags/user_upload_dump_WorkInProgress
  cd /root/airflow/dags/user_upload_dump_dir
  #move each file to user_upload_dump_WorkInProgress
  mv  $file  /root/airflow/dags/user_upload_dump_WorkInProgress
  #remove special character ":" before saving file to hadoop
  cd  /root/airflow/dags/user_upload_dump_WorkInProgress
  mv $file ${file//:};
  #remove directory if exists
  hadoop dfs -rmr /user/root/user_upload_dump_WorkInProgress
  #copy file Directory to HDFS
  hadoop fs -put /root/airflow/dags/user_upload_dump_WorkInProgress
  #hadoop fs -cat  /user/root/user_upload_dump_WorkInProgress/$file
  hive -e "load data  inpath '/user/root/user_upload_dump_WorkInProgress' into  table user_active_dump.user_upload_dump;"
  #move prcoessed files to  user_upload_dump_loadedfiles
  mv /root/airflow/dags/user_upload_dump_WorkInProgress/*   /root/airflow/dags/user_upload_dump_loadedfile
  #remove file from user_upload_dump_WorkInProgress directory incase it failed to move.
  rm -r /root/airflow/dags/user_upload_dump_WorkInProgress
done
~                                                           