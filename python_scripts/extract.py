from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NY_taxi").getOrCreate()

def extract_trip_data(file_path):
    print(f"Extracting raw data from parquet file...")
    df = spark.read.parquet(file_path)
    return df

def extract_zone_data(file_path):
    print(f"Extracting zone data from csv file...")
    df = spark.read.format("csv").option("header", "true").load(file_path)
    return df