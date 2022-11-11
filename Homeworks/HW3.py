"""
Andrew Cohen
"""
import requests
from In_Class_Practices import Web_Scraping as wb
import re
"""
Homework #3 objective is to fill out and complete each of the following methods.    
"""

def Generate_Links_For_All_Bugs_Pages(link):
    """
        20 POINTS
       A method which creates an entire list of URLs of all bug pages of the initial link
       :param link: link to the initial launchpad vulnerabilities (page one) passed from main
       :return: list of URLs, each to a page of bugs
    """
    # Empty list, add all urls to this list
    bug_pages_list = []

    # Each time you create a new link, store it in this variable
    noOfPages = GetTotalNumberOfPages(link)
    pageCounter = 0
    startCounter = 0
    current_link = ""
    while pageCounter < noOfPages:
        startCounter = pageCounter * 75
        # Remove numbers at the end
        link = re.sub(r'\d+$', '', link)

        # combine page number with start string
        current_link = ('&start=' + str(startCounter))

        # combine page number with memo string
        memo = '&memo=' + str(startCounter)
        linkx = link.replace('&start=0', current_link)
        linkx = linkx.replace('&memo=75', memo)
        bug_pages_list.append(linkx)
        pageCounter += 1

    # add the current link to the list
    bug_pages_list.append(current_link)

    return bug_pages_list


def GetBugIDs(page_link):
    """
    10 POINTS
        A method which iterates through the entire list of bug reports of any  given link
        :param link: link to launchpad bug report page passed from main
        :return: list of bug IDs of the page_link page
    """
    main_tree = wb.get_web_tree(page_link)
    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')

    # Get rid of # in each bug id, and return the clean list
    bug_list = [ele.replace('#', '') for ele in bug_list]
    return bug_list


def GetBugPackages(page_link):
    """
    20 POINTS
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: list of bug packages of the page_link page
    """
    # Empty list, add all bug packages to this list
    bug_package = [page_link]

    # pulls all the names of the bugs on the page
    main_tree = wb.get_web_tree(page_link)
    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]/span/text()')
    # cleanup package names and only include elements which are not empty.

    bug_package = [ele for ele in ([ele.strip() for ele in bug_package]) if ele != '']
    return bug_package

def GetTotalNumberOfBugs(page_link):
    """
    20 POINTS
        A method which gets extracts total number of bugs from the initial link of Ubuntu Vulnerabilities
        :param link: link to launchpad bug reports page
        :return: the total number of bugs from the first page
    """
    # Extract and clean total number of bugs
    main_tree = wb.get_web_tree(page_link)
    noOfBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td/text()')[2]
    noOfBugs = [int(i) for i in noOfBugs.split() if i.isdigit()][0]
    return noOfBugs


def GetTotalNumberOfPages(page_link):
    """
    20 POINTS
            A method which calculates the total number of bug pages from the initial link of Ubuntu Vulnerabilities
            :param link: link to launchpad bug reports page
            :return: the total number of bug pages
        """
    noOfBugs = GetTotalNumberOfBugs(page_link)
    # Number of total pages that we will have
    noOfPages = (int(noOfBugs) / 75)+ 1
    # Extract and clean total number of bugs
    return round(noOfPages)
