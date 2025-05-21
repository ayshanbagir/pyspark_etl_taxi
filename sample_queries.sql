SELECT * FROM project1.ny_vendor;
SELECT * FROM project1.ny_paymtype;
SELECT * FROM project1.ny_location;
SELECT * FROM project1.ny_tripdata;

CREATE OR REPLACE VIEW project1.ny_tripdata_v AS
 SELECT tripid,
        vendorid,
        pickup_datetime,
        dropoff_datetime,
        passenger_count,
        trip_distance,
        pulocationid,
        dolocationid,
        payment_type,
        fare_amount,
        tip_amount,
        tolls_amount,
        airport_fee,
        other_amounts,
        fare_amount + tip_amount + tolls_amount + airport_fee + other_amounts AS total_amount
   FROM project1.ny_tripdata
   ;


  SELECT p.payment_type_desc, 
	 count(*) total_count,
	 sum(t.total_amount) total_amount
    FROM project1.ny_tripdata_v t
    JOIN project1.ny_paymtype p
      ON p.payment_type = t.payment_type
GROUP BY p.payment_type_desc
;


  SELECT  v.vendorname,
          t.pickup_datetime,
          t.dropoff_datetime,
          t.passenger_count,
          t.trip_distance,
          l.zone,
          p.payment_type_desc,
          t.fare_amount,
          t.tip_amount,
          t.tolls_amount,
          t.airport_fee,
          t.other_amounts,
          t.total_amount
  FROM project1.ny_tripdata_v t
  JOIN project1.ny_location l 
    ON l.locationid = t.pulocationid
  JOIN project1.ny_vendor v
    ON v.vendorid = t.vendorid
  JOIN project1.ny_paymtype p
    ON p.payment_type = t.payment_type
 WHERE 1=1
   AND l.borough = 'Brooklyn'
   AND p.payment_type = 2 --'Credit card'
   ;


  SELECT pickup_date,
          borough,
          payment_type_desc,
          COUNT(*) trip_count,
          SUM(trip_distance) trip_distance,
          SUM(total_amount) total_amount 
    FROM (SELECT  TO_CHAR(t.pickup_datetime, 'yyyy-mm-dd') pickup_date,
                  ROUND(CAST(trip_distance AS NUMERIC), 2) trip_distance,
                  l.borough,
                  p.payment_type_desc,
                  ROUND(CAST(total_amount AS NUMERIC), 2) total_amount
            FROM project1.ny_tripdata_v t
            JOIN project1.ny_location l 
              ON l.locationid = t.pulocationid
            JOIN project1.ny_paymtype p
              ON p.payment_type = t.payment_type
            WHERE p.payment_type IN (1, 2) --'Credit card' or 'Cash'
              AND t.airport_fee > 0)
GROUP BY pickup_date, 
	 borough,
	 payment_type_desc
;
