#FileHandling
import time
STARTING_YEAR = 1993
ENDING_YEAR = 2013
STARTING_MONTH = 1
ENDING_MONTH = 12

def get_price(str):
    items = str.split(':')
    return float(items[1])

def get_month(str):
    items = str.split('-')
    return int(items[0])

def get_day(str): 
    items = str.split('-')
    return int(items[1])

def get_year(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])

def get_yearly_average(gas_list, year):
    total = 0
    count = 0

    for e in gas_list:
        if get_year(e) == year:
            total += get_price(e)
            count += 1

    average = total / count
    return average

def get_monthly_average(gas_list, year,month):
    total = 0
    count = 0

    for e in gas_list:
        if ((get_year(e) == year) and (get_month(e) == month)):
                    total += get_price(e)
                    count += 1
        if(count>0):
            avg = total / count
            print("The avg for year ",year, " and month ",month," is ",avg)
            return avg


def sortList(gas_list):
    sortPrice = dict()
    for e in gas_list:
            date, price = e.strip('\n').split(":")
            sortPrice[date] = price
    outfile = open('Ascending.txt','w')
    sorted_values=sorted(sortPrice.items(), key=get_value,reverse=False)
    for date, price in sorted_values:
            outfile.write(date+ ": ")
            outfile.write(price +'\n')
    #for key in sorted(dict.keys()):
        #print (key, dict[key])
    print("A new file is created in the same directory (\"Ascending.txt\")for lowest to highest sorted by price")
    #fout.close()
    fout = open('Descending.txt','w')
    sorted_values=sorted(sortPrice.items(), key=get_value,reverse=True)
    for date, price in sorted_values:
            fout.write(date+ ": ")
            fout.write(price +'\n')
    print("A new file is created in the same directory (\"Descending.txt\") for highest to lowest sorted by price")
    #fout.close()
    
def get_value(x):
    return x[1]

def main():
    gas_file = open('GasPrices.txt', 'r')

    gas_list = gas_file.readlines()
    print("---------------------------------AVERAGE PER YEAR----------------------------------")
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        print('The average price in ', i,
              ' was $', format(get_yearly_average(gas_list, i), '.2f'),
              sep = '')

    time.sleep(3)
    print("---------------------------------AVERAGE PER MONTH-----------------------------------")
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        for j in range(STARTING_MONTH, ENDING_MONTH + 1):
            get_monthly_average(gas_list,i,j)

    time.sleep(3)
    sortList(gas_list)

main()
