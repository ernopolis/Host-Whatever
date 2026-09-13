import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from urllib.parse import parse_qs
import sys

def extract_opml(ifile,ofile):
    tree = ET.parse(ifile)
    root = tree.getroot()

    with open(ofile, "w") as txt_file:

        for item in root.findall("body/outline/outline"):

            title = item.get("title")
            xmlUrl = item.get("xmlUrl") or ""

            parsed_url = urlparse(xmlUrl)
            channel_id = parse_qs(parsed_url.query)["channel_id"][0]

            print(channel_id, title, file=txt_file)
    print("Written to current directory:",ofile)


if len(sys.argv) < 2:
	print('usage: python3 pipe-viewer.py <xml file>')
	sys.exit()


extract_opml(sys.argv[1],'subscribed_channels.txt')
