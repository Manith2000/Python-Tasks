import bs4, requests

# res = requests.get(Website)
# soup = bs4.BeautifulSoup(res.text, 'html.parser') #finds html elemnts
# #res.text is the markup
# soup.select('Enter CSS address of element') #this can be found on the webpage by inspect elenment

def getamazonprice(amazonurl):
    res = requests.get(amazonurl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elm = soup.select('#price_inside_buybox') #this contains the CSS selector
    return elm

# price = getamazonprice('http://www.amazon.co.uk/Echo-Dot-3rd-Gen-Charcoal/')
# print(price)


def weather(weatherurl):
    res = requests.get(weatherurl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elm = soup.select('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._2h2vG.cc_cursor > div._3xWnK > span') #this contains the CSS selector
    return elm
condition = weather('http://weather.com/weather/today/l/25.41,51.51')
# print("It's a " + condition + " day" )
print(condition)




