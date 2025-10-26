import serpapi
import pandas as pd


api1 = ''
api2 = ''
def search_google_scholar(engine: str, api_key: str, query: str, search_size: int):
    params = {
      "engine": engine,
      "q": query,
      "api_key": api_key,
      "start": 0
    }
    
    article_results = []
    count = 0
    articles_is_present = True
    while articles_is_present:
        search = serpapi.search(params)
        results = search.as_dict()
        for article in results['organic_results']:
            title = article["title"]
            try:
                link = article["link"]
            except:
                link = 'NA'
            authors_year = article["publication_info"]['summary']
            article_results.append({
                "title": title,
                "link": link,
                "authors_year": authors_year
            })
        count += 10
        if "next" in results.get("serpapi_pagination", []) and len(article_results) <= search_size:
            params['start'] = count
        else:
            articles_is_present = False
    df = pd.DataFrame({'author': [],
                       'link':[],
                       'title': [],
                       'year': []})
    for article in article_results:
        try:
            authors = article['authors_year'].split(' - ')[0]
        except:
            authors = 'NA'
        try:
            year_1 = article['authors_year'].split(' - ')[1]
            year_2 = year_1.split(', ')[1]
            year = year_2.split(' -')[0]
        except:
            year =' NA'
        article['author'] = authors
        article['year'] = year
        article.pop('authors_year')
        article = pd.DataFrame(article,index=[0])
        df = pd.concat([df, article], ignore_index=True)
    return df

argentina = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Argentina' AND 'cost')", search_size = 190)
bolivia = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Bolivia' AND 'cost')", search_size =  190)
colombia = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Colombia' AND 'cost')", search_size =  190)
venezuela = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Venezuela' AND 'cost')", search_size =  190)
mexico = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Mexico' AND 'cost')", search_size =  200)
peru = search_google_scholar(engine = 'google_scholar', api_key = api2, query = "('Chagas disease' AND 'Peru' AND 'cost')", search_size =  200)

with pd.ExcelWriter('results_google.xlsx') as writer:
    argentina.to_excel(writer, sheet_name='Argentina', index = False)
    bolivia.to_excel(writer, sheet_name='Bolivia', index = False)
    colombia.to_excel(writer, sheet_name='Colombia', index = False)
    mexico.to_excel(writer, sheet_name='Mexico', index = False)
    peru.to_excel(writer, sheet_name='Peru', index = False)
    venezuela.to_excel(writer, sheet_name='Venezuela', index = False)
    