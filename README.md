run_python_script.py: 
     Dag created with dag_id practical_project_dag 2 task_id's data_load and csv_creation
     
allscript.py
    Dag with dag_id practical_exercise and  5 task_id's - load_csvfile_import, load_user,load_activitylo ,user_report, user_total

load_csv.sh :
    steps to processing csv_file and loading to hive,
load_csvfile_import:
       task_id for loading csv_ file to hive,

load_user.sh
     steps to import the user  table to hive,
load_activitylog.sh
     steps to import the user  table to hive,
load_user     
    task_id for importing user table to hive 
 load_activitylog
     task_id for importing activitylog table to hive 

user_total.sh
        steps to generate the reporting table data for user_total,
user_total
       task_id to genetate the  reporting_table user_total 
       
 user_report.sh
        steps to generate the reporting tables data for user_repor,
  user_report
       task_id to genetate the  reporting_table user_report
        
