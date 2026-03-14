import sys
import os
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    
    def __init__(self,error_message,error_detsils:sys):
        self.error=error_message
        _,_,exc_tb=error_detsils.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
    
    def __str__(self):
        return "error occured in python script name[{0}] line name [{1}] error message [{2}]".format(
            self.file_name,self.lineno,str(self.error_message)
        ) 
               
     