from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime


def get_amount_from_verkami():
  soup = BeautifulSoup(urlopen("http://www.verkami.com/projects/8555-runequest-6"))
  #print(soup.find('div','current_amount'))
  current_amount = soup.find('div','current_amount').strong.contents[0] 
  current_amount = current_amount[:-1]
  #print datetime.now(), " - ", current_amount, " euros conseguidos"
  return current_amount

def open_file():
  cvsfile = open('embrion.cvs', 'a')
  return cvsfile

def save_file(cvsfile, current):
  now = datetime.now()
  cvsfile.write(str(now.day))
  cvsfile.write(",")
  cvsfile.write(str(now.month))
  cvsfile.write(",")
  cvsfile.write(str(now.year))
  cvsfile.write(",")
  cvsfile.write(str(now.hour))
  cvsfile.write(",")
  cvsfile.write(str(now.minute))
  cvsfile.write(",")
  cvsfile.write(str(current))
  cvsfile.write("\n")
  cvsfile.close()


if __name__ == '__main__':
    cvsfile = open_file()
    current_amount = get_amount_from_verkami()
    save_file(cvsfile, current_amount)
    print(current_amount, " - Ok")

