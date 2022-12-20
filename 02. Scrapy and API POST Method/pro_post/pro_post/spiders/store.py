#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74774973/graphql-api-with-scrapy/74775409#74775409


import scrapy
import json
from scrapy.loader import ItemLoader

class StoresSpider(scrapy.Spider):
    name = 'stores'

    #Base url: https://www.ouedkniss.com/boutiques/immobilier
    #allowed_domains = ['www.ouedkniss.com']
  
    def start_requests(self):
        payload = {
            "operationName":"SearchStore",
            "variables":{
                "q":"",
                "filter":{
                "categorySlug":"immobilier",
                "count":12,
                "page": 1
                }},
            "query":"query SearchStore($q: String, $filter: StoreSearchFilterInput!) {\n  stores: storeSearch(q: $q, filter: $filter) {\n    data {\n      id\n      name\n      slug\n      description\n      imageUrl\n      followerCount\n      announcementsCount\n      url\n      mainLocation {\n        location {\n          region {\n            name\n            __typename\n          }\n          city {\n            name\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      announcements(count: 6, page: 1) {\n        data {\n          id\n          defaultMedia(size: SMALL) {\n            mediaUrl\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    paginatorInfo {\n      lastPage\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        headers= {
            "Content-Type": "application/json",
            # "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            }
       
        for payload['variables']['filter']['page'] in range(1,3):
            yield scrapy.Request(
                url='https://api.ouedkniss.com/graphql',
                method="POST",
                headers=headers,
                body=json.dumps(payload),
                callback=self.parse
                )
       
    

    def parse(self, response):
        json_resp = json.loads(response.body)
        #print(json_resp)
        
        stores = json_resp['data']['stores']['data']
        for store in stores:
            yield {
                'id':store['id']
            }
       
        