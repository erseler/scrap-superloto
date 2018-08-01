## scrap-superloto :money_with_wings:
A web scrapping project to fetch all lottery winning numbers, date, prizes etc. from [Milli Piyango official site](http://www.millipiyango.gov.tr/sonuclar/_cs_superloto.php). It requires:

- python 2.7
- Scrapy 1.5.1

### Settings
Waiting time between requests and caching options can be changed in [settings](https://github.com/erseler/scrap-superloto/blob/master/superloto/settings.py) file. Following settings are used by default:

    DOWNLOAD_DELAY = 0.5
    HTTPCACHE_ENABLED = True

### Run crawler
In order to run crawler, change directory to project file, then start crawling with spider name [getres](https://github.com/erseler/scrap-superloto/blob/master/superloto/spiders/getres.py):

    cd scrap-superloto-master
    scrapy crawl getres -o output.json
