# -*- coding: utf-8 -*-
import scrapy
from scrapy.log import logger


def parse_query(url):
    queries = url.split("?")[-1]
    params = dict()
    for item in queries.split("&"):
        tmp = item.split("=")
        params[tmp[0]] = tmp[1]
    return params


def build_url(url, queries: dict):
    # Strim queries from url
    base_url = url.split("?")[0]
    base_url = base_url + "?" + "&".join(["%s=%s" % (k, v) for k, v in queries.items()])
    return base_url


class Mainlv2Spider(scrapy.Spider):
    name = 'mainlv2'
    allowed_domains = ['jet.com']
    start_urls = []
    headers = {
        "Authorization": "3ff84632-35e9-49b7-8a3a-7638cdd208cf",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Accept": "*/*",
        "Cookie": "X-Akamai-Chosen=jet_com_phased_prod_eastus2; jet.csrf=82V5sTDmjkcnLtHwj7CrIfbi; signupShown=0; jid=d87295c4-7aa5-4fcd-8362-9f8b1ca81f99; jet-referer=%2Fc%2Fhome%2F4826017542%3F%3D; jet-phaser=2%3B09bd0e1298064478aee0bf0e5630be44%3B4OyK%3B4cxPUB%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563379918; jet-id=b3c4ff9f-5aab-496e-8244-a8bc96a0c776; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJjYzRhZDNjYjUxYjk0N2JjOWI3OWI2MmJhZGM5MDY0NyIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.5f2eY6NkohDL1RTIJ0kzp0ZZF4_bmLTjn0wXl3z6b-E; ak_bmsc=62678B129AB5A2068F285FD36872B9E5172B304D1A160000CF482F5D11685102~plbCVmtTj3vNUd7DwBXpVoygx/cCOU+pKiyLyo78zbQlQN7hqiEKGGM8S5aeHkS8YkLM+gwb/UZvqm0s1CTajikJf0FW37b43hetKLFIuoXjwJdMMtjjzGO2CyRi26okNFzKn+fCijvfmlWRy7WAQe4a+UpaW4UxRDb1QZFTI4z8teN5c2tuYSMjeDSpgfBf9pXfB9M0oB6hfKcfo0xQ6VTGEkzJ0xskCyb+cvSRNHFoM=; akacd_phased_release=3740832716~rv=11~id=618db41dcf630b9ae0f25a506fff8171"
    }
    with open("level2.txt") as f:
        for line in f:
            start_urls.append("https://jet.com" + line.strip())

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=self.headers)

    def parse(self, response):
        with open("level3_product.txt", "a+") as f:
            if len(response.css("div.dGInLu > div")) >= 1:
                try:
                    urls = response.css("div.dGInLu > div")[1].css("div > a::attr(href)").extract()
                    for u in urls:
                        f.write(u + "\n")

                    request_url = response.url
                    queries = parse_query(request_url)

                    if "page" in queries:
                        if len(queries["page"].strip()) > 0:
                            queries["page"] = int(queries["page"]) + 1
                    else:
                        queries["page"] = 2

                    new_url = build_url(request_url, queries)

                    logger.info("Next page: %s", new_url)

                    yield scrapy.Request(url=new_url,
                                         callback=self.parse,
                                         dont_filter=False)

                except Exception as e:
                    logger.exception("Error on url %s: %s", response.url, e)
                    with open("error_lv2.txt", "a+") as f:
                        f.write(response.url + "\n")
                    return
            else:
                logger.info("Crawling level 2")
                self.parse_lv2(response)
                return

    def parse_lv2(self, response):
        try:
            urls = response.css("div.kUwsKn > div")[0].css("div>div>span>a::attr(href)").extract()
            logger.info("Write %s urls ", len(urls))
            with open("level2_add.txt", "a+") as f:
                for url in urls:
                    f.write(url + "\n")
            # for url in urls:
            #     yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

        except Exception as e:
            logger.exception("Cannot crawl url level from url %s: %s", response.url, e)
