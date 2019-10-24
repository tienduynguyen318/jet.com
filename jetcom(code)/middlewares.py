# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import numpy as np
from scrapy import signals

from scrapy.log import logger


class JetcomSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JetcomDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomAgentDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):
        with open("data/list_user_agent.txt") as f:
            self.user_agent_list = []
            for line in f:
                self.user_agent_list.append(line.strip().replace(",", ""))
        self.number_of_requests_interval = 100
        logger.info("Enable to get randon user-agent")

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def get_random_ua(self):
        idx = np.random.poisson(self.number_of_requests_interval) % len(self.user_agent_list)
        return self.user_agent_list[idx]

    def spider_opened(self, spider):
        self.user_agent = getattr(spider, 'user_agent', self.get_random_ua())

    def process_request(self, request, spider):
        if self.user_agent:
            user_agent = self.get_random_ua()
            logger.info(user_agent)
            request.headers.setdefault(b'User-Agent', user_agent)


class JetAgentDownloaderMiddleware(object):

    def __init__(self):
        self.cookies = [
            "X-Akamai-Chosen=jet_com_phased_prod_eastus2; jet.csrf=82V5sTDmjkcnLtHwj7CrIfbi; signupShown=0; jid=d87295c4-7aa5-4fcd-8362-9f8b1ca81f99; jet-referer=%2Fc%2Fhome%2F4826017542%3F%3D; jet-phaser=2%3B09bd0e1298064478aee0bf0e5630be44%3B4OyK%3B4cxPUB%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563379918; jet-id=b3c4ff9f-5aab-496e-8244-a8bc96a0c776; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJjYzRhZDNjYjUxYjk0N2JjOWI3OWI2MmJhZGM5MDY0NyIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.5f2eY6NkohDL1RTIJ0kzp0ZZF4_bmLTjn0wXl3z6b-E; ak_bmsc=62678B129AB5A2068F285FD36872B9E5172B304D1A160000CF482F5D11685102~plbCVmtTj3vNUd7DwBXpVoygx/cCOU+pKiyLyo78zbQlQN7hqiEKGGM8S5aeHkS8YkLM+gwb/UZvqm0s1CTajikJf0FW37b43hetKLFIuoXjwJdMMtjjzGO2CyRi26okNFzKn+fCijvfmlWRy7WAQe4a+UpaW4UxRDb1QZFTI4z8teN5c2tuYSMjeDSpgfBf9pXfB9M0oB6hfKcfo0xQ6VTGEkzJ0xskCyb+cvSRNHFoM=; akacd_phased_release=3740832716~rv=11~id=618db41dcf630b9ae0f25a506fff8171",
            "jet.csrf=QMZ9K_h7TtrRem1cUsjUC59C; signupShown=0; jid=032a278b-f5ad-4878-bc8b-5373147a4aa5; jet-id=75abe698-2283-4b97-af25-2573cd39e36e; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiI5OGRjNjQyODUwNWY0ZDI1OGI5MzQwMzM5MzU1OGJhOCIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.WoCIEVBptpTQQ2ypDTnovsOr0aJn8hqWJHB-TF8Emjk; X-Akamai-Chosen=jet_com_phased_prod_eastus2; akacd_phased_release=3740741317~rv=55~id=f128a80c50fe167436e09d556ac2b293; AMCVS_A7EE579F557F617B7F000101%40AdobeOrg=1; _sdsat_cart_status=inactive; s_cc=true; _hjIncludedInSample=1; _sdsat_adobe_mcid=12163799809764216403973836437884974460; __ssid=812e71a0711a679068f4e28f1ef248a; _gcl_au=1.1.488171996.1563288539; _scid=9fd6c2b6-f9af-4759-8c95-192bbb3b979c; IR_gbd=jet.com; jet-phaser=2%3B608cc2d64db049e98efa704d753e3eff%3B4Nk66%3B4OyK%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9V3mr%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563288538; cto_lwid=711f599f-c91c-48cf-8a9c-bd079284743a; brwsr=d9249ae6-a7d8-11e9-9c98-42010a246302; __qca=P0-1767397179-1563288539017; _sctr=1|1563210000000; __pr.NaN=580oihgbkf; __pr.11xw=cnaaa39daq; s_sq=%5B%5BB%5D%5D; ak_bmsc=9E3B2EF360611B56F0D03A8F183A19AE172B304D1A1600000E462F5D8F354F5C~plNeY7rRMNW954D4uWcscQ7sRiwQh7RPdz9R/eYy4xqXHOCwZd85NgzwNzXU2/6MuqWrRqxHX5+kL3XNZOIpIyxjaJ35u3fchOQfJfHuHP+ERhoSIiEHvNpfZhRn2sHA5+k45zjmX4KsjkTdCqAy7yDd9g7HUv2O/UOj5sgIWEd0kk9tTrWQGQ5WE3wN9/qyjoX9fxPBwMvcneLZXpWLEhexqxJXwa7CrujJTH0GSckCErfFZ5XPneQUiOW9Gyg8Fa; jet-referer=%2Fc%2Fhome%2F4826017542; _tq_id.TV-098163-1.3372=bdc9c256f07cb6db.1563288542.0.1563379719..; IR_PI=d9249ae6-a7d8-11e9-9c98-42010a246302%7C1563466119067; IR_9768=1563379719067%7Cc-15418%7C1563379218532%7C%7C; _derived_epik=dj0yJnU9dkZOQ0tibUpsOW45NWtTckx4ZzhhZHBRU05NZ1dGMmImbj1tekZPQmk3Y3EtdUhIck9jZEt0cHBnJm09MSZ0PUFBQUFBRjB2U0FjJnJtPTEmcnQ9QUFBQUFGMHZTQWM; bm_sv=F42EBDB0B8EEF084CF3C5408B6C78F98~L+oVH/n2Yvw7sg+qRjmqVMz4xAZ03CT8iLn33C95XT5gnVdyfIvH39iT7d1lDd18TZZ2/DO12W1TRv6t3y+mK47IgN/c9lDjzBkJOhaZFmWf9b8vT1YdD/HPC7hJqQPT/4OM3oHtxnADyejxjhfPNA==; AMCV_A7EE579F557F617B7F000101%40AdobeOrg=-330454231%7CMCIDTS%7C18094%7CMCMID%7C12163799809764216403973836437884974460%7CMCAAMLH-1563984559%7C11%7CMCAAMB-1563984559%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1563386416s%7CNONE%7CMCAID%7C2E857809052ABCAC-60000300C0067342%7CvVersion%7C3.1.2%7CMCCIDH%7C-102216157"
            ]

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def get_random_ua(self):
        idx = np.random.poisson(100) % len(self.cookies)
        return self.cookies[idx]

    def spider_opened(self, spider):
        self.cookie = getattr(spider, 'cookie', self.get_random_ua())

    def process_request(self, request, spider):
        if self.cookie:
            cookie = self.get_random_ua()
            request.headers.setdefault(b'Cookie', cookie)
