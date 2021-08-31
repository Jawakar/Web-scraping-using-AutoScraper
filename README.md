# Web-scraping-using-AutoScraper
AutoScraper is a smart scraper library that quickly scraps the webpage automatically and it is a lightweight web scraper for Python. I have built an `API` that uses autoscraper to scrap the data from a website. The data scraped will be in the form of a JSON file and it can be used in any database.
</br>

## Installing from PyPI
```Python
pip install autoscraper
```
</br>

## Importing AutoScraper class from autoscraper
```Pyhton
from autoscraper import AutoScraper
```
</br>

## Getting URL and creating a wanted list
Now get an URL from any websites, here I have taken from Amazon and have created a wanted list. The wanted list just holds the information to be scraped from that particular website.
```Python
# I want Alexa's data from amazon so I use the following URL
amazon_url='https://www.amazon.in/s?k=alexa'

# The below wanted list consists of image URL followed by title and price
wanted_list=['https://m.media-amazon.com/images/I/61KIy6gX-CL._AC_UY218_.jpg','All-new Echo Dot (4th Gen) | Next generation smart speaker with improved bass and Alexa (Black)','₹3,449']
```
</br>

## Building autoscraper
- Create an object for AutoScraper() class and use the build() function to build an autoscraper and group the data.
```Python
# Creating an object for AutoScraper()
scraper = AutoScraper()

# Building autoscraper with build()
result = scraper.build(amazon_url,wanted_list)

#By using get_result_similar() function, we group into three groups according to our wanted list
data = scraper.get_result_similar(amazon_url, grouped=True)

print(data)
```
- Here is the output with their rules.
```Python
{'rule_nh7g': ['https://m.media-amazon.com/images/I/61KIy6gX-CL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61MbLLagiVL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61EXU8BuGZL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61u0y9ADElL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61V25P7mlyL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/51UZ17lvVFL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61EXU8BuGZL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61-DjUz7JxL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61RvgtLChZL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/618AB7m2HML._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61NIsUGl+FL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61fAoBkYQ1L._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61fAoBkYQ1L._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/61RyEv5mnNL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/51b9EVQUNNL._AC_UY218_.jpg', 'https://m.media-amazon.com/images/I/51mXq6pWMYL._AC_UY218_.jpg'], 'rule_0eo0': ['All-new Echo Dot (4th Gen) | Next generation smart speaker with improved bass and Alexa (Black)', 'All-new Echo Dot (4th Gen) | Next generation smart speaker with improved bass and Alexa (Blue)', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (Black)', 'All-new Echo Dot (4th Gen) with clock | Next generation smart speaker with improved bass, LED display and Alexa (Blue)', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (Purple)', 'Introducing Echo Show 8 – Smart display with Alexa - 8" HD screen with stereo sound – Black', 'Echo Dot (3rd Gen), Certified Refurbished, Black – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (Black)', 'Introducing Echo Show 5 - Smart display with Alexa - 5.5" screen & crisp sound (White)', 'Echo Dot (3rd Gen, Purple) Combo with Wipro 9W LED Smart Color Bulb - Smart Home Starter Kit', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (Blue)', 'Echo Dot (3rd Gen), Certified Refurbished, White – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (White)', 'Echo Dot (3rd Gen), Certified Refurbished, Grey – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'Echo Auto - add Alexa to your car', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (White)'], 'rule_x4sz': ['All-new Echo Dot (4th Gen) | Next generation smart speaker with improved bass and Alexa (Black)', 'All-new Echo Dot (4th Gen) | Next generation smart speaker with improved bass and Alexa (Blue)', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (Black)', 'All-new Echo Dot (4th Gen) with clock | Next generation smart speaker with improved bass, LED display and Alexa (Blue)', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (Purple)', 'Introducing Echo Show 8 – Smart display with Alexa - 8', 'Echo Dot (3rd Gen), Certified Refurbished, Black – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (Black)', 'Introducing Echo Show 5 - Smart display with Alexa - 5.5', 'Echo Dot (3rd Gen, Purple) Combo with Wipro 9W LED Smart Color Bulb - Smart Home Starter Kit', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (Blue)', 'Echo Dot (3rd Gen), Certified Refurbished, White – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'Echo Dot (3rd Gen) – Smart speaker with Alexa (White)', 'Echo Dot (3rd Gen), Certified Refurbished, Grey – Improved smart speaker with Alexa – Like new, backed with 1-year warranty', 'Echo Auto - add Alexa to your car', 'All-new Echo (4th Gen) | Premium sound powered by Dolby and Alexa (White)'], 'rule_4uln': ['₹3,449', '₹4,499', '₹3,449', '₹4,499', '₹2,449', '₹4,499', '₹4,449', '₹5,499', '₹2,449', '₹4,499', '₹8,499', '₹12,999', '₹2,999', '₹3,799', '₹5,999', '₹9,999', '₹4,999', '₹8,999', '₹2,499', '₹6,598', '₹6,999', '₹9,999', '₹2,999', '₹3,799', '₹2,449', '₹4,499', '₹2,999', '₹3,799', '₹2,999', '₹4,999', '₹6,999', '₹9,999'], 'rule_nabn': ['₹3,449', '₹4,499', '₹3,449', '₹4,499', '₹2,449', '₹4,499', '₹4,449', '₹5,499', '₹2,449', '₹4,499', '₹8,499', '₹12,999', '₹2,999', '₹3,799', '₹5,999', '₹9,999', '₹4,999', '₹8,999', '2499.00', '6598.00', '₹6,999', '₹9,999', '₹2,999', '₹3,799', '₹2,449', '₹4,499', '₹2,999', '₹3,799', '₹2,999', '₹4,999', '₹6,999', '₹9,999'], 'rule_l78b': ['₹3,449', '₹4,499', '₹3,449', '₹4,499', '₹2,449', '₹4,499', '₹4,449', '₹5,499', '₹2,449', '₹4,499', '₹8,499', '₹12,999', '₹2,999', '₹3,799', '₹5,999', '₹9,999', '₹4,999', '₹8,999', '₹2,499', '₹6,598', '₹6,999', '₹9,999', '₹2,999', '₹3,799', '₹2,449', '₹4,499', '₹2,999', '₹3,799', '₹2,999', '₹4,999', '₹6,999', '₹9,999'], 'rule_bmwz': ['₹3,449', '₹4,499', '₹3,449', '₹4,499', '₹2,449', '₹4,499', '₹4,449', '₹5,499', '₹2,449', '₹4,499', '₹8,499', '₹12,999', '₹2,999', '₹3,799', '₹5,999', '₹9,999', '₹4,999', '₹8,999', '2499.00', '6598.00', '₹6,999', '₹9,999', '₹2,999', '₹3,799', '₹2,449', '₹4,499', '₹2,999', '₹3,799', '₹2,999', '₹4,999', '₹6,999', '₹9,999']}
```
- Assume the rule IDs with appropriate aliases and these rule IDs will get changed every time we try to execute this.
```Python
# Find the rule IDs from the output
# set_result_aliases() is used to set names as alias
scraper.set_rule_aliases({'rule_0eo0':'Title', 'rule_nh7g':'ImageUrl', 'rule_4uln':'Price'})

# Keeping this rule for other pages also
scraper.keep_rules(['rule_0eo0','rule_nh7g','rule_4uln'])
```
- Save as a JSON file
```Python
scraper.save('amazon-search.json')
```
</br>

## Building an `API`
Here, the API is defined with the parameter q as our search query, the search query will retrieve data as a valid JSON.
```Python
# install flask
pip install flask

from autoscraper import AutoScraper
# request library is used to retrieve results according to our query
from flask import Flask, request

amazon_scraper = AutoScraper()
# loading the JSON file which we have saved earlier
amazon_scraper.load('amazon-search.json')
app = Flask(__name__)

# get_amazon_result() returns the result URL 
def get_amazon_result(search_query):
    url = 'https://www.amazon.in/s?k=%s' % search_query
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

# _aggregate_result() formats the data
def _aggregate_result(result):
    final_result = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:
            final_result.append({alias:result[alias][i] for alias in result})
        except:
            pass
    return final_result

# This method gathers that specific query we write
@app.route('/',methods=['GET'])
def search_api():
    query = request.args.get('q')
    print(query)
    return dict(result=get_amazon_result(query))

if __name__=='__main__':
    app.run(port=8080, host='0.0.0.0')
```
</br>

The screenshot below is a validated JSON output from the created API.

![JSON_JBL_Output](https://user-images.githubusercontent.com/52590526/116808190-18b4bd00-ab55-11eb-941f-0d5d8b1c5b11.JPG)
</br></br>

Just replace `JBLspeaker` in the URL with any other query to get its search results as done in the gif below. </br>

![SearchGif](https://user-images.githubusercontent.com/52590526/116809238-a515ae80-ab5a-11eb-8def-4948afeaaaeb.gif)
</br>
This is like a `search engine` which will help us to find out the `title`, `imageURL` and `price` of the product we search for.</br>
And you can validate the JSON and thereby can upload it to our databases.
</br>
</br>
You could also scrape data to a csv file by going through my blog. [click here to visit my blog](https://medium.com/@jawakarselvavinayagam/scrape-data-from-web-to-csv-in-minutes-dfbaa1e8775d)

## Acknowledgment
I thank [Alirezamika](https://github.com/alirezamika/autoscraper) for creating this wonderful library which makes our works easier when it comes to scraping the data.
