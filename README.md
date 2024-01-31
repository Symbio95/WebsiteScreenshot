# WebsiteScreenshot
Creates a API which takes an website as a query parameter and returns a "Screenshot" of the whole website.

e.g. 192.02.75.01:8000?url=https://www.ebay.de/itm/404492733074 would return a picture (PNG format) of this ebay site.

TODO:
make it more scaleable - currently opening a new selenium browser for each request which makes it way less error prone but slow
more query parameters - for example only show 50% of the site height or custom sleep time for all elements to load on the site
