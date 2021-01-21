import argparse

from predictions import color, license_number, make_model


def main(img_filepath):
    print("------------------------------------------------------")
    print("Color info:", color.main(img_filepath))
    print("------------------------------------------------------")
    print("Number plate info:", license_number.main(img_filepath))
    print("------------------------------------------------------")
    print("Make and model info:", make_model.main(img_filepath))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args.filepath)
