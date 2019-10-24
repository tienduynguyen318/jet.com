# -*- coding: utf-8 -*-
import scrapy

from scrapy.log import logger


class Mainlv1Spider(scrapy.Spider):
    name = 'mainlv1'
    allowed_domains = ['jet.com']
    headers = {
        "Authorization": "3ff84632-35e9-49b7-8a3a-7638cdd208cf",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "*/*",
        "Cookie": "X-Akamai-Chosen=jet_com_phased_prod_eastus2; jet.csrf=82V5sTDmjkcnLtHwj7CrIfbi; signupShown=0; jid=d87295c4-7aa5-4fcd-8362-9f8b1ca81f99; jet-referer=%2Fc%2Fhome%2F4826017542%3F%3D; jet-phaser=2%3B09bd0e1298064478aee0bf0e5630be44%3B4OyK%3B4cxPUB%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563379918; jet-id=b3c4ff9f-5aab-496e-8244-a8bc96a0c776; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJjYzRhZDNjYjUxYjk0N2JjOWI3OWI2MmJhZGM5MDY0NyIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.5f2eY6NkohDL1RTIJ0kzp0ZZF4_bmLTjn0wXl3z6b-E; ak_bmsc=62678B129AB5A2068F285FD36872B9E5172B304D1A160000CF482F5D11685102~plbCVmtTj3vNUd7DwBXpVoygx/cCOU+pKiyLyo78zbQlQN7hqiEKGGM8S5aeHkS8YkLM+gwb/UZvqm0s1CTajikJf0FW37b43hetKLFIuoXjwJdMMtjjzGO2CyRi26okNFzKn+fCijvfmlWRy7WAQe4a+UpaW4UxRDb1QZFTI4z8teN5c2tuYSMjeDSpgfBf9pXfB9M0oB6hfKcfo0xQ6VTGEkzJ0xskCyb+cvSRNHFoM=; akacd_phased_release=3740832716~rv=11~id=618db41dcf630b9ae0f25a506fff8171"
    }

    start_urls = ['https://jet.com/c/home/4826017542?experienceId=25',
                  'https://jet.com/c/fashion/7932596029?experienceId=24',
                  'https://jet.com/c/beauty/2454290113?experienceId=27',
                  'https://jet.com/c/grocery-and-household/8098170768?experienceId=23',
                  'https://jet.com/c/baby/2000000?experienceId=21',
                  'https://jet.com/c/arts-crafts-and-hobbies/5000000?experienceId=21',
                  'https://jet.com/c/pet-supplies/11000000?experienceId=21',
                  'https://jet.com/c/office-supplies/12000000?experienceId=21',
                  'https://jet.com/c/category/1000000',
                  'https://jet.com/c/sporting-goods/17000000?experienceId=21'
                  ]

    def start_requests(self):
        for i in range(len(self.start_urls)):
            yield scrapy.Request(self.start_urls[i], headers=self.headers)

    def parse(self, response):
        urls = response.css("#__next > div")[1].css("div.eWvQyF > div > div > div >a::attr(href)").extract()
        if len(urls) == 0:
            logger.info("Not found urls in menu bar")
            logger.info("Try to fetch on top categories")
            urls = response.css("#__next  div.eIYDfA > div > div > a::attr(href)").extract()
            if len(urls) == 0:
                urls.append(response.url)

        with open("level2.txt", "a") as f:
            for url in urls:
                f.write(url + "\n")

        logger.info("Write %s urls to file", len(urls))
