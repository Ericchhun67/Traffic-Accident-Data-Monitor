from utils.db_handler import init_db, insert_bulk_traffic_data
from utils.data_fetcher import get_traffic_data
from utils.map_handler import prepare_map_data

# Initialize the database
init_db()

# Generate and insert mock traffic data
data = get_traffic_data(use_mock=True, num_records=5)
insert_bulk_traffic_data(data)

# Prepare data for map visualization
map_data = prepare_map_data()

print("\n[TEST] Map-ready data points:\n")
for item in map_data:
    print(item)