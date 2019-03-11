import xml.etree.ElementTree as ET
import pandas as pd

class xmlparse:
    
    # Meant to store an XML file as an object to managed with methods
    def __init__(self, XMLFILE):
        self.XMLFILE = XMLFILE

    # Goes through an XML file and retrieves all IDs and saves them as a list in txt file
    
    # Securities are each uniquely identified by ID    
    # bigI gets IDs of ET.parsed.root() object and creates a txt list of IDs within the XML File

    # 1) Finds all IDs in XML, stores them as a generator object
    # 2) The id list can be used to create text files, retrieve certain paths, etc.

    def bigI(self):
        id_Path = './payload/instrument/[@id]'
        self.root = ET.parse(self.XMLFILE).getroot()
        self.id_list_gen = self.root.findall(id_Path)
        for id_tag in self.id_list_gen:
            yield id_tag.attrib['id']

    # convert_path creates a list of xml root-based xPaths, a 2-step process:
    # 1) A list of edited paths for creating the list of data
    # 2) Create a dictionary necessary to perform mapping of paths to (common interface) fields

    def convert_path(self, original_path_list, ci_fields):
    # CREATES A LIST OF UPDATED PATHS FOR PROCESSING
    # THE USER WILL PROVIDE A LIST OF PATHS AS WELL AS A LIST MAPPED FIELDS, THE LENGTH OF EACH LIST MUST BE THE SAME
        new_path_list = [p.replace('/instrument/', '/instrument[@id="{}"]/') for p in original_path_list]
        self.new_path_and_keys = [q.replace('/security_master/', './') for q in new_path_list]
        self.dict_list = dict(zip(self.new_path_and_keys, ci_fields))
    # CREATES A DICTIONARY WITH


    # THIS METHOD ACCEPTS A LIST OF:
    # 1) Instrument Ids
    # 2) Dictionary mapping list
    # 3) Path list to search the XML for

    def build_list(self,id_l, dictionary_list, q_path_list):
        extract = ET.parse(self.XMLFILE).getroot()
        df = {}

    # The 1st first step is to pick a path
        for p in q_path_list:
    # MAPPING DICTIONARY IS HERE
            path_dict = dictionary_list
            valueList = []
            df.update({'Security_ID': id_l[0:500]})

    # The 2nd second step is to select an id from the id List provided
            for id in id_l[0:500]:

    # The 3rd third step is to select a path for that particular instrument and find it within the xml
                pr = extract.find(p.format(id))
    # Some IDs will not have certain paths; exception handling for XPath that does exist for a specific security
                try:
                    valueList.append(pr.text)
    # d.update({path_dict[p]: valueList})
                except:
                    valueList.append(str("N/A"))
                df.update({path_dict[p]: valueList})

        yield df


    # results = list(build_list(cmo_data, cmo_list, paths))

    # print(str(results))
    # with open('ACCRUAL_FIELDS.txt', 'w') as finalfile:
    #     finalfile.write(str(results))
