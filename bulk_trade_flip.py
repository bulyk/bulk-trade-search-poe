from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import csv



zaderjka_v_razvitii = 3
expedition = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[7]')
delirium = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[8]')
scarab = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[12]')
fossil = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[15]')
exotic = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]')
essence = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[16]')

dict_flip = { 1: expedition,
              2: delirium,
              3: scarab,
              4: fossil,
              5: exotic,
              6: essence
            }

#print (len(dict_flip))
a = 0

def bulk_trade_flip():
    divine = 250
    a = 4
    # with open("flip.csv", mode="a", ) as w_file:
    #     file_writer = csv.writer(w_file, delimiter = ";", )
    #     file_writer.writerow(['хаосов за шт', 'итем', 'шт за диван','стоимость необходимого булка', 'продажа булка за диван', 'профит', "профит за трейд",  ])

    while a <= len(dict_flip):


        x = 1
        options = Options()
        options.binary_location = r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
        browser = webdriver.Firefox(executable_path=r'C:\Users\user\Desktop\python\parserpoe\selenium\geckodriver.exe', options=options)
        browser.get('https://www.pathofexile.com/trade/exchange/Sentinel')
        #авторизация
        time.sleep(3)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/fieldset[1]/button').click()
        browser.find_element(By.XPATH, '//*[@id="login_email"]').send_keys("alkaizer@inbox.ru")
        browser.find_element(By.XPATH, '//*[@id="login_password"]').send_keys("89182888108")
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/form/input[3]').click()


        time.sleep(30)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]').click()
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div').click()
        #delirium = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div[9]/div/span')

        browser.find_element(By.XPATH, dict_flip[a]+'/div[1]').click()
        
        skoka_poz = browser.find_elements(By.CLASS_NAME, 'exchange-filter-item')
        skoka_orbov_v_razdele = len(skoka_poz)
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div').click()
        time.sleep(1)

        while x <= skoka_orbov_v_razdele:

            nomer_item_want = str(x)
            want_item = (dict_flip[a]+'/div[2]/div['+nomer_item_want+']')
            search = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[3]/div[2]/button')
            clear = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[3]/div[3]/button[1]')
            have_chaos = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[4]')
            have_div = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[17]')
            show_filter = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[3]/div[3]/button[2]')
            search_listed = ('/html/body/div[1]/div/div[1]/div[5]/div[3]/ul[1]/li[1]/a')
            bulk_item = ('/html/body/div[1]/div/div[1]/div[5]/div[3]/ul[1]/li[2]/a')


            test_knopki_show = browser.find_element(By.XPATH, show_filter)
            if 'Show Filters' in test_knopki_show.text:
                test_knopki_show.click()
                time.sleep(zaderjka_v_razvitii)


            browser.find_element(By.XPATH, have_chaos).click()
            browser.find_element(By.XPATH, want_item).click()
            browser.find_element(By.XPATH, search).click()
            time.sleep(zaderjka_v_razvitii)   
            try:
                price_chaos = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[13]/div[1]/div/div[1]/span[3]/span[1]").text.strip()
                value = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[4]/div[2]/div/span[1]/div/span[1]').text
                print(price_chaos)
                #print(price_chaos+'_for_'+value)

                time.sleep(zaderjka_v_razvitii)

                browser.find_element(By.XPATH, show_filter).click()
                time.sleep(zaderjka_v_razvitii)
                browser.find_element(By.XPATH, clear).click()
                time.sleep(zaderjka_v_razvitii)

                browser.find_element(By.XPATH, want_item).click()
                browser.find_element(By.XPATH, have_div).click()
                time.sleep(zaderjka_v_razvitii)
                browser.find_element(By.XPATH, search).click()
                time.sleep(zaderjka_v_razvitii)
                price = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[1]/div[1]/div/div[1]/span[3]/span[1]").text


                how_many_need_per_di = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[5]/div[6]/div[2]/div[1]/div[1]/div/div[2]/span[3]/span[1]').text.strip()
                how_many_need_per_div = round(float(how_many_need_per_di), 2)
                print(how_many_need_per_div)
                print(type(how_many_need_per_div))
                price_div = round(float(price)*divine*float(how_many_need_per_div), 2)
                price_chaoss = float(price_chaos)
                profit_per_trade = round((price_div/float(how_many_need_per_div) - price_chaoss), 2)
                price_stack_chaos = round(float((how_many_need_per_div)*price_chaoss),2)
                profit_total = round((price_div - price_stack_chaos), 2)
                print(how_many_need_per_div)
                print(price_stack_chaos)
                print(price_chaos, value, how_many_need_per_div, price_stack_chaos, price_div, profit_per_trade, )
#запись в Excel
#если стоимость необходимого булка меньше 120 результат в таблицу не идет
                # if price_stack_chaos > 120:
                with open("flip.csv", mode="a", ) as w_file:
                    file_writer = csv.writer(w_file, delimiter = ";", )
                    file_writer.writerow([price_chaos, value, "'"+str((how_many_need_per_div)), "'"+str((price_stack_chaos)), "'"+str((price_div)), "'"+str((profit_total)), "'"+str((profit_per_trade)),  ])
                # else:
                #     pass
                                
                # writer = csv.writer(file, delimiter=';')
                # writer.writerow(['price_chaos', 'value', 'price_div', 'profit_per_trade'])

                # writer.writerow([price_chaos, value, price_div, profit_per_trade])
                # os.startfile(file)





                time.sleep(zaderjka_v_razvitii)
                show_filter = ('/html/body/div[1]/div/div[1]/div[5]/div[4]/div/div[3]/div[3]/button[2]')
                browser.find_element(By.XPATH, clear).click()
                time.sleep(zaderjka_v_razvitii)
      
                if 'Show Filters' in test_knopki_show.text:
                    test_knopki_show.click()
                    time.sleep(zaderjka_v_razvitii)
                

                x = x + 1
            except:
                time.sleep(zaderjka_v_razvitii)
                time.sleep(zaderjka_v_razvitii)
                browser.find_element(By.XPATH, clear).click()
                time.sleep(zaderjka_v_razvitii)
                x = x + 1 
#очитска вкладки и выбор следующей категории
        browser.find_element(By.XPATH, search_listed).click()
        time.sleep(zaderjka_v_razvitii)
        browser.find_element(By.XPATH, bulk_item).click()
        time.sleep(zaderjka_v_razvitii)
        browser.find_element(By.XPATH, clear).click()
        time.sleep(zaderjka_v_razvitii)

#        browser.quit()
        a = a + 1         
    return 







bulk_trade_flip()