import requests
import json

SHODAN_API_KEY = 'your_shodan_api_key'
NVD_API_URL = 'https://services.nvd.nist.gov/rest/json/cves/1.0'

def get_shodan_results(query):
    shodan_url = f'https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}'
    response = requests.get(shodan_url)
    data = response.json()
    return data['matches']

def get_cves_for_product(product):
    params = {'keyword': product}
    response = requests.get(NVD_API_URL, params=params)
    data = response.json()
    return data['result']['CVE_Items']

def main():
    query = input('Enter your query: ')
    results = get_shodan_results(query)

    for result in results:
        product = result.get('product')
        if product:
            print(f'Product: {product}')
            cves = get_cves_for_product(product)
            for cve in cves:
                print(f"CVE: {cve['cve']['CVE_data_meta']['ID']}, Description: {cve['cve']['description']['description_data'][0]['value']}")
        else:
            print('No product info for this host.')

if __name__ == '__main__':
    main()