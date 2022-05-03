from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


class StockList:
    def __init__(self, sector):
        self.list = []
        self.TO_SEARCH = sector
        self.web_url_sector = 'https://www.sharesansar.com/today-share-price'
        self.web_url_data = 'https://merolagani.com/CompanyDetail.aspx?symbol=LICN'
        self.chrome_driver_path = os.environ['chrome']

    # This function will get list of companies from sector we want from website sharesansar
    def search_sector_list(self):
        try:
            s = Service(self.chrome_driver_path)
            driver = webdriver.Chrome(service=s)
            driver.get(self.web_url_sector)

            # time.sleep(3)
            sector_select_dropdown = driver.find_element(By.XPATH,
                                                         '//*[@id="frm_todayshareprice"]/div[1]/span/span[1]/span/span[2]')
            sector_select_dropdown.click()

            select_sector_input = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
            select_sector_input.send_keys(self.TO_SEARCH)
            select_sector_input.send_keys(Keys.ENTER)

            search_button = driver.find_element(By.XPATH, '//*[@id="btn_todayshareprice_submit"]')
            search_button.click()
            time.sleep(2)

            data = driver.find_elements(By.CSS_SELECTOR, 'tr td a')
            for i in range(len(data) - 1):
                self.list.append(data[i].text)
            return self.list

            time.sleep(2)
        except:
            print("There was some error while fetching sector list")
            # print("PLease try again later")
        driver.close()

    # This function will get all the datas needed of companies from the list
    def search_datas_for_sector(self, s_list):
        '''returns the list containing two lists i.e. error list and data list'''
        data = []
        error = []
        s = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=s)
        # try:
        driver.get(self.web_url_data)
        for item in s_list:
            row = []
            final_row = []
            text_input_area = driver.find_element(By.XPATH, '//*[@id="ctl00_AutoSuggest1_txtAutoSuggest"]')
            text_input_area.clear()
            # time.sleep(1)
            text_input_area.send_keys(item)
            text_input_area.send_keys(Keys.ENTER)

            share_string = driver.find_element(By.XPATH, '//*[@id="accordion"]/tbody[2]/tr/td').text
            if share_string == '':
                error.append(item)
                continue
            row.append(share_string)
            price_string = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice"]').text
            row.append(price_string)
            eps_string = driver.find_element(By.XPATH, '// *[ @ id = "accordion"] / tbody[10] / tr / td').text.split()[0]
            row.append(eps_string)
            book_value_string = driver.find_element(By.XPATH, '//*[@id="accordion"]/tbody[12]/tr/td').text
            row.append(book_value_string)
            for item in row:
                split_value = item.split(',')
                share = ''.join(split_value)
                final_row.append(float(share))
            bonus_stock = driver.find_element(By.XPATH, '//*[@id="accordion"]/tbody[15]/tr[1]/td').text
            bonus_cash = driver.find_element(By.XPATH, '//*[@id="accordion"]/tbody[14]/tr[1]/td').text
            if bonus_stock == '':
                bonus_stock = None
                if bonus_cash == '' or bonus_cash == '0.00':
                    final_row.append(bonus_stock)
                else:
                    bonus_cash = bonus_cash.split()[0]
                    final_row.append(bonus_cash)
            else:
                bonus_stock = bonus_stock.split()[0]
                if bonus_cash == '' or bonus_cash == '0.00':
                    final_row.append(bonus_stock)
                else:
                    bonus_cash = bonus_cash.split()[0]
                    total_bonus = float(bonus_stock) + float(bonus_cash)
                    final_row.append(float(total_bonus))
            data.append(final_row)
        driver.close()
        return [error, data]
        # except:
        #     print("There was some error while collecting datas for sector")
        #     print("PLease try again later")

