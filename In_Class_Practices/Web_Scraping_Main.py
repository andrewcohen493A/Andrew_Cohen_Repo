import Web_Scraping as wb

def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)
    uni_name = main_tree.xpath('//*[@id="wvu-main"]/h2/text()')
    #relationships = main_tree.xpath('//*[@id="oc_888_Relationships"]/div/div/div/div/div/text()')
    print(((uni_name)))
    # Let us see how many divs are they under this section
    all_divs = main_tree.xpath('//*[@id="wvu-main"]/div')
    print(str(len(all_divs)))
    # Interact with the first div
    first_div = all_divs[0]
    print(str(len(first_div)))

if __name__ == "__main__":
    main()

