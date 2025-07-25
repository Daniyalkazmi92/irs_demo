import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Hardcoded XML link (IRS archive) for demo
XML_LINK = "https://s3.amazonaws.com/irs-form-990/202240579349301004_public.xml"

def parse_irs_xml(xml_url):
    res = requests.get(xml_url)
    if res.status_code != 200:
        return [], "", "", "XML download failed"

    root = ET.fromstring(res.content)
    officers = []
    for person in root.findall(".//{*}OfficerDirectorTrustee"):
        name = person.findtext("{*}PersonName", default="")
        title = person.findtext("{*}Title", default="")
        officers.append((name, title))

    preparer_name = root.findtext(".//{*}PreparerFirmGrp/{*}PreparerPersonNm", default="")
    preparer_firm = root.findtext(".//{*}PreparerFirmGrp/{*}PreparerFirmName/{*}BusinessNameLine1", default="")

    return officers, preparer_name, preparer_firm, ""

# Load input
df = pd.read_csv("sample_input.csv")
output = []

for _, row in df.iterrows():
    ein = row["EIN"]
    officers, prep_name, prep_firm, error = parse_irs_xml(XML_LINK)

    if not officers:
        officers = [("", "")]

    for name, title in officers[:5]:
        output.append({
            **row,
            "officer_name": name,
            "officer_title": title,
            "tax_preparer_name": prep_name,
            "tax_preparer_firm": prep_firm,
            "filing_url": XML_LINK,
            "error": error
        })

pd.DataFrame(output).to_csv("demo_output.csv", index=False)
print("✅ Demo done. File saved: demo_output.csv")
