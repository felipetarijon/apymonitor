**Author**: Felipe Tarijon  
**Started**: 01/18/2021
  
## Clone and getting ready:
```code:bash
git clone git@github.com:felipetarijon/apymonitor.git
python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt
python apymonitor.py
```
  
## Build:
```code:bash
pyinstaller apymonitor.py
./dist/apymonitor/apymonitor -h
```
  
## To do:  
* [ ] Replace the XML lib (xml.dom.minidom) by another more secure  
* [x] Implement argparse  
* [x] Build an executable file to be used as a tool  
* [ ] Add more arguments/options to:  
    * [x] allow change xml output filename  
    * [x] generate the xml without the extra_header (non-default option)  
    * [ ] blacklist some api function or dll
  
## Changelog:  
* 01/19/2021:  
    * Added pyinstaller package to build executable files.  
    * Implemented argparse.
* 03/13/2021:  
    * Fixed the argparse to show help message when user provide no args.
    * Added the option to not output the extra_header.