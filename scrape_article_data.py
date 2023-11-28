from imports import *

daily_article_urls=list(pickle.load(open('data/daily_article_urls.pickle','rb')))

#scrape articles data
daily_data=[]
def scrape_article(argument):
    i,article_url,now,usd_gel_exchange_rate=argument
    try:
        article_html=requests.get(article_url).content
        article_soup=BeautifulSoup(article_html, 'html.parser')

        article_id=article_soup.select('span[class*="sc-6e54cb25-12 GRQvX"]')
        article_title=article_soup.select_one('div[class="screen-section"] div[class*="sc-"] h1[class="sc-6e54cb25-0 gDYjuA"]')
        date_published=article_soup.select('span[class*="sc-6e54cb25-12 GRQvX"]')
        appatment_price=article_soup.select_one('aside[class="detail-page-aside"] h4[id="price"]')
        appatment_address=article_soup.select_one('div[class="screen-section"] a[id="address"]')

        apparment_details_1={i.select_one('p').text:i.select_one('span[class="sc-6e54cb25-9 hndTLK"]').text if i.select_one('p') and i.select_one('span[class="sc-6e54cb25-9 hndTLK"]') else None
                            for i in article_soup.select('div[id="details_desc"] div[class="sc-81da871a-0 jzdJsr"] div[class="sc-81da871a-1 efseYp"]')}
        
        apparment_details_2={i.select_one('p').text:i.select_one('span[class="sc-6e54cb25-10 ezYsac"]').text if i.select_one('p') and i.select_one('span[class="sc-6e54cb25-10 ezYsac"]') else None
                            for i in article_soup.select('div[id="details_desc"] div[class*="sc-1b705347-0"] div[class="sc-1b705347-1 bwYjOT"]')}

        article_id=article_id[-1].text if article_id else None
        article_title=article_title.text if article_title else None
        date_published=date_published[-2].text if date_published else None
        appatment_price=appatment_price.text if appatment_price else None
        appatment_address=appatment_address.text if appatment_address else None

        aparment_data_dict={'Article ID':article_id,'Article URL':article_url,'Title':article_title,'Date Published':date_published,'Price':appatment_price,'USD-GEL Rate':usd_gel_exchange_rate,'Address':appatment_address,'Details_1':apparment_details_1,'Details_2':apparment_details_2,'Time Scraped':now}
        return aparment_data_dict
    except:
        return None

num_cores = multiprocessing.cpu_count()

if __name__ == "__main__":

    with multiprocessing.Pool(processes=num_cores) as pool:
        args_list = [(i, article_url, now, usd_gel_exchange_rate) for i, article_url in enumerate(daily_article_urls)]
        results = list(tqdm(pool.imap(scrape_article, args_list), total=len(args_list)))

    for i, result in enumerate(results, start=1):
        try:
            daily_data.append(result)
        except:
            daily_data.append(None)

    

#save daily data as csv
daily_data=[i for i in daily_data if i is not None]
daily_df=pd.DataFrame(daily_data)
daily_df.to_csv('data/daily_df.csv',index=False)
print(f'Finished Scraping {len(daily_df)}')

#save all time unprocessed
all_time_unprocessed=pd.read_csv('data/all_time_unprocessed.csv')
all_time_unprocessed=pd.concat([all_time_unprocessed,daily_df],ignore_index=True)
all_time_unprocessed=all_time_unprocessed.drop_duplicates(subset='Article ID')
all_time_unprocessed.to_csv('data/all_time_unprocessed.csv',index=False)


