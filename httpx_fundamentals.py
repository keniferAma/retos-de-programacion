
import httpx
import time
import asyncio



# r = httpx.get('http://google.com.co')

# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(r.headers['content-type'])


# get = httpx.get('https://google.com.co')
# post = httpx.post('https://google.com.co/post', data={'key': 'value'})
# put = httpx.put('https://google.com.co/put', data={'key': 'value'})
# delete = httpx.delete('https://google.com.co/delete')
# options = httpx.options('https://google.com.co/options')
# head = httpx.head('https://google.com.co/head')


# # Pass parameters #
# parameters = {'key1': 'value1', 'key2': 'value2'}
# get_para = httpx.get('https://google.com.co', params=parameters)

# # Costume headers #
# costume_header = {'user-agent': 'app-v1.00'}
# post_header = httpx.post('https://google.com.co/post_with_headers', headers=costume_header)

# # json #
# json_data = {"title": "json", "boolean": True, "number": 1}
# r = httpx.post('https://google.com.co', json=json_data)

# # Cookies #
# r = httpx.get('https://google.com.co/cookies/set?chocolate=chip')
# #print(r.cookies['chocolate'])

# # Authentication #
# # httpx.get('https://google.com.co', auth={'key': 'value'})



# # Practices with web scraping with https://www.scrapethissite.com/ #

# client = httpx.Client() # assigning a Client object to reuse the instance 'client'

# get_response = client.get('https://www.scrapethissite.com/')

# print(get_response.status_code)
# print(get_response.text)


# get_response = client.get('https://www.scrapethissite.com/pages/forms/?q=boston')



# print(get_response.content)







# proving with no asynchronous function #
def no_async_fetch():
    urls = [
        'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'https://books.toscrape.com/catalogue/soumission_998/index.html',
        'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
    ]

    no_async_client = httpx.Client()

    result = [no_async_client.get(url) for url in urls]

    print(result)


init = time.time()
no_async_fetch()
"""[<Response [200 OK]>, <Response [200 OK]>, <Response [200 OK]>, <Response [200 OK]>]"""
"""1.349520206451416""" # Time that takes to execute all the 4 requests
end = time.time()
print(end - init)


# Proving with asynchronous function #
async def async_fetch():
    urls = [
        'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'https://books.toscrape.com/catalogue/soumission_998/index.html',
        'https://books.toscrape.com/catalogue/sharp-objects_997/index.html'
    ]

    async_client = httpx.AsyncClient()

    reqs = [async_client.get(url) for url in urls]

    result = await asyncio.gather(*reqs)

    print(result)

init = time.time()
asyncio.run(async_fetch())
"""[<Response [200 OK]>, <Response [200 OK]>, <Response [200 OK]>, <Response [200 OK]>]"""
"""0.6505711078643799""" # Execution time decreases 
end = time.time()
print(end - init)
