import sys
from xml.dom import minidom

import pefile


extra_header = """
    -
    This document was generated by Apymonitor.
    A python project which generates a valid APIMonitor XML document with a PE as input.
    More info: github.com/felipetarijon/apymonitor"""

xml_header = """<?xml version="1.0"?>
	<!--
	API Monitor Filter
	(c) 2010-2013, Rohitab Batra <rohitab@rohitab.com>
	http://www.rohitab.com/apimonitor/{}
	-->\n""".format(extra_header)


if __name__ == '__main__':
    pe = pefile.PE(sys.argv[1])

    doc = minidom.Document()

    root = doc.createElement('ApiMonitor')
    doc.appendChild(root)

    capture_filter = doc.createElement('CaptureFilter')
    root.appendChild(capture_filter)

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        module = doc.createElement('Module')
        module.setAttribute('Name', entry.dll.decode())

        capture_filter.appendChild(module)
        
        for imp in entry.imports:
            api = doc.createElement('Api')
            api.setAttribute('Name', imp.name.decode())

            module.appendChild(api)

    with open("output.xml", "w+") as output_file:
        output_file.write(xml_header + root.toprettyxml())
        output_file.close()
