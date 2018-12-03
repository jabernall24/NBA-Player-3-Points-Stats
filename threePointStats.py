import requests
from bs4 import BeautifulSoup as bs
import sys

def threePointStats(url):
    try:
        html = requests.get(url).text
    except:
        print("Unable to parse your request")
        sys.exit()

    doc = bs(html, "html.parser")

    table = doc.find('div', id = 'all_pgl_basic')
    mclass = table.find('div', class_ = 'overthrow table_container')
    games_table = mclass.find('table', id = 'pgl_basic')
    rows = games_table.find_all('tr')

    game = []
    three_pointers_made = []
    three_pointers_taken = []
    for row in rows:
        games = row.find_all('strong')
        for t in games:
            game.append(t.text)
        
        threesMade = row.find_all('td', {'data-stat' : 'fg3'})
        for t in threesMade:
            three_pointers_made.append(t.text)

        threesTaken = row.find_all('td', {'data-stat' : 'fg3a'})
        for t in threesTaken:
            three_pointers_taken.append(t.text)

    print("Game\tMade\tTaken")
    for game, made, taken in zip(game, three_pointers_made, three_pointers_taken):
        print(game + "\t" + made + "\t" + taken)

def composeURL(player, year):
    lower = player.lower()
    firstName = lower.split()[0]
    lastName = lower.split()[1]
    first = ""
    last = ""
    if len(firstName) <= 2:
        first = firstName
    else:
        for i, f in enumerate(firstName):
            if i <= 1:
                first += f
            else:
                break
            
    if len(lastName) <= 5:
        last = lastName
    else:
        for i, l in enumerate(lastName):
            if i <= 4:
                last += l
            else:
                break
    
    return "https://www.basketball-reference.com/players/" + lastName[0] + "/" + last + first + "01/gamelog/" + year

def main():
    player = input("What player would you like to know the stats three point stats for: ")
    year = input("What year(btw: 1967 and now): ")
            
    url = composeURL(player, year)
    threePointStats(url)
  
if __name__== "__main__":
  main()
