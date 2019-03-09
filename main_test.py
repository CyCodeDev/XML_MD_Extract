from XML_PARSE_CLASS_MAIN import xmlparse
import pickle


pathList = ['/security_master/payload/instrument/master_information/instrument_master/instrument_type', '/security_master/payload/instrument/master_information/instrument_master/apex_asset_type', '/security_master/payload/instrument/equity/equity_details/instrument_form', '/security_master/payload/instrument/master_information/organization_master/primary_name', '/security_master/payload/instrument/global_information/country_information/instrument_country_information/country_code', '/security_master/payload/instrument/master_information/market_master/market[@primary="true"]/country_of_quotation', '/security_master/payload/instrument/master_information/market_master/market/submarket', '/security_master/payload/instrument/master_information/market_master/market/mic', '/security_master/payload/instrument/equity/equity_details/dividend_currency', '/security_master/payload/instrument/master_information/instrument_master/issue_date', '/security_master/payload/instrument/master_information/market_master/market[@primary="true"]', '/master_information/market_master/market/xref[@status="Live"]', '/security_master/payload/instrument/master_information/instrument_master/primary_currency_code', '/security_master/payload/instrument/equity/equity_details/stamp_duty_type', '/security_master/payload/instrument/equity/equity_details/dividend_frequency', '/security_master/payload/instrument/master_information/instrument_master/primary_currency_code', '/security_master/payload/instrument/master_information/instrument_master/primary_exchange', '/security_master/payload/instrument/master_information/instrument_xref/xref', '/security_master/payload/instrument/equity/equity_details/registrar_code', '/security_master/payload/instrument/master_information/instrument_master/trading_restrictions_type', '/security_master/payload/instrument/master_information/organization_master/primary_name', '/security_master/payload/instrument/master_information/instrument_master/primary_name', '/security_master/payload/instrument/master_information/instrument_master/primary_name_abbreviated', '/security_master/payload/instrument/global_information/organization_information/classifications/GICS', '/security_master/payload/instrument/master_information/instrument_master/apex_asset_type', '/security_master/payload/instrument/equity/equity_details/shares_outstanding', 'instrument/master_information/market_master/market[@primary="true"]/xref[@type="Ticker"]', '/security_master/payload/instrument/equity/equity_details/warrant_type']


common_interface_fields = ['ASSETCLASSLEVEL1', 'ASSETCLASSLEVEL2', 'ASSETCLASSLEVEL3', 'COMPANYNAME', 'COUNTRYOFISSUANCE', 'COUNTRYOFTRADING', 'EXCHANGE_1', 'EXCHANGE_2', 'INCOMECCY', 'ISSUEDATE', 'LISTINGSTATUS_1', 'LISTINGSTATUS_2', 'LOCALCCYOFTRADING', 'LOCALTAXTYPE1NAME', 'PAYMENTFREQUENCY', 'PRICECURRENCY', 'PRIMARYLISTINGEXCHANGE', 'PRIMARYSECURITYSYMBOL', 'REGISTRARNAME', 'RESTRICTIONREASON', 'SECURITYDESCRIPTION_1 / SECURITYNAME_1', 'SECURITYDESCRIPTION_2', 'SECURITYNAME_2', 'SECURITYSECTORLEVEL1', 'SECURITYTYPE', 'SHARESOUTSTANDING', 'TICKER', 'WARRANTINDICATOR']


x = xmlparse('gsm_update_etd_APINVCLD_GSMF00O.16.1_1.20180417T1800-04.xml')
#y = x.bigI()
y = open('OPTIONS_ID_List_1.txt', 'r')
x.convert_path(pathList, common_interface_fields)

npak = x.new_path_and_keys
dl = x.dict_list
id_list = eval(y.read())

output = list(x.build_list(id_list, dl, npak))


cdd = open('OPTIONS_Mappings.pickle', 'wb')

#cdd.write(str(output))

pickle.dump(output, cdd)

cdd.close()
y.close()