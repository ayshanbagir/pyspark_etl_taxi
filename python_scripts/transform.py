from pyspark.sql.functions import when, col

def create_dim_vendor(df):
    df2 = df.select("vendorID").distinct().orderBy("vendorID")
    df_vendor = df2.withColumn(
    "vendorName",
    when(col("vendorID") == 1, "Creative Mobile Technologies, LLC")
    .when(col("vendorID") == 2, "Curb Mobility, LLC")
    .when(col("vendorID") == 6, "Myle Technologies Inc")
    .when(col("vendorID") == 7, "Helix")
    .otherwise("Unknown")
)
    return df_vendor

def create_dim_payment(df):
    df2 = df.select("payment_type").distinct().orderBy("payment_type")
    df_payment = df2.withColumn(
    "payment_type_desc",
     when(col("payment_type") == 0, "Flex Fare trip")
    .when(col("payment_type") == 1, "Credit card")
    .when(col("payment_type") == 2, "Cash")
    .when(col("payment_type") == 3, "No charge")
    .when(col("payment_type") == 4, "Dispute")
    .otherwise("Unknown")
)
    return df_payment

def create_dim_location(df):
    df_loc = df.select("LocationID", "Borough", "Zone")
    df_loc = df_loc.withColumn("LocationID", col("LocationID").cast("int"))
    return df_loc

def create_fact(df):
    df_fact = df.select("VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count",
         "trip_distance", "PULocationID", "DOLocationID", "payment_type", "fare_amount", "tip_amount", 
         "tolls_amount", "Airport_fee", \
        (col("extra") + col("mta_tax") + col("improvement_surcharge") \
         + col("congestion_surcharge") + col("cbd_congestion_fee")).alias("other_amounts"))
    
    #Drop nulls in critical fields
    df_fact = df_fact.dropna(subset=["tpep_pickup_datetime", "tpep_dropoff_datetime", "PULocationID", "DOLocationID", "fare_amount"])

    #Pickup time should be lower than dropoff time
    df_fact = df_fact.where(col("tpep_pickup_datetime") < col("tpep_dropoff_datetime"))

    #Passenger count should be between 1 and 6 for a typical yellow cab
    df_fact = df_fact.where((col("passenger_count") >= 1) & (col("passenger_count") <= 6))

    #Remove trips with: <= 0 or unreasonably high
    df_fact = df_fact.where((col("fare_amount") > 0) & (col("fare_amount") < 500))
    df_fact = df_fact.where((col("trip_distance") > 0) & (col("trip_distance") < 100))
    
    #Remove dublicates if it is really needed, otherwise it can consume a lot of memory
    #df_fact = df_fact.dropDuplicates() 

    column_mapping = {
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime"
    }

    for old_name, new_name in column_mapping.items():
        df_fact = df_fact.withColumnRenamed(old_name, new_name)

    return df_fact

def transform_data(df_raw, df_zone):
    print(f"Creating dimension dataframes...")
    dim_vendor = create_dim_vendor(df_raw)
    dim_payment = create_dim_payment(df_raw)
    dim_loc = create_dim_location(df_zone)

    print(f"Creating fact dataframes...")
    fact_data = create_fact(df_raw)

    print("Data transformed successfully.")
    return [dim_vendor, dim_payment, dim_loc, fact_data]