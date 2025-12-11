# learn-airflow

## How to run in Docker :
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

```
mkdir -p ./dags ./logs ./plugins ./config

docker compose up airflow-init

docker-compose up -d

docker ps
```