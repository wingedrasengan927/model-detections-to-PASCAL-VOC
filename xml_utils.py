import xml.etree.cElementTree as ET
from xml.etree.ElementTree import ElementTree

def create_root(file_prefix, width, height):
    root = ET.Element("annotation")
    ET.SubElement(root, "folder").text = "images"
    ET.SubElement(root, "filename").text = "{}.jpg".format(file_prefix)
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = "3"
    ET.SubElement(root, "segmented").text = str(0)
    return root

def create_objects_annotation_from_list(root, dict_list):
    for temp_dict in dict_list:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = temp_dict['label']
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = str(0)
        ET.SubElement(obj, "difficult").text = str(0)
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(temp_dict['bbox'][0])
        ET.SubElement(bbox, "ymin").text = str(temp_dict['bbox'][1])
        ET.SubElement(bbox, "xmax").text = str(temp_dict['bbox'][2])
        ET.SubElement(bbox, "ymax").text = str(temp_dict['bbox'][3])
    return root


def write_to_file(root, filename, root_dir = "xml_files"):
    tree = ElementTree(root)
    with open(root_dir +"/"+filename+".xml", 'wb') as f:
        tree.write(f)
