from bs4 import BeautifulSoup
import requests

session = requests.Session()



with open('sites') as f:
    ogSites = f.read().splitlines()

# print ogSites
def removeEnding():
    sites = []
    for url in ogSites:
        if '/sitemap_products_1.xml' in url:
            newLink = url.replace('/sitemap_products_1.xml', '')
            sites.append(newLink)

        elif 'sitemap_products_1.xml' in url:
            newLink = url.replace('sitemap_products_1.xml', '')
            sites.append(newLink)

        else:
            sites.append(url)

    with open('sites', 'w') as f:
        for url in sites:
            f.write(url + '\n')


def checkShopify(url):
    newUrl = url + '/admin'
    try:
        r = session.get(newUrl , timeout=10)
        if 'admin/auth/login' in r.url:
            return True
        else:
            return False

    except:
        pass



shopifySiteList=[]
count = 0
for url in ogSites:
    count += 1
    if checkShopify(url):
        print 'found and added', count
        shopifySiteList.append(url)
        with open('shopifySiteList.txt', 'a') as f:
            f.write(url+'\n')
    else:
        print 'Not a shopify Site'
