

class Script():
    
    def __init__(self):
        pass
    
    def script_framework(self):
        self.header = header_block 
        self.body = ""
        self.footer = footer_block 
        
        ## Standin for list input from Gui
        nmap = True
        dnsenum = True
        whois = True
        
        portscan_group = [nmap]
        dns_group = [dnsenum, whois]
        
        ## Do these in order, so headers and footers go in properly
        
        ## if any in this group are active, put header
        if any(portscan_group) == True:
            #
            self.body += self.headfoot("<Portscan>")
        
            ## Nested if to do individual functions. 
            ## Nested becuase these wouldn't go off if nothing was true in portscan_group
            ## Plus headers are easier
        
            if nmap == True:
                self.body += nmap_block 
            
            self.body += self.headfoot("</Portscan>")
                
        if any(dns_group) == True:    
            self.body += self.headfoot("<DNS>")
            
            if dnsenum == True:
                self.body += dnsenum_block 
            
            self.body += self.headfoot("</DNS>")
        
        
        self.script_build()
    
    
    def headfoot(self, input):
        
        ## Didn't use Fstrings for readability/quotation hell
        headfoot_block = '''
printf "${}########## {} ##########${}\\n" | tee -a Reports/$NAME
'''.format('{PURPLE}', input, '{NC}')

        return headfoot_block
    
        
    def script_build(self):
        script = f'''
{self.header}\n
{self.body}\n
{self.footer}\n
        '''
        
        print(script)

#####
## Script pieces
#####

header_block  = '''
## Colors
RED="\\033[0;31m"
BLUE="\\033[0;34m"
GREEN="\\033[0;32m"
YELLOW="\\033[0;33m"
PURPLE="\\033[0;35m"
GREY="\\033[0;37m"
NC="\\033[0m"
UNDERLINE="\\033[4m"
NU="\\033[0m"

printf "${RED}Generated ${GREY}by ${BLUE}Logec-Suite${NC} \n\n"

printf "Enter a name for this report and hit enter: "
read NAME

printf "Enter Target IP/FQDN and hit enter: "
read IP

while [ $# -gt 0 ]; do
  case "$1" in
    --nmap-all)
      nmap_all=true
      ;;
    --nmap-fast)
      nmap_fast=true
      ;;
    --install)
      install=true
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
  shift
done

## Init Vars


## Current Dir
CURRENT_DIR_RAW=$(pwd)
CURRENT_DIR="${CURRENT_DIR_RAW}/"

#echo $CURRENT_DIR

## Making reports dir
mkdir "${CURRENT_DIR}Reports"

##########
## Install
##########
if [ "$install" = true ]; then
    sudo apt-get install ansi2html -y
    sudo apt-get install nmap -y
    sudo apt-get install dnsenum -y

fi

'''

diagnostic_block  = '''
printf "\\n${YELLOW}########## <Diagnostic Info> ##########${NC}\\n" | tee -a Reports/$NAME
printf "Report Name: ${NAME}\\n" | tee -a Reports/$NAME
date | tee -a Reports/$NAME
printf "\\n## HostName ##:\\n" && hostname| tee -a Reports/$NAME
printf "\\n## Kernel ##:\\n" && uname -v| tee -a Reports/$NAME
printf "\\n## Generic Kernel \\n##:" && uname -r| tee -a Reports/$NAME
printf "\\n## Architecture \\n##:" && uname -m| tee -a Reports/$NAME
printf "\\n## IP ##:\\n" && hostname -I | tee -a Reports/$NAME

printf "${YELLOW}########## </Diagnostic Info> ##########${NC}\n\n" | tee -a Reports/$NAME
'''




nmap_block = '''


if [ "$nmap_all" = true ]; then
    printf "NMAP all selected... \\n"
    sudo nmap ${IP} -sV -Pn -A -p- --script=vulners --script=ssh-auth-methods --script=smb-enum-shares,smb-ls --script=nfs-showmount --script=nfs-ls  | tee -a Reports/$NAME
elif [ "$nmap_fast" = true ]; then
    printf "NMAP fast selected... \\n"
    sudo nmap ${IP} -F | tee -a Reports/$NAME
else
    sudo nmap ${IP} | tee -a Reports/$NAME
fi
'''



dnsenum_block  = '''
printf "\n${UNDERLINE}DNS Enum:${NU}\n" | tee -a Reports/$NAME

dnsenum ${IP} | tee -a Reports/$NAME
'''

whois_block  = '''
whois ${IP} -H | tee -a Reports/$NAME
'''


footer_block  = '''
printf "\\n${GREEN}########## <End of Report> ##########${NC}\\n\\n" | tee -a Reports/$NAME
'''

s = Script()

s.script_framework()