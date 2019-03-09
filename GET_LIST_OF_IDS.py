from XML_PARSE_CLASS_MAIN import xmlparse


a = xmlparse('gsm_update_etd_APINVCLD_GSMF00O.16.1_1.20180417T1800-04.xml')

with open('OPTIONS_ID_List_1.txt', 'w') as f:
	I = list(a.bigI())
	f.write(str(I))