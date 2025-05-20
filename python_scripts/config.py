import os

log4j_path = '/Users/.../log4j.properties'

os.environ["PYSPARK_SUBMIT_ARGS"] = (
    f"--conf spark.driver.extraJavaOptions=-Dlog4j.configuration=file:{log4j_path} "
    f"--conf spark.executor.extraJavaOptions=-Dlog4j.configuration=file:{log4j_path} "
    "--packages org.postgresql:postgresql:42.6.0 "
    "pyspark-shell"
)

db_config = {
    "url": "jdbc:postgresql://<host>:<port>/<database>",  
    "properties": {
        "user": "<username>",
        "password": "<password>",
        "driver": "org.postgresql.Driver"
    }
}



