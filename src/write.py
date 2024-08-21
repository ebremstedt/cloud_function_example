from google.cloud import bigquery


def write_to_bigquery(json_data: str, table_id: str, project_id: str):

    client = bigquery.Client(project=project_id)

    errors = client.insert_rows_json(table=table_id, json_rows=json_data)
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
