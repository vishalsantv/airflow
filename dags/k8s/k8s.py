import airflow
from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'adhoc':False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}



dag = DAG('hello_world_k8s', default_args=default_args, description='Simple tutorial DAG',
          schedule_interval=timedelta(days=1)
         )





dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

k8s_operator = KubernetesPodOperator(task_id='dummy_task', image='hello-world', name='analytics-eng',  namespace='analytics-eng', dag=dag)

dummy_operator >> k8s_operator
