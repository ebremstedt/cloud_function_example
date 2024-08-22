import os
from read import fetch_weather_data
from transform import parse_json_response
from write import write_to_bigquery
from requests import Request
import functions_framework

# iweunfiweun
@functions_framework.http
def main(request: Request):

    api_key = os.getenv('API_KEY')
    api_url = "http://api.weatherapi.com/v1/history.json"

    project_id = 'cloud-function-example-433209'
    destination_table = f"{project_id}.raw.weather"

    location="STOCKHOLM"
    date="2024-08-14"

    print("Fetching data...")

    data = fetch_weather_data(
        api_key=api_key,
        api_url=api_url,
        location=location,
        date=date
    )

    print("Transforming data...X")

    transformed_data = parse_json_response(data=data)

    print("Inserting data to BigQuery...")

    write_to_bigquery(
        json_data=transformed_data,
        table_id=destination_table,
        project_id=project_id
    )

    return 'Massive success!', 200
