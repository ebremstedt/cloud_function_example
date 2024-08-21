import json
import pendulum


def parse_json_response(data: str):

    data_dict = json.loads(s=data)

    print(data_dict)

    formatted_data = {
        'location': data_dict['location'],
        'hour': data_dict['forecast']['forecastday'][0]['hour']
    }

    parsed_json_response = []
    for hour in formatted_data['hour']:
        ingestion_timestamp = pendulum.now().format('YYYY-MM-DD HH:mm:ss')
        modified_timestamp = pendulum.from_format(formatted_data['location']['localtime'], 'YYYY-MM-DD HH:mm').format('YYYY-MM-DD HH:mm:ss')
        data = json.dumps(hour, indent=4)
        parsed_json_response.append(
            {
                "ingestion_timestamp":ingestion_timestamp,
                "modified_timestamp":modified_timestamp,
                "data":data
            }
        )
    return parsed_json_response
