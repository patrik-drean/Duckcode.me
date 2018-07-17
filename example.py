import schedule
import time

######################################################
############ Setting the scheduled tasks #############
######################################################

# Function that will be called at a certain time
def print_something():
    print('I am something')

# Every 5 minutes run the function
schedule.every(5).minutes.do(print_something)

# Every hour run the function
schedule.every().hour.do(print_something)

# Every day at 9:30am run the function
schedule.every().day.at('9:30').do(print_something)

# Every friday at 2:15pm run the function
schedule.every().friday.at('14:15').do(print_something)


######################################################
###### Setting scheduled tasks with parameters #######
######################################################

# Function with a paremter
def print_my_language(language):
    print('My language is {}'.format(language))

# Function that passes a paremeter
schedule.every(1).minutes.do(print_my_language, 'English')

#####################################################
### Run endless loop to check for scheduled tasks ###
#####################################################

while True:

    # This runs any of the tasks
    schedule.run_pending()

    # This will pause for 30 seconds before continuing
    time.sleep(30)
