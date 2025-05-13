import asyncio
from playwright.async_api import async_playwright
links: list[str] = ["https://bot.incolumitas.com/"]
#"https://amiunique.org/fp"]
async def visit_fingerprint_site(headless: bool=True) -> None:
    async with async_playwright() as p:
        for link in links:
            browser = await p.chromium.launch(headless=headless)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(link)
            if link == links[0]:
                await page.get_by_placeholder("Text input").fill("noob")
                await page.get_by_placeholder("Email input").fill("ligma@gmail.com")
                await page.get_by_role("checkbox", name="terms").check()
                await page.locator("#smolCat").check()
                await page.locator("#submit").click()

            print(f"Opened with headless={headless}. You have 10 seconds to inspect.")
            await page.wait_for_timeout(100000)  # 10 seconds to manually inspect
            await browser.close()
            # Locator for when you want raw control, get by for cleanf flow

# Run both headless and headful manually
async def main():
    await visit_fingerprint_site(headless=False)
    await visit_fingerprint_site(headless=True)

asyncio.run(main())

# import asyncio
# from playwright.async_api import async_playwright

# async def solve_challenge(page):
#     await page.wait_for_selector('#formStuff')

#     await page.locator('[name="userName"]').click(click_count=3)
#     await page.locator('[name="userName"]').fill("bot3000")

#     await page.locator('[name="eMail"]').click(click_count=3)
#     await page.locator('[name="eMail"]').fill("bot3000@gmail.com")

#     await page.get_by_text("I agree to this").check()
#     await page.check('#smolCat')
#     await page.check('#bigCat')


#     await page.select_option('[name="cookies"]', label="I want all the Cookies")
#     await page.click('#smolCat')
#     await page.click('#bigCat')
#     await page.click('#submit')

#     async def handle_dialog(dialog):
#         print("Dialog says:", dialog.message)
#         await dialog.accept()
#     page.on("dialog", handle_dialog)

#     await page.wait_for_selector('#tableStuff tbody tr .url')

#     await asyncio.sleep(0.1)

#     await page.click('#updatePrice0')
#     await page.wait_for_function("!!document.getElementById('price0').getAttribute('data-last-update')")

#     await page.click('#updatePrice1')
#     await page.wait_for_function("!!document.getElementById('price1').getAttribute('data-last-update')")

#     # Scrape results from the table
#     data = await page.evaluate('''() => {
#         const results = [];
#         document.querySelectorAll('#tableStuff tbody tr').forEach(row => {
#             results.push({
#                 name: row.querySelector('.name').innerText,
#                 price: row.querySelector('.price').innerText,
#                 url: row.querySelector('.url').innerText,
#             });
#         });
#         return results;
#     }''')
#     print("Scraped table data:", data)

#     # Read internal detection results
#     new_tests = await page.inner_text('#new-tests')
#     old_tests = await page.inner_text('#detection-tests')

#     print("New detection tests:", new_tests)
#     print("Old detection tests:", old_tests)


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
#         context = await browser.new_context(viewport=None)
#         page = await context.new_page()
#         await page.goto('https://bot.incolumitas.com/')
#         await solve_challenge(page)
#         await page.wait_for_timeout(5000)
#         await browser.close()

# asyncio.run(main())
