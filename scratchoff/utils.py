import csv
import re

from bs4 import BeautifulSoup
import requests


base_lotto_url = 'http://www.txlottery.org/'
start_url = base_lotto_url + 'export/sites/lottery/Games/Scratch_Offs/all.html'
soup = BeautifulSoup(requests.get(start_url).text, 'html.parser')


def get_scratchoff_attributes():
    """Get tables' column labels.

    :return: List of column headers.
    """
    table_url = soup.find('a', href=True, text='Printer-friendly version')
    if table_url is None:
        common_pattern = '/export/sites/lottery/Games/Scratch_Offs/print'
        possible_links = []
        for link in soup.find_all('a', href=True):
            if re.search(common_pattern, link.get('href')):
                possible_links.append(link)
        if len(possible_links) == 1:
            table_url = possible_links[0].get('href')
    else:
        table_url = base_lotto_url + table_url.get('href')
    table_soup = BeautifulSoup(requests.get(table_url).text, 'html.parser')
    fields = []
    for header in table_soup.find_all('th'):
        if header.text != u'\xa0':
            fields.append(str(header.text))
    return fields


def get_rinsed_data():
    """Get the data csv file containing scratchoff data set.

    Find link through its hard-coded text tag attribute.
    There should only be one .csv link in the soup.

    :return: Scratchoff data.
    """
    csv_url = soup.find('a', href=True, text='All Levels (.csv)')
    if csv_url is None:
        # TODO: Create a common_pattern regex. See get_scratchoff_attribute().
        links_ending_with_csv = []
        for link in soup.find_all('a', href=True):
            if re.search('.csv', link.get('href')):
                links_ending_with_csv.append(link)
        if len(links_ending_with_csv) == 1:
            return base_lotto_url + links_ending_with_csv[0].get('href')
    csv_data = []
    csv_reader = csv.reader(requests.get(csv_url.get('href')).iter_lines(), delimiter=',')
    for i in csv_reader:
        if i:
            csv_data.append(i)
    del csv_data[0:2]
    return csv_data
