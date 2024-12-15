from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def fill_columns(cols):
    filled_cols = []
    for col in cols:
        span = col.get_attribute("colspan")
        span = int( span) if span else 1
        filled_cols.extend(span*[col])
    return filled_cols

url1 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRXLWDLpnv-108LNY1vMSst-yvrWKqGlytCjlt2Qauid7gv7x2MLzKsO0fPWJ9Cfxj3AfevBvc9gGC0/pubhtml#"

driver = webdriver.Chrome()
driver.get(url1)
navigate = driver.find_element(by=By.ID, value="sheet-menu")
list_of_tables = navigate.find_elements(By.TAG_NAME, "li")[:2]
timetables = driver.find_elements(by=By.TAG_NAME, value="table")[:2]
days = ["Luni", "Marti", "Miercuri"]
weekly_hours = {}



for table,timetable in zip(list_of_tables,timetables):
    table.click()
    sleep(2)
    table_name = table.text.strip()
    if table_name.startswith('An') and table_name[-1].isdigit():
        table_name = table.text + " CTI-Ro"
    if table_name != 'Legenda sali':
        weekly_hours[table_name]     = {}

   
    table_body = timetable.find_element(by=By.TAG_NAME, value="tbody")
    table_rows = table_body.find_elements(by=By.TAG_NAME, value="tr")

    series_row = table_rows[2]
    series = [serie for serie in  series_row.find_elements(by=By.TAG_NAME, value="td") if len(serie.text)]

    for serieNo,serie in enumerate(series):
        groups_number = int(serie.get_attribute("colspan"))
        groups_row = table_rows[3]
        groups = [group.text for group in  groups_row.find_elements(by=By.TAG_NAME, value="td") if len(group.text)][serieNo*groups_number:groups_number *(serieNo+1)]
        
        weekly_hours[table_name][serie.text] = {}
        for dayno, day in enumerate(days):
            rowNo = 5+13*dayno
            rows = table_rows[rowNo:rowNo+13]
            for row in rows:
                cols = fill_columns( [col for col in row.find_elements(by=By.TAG_NAME, value="td")[3:] if col.text])
                cols = cols[groups_number*serieNo:groups_number *(serieNo+1)]
                for group,col in zip (groups,cols):
                    hours = col.get_attribute("rowspan")
                    hours = int(hours) if hours else 1
                    if group not in weekly_hours[table_name][serie.text]:
                        weekly_hours[table_name][serie.text][group] = {}
                    if(len(col.text)):
                        weekly_hours[table_name][serie.text][group][day] =  weekly_hours[table_name][serie.text][group].get(day,0)+hours

print(weekly_hours)
    
    
   
       


    

    

# print(weekly_hours)






driver.quit()
