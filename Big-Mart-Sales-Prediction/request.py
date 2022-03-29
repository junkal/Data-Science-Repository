import io
import os
import requests
import argparse
import json
import pandas as pd

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument("-data", type = str, default=None, help="path way to the csv file")
    parser.add_argument("-ip", type = str, default='127.0.0.1:4000', help="ip address:port of service")

    return parser


def predict(data, url):

    payload = {"data": json.dumps(data).encode('utf-8')}

    headers = {'X-Access-Tokens': '1@3$582Dwj77'}

    # submit the request
    response = requests.post(url+"predict_batch", headers = headers, files=payload)

    if response.status_code == 200:
        # ensure the request was sucessful
        data = response.json()
        print("[INFO] POST successful, success:{}, data_size:{}, result: {}, time taken: {}s"
            .format(data["success"], data["data_size"], data["result"], response.elapsed))
    else:
        print("[ERROR] POST not successful, status {} reason {}".format(response.status_code, response.reason))

def predict(data, url, mode):

    payload = { "data": json.dumps(data).encode('utf-8'), "mode": mode}

    headers = {'X-Access-Tokens': '1@3$582Dwj77'}

    # submit the request
    response = requests.post(url+"predict", headers = headers, files=payload)

    if response.status_code == 200:
        # ensure the request was sucessful
        data = response.json()
        print("[INFO] POST successful, success:{}, data_size:{}, result: {}, time taken: {}s"
            .format(data["success"], data["data_size"], data["result"], response.elapsed))
    else:
        print("[ERROR] POST not successful, status {} reason {}".format(response.status_code, response.reason))


def main(args = None):
    parser = parse_opt()
    args = parser.parse_args(args)

    URL = "http://" + args.ip + "//"

    if args.data is not None:
        data = pd.read_csv(args.data)
        predict(data.to_dict(), URL, mode='batch')
    else:
        data = {'Item_Identifier':	'FDW58',
                'Item_Weight': 20.75,
                'Item_Fat_Content':	'Low Fat',
                'Item_Visibility':	'0.007564836',
                'Item_Type': 'Snack Foods',
                'Item_MRP' : 107.8622,
                'Outlet_Identifier': 'OUT049',
                'Outlet_Establishment_Year': 1999,
                'Outlet_Size': 'Medium',
                'Outlet_Location_Type': 'Tier 1',
                'Outlet_Type': 'Supermarket Type1'}

        predict(data, URL, mode='single')

if __name__ == '__main__':
    main()
