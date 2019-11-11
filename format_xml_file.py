import lxml.etree as etree

def format_tree(filename, root_dir="xml_files"):
    filepath = root_dir + "/" + filename + ".xml"
    x = etree.parse(filepath)
    xmlstr = etree.tostring(x, pretty_print=True)

    with open(filepath, 'wb') as f:
        f.write(xmlstr)