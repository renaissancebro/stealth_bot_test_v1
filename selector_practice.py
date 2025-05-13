from playwright.sync_api import sync_playwright


"""
Goal:
1. Use 3 different playwright selectors and get information from site
2. Get comforatble with # to select
"""



link = "https://www.amazon.com/?tag=amazusnavi-20&hvadid=675149237887&hvpos=&hvnetw=g&hvrand=5837868742660567159&hvpone=&hvptwo=&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9007181&hvtargid=kwd-10573980&ref=pd_sl_7j18redljs_e&hydadcr=28883_14649097"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(link)
    page.wait_for_timeout(5000)
    print(page.title())
    page.get_by_placeholder("Search Amazon").fill("modem")
    if page.get_by_text("Gucci"):
        print("gucci was found")
    #Locator.filter()
    page.get_by_alt_text("Gucci")
    page.wait_for_timeout(1000)
    # Able to click the gucci icon and go to the page
    page.get_by_text("Gucci").click()
    page.wait_for_timeout(5000)
    print(page.get_by_text("Price, product page"))
    page.get_by_text("Price").click()

    page.wait_for_timeout(5000)
    browser.close()

