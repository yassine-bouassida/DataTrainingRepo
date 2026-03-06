from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

with DAG(
    dag_id="simple_taskflow_dag",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
    tags=["example"]
) as dag:

    @task()
    def extract_data():
        data = {"numbers": [1, 2, 3]}
        return data

    @task()
    def transform_data(data):
        return [x * 10 for x in data["numbers"]]

    @task()
    def load_data(transformed_data):
        print(f"Loading: {transformed_data}")

    # Implicit dependencies via XCom
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)


###
# Make sure you have Python 3.12.3 or 3.12.* for this exact setup
# python3 --version

# # Upgrade pip
# python3 -m pip install --upgrade pip setuptools wheel

# # Set Airflow constraints (required)
# export AIRFLOW_VERSION=3.1.7
# export PYTHON_VERSION=3.12
# export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# # Install Airflow
# pip install apache-airflow==${AIRFLOW_VERSION} --constraint ${CONSTRAINT_URL}


#could do below but above is better
# pip install apache-airflow
# pip show apache-airflow

#mkdir ~/airflow

# export AIRFLOW_HOME=~/airflow
# export AIRFLOW__CORE__DAGS_FOLDER=$AIRFLOW_HOME/dags
# (two different terminals)
# airflow standalone
# airflow api-server --port 8080


#~/airflow$ cat simple_auth_manager_passwords.json.generated

# airflow dags list

# airflow dags trigger simple_taskflow_dag


