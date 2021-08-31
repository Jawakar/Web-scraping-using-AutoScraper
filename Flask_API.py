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