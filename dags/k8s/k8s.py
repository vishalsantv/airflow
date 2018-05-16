from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('hello_world_k8s', description='Simple tutorial DAG',
          schedule_interval=timedelta(days=1)
         )

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

k8s_operator = KubernetesPodOperator(task_id='dummy_task', image='hello-world', name='analytics-eng',  namespace='analytics-eng', dag=dag)

dummy_operator >> k8s_operator
