from airflow import DAG
from airflow.operators import BashOperator, HiveOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'avi',
     'start_date': datetime.now() - timedelta(minutes=1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('practical_exercise',schedule_interval=timedelta(minutes=60),default_args=default_args)

# Importing the incremental data from Mysql table to HDFS
task1 = BashOperator(
        task_id= 'load_csvfile_import',
        bash_command='./root/airflow/scripts/load_csv.sh',
        dag=dag)
# importing user_table
task2 = BashOperator(
        task_id= 'load_user_import',
        bash_command='./root/airflow/scripts/load_user.sh',
        dag=dag)
#importing  activitylogtable
task3 = BashOperator(
        task_id= 'load_active_import',
        bash_command='./root/airflow/scripts/load_activitylog.sh',
        dag=dag)

# loading reporting tables
task4 = BashOperator(
        task_id= 'user_report',
        bash_command='./root/airflow/scripts/user_report.sh',
        dag=dag)
task5 = BashOperator(
        task_id= 'user_total',
        bash_command='./root/airflow/scripts/user_total.sh',
        dag=dag)


task2.set_downstream(task4)
task3.set_downstream(task4)
task1.set_downstream(task4)
task3.set_downstream(task5)
task2.set_downstream(task5)
