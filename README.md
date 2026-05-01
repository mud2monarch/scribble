# Scribble
A fast graph drawing library.

# Project description

The ease with which we can access, analyze, and visualize data changes our relationship with that data. **Scribble** is a library that draws and analyzes graph data structures with GPU acceleration. It's written in Rust, compiled to WASM, and accessible via the browser.

The performance target is to handle >100k nodes with millions of edges at 60 fps.

# POC

A map showing Citibike activity in April 2026, split into 48 subplots:
- Weekday or weekend?
- Hour of the day

ToDo
1. Parse Citi Bike CSVs.
2. Build station table from observed station IDs and lat/lon.
3. Build 48 edge buckets.
4. Render one bucket on a WebGPU canvas.
5. Render 48 small multiples.
6. Add slider / hover / click.
7. Add benchmark panel.

# Demo data
- Citibike trips in March (NYC only) have 2300 total stations.
- Across 48 facets, this is ~110k nodes and 1.879m edges when aggregated into startStation/endStation/hour/is_weekend
- One hour slice is 2278 nodes and 121k edges 
