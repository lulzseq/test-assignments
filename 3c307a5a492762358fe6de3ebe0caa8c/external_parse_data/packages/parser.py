import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

from .logger import log


class Parser():
    def __init__(self, url, market_dict):
        self.url = url
        self.host = self.url.split('/')[2]
        self.market_dict = market_dict

    def _open_browser(self):
        caps = DesiredCapabilities().CHROME
        caps['pageLoadStrategy'] = 'eager'
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options,
                                       desired_capabilities=caps)

    def _load_page(self, url):
        print(f'Page: {url}')
        try:
            self.driver.get(url)
            time.sleep(5)
            self.driver.implicitly_wait(5)
        except InvalidArgumentException:
            self.driver.quit()
            return log('Load page: ERROR'), -1

        html = self.driver.page_source

        # Captcha
        # if self.host == 'www.wildberries.ru' and 'popup__btn-main j-confirm' in html:
        #     self.driver.find_element(By.XPATH, '//button[@class="popup__btn-main j-confirm"]').click()
        #     self.driver.implicitly_wait(5)
        #     html = self.driver.page_source
        log('Load page: OK')
        return html

    def get_elements(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        name = ''.join([p.text for p in soup.find_all('h1')])

        if name == '':
            return None, None

        market_page = self.market_dict[self.host]

        for classname in market_page['classname']:
            price_container = soup.find_all(market_page['tag'], {'class': classname})

            if len(price_container) != 0:
                for p in price_container:
                    price = int(''.join(re.findall(r'\d+', p.text)))
                    return name, price
        return name, None

    # def find_on_market(self, name):
    #     search_link = 'https://' + self.host + '/' + self.market_dict[self.host]['search_link'] + \
    #                   name.replace(',', '').replace(' ', '+').lower()
    #
    #     self.driver.switch_to.new_window('tab')
    #     page = self._load_page(search_link)
    #
    #     if len(page) == 2:
    #         return page[0], -1
    #
    #     return self.get_elements(page)
