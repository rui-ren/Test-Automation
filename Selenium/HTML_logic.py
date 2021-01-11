
# can you traverse back using css? no

# only xpath can do so!

# validate the item is the same in two pages


discountAmount = driver.find_element_by_css_selector(".discount").text

originalAmount = driver.find_element_by_css_selector(".discount").text

assert float(discountAmount) < float(discountAmount)

# use the CSS selector to locate the HTML item and 
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")

sum = 0

for amount in amounts:
    sum += int(amount.text)

# all the automation test cases!
assert sum == 388


