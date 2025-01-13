from bs4 import BeautifulSoup
import requests

session = requests.Session()
url = 'https://www.careerpointkenya.co.ke/jobs/'

def get_categories():
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
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
    ]
    
    return options

def fetch_jobs(num, options):
    try:
        extended = url + '?684154100=' + list(options[num-1].keys())[0]
        response = session.get(extended)
        soup = BeautifulSoup(response.content, 'html.parser')

        job_links = [a['href'] for a in soup.find_all('a', class_='kb-section-link-overlay')]
        job_titles = [title.text for title in soup.find_all('div', class_="wp-block-kadence-dynamichtml")]

        return job_links, job_titles

    except requests.RequestException as RE:
        print(f'Error occurred: {RE}')
        return [], []

def get_job_details(num, links):
    try:
        linkurl = links[num-1]
        return linkurl
    except IndexError:
        print("Invalid job number.")
        return None

def save_to_text(titles, links, options, category_num):
    file_name = "job_listings.txt"
    category = list(options[category_num-1].values())[0]
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Job Listings for {category}\n\n")
        for title, link in zip(titles, links):
            file.write(f"{title}\n{link}\n\n")
    
    print(f"Job listings saved to {file_name}")

def job_scraper():
    options = get_categories()
    
    print('Job categories:')
    i = 1
    for option in options:
        for key, val in option.items():
            print(f'{i}: {val}')
            i += 1

    try:
        choose_category = int(input('Input number of category you would like to choose from: '))
        if choose_category <= 0 or choose_category > len(options):
            print('Invalid input')
            return
    except ValueError:
        print('Invalid input')
        return

    links, titles = fetch_jobs(choose_category, options)
    
    print('Jobs in category: ')
    t = 1
    for ti in titles:
        print(f'{t}: {ti}')
        t += 1

    try:
        choose_job = int(input('Input number of the job chosen to get link: '))
        if choose_job <= 0 or choose_job > len(titles):
            print('Invalid input')
            return
    except ValueError:
        print('Invalid input')
        return

    job_details_url = get_job_details(choose_job, links)
    if job_details_url:
        print(f'Job details: {job_details_url}')

    save_choice = input('Do you want to save the job listings to a text file? (yes/no): ').strip().lower()
    if save_choice == 'yes':
        save_to_text(titles, links, options, choose_category)

if __name__ == '__main__':
    job_scraper()