## Logs

- Mock API's?
- Can work with placeholder in playwright because straight forward

- Use text locators to find non interactive aelements like div, span, p
- Use role locators for elements that are interactive like button, a, input

- Custom set attruibutes can be defined, playwright.slectors.set_test_id_attribute(""), switches the test id

- page.locator()

- Good practice is to come up with locator so not brittle when DOM structure changes

- Amazon website changes so strucutre probaby changes and even with same url can't control what comes

- alt locators for img or area
- .filter() option to tack on after

- Able to chain locators .getbyrole.filter
- page.get_by_role("button").and_(page.getbyTitle("Subscribe")) Narrows down locators further

- locator.or_() chooses one or other
- What is expect in playwright?
- What about is visible? .filter(visible=True)
- data-testid found by page.get_by_test_id()
- get item from list using .nth(i) element you want
- Delve more into chaining filters, filter(has = page.get_by_role("button", name= "say goodbye"))
- .all() do something with every item in a list
- can iterate with a for loop

- CSS selectors are not reccomended!!!!!!
- Other locators important


supported ids:
id
data-testid
data-test-id
data-test

- # Fill an input with the id "username"
page.locator('id=username').fill('value')

# Click an element with data-test-id "submit"
page.locator('data-test-id=submit').click()

- chain locators not selectors
