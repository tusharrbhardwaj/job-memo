from playwright.sync_api import sync_playwright
import bs4
from urllib.parse import urljoin

with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    
    page = browser.new_page()
    page.goto("https://tusharbhardwaj.dev")
    
    
    
    print(page.title())
    print(page.url)
    
    body = page.locator("body").inner_html()
    parsed_html = bs4.BeautifulSoup(body, "html.parser")

    links = parsed_html.find_all("a")
    
    unique_links = set()
    for link in links:
        full_link = urljoin(page.url, link.get("href"))
        
        if full_link.startswith("https://github.com/"):
            unique_links.update([f"{full_link}"])
    
    print("Unique Links pointing to Github : ")
    
    for each in unique_links:
        print(f"\t{each}")