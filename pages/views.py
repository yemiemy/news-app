from django.shortcuts import render

# importing the news api library
from newsapi import NewsApiClient



# Create your views here.
def index(request):
    # init
    newsapi = NewsApiClient(api_key='MY_NEWS_API')
    
    top_headlines = newsapi.get_top_headlines(
                                          sources='bbc-news,the-verge,bbc-news',
                                          language='en'
                                          )
    articles = top_headlines['articles']

    description = []
    news = []
    author = []
    pub = []
    news_url = []
    content = []

    for i in range(len(articles)):
        # get the article dictionary from the articles list of dictionaries
        latest_article = articles[i]

        # append the values of the keys below to their respective lists.
        author.append(latest_article['author'])
        news.append(latest_article['title'])
        description.append(latest_article['description'])
        pub.append(latest_article['publishedAt'])
        news_url.append(latest_article['url'])
        content.append(latest_article['content'])

    mycontext = zip(author, news, description, pub, news_url, content)
                                          
    return render(request, 'index.html', context={'mycontext':mycontext})

    
def comments(request):
    return render(request, 'comments.html')

# 0c2ec4fcf8064577b434de00580ba552
