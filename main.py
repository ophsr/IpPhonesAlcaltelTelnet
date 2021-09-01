import socket
import xlrd
import re
import telnetlib
import logging
from os import system, name


# Regex valid IP Address IPV4
regexIP = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

#Config LOG
def log_config():
    root_logger= logging.getLogger()
    root_logger.setLevel(logging.DEBUG) # or whatever
    handler = logging.FileHandler('IpPhonesAlcaltelTelnet.log', 'w', 'utf-8') # or whatever
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')) # or whatever
    root_logger.addHandler(handler)

 
def runnig_message():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("Running...")

def finished_message():
    print("Log is: "+str(logging.getLogger("IpPhonesAlcaltelTelnet.log"))+"\nFINISHED!")


## Give the location of the file and set array of the column, this method return this array
def ips_from_excel_file():
    # location = ("C:\Temp\MD5.xls")
    location = ("/home/phsr/Documentos/Projects/ScriptsPython/IpPhonesAlcaltelTelnet/MD5.xls")

    ## To open Workbook
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    
    ## Array with values(ip) from table
    #arrayofvalues = sheet.col_values(1)
    arrayofvalues = sheet.col_values(0)

    logging.info('The amount IP address: '+ str(len(arrayofvalues)))
    logging.info('Location is '+location)

    return arrayofvalues

def telnet_session(value_ip_host):
    #Open Telnet and command run
    tn = telnetlib.Telnet(value_ip_host,23,10)
    logging.info("Telnet session start in "+value_ip_host)

    tn.write(b"dot1x tls on \n")
    tn.write(b"reset \n")
    
    # Record all output and close session
    tn.get_socket().shutdown(socket.SHUT_WR)
    data = tn.read_all().decode('ascii')
    out = data.splitlines()
    tn.close()
    
    #Print OutPut
    print(data+"\n")
    logging.info("Command response in ip: "+ value_ip_host - out[2])


def main():
    log_config()
    for value in ips_from_excel_file():
        runnig_message()
        if regexIP.match(str(value)):
            try:
                telnet_session(value)
            except ConnectionRefusedError:
                logging.error("Connection Refused Error in HOST: "+value)
            except Exception as e:
                logging.error(str(e)+" in HOST: "+value)
        else:
            logging.warning("Not valid IP number: "+ str(value))
    finished_message()


main()




