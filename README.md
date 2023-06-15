# Shodan and NVD API Integration
This script allows you to search the Shodan database for servers based on a query and check if these hosts have any associated Common Vulnerabilities and Exposures (CVEs) in the National Vulnerability Database (NVD).

## Dependencies
This script requires the requests library. You can install it with pip:

`pip install requests`

## Usage
First, replace 'your_shodan_api_key' with your actual Shodan API key in the script.

To run the script, use:

`python shodan_nvd_search.py`

When prompted, enter your query string to search for hosts in Shodan.

The script will then find the hosts related to your query in Shodan, and for each host, it will search for associated CVEs in the NVD database. The results will be printed on the screen.

## Note
This script does not handle errors that might occur if the Shodan or NVD API is not reachable. It also does not handle rate limiting, so if you're planning to use this script heavily, you might want to add some functionality to handle that. It also assumes that each host has a 'product' field, which might not always be the case. Also, the NVD database is quite large, so the requests might take some time.
