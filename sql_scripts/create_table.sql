CREATE TABLE project1.ny_vendor (
	vendorid   INT PRIMARY KEY,
	vendorname VARCHAR(255)
);

CREATE TABLE project1.ny_paymtype (
	payment_type      INT PRIMARY KEY,
  	payment_type_desc VARCHAR(255)
);

CREATE TABLE project1.ny_location (
 	locationid INT PRIMARY KEY,
	borough    VARCHAR(255),
 	zone       VARCHAR(255)
);

CREATE TABLE project1.ny_tripdata (
  	tripid     		  SERIAL PRIMARY KEY,
	vendorid   		  INT REFERENCES project1.ny_vendor(vendorid),
	pickup_datetime	  TIMESTAMPTZ,
	dropoff_datetime  TIMESTAMPTZ,
	passenger_count	  BIGINT,
	trip_distance	  REAL,
	pulocationid	  INT REFERENCES project1.ny_location(locationid),
	dolocationid	  INT REFERENCES project1.ny_location(locationid),
	payment_type	  INT REFERENCES project1.ny_paymtype(payment_type),
	fare_amount		  REAL,
	tip_amount		  REAL,
	tolls_amount	  REAL,
	airport_fee	      REAL,
	other_amounts	  REAL
);