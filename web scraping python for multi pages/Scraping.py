# 1st Step import Libraries that we will need it for our programm

from os import link
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


job_title = []
company_name = []
locations_name = []
skills = []
links = []
salary = []
responsibilities = []
date = []
page_num = 0


while (True):
    try:
        # 2nd Step we will use Requests to fetch the URL (the aim)
        # result will storage the site (the aim)
        result = requests.get(
            f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")

        # 3rd Step save page content / markup
        # src will storage the content of tje page
        src = result.content
        # print(src)

        # 4th Step creat object from the Library BeautifulSoup
        soup = BeautifulSoup(src, "lxml")
        # print(soup)

        page_limit = int(soup.find("strong").text)
        # print(page_limit)

        if(page_num > page_limit//15):
            print("THE END")
            break

        # 5th Step find the elements containing info we need
        # jod title , company names  ,  location names , job skills
        job_titles = soup.find_all("h2", {"class": "css-m604qf"})
        company_names = soup.find_all("a", {"class": "css-17s97q8"})
        locations_names = soup.find_all("span", {"class": "css-5wys0k"})
        job_skills = soup.find_all("div", {"class": "css-y4udm8"})

        posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
        posted_old = soup.find_all("div", {"class": "css-do6t5g"})
        posted = [*posted_new, *posted_old]

        # 6th step loop over returned lists to extract needed info into other lists

        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append("https://wuzzuf.net" +
                         job_titles[i].find("a").attrs['href'])
            company_name.append(company_names[i].text.replace("-", ""))
            locations_name.append(locations_names[i].text)
            skills.append(job_skills[i].text)
            date.append(posted[i].text)

        # Caution in line 48 you need to add "https://wuzzuf.net" because the Url in site in "Inspect" don't have this part of Url ,
        # then the code will give you an Eception --->
        # Exception has occurred: MissingSchema Invalid URL '/jobs/p/T2ShpO8q8U6v-Python-Tech-Lead-Eastern-Enterprise-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|hpb':
        # No scheme supplied. Perhaps you meant http:///jobs/p/T2ShpO8q8U6v-Python-Tech-Lead-Eastern-Enterprise-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|hpb?
        #   File "D:\programing\Python holiday\Holy.py", line 55, in <module>
        #     result = requests.get(link)
        page_num += 1
        print("page Changed")
    except:
        print("some thing error")
        break

try:
    for link in links:
        result = requests.get(link)
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        salaries = soup.find("div", {"class": "css-rcl8e5"})
        salary.append(salaries.text.strip())
        requirements = soup.find("div", {"class": "css-1t5f0fr"}).ul
        respon_text = ""
        for li in requirements.find_all("li"):
            respon_text += li.text+" || "
        respon_text = respon_text[0:-4]
        responsibilities.append(respon_text)
except:
    print("some thing error in Link's Loop")

    # 7th step create csv file and fill it with values
file_list = [job_title, company_name, locations_name,
             skills, links, salary, responsibilities, date]
exported = zip_longest(*file_list)
with open("D:\programing\web scraping python/jobstest.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name",
                "Location", "Skills", "Links", "Salary", "Responsibilities", "Date of poste"])
    wr.writerows(exported)
