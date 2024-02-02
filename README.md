# WebsiteScreenshot
Creates a API which takes an url as a query parameter and returns a "Screenshot" of the specified website.  

e.g. 127.0.0.1:8000?url=https://www.ebay.com/itm/404492733074 would return a picture (PNG format) of this ebay site.  

optional endpoints:  
timeout=3 (eg waits for website to load javascript content for 3 seconds)

install guide:  
pip install uvicron  
pip install fastAPI  
pip install playwright  
playwright install  
