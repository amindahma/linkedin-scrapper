from linked_in_scrapper import Linked_in_scraper


def scrape_linkedin_profile(profile_name):
    linkedin_page = Linked_in_scraper(profile_name)
    return linkedin_page.scrape_one_profile(profile_name)


def get_linkedin_profile(link):
    return scrape_linkedin_profile(link)


get_linkedin_profile('https://www.linkedin.com/in/manura-jithmal-de-silva-988b385b/')