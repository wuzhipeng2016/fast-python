»’÷æ
http://www.cnblogs.com/arkenstone/p/5727883.html
log_file = open("message.log", "w")
sys.stdout = log_file
print "Now all print info will be written to message.log"
log_file.close()

import logging
logging.basicConfig(filename='example.log', filemode="w", level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logger.debug('debug message')
logger.info('info message')

'logging.conf'
[loggers]
keys=root,simpleExample
[handlers]
keys=consoleHandler
[formatters]
keys=simpleFormatter
[logger_root]
level=DEBUG
handlers=consoleHandler
[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)
[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt= '%m/%d/%Y %I:%M:%S %p'



import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

“Ï≥£
try:
    #todo
except Exception as e:
    print(str(e))
