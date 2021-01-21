import argparse
import subprocess


def main(img_filepath):
    try:
        process = subprocess.run(["alpr", img_filepath], stdout=subprocess.PIPE)
        return process.stdout
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args)
