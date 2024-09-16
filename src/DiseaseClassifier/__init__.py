import os
import sys
import logging

#current time stamp, log level name, module in our folders, messages
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"
#Creating log folder and all logs are recorded there
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        #also see the log in terminal
        logging.StreamHandler(sys.stdout)
    ]
)

#creating logger object and name
logger=logging.getLogger("DiseaseClassifierLogger")