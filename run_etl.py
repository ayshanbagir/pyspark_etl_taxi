from python_scripts import config
from python_scripts.extract import extract_trip_data, extract_zone_data
from python_scripts.transform import transform_data
from python_scripts.load import load_to_postgres

if __name__ == "__main__":
    data_path = "/Users/.../data"
    raw_df = extract_trip_data(data_path + "/yellow_tripdata_2025-02.parquet")
    zone_df = extract_zone_data(data_path + "/taxi_zone_lookup.csv")

    transformed_df = transform_data(raw_df, zone_df)
    db_table_map = {
        0: "ny_vendor",
        1: "ny_paymtype",
        2: "ny_location",
        3: "ny_tripdata"
    }

    for mapID, table_name in db_table_map.items():
        load_to_postgres(transformed_df[mapID], "project1." + table_name, config.db_config)


