import os
from lxml import etree


class ParseClass(object):
    """
    The ParseClass gets the input file path of the xml file to be parsed.
    The method extract_cont() can be used to extract Container short name and
    Definition Ref and also Sun Container short name and Definition Ref from
    an AUTOSAR xml file and return the extracted values of type list.
    """
    def __init__(self, filename):
        self.fileName = filename

    def extract_cont(self):
        url = os.path.abspath(self.fileName)
        tree = etree.parse(url)
        cont_tag = "//*[local-name() = 'ECUC-MODULE-CONFIGURATION-VALUES']/*[local-name() = 'CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'SHORT-NAME']/text()"
        cont_name = tree.xpath(cont_tag)
        cont_def_tag = "//*[local-name() = 'ECUC-MODULE-CONFIGURATION-VALUES']/*[local-name() = 'CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'DEFINITION-REF']/text()"
        cont_def = tree.xpath(cont_def_tag)
        subcont_tag = "//*[local-name() = 'ECUC-MODULE-CONFIGURATION-VALUES']/*[local-name() = 'CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'SUB-CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'SHORT-NAME']/text()"
        subcont_name = tree.xpath(subcont_tag)
        subcont_def_tag = "//*[local-name() = 'ECUC-MODULE-CONFIGURATION-VALUES']/*[local-name() = 'CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'SUB-CONTAINERS']\
        /*[local-name() = 'ECUC-CONTAINER-VALUE']/*[local-name() = 'DEFINITION-REF']/text()"
        subcont_def = tree.xpath(subcont_def_tag)
        return list(zip(cont_name, cont_def)), list(zip(subcont_name, subcont_def))
