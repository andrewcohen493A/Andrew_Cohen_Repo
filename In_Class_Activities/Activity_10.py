import requests
import re
from lxml import html

def get_web_tree(link):
    # Welcome message
    print('Obtaining the page: ', str(link))
    # get the page
    page = requests.get(link)
    # get the elements from the page
    page_tree = html.fromstring(page.content)
    # return the tree of the web page
    return page_tree

link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start="

main_tree = get_web_tree(link)

totalBugs = main_tree.xpath('//*[@id="bugs-table-listing"]/div/table/tbody/tr/td//text()')[4]
numberofBugs = re.findall(r'\d+', totalBugs)
numberofBugs = str(numberofBugs[0]).replace('\'', '')
print(numberofBugs)

#Gains number of total bugs
noOFBugs = int(numberofBugs)
#Number of total pages that we will have
noOFPages = (int(noOFBugs/75))+1
pageCounter = 0
startCounter = 0
newStart = ""

while(pageCounter < noOFPages):
        startCounter = (pageCounter * 75)
        newStart = (str(startCounter))
        link = link.replace("memo=75&start=", f"memo={newStart}&start={newStart}")
        print(f"This is page {pageCounter} of {noOFPages}")
        print(link)
        pageCounter += 1

        #This is what i have but i am still unable to get the code to add 1 and not keep multiplying by 0


