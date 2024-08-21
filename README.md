# Weather API -> weather -> BigQuery

This pipeline moves data from weather API to our project in BigQuery


## Setup

First, set an environemnt variable for the API KEY

```
export API_KEY=value_here
```

## Run

Start functions framework. `--debug`
```
functions-framework --target main --debug
```

## Test

Send a random request
```
curl -X POST http://localhost:8080/ \
    -H "Content-Type: application/json" \
    -d '{"key": "value"}'
```

Should get a response like
```
Massive success!
```