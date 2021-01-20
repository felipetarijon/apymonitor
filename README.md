Author: Felipe Tarijon  
Started: 01/18/2021 9:31 PM  
  
Firstly, this project aims to generate a valid XML document to be used on APIMonitor software to filter and monitor the API calls using an PE as input.  
  
Later, new features can be included on demand. I thought implement something to read the api monitor output file and interpret the informations. Maybe run yara rules or another tools such as suricata.  
  
TODO:    
* [ ] Replace the XML lib (xml.dom.minidom) to another more secure  
* [x] Implement argparse  
* [x] Build an EXE file to be used on Windows as a tool  
* [ ] Add more arguments/options to:  
    * [x] allow change xml output filename  
    * [ ] generate the xml without the extra_header (non-default option)  
  
Changelog:  
* 01/19/2021:  
    * Added pyinstaller package to build executable files.  
    * Implemented argparse.