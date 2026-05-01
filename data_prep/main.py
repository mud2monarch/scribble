# %%
import polars as pl

from utils import convert_citibike_csv_to_parquet, haversine_miles

# %%
convert_citibike_csv_to_parquet(
    "data/202603-citibike-tripdata/*.csv", "data/202603_rides.parquet"
)
# %%

(pl.read_parquet("data/202603_rides.parquet").schema)
# %%

(
    pl.read_parquet("data/202603_rides.parquet")
    .with_columns(
        (pl.col("ended_at") - pl.col("started_at")).alias("ride_duration"),
        pl.col("started_at").dt.hour().alias("hour"),
        pl.col("started_at").dt.weekday().alias("day_of_week"),
    )
    .with_columns(
        pl.when(pl.col("day_of_week") <= 5)
        .then(True)
        .otherwise(False)
        .alias("is_weekday"),
        haversine_miles(
            pl.col("start_lat"),
            pl.col("start_lng"),
            pl.col("end_lat"),
            pl.col("end_lng"),
            unit="miles",
        ).alias("trip_distance_miles"),
    )
    .group_by(["start_station_id", "end_station_id", "is_weekday", "hour"])
    .agg(
        pl.col("trip_distance_miles").mean().alias("trip_distance_miles"),
        pl.len().alias("num_trips"),
    )
    .filter(pl.col("is_weekday"), pl.col("hour") == 17)
    # .write_csv("data/202603_demo_data_weekday_5pm.csv")
    .select(pl.all().n_unique())
    # .head()
    # .describe()
    # .n_unique()
)
