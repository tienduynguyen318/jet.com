Requirement
Install Postman
https://www.getpostman.com/downloads/
Install Python > 3.6
https://www.python.org/downloads/
Install Scrapy
https://scrapy.org/download/

Call api using postman 
https://www.quora.com/How-can-I-convert-cURL-code-to-Postman

API for review 
curl -X GET \
  'https://readservices-b2c.powerreviews.com/m/786803/l/en_US/product/9addc593f494436d97d93af14d7b3e73/reviews?paging.from=0&paging.size=5&filters=&search=&sort=Newest&image_only=false' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: 3ff84632-35e9-49b7-8a3a-7638cdd208cf' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: readservices-b2c.powerreviews.com' \
  -H 'Postman-Token: e7e7b556-3c8c-4bd7-ba6e-3a406657fb33,08c52a2a-0a16-420b-b1ab-0669b2ea7b99' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache'

change product id to continue crawling (9addc593f494436d97d93af14d7b3e73)
check paging
