from airflow import DAG
from airflow.operators import BashOperator, HiveOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='example_hive_executor', default_args=args,
    schedule_interval=None
)


# Inserting the data from Hive external table to the target table
task2 = HiveOperator(
        task_id= 'hive_select',
        hql='SELECT * from kraken_app_session limit 10;',
        depends_on_past=False,
        dag=dag
)
# defining the job dependency
task2.set_upstream(task1)
