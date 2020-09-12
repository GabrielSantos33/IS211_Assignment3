#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Gabriel Santos IS-211 9/12/2020

import urllib.request
import re
import logging
import csv
import argparse
import datetime
import requests


hours = {0: 0, 1: 0, 2: 0, 3: 0,
         4: 0, 5: 0, 6: 0, 7: 0,
         8: 0, 9: 0, 10: 0, 11: 0,
         12: 0, 13: 0, 14: 0, 15: 0,
         16: 0, 17: 0, 18: 0, 19: 0,
         20: 0, 21: 0, 22: 0, 23: 0, }



def downloadData(url):
    
    """Part I Pull
        Down Web Log File
        Your program should download the web log file from the location provided by a url
        parameter. This is just
        like the previous assignment (remember to use agrparse). The URL you can use for testing is located here:
        TODO .
        Accepts a URL as a string and opens it.
        Parameters:
            url (string): the url to be opened
        Example:
            >>> downloadData('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')
    """

    file = requests.get(url)
    csvFile = file.content.decode()

    return csvFile

def processData(data):
        
    """Part II Process
        File Using CSVThe file should then be processed, using the CSV module from this week. Here is an example line from the
        file, with an explanation as to what each fields represents:
        /images/test.jpg, 01/27/2014 03:26:04, Mozilla/5.0 (Linux) Firefox/34.0, 200, 346547
        When broken down by column, separated by commas, we have:
        path to file, datetime accessed, browser, status of request, request size in bytes
        Processes data from the contents of a CSV file line by line.
        Parameters:
            data - the contents of the CSV file
        Example:
            >>> processData(downloadedData)
    """
    lines = 0
    images = 0
    browsers = {'Firefox': 0,
                'Google Chrome': 0,
                'Internet Explorer': 0,
                'Safari': 0}

    file = csv.reader(data.splitlines())

    
    """Part III Search
        for Image Hits
        After processing the file, your next task will be to search for all hits that are for an image file. To check if a hit
        is for an image file or not, we will simply check that the file extension is either .jpg, .gif or .png. Remember to
        use regular expressions for this. Once you have found all the hits relating to images, print out how many
        hits, percentagewise,
        are for images. As an example, your program should print to the screen something
        like “Image requests account for 45.3% of all requests”
    
     """
    for line in file:
        lines += 1
        if re.search('jpe?g|JPE?G|gif|GIF|png|PNG', line[0]):
            images += 1
    """Part IV Finding
        Most Popular Browser
        Once Part III is done, your program should find out which browser people are using is the most popular. The
        third column of the file stores what is known as the UserAgent,
        which is a string web browser’s use to
        identify themselves. The program should use a regular expression to determine what kind of browser
        created each hit, and print out which browser is the most popular that day. For this exercise, all you need to
        do is determine if the browser is Firefox, Chrome, Internet Explorer or Safari.
    
    """
        if re.search("Firefox", line[2]):
            browsers['Firefox'] += 1
        elif re.search("Chrome", line[2]):
            browsers['Google Chrome'] += 1
        elif re.search("MSIE", line[2]):
            browsers['Internet Explorer'] += 1
        elif re.search("Safari[^Chrome]", line[2]):
            browsers['Safari'] += 1
            
    """Part V Extra Credit
        For extra credit, your program should output a list of hours of the day sorted by the total number of hits that
        occurred in that hour. The datetime is given by the second column, which you can extract the hour from
        using the Datetime module from last week. Using that information, your program should print to the screen
        something like:
    """
     HoursSorted(line)   

    print("Files that are images: " + str(images))
    imagePct = float((images / lines) * 100)
    print("Image requests account for {}% of all requests".format(imagePct))

    for browser in browsers:
        print(browser + " usage: " + str(browsers[browser]))

    topB = max(browsers, key=browsers.get)
    print("{} is the most popular broswer with {} uses.".format(topB, browsers[topB]))

    for hour in hours:
        print("Hour {} has {} hits.".format(hour, hours[hour]))


def HoursSorted(line):
    hour = (datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")).hour

    hours[hour] += 1


def main():
    try:
        # Pull file from internet
        source = input('File Source: ')
        csvData = downloadData(source)
    except ValueError:
        print('Invalid URL.')
        exit()

    processData(csvData)


if __name__ == '__main__':
    main()


# In[ ]:




