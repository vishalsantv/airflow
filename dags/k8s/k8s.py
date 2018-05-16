from datetime import datetime
from airflow import DAG
from airflow.operators.contrib.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('hello_world_k8s', description='Simple tutorial DAG',
          schedule_interval='* * * * *',
          start_date=datetime(2018, 4, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

k8s_operator = KubernetesPodOperator(task_id='dummy_task', image='hello-world', namespace='analytics-eng', dag=dag)

dummy_operator >> hello_operator
