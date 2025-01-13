from bs4 import BeautifulSoup
import requests

# url = 'https://www.careerpointkenya.co.ke/jobs/'

# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# select = soup.find('select', class_='kb-filter')
# options = select.find_all('option')

# all_catergories = []
# for option in options:
#     val = option['value']
#     name = option.text
#     all_catergories.append({val:name})

# print(all_catergories)

session = requests.session()
url = 'https://www.careerpointkenya.co.ke/jobs/'

response = session.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

def job(num, options):
    # filtered = filter(lambda x: x == num, options)
    try:
        extended = url + '?684154100=' + list(options[num-1])[0]

        response = session.get(extended)
        soupext = BeautifulSoup(response.content, 'html.parser')

        a_tags = soupext.find_all('a', class_='kb-section-link-overlay')
        rawtitles = soupext.find_all('div', class_="wp-block-kadence-dynamichtml")

        links = []
        titles = []

        for a in a_tags:
            val = a['href']
            links.append(val)
        for title in rawtitles:
            titles.append(title.text)

        return links, titles

    except requests.exceptions.RequestException as RE:
        print(f'Error occured: {RE}')

def title(num, links):
    # try:
        linkurl = links[num-1] 
        return linkurl
    #     resp = session.get(linkurl)
    #     soup = BeautifulSoup(resp.content, 'html.parser')

    #     headings = soup.find_all('mark', class_='has-inline-color')
    #     txtheadings = []
    #     for heading in headings:
    #         txtheadings.append(heading.text)
    #     uls = soup.find_all('ul', class_="wp-block-list")
    #     lis = []
    #     for ul in uls:
    #         lifind = ul.find_all('li')
    #         for li in lifind:
    #             lis.append(li.text)
    #     para = []
    #     for heading in txtheadings:
    #         ulindex = txtheadings.index(heading)
    #         para.append([heading, li[ulindex]])
        
    #     return para

    # except requests.exceptions.RequestException as RE:
    #     print(f'Error occured: {RE}') 

def job_scraper():
    options = [
        {'228': 'university jobs in kenya'},
        {'48': 'trending jobs today'},
        {'880': 'tours & travel jobs in kenya'},
        {'22145': 'technician jobs in kenya'},
        {'345': 'technical jobs in kenya'},
        {'49': 'teaching jobs in kenya'},
        {'209': 'supply chain jobs in kenya'},
        {'158': 'social work jobs in kenya'},
        {'249': 'security jobs in kenya'},
        {'22651': 'science jobs in kenya'},
        # {'22995': 'scholarships in kenya'},
        # {'71': 'sales & marketing jobs in kenya'},
        # {'22107': 'real estate jobs in kenya'},
        # {'1137': 'quantity surveyor jobs in kenya'},
        # {'22336': 'quality control jobs in kenya'},
        # {'383': 'public relations jobs in kenya'},
        # {'203': 'public health jobs in kenya'},
        # {'22002': 'project management jobs in kenya'},
        # {'69': 'procurement jobs in kenya'},
        # {'88': 'pharmaceutical jobs in kenya'},
        # {'1901': 'part time jobs in kenya'},
        # {'111': 'parastatal jobs in kenya'},
        # {'143': 'other professions'},
        # {'41': 'other posts'},
        # {'622': 'nutrition jobs in kenya'},
        # {'267': 'nursing jobs in kenya'},
        # {'202': 'ngo jobs in kenya'},
        # {'142': 'medical jobs in kenya'},
        # {'769': 'media jobs in kenya'},
        # {'22659': 'manufacturing jobs in kenya'},
        # {'353': 'logistics jobs in kenya'},
        # {'226': 'librarian jobs in kenya'},
        # {'201': 'legal jobs in kenya'},
        # {'239': 'laboratory technologist jobs in kenya'},
        # {'22887': 'jobs in somali'},
        # {'208': 'jobs in nairobi'},
        # {'140': 'jobs in kisumu'},
        # {'23002': 'jobs in kenya'},
        # {'61': 'it jobs in kenya'},
        # {'97': 'internships in kenya'},
        # {'336': 'insurance jobs in kenya'},
        # {'68': 'hr jobs in kenya'},
        # {'326': 'hotel jobs in kenya'},
        # {'21790': 'hospitality jobs in kenya'},
        # {'22456': 'graphic design jobs in kenya'},
        # {'67': 'finance jobs in kenya'},
        # {'98': 'engineering jobs in kenya'},
        # {'59': 'driver jobs in kenya'},
        # {'682': 'director jobs in kenya'},
        # {'89': 'customer service jobs in kenya'},
        # {'57': 'credit control jobs in kenya'},
        # {'86': 'county government jobs in kenya'},
        # {'1717': 'consultancy jobs in kenya'},
        # {'238': 'communication jobs in kenya'},
        # {'147': 'banking jobs in kenya'},
        # {'53': 'audit jobs in kenya'},
        # {'325': 'architecture jobs in kenya'},
        # {'330': 'airline jobs in kenya'},
        # {'205': 'agricultural jobs in kenya'},
        # {'66': 'administration jobs in kenya'},
        # {'146': 'actuarial science jobs in kenya'},
        # {'45': 'accounting jobs in kenya'}
    ]

    print('Job categories:')
    i = len(options) - (len(options) -1)
    for option in options:
        for val in option.values():
            print(f'{i}: {val}')
            i+=1

    choose = True
    while choose:
        choose_category = int(input('Input number of category you would like to choose from: '))
        if choose_category <= 0 or choose_category > 10:
            print('Invalid input')
        else:
            links, titles = job(choose_category, options)
            choose = False
    
    print('Jobs in category: ')
    t = len(titles) - (len(titles) -1)
    for ti in titles:
        print(f'{t}: {ti}')
        t += 1

    jobchoose = True
    while jobchoose:
        choose_job = int(input('Input number of the job choosen to get link: '))
        if choose_job <= 0 or choose_job > 10:
            print('Invalid input')
        else:
            linkurl = title(choose_job, links)
            jobchoose = False
    
    print(f'Job details: {linkurl}')

job_scraper()