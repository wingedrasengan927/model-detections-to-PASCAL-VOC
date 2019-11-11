import argparse
import matplotlib.pyplot as plt

from objdet import show_inference, detection_model, category_index
from detection_utils import parse_output_dict
from xml_utils import create_root, create_objects_annotation_from_list, write_to_file
from format_xml_file import format_tree


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_name", type=str, help="path to the input image")
    args = parser.parse_args()

    # get model predictions
    img, output_dict = show_inference(detection_model,"input_images/"+ args.image_name + ".jpg")

    # parse the model prediction
    im_height = img.shape[0]
    im_width = img.shape[1]
    dict_list = parse_output_dict(output_dict, category_index, im_height, im_width, 0.5)

    # create and write the file
    root = create_root(args.image_name, im_width, im_height)
    root = create_objects_annotation_from_list(root, dict_list)
    write_to_file(root, args.image_name)

    # read the file, pretty format it, write it again (optional)
    format_tree(args.image_name)

    # save the output image
    plt.imsave("output_images/"+args.image_name+".jpg", img)

if __name__ == "__main__":
    main()