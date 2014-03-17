from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from roster.models import Player, Coach

#import two lines below only if from URL, not local
import urllib2
import re

print ("starting to scrape")

class Command(BaseCommand):
    args = '<url>'
    help = 'Parses and imports players from goheels.com'
    
    def handle(self, *args, **options):
        try:
            print("trying to scrape")

            #Use code below when file to import is on web server:
            response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?SITE=UNC&DB_OEM_ID=3350&SPID=12960&SPSID=668154")
            html = response.read()
            
            #use if the file is local:
            #with open ("transcript.html", "r") as tempFile:
            #html=tempFile.read();
            
            soup = BeautifulSoup(html)
            
            tabledata = soup.find("table", {"id" : "roster-table"}) #find proper table
            player_names = []
            player_numbers = []
            player_links = []
            player_position = []
            countPlayers = 0
            
            for link in tabledata.find_all('a'):
                player_links.append(link.get('href'))
                player_names.append(link.get('title'))
                
            print player_names
            
            for position in tabledata.find_all("td", {"class" : "position"}):
                player_position.append(position.text.strip())
            
            print player_links
            print player_position
            
            for player_link, val in enumerate(player_links):
                
                print(player_link, val, countPlayers)
                response = urllib2.urlopen("http://goheels.com", val)
                html = response.read()
                soup = BeautifulSoup(html)
                print(player_names[countPlayers])
                player_data = Player.objects.create(name= player_names[countPlayers])
                player_data.save()
                countPlayers += 1;
            
        except Player.DoesNotExist:
            raise CommandError('didn\'t work')
            
        self.stdout.write("end of scrape.py")
