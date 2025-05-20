def load_to_postgres(df, table_name, db):
    df.write.jdbc(
        url = db["url"],
        table = table_name,     
        mode = "append",              
        properties = db["properties"]
    )

    print(f"DataFrame with {df.count()} rows loaded to '{table_name}' successfully.")

