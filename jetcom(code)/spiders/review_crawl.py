# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.log import logger

class ReviewCrawlSpider(scrapy.Spider):
    name = 'review-crawl'
    allowed_domains = ['jet.com']
    start_urls = ['https://readservices-b2c.powerreviews.com//m/786803/l/en_US/product/9addc593f494436d97d93af14d7b3e73/reviews?paging.size=5&filters=&search=&sort=Newest&image_only=false']

    headers = {
        "Authorization": "3ff84632-35e9-49b7-8a3a-7638cdd208cf",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "*/*",
        "Cookie": "X-Akamai-Chosen=jet_com_phased_prod_eastus2; jet.csrf=82V5sTDmjkcnLtHwj7CrIfbi; signupShown=0; jid=d87295c4-7aa5-4fcd-8362-9f8b1ca81f99; jet-referer=%2Fc%2Fhome%2F4826017542%3F%3D; jet-phaser=2%3B09bd0e1298064478aee0bf0e5630be44%3B4OyK%3B4cxPUB%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563379918; jet-id=b3c4ff9f-5aab-496e-8244-a8bc96a0c776; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJjYzRhZDNjYjUxYjk0N2JjOWI3OWI2MmJhZGM5MDY0NyIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.5f2eY6NkohDL1RTIJ0kzp0ZZF4_bmLTjn0wXl3z6b-E; ak_bmsc=62678B129AB5A2068F285FD36872B9E5172B304D1A160000CF482F5D11685102~plbCVmtTj3vNUd7DwBXpVoygx/cCOU+pKiyLyo78zbQlQN7hqiEKGGM8S5aeHkS8YkLM+gwb/UZvqm0s1CTajikJf0FW37b43hetKLFIuoXjwJdMMtjjzGO2CyRi26okNFzKn+fCijvfmlWRy7WAQe4a+UpaW4UxRDb1QZFTI4z8teN5c2tuYSMjeDSpgfBf9pXfB9M0oB6hfKcfo0xQ6VTGEkzJ0xskCyb+cvSRNHFoM=; akacd_phased_release=3740832716~rv=11~id=618db41dcf630b9ae0f25a506fff8171"
    }

    def parse(self, response):
        try:
            json_obj = json.loads(response.text())
            results = json_obj["results"]["reviews"]
            page_id = json_obj["results"]["page_id"]

            if len(results) > 0:
                with open("reviews.json","a+") as f:
                    for review in results:
                        review["page_id"] = page_id
                        f.write(json.dumps(review)+"\n")

            if "next_page_url" in  json_obj["paging"]:
                next_page_url = json_obj["paging"]["next_page_url"]
                if len(next_page_url) > 0:
                    logger.info("next paging: %s",next_page_url)
                    # yield scrapy.Request(url=next_page_url,
                    #                      headers=self.headers,
                    #                      callback=self.parse)

            return

        except Exception as e:
            logger.exception("Error to parse review: %s", e)
        pass
