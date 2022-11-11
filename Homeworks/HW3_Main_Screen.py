"""
This is the main screen for Homework #3. Do not make any changes to this file.
"""
import HW3
# import the necessary files
# Global variables, accessed by all method in this file
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
    bugsTotal = HW3.GetTotalNumberOfBugs(link)
    pagesTotal = HW3.GetTotalNumberOfPages(link)
    print('Welcome! Infor about this Vulnerabilities DB')
    print('Initial Link:\n' + link)
    print('Total Number of Bugs:\t', bugsTotal)
    print('Total Number of Pages:\t', pagesTotal)

    # Accept page number form user
    page_input = int(input(('Which page would you like to view? Enter a number between 0 and ', pagesTotal - 1)))

    # Get data for user's input page
    print('Page # ', page_input, ' information:\t')
    print('Page Link:\t' + bugsLinks_list[page_input])
    print('List of Bugs\t', HW3.GetBugIDs(bugsLinks_list[page_input]))
    print('List of Packages\t', HW3.GetBugPackages(bugsLinks_list[page_input]))


if __name__ == "__main__":
    main()
