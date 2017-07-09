import requests

for i in range(20):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}
    url="http://other.51cto.com/php/get_channel_recommend_art_list.php?callback=jsonp1499596309886&page=2&type_id=519&type=recommend&page_size=19"
    response = requests.get(url,  headers = headers)
    print  response.text
    # print type(response.text)
    # f = open(str(i) + "_lagou.html", "a+")
    # f.write(response.text.dncode("ISO-8859-1").encode("utf8"))
    # f.close()
    print response.url
    print response.encoding
    print response.status_code