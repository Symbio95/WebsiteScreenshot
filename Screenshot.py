from fastapi import FastAPI
from fastapi.responses import FileResponse
from playwright.sync_api import sync_playwright
import time, uvicorn

path_for_pics = "C:/Projects/ScreenshotAPI/"

app = FastAPI()

@app.get("/")
def run(url: str, timeout: float | None = 0):
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=None)
        page.goto(url)
        time.sleep(timeout)

        filename = str(time.time())+".png"
        page.screenshot(path=path_for_pics+filename, full_page=True)
        return FileResponse(path_for_pics+filename)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
