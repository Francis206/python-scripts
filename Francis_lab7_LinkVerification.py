# IT 280 – Lab #7: Link Verification Lab by Francis
import re
import bs4
import requests
import validators


def checkStatus(res):
    if res.status_code == 200:
        print('[' + str(res.status_code) + ' - Good] -', res.url)
    elif res.status_code == 404:
        print('[' + str(res,status_code) + ' - Broken: Web not Found] -', res.url)
    elif res.status_code == 500:
        print('[' + str(res.status_code) + ' - Broken: Internal Server Error] -', res.url)
    else:
        print('[' + str(res.status_code) + ' - Good: Redirect or others] -', res.url)

def openUrl(url):
    res = requests.get(url)
    checkStatus(res)
    return res


def checkUrl(links):
    try:
        for url in links:
            res = requests.options(url)
            checkStatus(res)
    except BaseException as e:
        # FIXME: Find out how to avoid: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
        print(str(e))


def extractUrl(html):
    links = []
    for link in html.findAll('a', attrs={'href': re.compile("^http.*://")}):
        url = link.get('href')
        if validators.url(url):
            links.append(url)
    return links


def main():
    option = ''
    while option != '0':
        print()
        print('Menu:')
        print('\t1. Validate url')
        print('\t0. Exit')
        option = input('Option: ')
        if option == '1':
            url = input("Input a url to check broken link: ")
            validators.url(url)
            res = openUrl(url)
            html = bs4.BeautifulSoup(res.text, 'html.parser')
            links = extractUrl(html)
            checkUrl(links)
        elif option == '0':
            sys.exit('Thank you for using my program!')
        else:
            print('URL informed is invalid: ' + url)
main ()
