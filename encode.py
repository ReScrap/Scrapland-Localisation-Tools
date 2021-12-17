import functions as f
import argparse

def main(filename):
    res = f.encode_file(filename)
    with open(".".join(filename.split('.')[:-1]) + "_encoded.txt", "wb") as out_file: # weird file_path manipulations are for cutting of file extensions but with extra coution in case if filename contains extra dots
        out_file.write(res)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the translation file to encode.")
    args = parser.parse_args()
    main(args.filename)