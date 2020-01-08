#! /usr/bin/env python
import requests,json

def clear_cache(list):
	for host in list:
		params = (('host_name', host),)

		response = requests.get('https://infoblox/wapi/v2.9.1/member:dns', params=params, verify=False, auth=('user', 'pass'))

		if response.status_code == requests.codes.ok:
			r = response.json()

			for dict in r:
				params = (('_function', 'clear_dns_cache'),)
				response = requests.post('https://infoblox/wapi/v2.9.1/' + dict['_ref'], params=params, verify=False, auth=('user', 'pass'))

				if response.status_code == requests.codes.ok:
					cache_response = response.json()

if __name__ == '__main__':
	host_list = ['ukx1dn65.msm','ukx1dn64.msm']
	clear_cache(host_list)
