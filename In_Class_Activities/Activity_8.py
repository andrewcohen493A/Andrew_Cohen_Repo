import requests
import re
from lxml import html

def get_web_tree(link):
    """
    This method gets a web page from the specified url, and returns a tree of all elements in the page
    :param link: The webpage to access and process
    :return: The tree element created from the page
    """
    # Welcome message
    print('Obtaining the page: ', str(link))
    # get the page
    page = requests.get(link)
    # get the elements from the page
    page_tree = html.fromstring(page.content)
    # return the tree of the web page
    return page_tree

#link to the bug web page
main_tree = get_web_tree("https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-emptymarker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-emptymarker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0")

#xpath too the number of bugs that are found throughout
totalBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td//text()')[4]
numbers = re.findall(r'\d+', totalBugs)
numbers = str(numbers[0]).replace('\'','')
print(numbers)

#gets the bug ID that each bug has
BugID = main_tree.xpath('//*[@class="bugnumber"]//text()')
BugID = str(BugID).replace('#', "")
print(BugID)

#pulls all the names of the bugs on the page
Bugname = main_tree.xpath('//*[@class="bugtitle"]//text()')
print(Bugname)