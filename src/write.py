from google.cloud import bigquery


def write_to_bq(json_data: str, table_id: str):

    client = bigquery.Client()

    errors = client.insert_rows_json(table_id=table_id, data=json_data)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
