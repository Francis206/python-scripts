# Francis IT 280 – Lab #15: BeautifulSoup Lab CWC - Assignment Instructions
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
import bs4
import requests
import validators
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone='US/Mountain')
scheduler.start()


def checkStatus(res):
    if not res.ok:
        print('[' + str(res.status_code) + ' - Broken] -', res.url)


def openUrl(url):
    res = requests.get(url)
    checkStatus(res)
    return res


def extractUrl(html):
    links = []
    for link in html.findAll('a', attrs={'href': re.compile("^http.*://")}):
        url = link.get('href')
        if validators.url(url):
            links.append(url)
    return links


def extractTime(html):
    links = []
    for link in html.findAll('time'):
        url = link.get('datetime')
        links.append(url)
        # if url and validators.url(url):
    return links


def extractImage(html):
    links = []
    for link in html.findAll('img'):
        url = link.get('src')
        if url and validators.url(url):
            links.append(url)
    return links


def extractVideo(html):
    links = []
    for link in html.findAll('video'):
        url = link.get('src')
        if url and validators.url(url):
            links.append(url)
    return links


def dowloadAndLoadImageTask(url):
    try:
        print('Start dowloadAndLoadImageTask() task')
        res = openUrl(url)
        html = bs4.BeautifulSoup(res.text, 'html.parser')
        links = extractImage(html)

        for url in links:
            request = requests.get(url, stream=True)
            if request.ok:
                request.raw.decode_content = True
                filename = Path(tempfile.gettempdir(), url.split("/")[-1].split(".")[0]+'.jpg')
                with open(filename, 'wb') as file:
                    print(filename)
                    shutil.copyfileobj(request.raw, file)
                    subprocess.Popen(['C:\\Windows\\System32\\mspaint.exe', filename], bufsize=0)
            else:
                print('Image could not be retrieved.', url)
        print('Finish dowloadAndLoadImageTask() task')
    except BaseException as e:
        print(str(e), 'Shutting down the task.')


def loadHtmlSummaryTask(url):
    try:
        print('Start loadHtmlSummaryTask task')
        res = openUrl(url)
        html = bs4.BeautifulSoup(res.text, 'html.parser')

        title = html.find('title').text
        print('Title=', title)

        times = extractTime(html)
        print('Time=', times)

        links = extractUrl(html)
        print('Links=', links)

        images = extractImage(html)
        print('Images=', images)

        videos = extractVideo(html)
        print('Videos=', videos)
        print('Finish loadHtmlSummaryTask task')
    except BaseException as e:
        print(str(e), 'Shutting down the task.')


def askForUrl():
    while True:
        url = input("Please, inform and URL: ")
        if validators.url(url):
            break
        else:
            print('URL informed is invalid: ' + url)
    return url


def main():
    url = askForUrl()
    delay = datetime.now() + timedelta(minutes=3)
    print('Scheduled Thread to download and open images at {}'.format(delay))
    scheduler.add_job(dowloadAndLoadImageTask, 'date', run_date=delay, args=[url])

    url = askForUrl()
    delay = datetime.now() + timedelta(minutes=5)
    print('Scheduled Thread to load website content summary at {}'.format(delay))
    scheduler.add_job(loadHtmlSummaryTask, 'date', run_date=delay, args=[url])

    while len(scheduler.get_jobs()) > 0:
        time.sleep(15)

    scheduler.shutdown()
    print('Done.')


main()
