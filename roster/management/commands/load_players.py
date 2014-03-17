from dateutil import parser
from django.core.management.base import BaseCommand
from optparse import make_option
from datetime import datetime

#import logger
from roster.models import Player
from __init__ import get_spreadsheet
 
GOOGLE_KEY = '0AikNzjrmEcGLdEY0cXpJUlp5Q3FHMTV1X1FhdjllMkE' # Enter the Google key here
GOOGLE_SHEET = 0 # This is the Google spreadsheet sheet number you're looking at, and 0 is the default first one
GOOGLE_ACCOUNT = 'kevin.uhrmacher@gmail.com' # Enter your Google account name here, blahwhatever@gmail.com
GOOGLE_PASS = 'Globe!343' # Enter your Google account password here
 
 
class Command(BaseCommand):
    """
    Downloads and ingests all players
    """
    option_list = BaseCommand.option_list + (
        make_option(
            '-c',
            '--clear',
            action='store_true',
            default=False,
            dest='clear',
            help='Clear all players in the DB.'),
        make_option(
            '-f',
            '--first',
            action='store_true',
            default=False,
            dest='first',
            help='Run the script for the first time.'),
    )
 
    def get_version(self):
        return "0.1"
 
    #def handle(self, *args, **options):
        #first_time = False
        #if options['clear']:
          #  logger.info("Clearing all players from the DB.")
           # Player.objects.all().delete()
       # if options['first']:
        #    first_time = True
 
       # self.init_reader(first_time)
 
    def dict_for_row(self, row):
        """
        Get a row of data, return a dict whose keys are Players properties
        and values are instance values for that row.
        """
        kwargs = {
            'number': row[0],
            'lastname': row[1],
            'firstname': row[2],
            'hand': row[3],
            'position': row[4],
            'height': row[5],
            'weight': row[6],
            'year': row[7],
            'hometown': row[8],
            'highschool': row[9],
            'story': row[10],
        }
 
        return kwargs
 
    def get_google_csv(self, key, sheet):
        """
        Connect to the Google doc and return a dict of the data to be used,
        including finding the header and the rest of the data
        """
        data = list(get_spreadsheet(
            GOOGLE_ACCOUNT, GOOGLE_PASS, key, sheet))
        return [self.dict_for_row(item) for item in data[1:]]
 
    def init_reader(self, first_time):
        """
        Loop through the spreadsheet and load the data
        """
        player_csv = self.get_google_csv(GOOGLE_KEY, GOOGLE_SHEET)
        already_exists = 0
        start_time = datetime.now()
 
        # Run through the spreadsheet, assigning values to certain fields
        for i, row in enumerate(player_csv):
            number = row['number']
            # Send some fields to functions that clean them
            lastname = row['lastname']
            firstname = row['firstname']
            hand = row['hand']
            position = row['position']
            height = row['height']
            weight = row['weight']
            year = row['year']
            hometown = row['hometown']
            highschool = row['highschool']
            story = row['story']
 
 
            # If the command doesn't use --first, run it this way.
            if first_time is not True:
                # Try and see if this player exists. If so, skip it.
                try:
                    player = Player.objects.get(
                        address=address,
                        name=name)
                    already_exists = already_exists + 1
                    
              #      logger.info('Already exists, skipping it.')
 
                # If the player doesn't exist, create it.
                except Player.DoesNotExist:
                    player = Player(
                        number=number,
                        lastname=lastname,
                        firstname=firstname,
                        hand=hand,
                        position=position,
                        height=height,
                        weight=weight,
                        year=year,
                        hometown=hometown,
                        highschool=highschool,
                        story=story)
                    player.save()
            # If you're running it with --first, save everything.
            else:
                player = Player(
                        number=number,
                        lastname=lastname,
                        firstname=firstname,
                        hand=hand,
                        position=position,
                        height=height,
                        weight=weight,
                        year=year,
                        hometown=hometown,
                        highschool=highschool,
                        story=story)
                player.save()
            #    logger.info("Saved player at %s" % address)
             #   logger.info("Skipped %s so far" % already_exists)
 
        finish_time = datetime.now()
        total_time = finish_time - start_time
    #    logger.info(
   #         "All done, took %s seconds to complete." % total_time.seconds)
  #      logger.info("Skipped %s homicides." % already_exists)
 
    def clean_date_time(self, date, time):
        """
        Turn the date and time into one field that Django will understand
        properly instead of being weird, just in case it was inputted wrong.
        """
        try:
            cleaned_date_time = parser.parse(
                "%s %s" % (date, time), ignoretz=True)
        except ValueError:
            cleaned_date_time = None
 
        return cleaned_date_time
 
    def clean_age(self, age):
        """
        Make sure it's an integer that's been entered, otherwise it'll break
        everything. If not, ignore it.
        """
        try:
            isinstance(age, int)
            age = int(age)
            if age is None:
                age = None
                return age
            else:
                return age
        except ValueError:
            age = None
            return age
 
    def clean_gender(self, gender):
        """
        Make sure it's a string that's been entered, otherwise it'll break
        everything. If not, save it as an unknown gender
        """
 
        try:
            isinstance(gender, basestring)
        except ValueError:
            new_gender = "Unkown"
            return new_gender
 
    def clean_link(self, link):
        """
        Django can only store URLs up to 200 characters, so if it's too long,
        this will allow you to ignore the URL and not break your importer.
        """
 
        try:
            isinstance(link, basestring)
            if len(link) > 200:
                new_link = None
                return new_link
            elif link == "":
                new_link = None
                return new_link
            else:
                return link
        except ValueError:
            new_link = None
            return new_link
    