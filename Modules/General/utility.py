from datetime import datetime, timezone, time
import time
import psutil
import os

import speedtest 
import dns
import dns.resolver


class Timestamp:
    
    def UTC_Time():
        current_date_time = datetime.now(timezone.utc)
        
        current_time = current_date_time.strftime("%H:%M:%S")
        print(current_time)
        return current_time
    
    def UTC_Date():
        current_date_time = datetime.now(timezone.utc)
        
        current_date = current_date_time.date()
        print(current_date)
        return current_date
    
class Performance:
    
    def __init__(self):
        self.PID = os.getpid()
        
    def CPU_all(self):
        return psutil.cpu_percent()
    
    def CPU_program(self):
        p = psutil.Process(self.PID)
        print(self.PID)
        print("Program CPU USAGE")
        return p.cpu_percent()
        
    def RAM_all(self):
        self.p = int((psutil.virtual_memory()[2]))
        #print(self.p)
        return self.p
        
    def RAM_program(self):
        p = psutil.Process(self.PID)
        mem_per = p.memory_percent()
        
        mem = mem_per * .01
        print(mem)
        
        print(self.PID)
        
        mem_2 = (self.p[1] * mem)/100000
        
        return mem_2

class Network:

  
    def __init__(self):
        self.st = speedtest.Speedtest()

  
    def download(self):
        return ((self.st.download())/1000000)  
    
    def upload(self):
        return (self.st.upload()/1000000)
    
    def ping(self):
    
        servernames =[]  
    
        self.st.get_servers(servernames)  

        #print(self.st.results.ping)
    
        return self.st.results.ping
    def lookup_A(self, cname):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(cname, 'A')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())
            
            return namelist
        except:
            return "NONE"
    
    def lookup_CNAME(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'CNAME')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())
            
            return namelist
        
        except:
            return "NONE"    
    def lookup_MX(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'MX')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        
        except:
            return "NONE"
        
    def lookup_TXT(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'TXT')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        except:
            return "NONE"
    
    def lookup_NS(self, name):
        try:
            ## Returns a list of items
            name = dns.resolver.resolve(name, 'NS')
            
            namelist = []

            for i in name:
                namelist.append(i.to_text())

            return namelist
        except:
            return "NONE"
    
    def lookup_Reverse(self, IP):
        try:
            ## Returns a list of items
            name = dns.reversename.from_address(IP)
            
            ## No iteration due to python seperating the string at each . :(
            
            namelist = (str(dns.resolver.resolve(name,"PTR")[0]))
            return namelist  
        
        except:
            return "NONE"  
    
    def lookup_All(self, IP):
        A = self.lookup_A(IP)
        CNAME = self.lookup_CNAME(IP)
        MX = self.lookup_MX(IP)
        TXT = self.lookup_TXT(IP)
        NS = self.lookup_NS(IP)
        Reverse = self.lookup_Reverse(IP)
        
        record_list = [A,CNAME,MX,Reverse,TXT,NS]
        return record_list
        
            
    
    
#N = Network()
#print(N.lookup_NS("courts.state.mn.us"))
#N.lookup_Reverse("8.8.8.8")

'''
N = Network()


print(N.download())
print(N.upload())
print(N.ping())'''
'''

ml = 1

while True:
    ml = ml *2 **20 **2
    os.system('clear')
    P = Performance()
    print(P.CPU_all())
    print(P.CPU_program())

    #print(P.RAM_all())
    #print(P.RAM_program())
    time.sleep(.0001)'''