import argparse

from predictions import color, license_number, make_model


def main(img_filepath):
    return {
        "cars": {
            **color.main(img_filepath),
            **license_number.main(img_filepath),
            **make_model.main(img_filepath)
        }
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args.filepath)
