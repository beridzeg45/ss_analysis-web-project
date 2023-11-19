from imports import *


daily_article_urls = []

def scrape_page(page):
    try:
        page_url = f'https://home.ss.ge/ka/udzravi-qoneba/l/bina/iyideba?cityIdList=95&currencyId=1&order=1&page={page}'
        page_html = requests.get(page_url).content
        page_soup = BeautifulSoup(page_html, 'html.parser')

        articles = page_soup.select('div[class*="sc-af116d90-0"]')

        article_urls=[]
        for article in articles:
            try:
                href = article.select_one('a')['href']
                article_url = 'https://home.ss.ge' + href
                article_urls.append(article_url)
            except:
                return None
            
        return article_urls

    except:
        pass

cores=multiprocessing.cpu_count()

if __name__=="__main__":
    with multiprocessing.Pool(cores) as pool:
        pages=range(1,1501)
        results=list(tqdm(pool.imap(scrape_page,pages),total=len(pages)))

    for result in results:
        try:
            daily_article_urls=daily_article_urls+result
        except:
            pass
daily_article_urls=set(daily_article_urls)
pickle.dump(daily_article_urls,open('data/daily_article_urls.pickle','wb'))

print('All done')