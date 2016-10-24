#
# This code uses BeautifulSoup to scrape www.innocentheroine.com (lo's blog)
# for certain words. This is meant to be an intro to get your feet wet
#
# LKS, October 2016
#
#
from bs4 import BeautifulSoup # this gets us our webscraper. If you run
# this code and it errors here, try reinstalling beautifulsoup (pip install
# BeautifulSoup)
import urllib # urllib and urllib2 work together to make your life easier when scripting
import urllib2 # see above
import sys  # without this, you will run into recursion limit errors, and as it is, you might anyway. This is a safety for trying to scrape from webpages 
sys.setrecursionlimit(50000)
import re # for regex string matching
#
import numpy as np
#

# Information we need!

# alright let's ask the user what webpage they want
# this will be entered from the command line 
#webpageName=raw_input("Enter URL for scraping here: ")
# or just enter directly here:
webpageName='http://www.innocentheroine.com/2016/06/experiment-61-why-i-chose-to-leave.html'
#
# enter the string you want
searchableString = 'advice'

# make it a function so we can use it again!
def FindStringMatches(webpageName, searchableString, printSoup=False):
    # webpageName = a string for searching for a html page
    # searchableString = what you want to look for in the text
    # printSoup = set to True to print all the html out to screen 
    
    # soupify the page
    soup = BeautifulSoup(urllib2.urlopen(webpageName), "lxml")

    #
    # now to get a specific string within a line of text
    # the re is a regex package (for regular expressions) that handles text well
    matches = soup(text=re.compile(searchableString))

    #
    # count how many matches
    print("There are " + str(len(matches)) + " matches for " + searchableString)

    #
    # play around with this, try looking at the soup code by printing
    if printSoup == True:
        print soup

    return None



# here's a sample, 
FindStringMatches(webpageName, searchableString, printSoup=False)

# wait, let's change that!
FindStringMatches(webpageName, 'Insight', printSoup=False) 


    
# bonus: how to access a different page based on information given 
#
# go to the home page
base= 'http://www.innocentheroine.com'
#
# get all the links
basesoup = BeautifulSoup(urllib2.urlopen(base), "lxml")
links=basesoup.findAll('a')
#
# just randomly choosing one, but you can see where you could search for
# the title you want and have your loop pick that
#
newbase=links[90]['href']
soup2=BeautifulSoup(newbase, 'lxml')

#
# let's see how much text I have in there for dating
FindStringMatches(newbase, 'dating')

# cool right?! 
