import argparse

from predictions import color, license_number, make_model


def main(arguments):
    return {
        "cars": {
            **color.main(arguments),
            **license_number.main(arguments),
            **make_model.main(arguments)
        }
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args)
