import logging

##############################
#Getting Started with Logging
##############################

#this sets the type of logging that is done
#Options include: 
#INFO
#DEBUG
#
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
#######
#logging to a file
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
#create a logging format to save into a file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
#add formatting to log
logger.addHandler(handler)
#begin logging


##############################
#Writing Log Recorrds at Proper Levels
##############################

########
#use DEBUG logs inside of complex loops to find issues later
mylist = [1,2,3,4]
def complex_algorithm(items):
	for i, item in enumerate(items):
		print(mylist[i])
		logger.debug('{} iteration, item ={}'.format(i,item))
# complex_algorithm(mylist)
########
#Use info for handling request or checking server states
def handle_requests(request):
	logger.info('Handling requests {}'.format(request))
	result = 'result'
	logger.info('Return result {}'.format(result))

def start_server(port):
	logger.info('Starting service at port {}'.format(port))
	logger.info('Service is started')

# handle_requests(request='myrequest')
# start_server(port='4081')
########
#Use warnings when somethign important happens, but not an error (e.g. incorrect password entered)
def authenticate(user_name, password, ip_address):
	if user_name != 'USER_NAME' and password != 'PASSWORD':
		logger.warn('Login attempt to {} from IP {}'.format(user_name, ip_address))
		return False

# authenticate('jj', 'test', '1234567')
#user erors when something is wrong, for example an exception is thrown
def get_user_by_id(user_id):
	user = input('id: ')
	if user is None:
		logger.error('Cannot find user with user_id={}'.format(user_id))
		return 'No user'
	return 'example user'
# get_user_by_id(None)
#catching exceptions with logging
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logger.error('Failed to open file', exc_info=True)





