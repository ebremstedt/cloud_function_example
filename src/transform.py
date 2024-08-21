import json
from typing import Dict, List
import pendulum


def parse_json_response(data: str) -> List[Dict]:

    data_dict = json.loads(s=data)

    formatted_data = {
        'location': data_dict['location'],
        'hour': data_dict['forecast']['forecastday'][0]['hour']
    }

    # Visa exempel om list comprehension

    parsed_json_response = []
    for hour in formatted_data['hour']:
        metadata_modified = pendulum.now().format('YYYY-MM-DD HH:mm:ss')
        data_modified = pendulum.from_format(formatted_data['location']['localtime'], 'YYYY-MM-DD HH:mm').format('YYYY-MM-DD HH:mm:ss')
        data = json.dumps(hour, indent=4)
        parsed_json_response.append(
            {
                "metadata_modified": metadata_modified,
                "data_modified": data_modified,
                "data":data
            }
        )
    return parsed_json_response
