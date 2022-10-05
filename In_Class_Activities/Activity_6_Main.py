import Activity_6 as wb

def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)

    # Apply to WVU
    uni_name = main_tree.xpath('//*[@id="wvu-main"]/div[2]/div/div/div/div/div[1]/a/span/text()')
    #Visit WVU
    uni_name2 = main_tree.xpath('//*[@id="wvu-main"]/div[2]/div/div/div/div/div[2]/a/span/text()')
    #ScholarshipChart
    uni_name3 = main_tree.xpath('//*[@id="wvu-main"]/div[2]/div/div/div/div/div[3]/a/span/text()')
    #Programs and Majors
    uni_name4 = main_tree.xpath('//*[@id="wvu-main"]/div[2]/div/div/div/div/div[4]/a/span/text()')
    #Confirm Admission
    uni_name5 = main_tree.xpath('//*[@id="wvu-main"]/div[2]/div/div/div/div/div[5]/a/span/text()')
    #relationships = main_tree.xpath('//*[@id="oc_888_Relationships"]/div/div/div/div/div/text()')
    print(((uni_name)))
    print(((uni_name2)))
    print(((uni_name3)))
    print(((uni_name4)))
    print(((uni_name5)))

if __name__ == "__main__":
    main()
