import webbrowser  # default libary - to open webpage via script
import csv  # defaut libabry - to save data in csv format
from requests import request  # libabry to get webpage
from bs4 import BeautifulSoup  # web scrapper library
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


def fetch_reviews(soup, url):
    file = csv.writer(open(movieName+".csv", 'w'))
    file.writerow(['Author', 'Review', 'Score','Star'])
    pagination = soup.find('span', {'class': 'pageInfo'})
    noOfReviewPage = int(pagination.text[10:])+1
    for x in range(1, noOfReviewPage):
        print("processing reviews on review page "+str(x))
        newUrl = url+"?page="+str(x)
        newPage = request('GET', newUrl)
        newSoup = BeautifulSoup(newPage.text, 'html.parser')
        for review in newSoup.find_all("div", {"class": "review_table_row"}):
            for reviewText in review.find_all("div", {"class": "the_review"}):
                theReview = reviewText.text
                theScore = analyser.polarity_scores(theReview)
                score = theScore['compound']
                star = rating(score)
            for author in review.find_all("a", {"class": "articleLink"}):
                theAuthor = author.text
            file.writerow([theAuthor, theReview, score, star])
    print("check "+movieName+".csv file")


def rating(score):
    if(score > -1 and score < -0.5):
        return 1
    elif(score > -0.5 and score <= 0):
        return 2
    elif(score > 0 and score < 0.5):
        return 3
    elif(score > 0.5 and score < 1):
        return 4

def webpage_url(url):
    page = request('GET', url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        fetch_reviews(soup, url)
    else:
        print("Check your movie name")


movieName = input("Please Enter the Movie Name :").replace(" ", "_")
url = "https://www.rottentomatoes.com/m/"+movieName+"/reviews"

webpage_url(url)
