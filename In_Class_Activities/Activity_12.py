from In_Class_Practices import Web_Scraping as wb
from Homeworks import HW3
import re


def GetBugIDs(page_link):
    """
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: N/A
    """
    main_tree = wb.get_web_tree(page_link)

    bug_list = main_tree.xpath('//*[@class="bugnumber"]//text()')
    # Get rid of # in each bug id, and return the clean list
    return [ele.replace('#', '') for ele in bug_list]


def GetBugPackages(page_link):
    """
        A method which iterates through the entire list of bug reports of teh given link
        :param link: link to launchpad bug reports passed from main
        :return: N/A
    """
    main_tree = wb.get_web_tree(page_link)
    bug_package = main_tree.xpath('//*[@class="buginfo-extra"]/span/text()')
    # cleanup package names and only include elements which are not empty.
    bug_package = [ele for ele in ([ele.strip() for ele in bug_package]) if ele != '']
    return bug_package


def GetBugTitles(page_link):
    main_tree = wb.get_web_tree(page_link)
    bug_title = main_tree.xpath('//*[@class="bugtitle"]//text()')
    # cleanup package names and only include elements which are not empty.
    bug_title = [ele for ele in ([ele.strip() for ele in bug_title]) if ele != '']
    return bug_title

def GetBugsLink(page_link):

    BugID = GetBugIDs(page_link)

    startCounter = 0
    count = 0
    bug_pages_list = []
    while count < 75:
        bid = BugID[count]
        BugsLink = f'https://bugs.launchpad.net/ubuntu/+bug/{bid}'
        startCounter += 1

        # combine page number with start string
        newStart = (f'{bid}' + str(BugsLink))
        linkx = BugsLink.replace(f'{BugID}', newStart)
        bug_pages_list.append(linkx)
        count += 1
    return bug_pages_list

def GetBugDescription(page_link):
    """I am trying to get the list of each bug and then with those links pull the xpath that shows the description
    given inside each specific bug"""
    #MJ: Here, you need to pass the link to EACH bug to get its description. There is no way - that i am aware of-
    # that can get you all descriptions in a list (similar to the list of all IDs).
    # In order for tihs to work, you will need to have a list of ALL bugs, then access each bug pare
    # then get the description. You wil need a for loop either here or in the main.

    main_tree = GetBugsLink(page_link)

    description = main_tree.xpath('//*[@id="yui_3_10_3_1_1668728702892_275"]//text()')

    return description

def GetAllBugsDescriptions(list_of_all_bugs_links):
    """
    A method that accesses each bug page, and gets its description
    :param list_of_all_bugs_links: List of aLL bugs pages.
    :return: list of all bugs descriptions. We shoul dave 75 descriptions one for each bug.
    """
    #temp list to hold all descriptions
    descriptions_list=[]
    # counter to keep track of pages
    linkCounter = 0
    # access each bug link, and get description
    while linkCounter < 75:
        print("Displaying descriptions for bug: " + list_of_all_bugs_links[linkCounter])
        main_tree = wb.get_web_tree(list_of_all_bugs_links[linkCounter])
        bug_description = main_tree.xpath('//*[@id="maincontentsub"]/div/div/div/div/div[2]//text()')
        print(bug_description)
        # add the current description to the list
        #descriptions_list.append(bug_description)
        linkCounter = linkCounter +1

    return descriptions_list



link = link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist" \
              "=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED" \
              "&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field" \
              ".importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance" \
              "%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type" \
              "%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA" \
              "&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field" \
              ".structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field" \
              ".status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field" \
              ".affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field" \
              ".has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field" \
              ".has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby" \
              "=-importance&memo=75&start=0 "


# Get links to all bug pages of Ubuntu Vulnerabilities
# Also Global
bugsLinks_list = HW3.Generate_Links_For_All_Bugs_Pages(link)


def main():
    """
    Main screen for HW #3.
    :return:N/A
    """
    # Display initial info
    bugsTotal = GetBugIDs(link)
    pagesTotal = GetBugPackages(link)
    bugTitles = GetBugTitles(link)
    linkForBug = GetBugsLink(link)
    #descriptionForBug = GetBugDescription(linkForBug)

    print('Initial Link:\n' + link)
    print('ID of all Bugs:\t', bugsTotal)
    print('Packages of all Bugs:\t', pagesTotal)
    print('Titles of all Bugs:\t', bugTitles)
    print('Links for each bug:\t', linkForBug)
    #Notice that i am only calling the method here to dsiplay descriptions ONLY.
    # We are not using what the method returns yet
    # Can you figure this out ;)
    GetAllBugsDescriptions(linkForBug)
    #print('Description: \t', descriptionForBug)
    #print("All Descriptions:\n"+ allBugsDescriptions)
    #print(str(len(allBugsDescriptions)))



if __name__ == "__main__":
    main()
