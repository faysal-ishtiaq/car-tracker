import argparse
import subprocess


def main(arguments):
    try:
        return subprocess.run("openalpr", arguments.filepath)
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()

    main(args)
