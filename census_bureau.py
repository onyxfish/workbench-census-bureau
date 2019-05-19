import numpy as np
import pandas as pd
import requests


API_URL_PATTERN = "https://api.census.gov/data/{vintage}/{dataset}"


def render(table, params, *, fetch_result, **kwargs):
    if not fetch_result:
        return pd.DataFrame()

    return fetch_result


# TODO: Make this async
def fetch(params, **kwargs):
    api_key = params["api_key"] or None
    dataset = params["dataset"]
    vintage = params["vintage"]
    variables = params["variables"] or None
    for_clause = params["for"] or None
    in_clause = params["in"] or None

    if not (dataset and vintage):
        return None

    url = API_URL_PATTERN.format(vintage=vintage, dataset=dataset)
    params = {}

    if api_key is not None:
        params["key"] = api_key

    if variables is not None:
        params["get"] = variables
    
    if for_clause is not None:
        params["for"] = for_clause

    if in_clause is not None:
        params["in"] = in_clause

    result = requests.get(url, params=params).json()

    return pd.DataFrame.from_records(result[1:], columns = result[0])