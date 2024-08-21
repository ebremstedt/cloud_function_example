import os
from read import fetch_weather_data
from transform import parse_json_response
from write import write_to_bq


def main():
    api_key = os.getenv('API_KEY')
    project_id = os.getenv('GCP_PROJECT')

    print(project_id)

    api_url = "http://api.weatherapi.com/v1/history.json"
    destination_table = f"{project_id}.raw.weather"

    data = fetch_weather_data(
        api_key=api_key,
        api_url=api_url,
        location='STOCKHOLM',
        date='2024-08-14'
    )

    transformed_data = parse_json_response(data=data)

    write_to_bq(json_data=transformed_data, table_id=destination_table)


if __name__ == "__main__":
    main()