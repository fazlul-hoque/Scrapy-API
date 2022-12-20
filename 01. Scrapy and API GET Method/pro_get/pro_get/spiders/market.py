

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/74434125/webscraping-no-any-data-shown-in-scrapy/74435441#74435441

import scrapy
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
 
class ShareSpider(scrapy.Spider):
    name = "market"
   #Base url: https://nepsealpha.com/investment-calandar/ipo
    def start_requests(self):
        params = {
            "draw": "1",
            "columns[0][data]": "symbol",
            "columns[0][name]": "symbol",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "true",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "units",
            "columns[1][name]": "units",
            "columns[1][searchable]": "true",
            "columns[1][orderable]": "true",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "opening_date",
            "columns[2][name]": "opening_date",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "true",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "closing_date",
            "columns[3][name]": "closing_date",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "true",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "issue_manager",
            "columns[4][name]": "issue_manager",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "true",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "columns[5][data]": "status",
            "columns[5][name]": "status",
            "columns[5][searchable]": "true",
            "columns[5][orderable]": "true",
            "columns[5][search][value]": "",
            "columns[5][search][regex]": "false",
            "columns[6][data]": "view",
            "columns[6][name]": "view",
            "columns[6][searchable]": "true",
            "columns[6][orderable]": "true",
            "columns[6][search][value]": "",
            "columns[6][search][regex]": "false",
            "start": "0",
            "length": "10",
            "search[value]": "",
            "search[regex]": "false",
            }
        headers = {"X-Requested-With": "XMLHttpRequest"}
        
        for params["draw"] in range(1, 3):
            yield scrapy.Request(
                url= f'https://nepsealpha.com/investment-calandar/ipo?{urlencode(params)}',
                method = "GET",
                callback=self.parse,
                headers=headers

                )
    def parse(self,response):
        json_response = json.loads(response.body)
        res = json_response["data"]
        #print(res)
        for data in res:
            yield {
                "symbol": BeautifulSoup(data["symbol"],'html.parser').get_text(strip=True)   
                }