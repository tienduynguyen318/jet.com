# -*- coding: utf-8 -*-

# Scrapy settings for jetcom project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jetcom'

SPIDER_MODULES = ['jetcom.spiders']
NEWSPIDER_MODULE = 'jetcom.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jetcom (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept-Language': 'en',
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  'Cookie':'jet.csrf=QMZ9K_h7TtrRem1cUsjUC59C; signupShown=0; jid=032a278b-f5ad-4878-bc8b-5373147a4aa5; jet-id=75abe698-2283-4b97-af25-2573cd39e36e; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiI5OGRjNjQyODUwNWY0ZDI1OGI5MzQwMzM5MzU1OGJhOCIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.WoCIEVBptpTQQ2ypDTnovsOr0aJn8hqWJHB-TF8Emjk; X-Akamai-Chosen=jet_com_phased_prod_eastus2; akacd_phased_release=3740741317~rv=55~id=f128a80c50fe167436e09d556ac2b293; AMCVS_A7EE579F557F617B7F000101%40AdobeOrg=1; _sdsat_cart_status=inactive; s_cc=true; _hjIncludedInSample=1; _sdsat_adobe_mcid=12163799809764216403973836437884974460; __ssid=812e71a0711a679068f4e28f1ef248a; _gcl_au=1.1.488171996.1563288539; _scid=9fd6c2b6-f9af-4759-8c95-192bbb3b979c; IR_gbd=jet.com; jet-phaser=2%3B608cc2d64db049e98efa704d753e3eff%3B4Nk66%3B4OyK%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9V3mr%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563288538; cto_lwid=711f599f-c91c-48cf-8a9c-bd079284743a; brwsr=d9249ae6-a7d8-11e9-9c98-42010a246302; __qca=P0-1767397179-1563288539017; _sctr=1|1563210000000; __pr.NaN=580oihgbkf; __pr.11xw=cnaaa39daq; s_sq=%5B%5BB%5D%5D; ak_bmsc=9E3B2EF360611B56F0D03A8F183A19AE172B304D1A1600000E462F5D8F354F5C~plNeY7rRMNW954D4uWcscQ7sRiwQh7RPdz9R/eYy4xqXHOCwZd85NgzwNzXU2/6MuqWrRqxHX5+kL3XNZOIpIyxjaJ35u3fchOQfJfHuHP+ERhoSIiEHvNpfZhRn2sHA5+k45zjmX4KsjkTdCqAy7yDd9g7HUv2O/UOj5sgIWEd0kk9tTrWQGQ5WE3wN9/qyjoX9fxPBwMvcneLZXpWLEhexqxJXwa7CrujJTH0GSckCErfFZ5XPneQUiOW9Gyg8Fa; jet-referer=%2Fc%2Fhome%2F4826017542; _tq_id.TV-098163-1.3372=bdc9c256f07cb6db.1563288542.0.1563379719..; IR_PI=d9249ae6-a7d8-11e9-9c98-42010a246302%7C1563466119067; IR_9768=1563379719067%7Cc-15418%7C1563379218532%7C%7C; _derived_epik=dj0yJnU9dkZOQ0tibUpsOW45NWtTckx4ZzhhZHBRU05NZ1dGMmImbj1tekZPQmk3Y3EtdUhIck9jZEt0cHBnJm09MSZ0PUFBQUFBRjB2U0FjJnJtPTEmcnQ9QUFBQUFGMHZTQWM; bm_sv=F42EBDB0B8EEF084CF3C5408B6C78F98~L+oVH/n2Yvw7sg+qRjmqVMz4xAZ03CT8iLn33C95XT5gnVdyfIvH39iT7d1lDd18TZZ2/DO12W1TRv6t3y+mK47IgN/c9lDjzBkJOhaZFmWf9b8vT1YdD/HPC7hJqQPT/4OM3oHtxnADyejxjhfPNA==; AMCV_A7EE579F557F617B7F000101%40AdobeOrg=-330454231%7CMCIDTS%7C18094%7CMCMID%7C12163799809764216403973836437884974460%7CMCAAMLH-1563984559%7C11%7CMCAAMB-1563984559%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1563386416s%7CNONE%7CMCAID%7C2E857809052ABCAC-60000300C0067342%7CvVersion%7C3.1.2%7CMCCIDH%7C-102216157; X-Akamai-Chosen=jet_com_phased_prod_eastus2; jet.csrf=82V5sTDmjkcnLtHwj7CrIfbi; signupShown=0; jid=d87295c4-7aa5-4fcd-8362-9f8b1ca81f99; jet-referer=%2Fc%2Fhome%2F4826017542%3F%3D; jet-phaser=2%3B09bd0e1298064478aee0bf0e5630be44%3B4OyK%3B4cxPUB%3B77M5%3B7Gu1F%3B7JcBC6%3B7zf2a%3B936sX%3B93oFG%3B93tPLk%3B94Rq9%3B95vEc%3B98Cw0%3B98uMSm%3B9A0LU8%3B9CKK%3B9FMG%3B9G8b%3B9GQ1%3B9GSao%3B9GWrB4%3B9HLr%3B9HsEo%3B9IJbe%3B9IwMPW%3B9JJvH%3B9Jp4i%3B9MAixN%3B9PD3%3B9SRhDL%3B9UbxmC%3B9YQH%3B9dNn7%3B9eYdD%3B9edsL%3B9euSgL%3B9j7L%3B9jm0d%3B9lTaR3%3B9ln3%3B9rjURs%3B9roN6j%3B9vFW8X%3B9xOqTs%3B9y1Lc%3B9zfkN%3B1563379918; jet-id=b3c4ff9f-5aab-496e-8244-a8bc96a0c776; jet-jetGeoIp=%7B%22subdivisions_code%22%3A%22HN%22%2C%22city_name%22%3A%22Hanoi%22%2C%22country_code%22%3A%22VN%22%2C%22time_zone%22%3A%22Asia%2FHo_Chi_Minh%22%7D; jet-clientTicket=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJjYzRhZDNjYjUxYjk0N2JjOWI3OWI2MmJhZGM5MDY0NyIsImlzcyI6ImpldC5jb20iLCJhdWQiOiJ3ZWJjbGllbnQifQ.5f2eY6NkohDL1RTIJ0kzp0ZZF4_bmLTjn0wXl3z6b-E; ak_bmsc=62678B129AB5A2068F285FD36872B9E5172B304D1A160000CF482F5D11685102~plbCVmtTj3vNUd7DwBXpVoygx/cCOU+pKiyLyo78zbQlQN7hqiEKGGM8S5aeHkS8YkLM+gwb/UZvqm0s1CTajikJf0FW37b43hetKLFIuoXjwJdMMtjjzGO2CyRi26okNFzKn+fCijvfmlWRy7WAQe4a+UpaW4UxRDb1QZFTI4z8teN5c2tuYSMjeDSpgfBf9pXfB9M0oB6hfKcfo0xQ6VTGEkzJ0xskCyb+cvSRNHFoM=; akacd_phased_release=3740832716~rv=11~id=618db41dcf630b9ae0f25a506fff8171; bm_mi=D3DD23A12828F55D7A5AFEF20A2B96BB~ILKS88NFaR0BFuXxwfKRGhybOKYZH44daMXv8V2sHXvV19cdA4PWfvjmOHNXEUZ82wAhODNvVRO70w7EgSZcOU69OTq0N3RuXfcDoDLX1w3WXDtJOiKJxkcj4eRVk1KXkFQ9TvCbTlZHajGqdxiazjN88qlt6CSi97sJM3mYlAOzce6QvypxXD5E4uJh+YmMRgsru7yX3rLAr/QZUbN4kKW6qvRQsrRvOunFoXILyoXWtM7NBVrT/OrhANiV4mxw; bm_sv=C5ED61699CDAD75D36EFB9DB50399ECF~L+oVH/n2Yvw7sg+qRjmqVGe9yEW1Sfs9Lkmm1Csvfbf8TH9WISeKMi5xvcobLLMh5t4+9mdAzd9Kq/Xdm5mIPatlkzvhLSj8seCNQQWSrkIiv+8Eh3hOM5apgWjVdEocpO2l/0SEeJ6QEUKOOnfGhg==',
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jetcom.middlewares.JetcomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'jetcom.middlewares.RandomAgentDownloaderMiddleware': 543,
   'jetcom.middlewares.JetAgentDownloaderMiddleware': 544,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jetcom.pipelines.JetcomPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
