import os


def list_files():
    """Return list of all files contained in the 'binary files' directory with the .bin extension.
    Print warning message if folder does not exist or does not contain binary files."""
    binary_path = "./binary files"

    if os.path.exists(binary_path):
        binary_files = os.listdir(binary_path)
        binary_files = [file for file in binary_files if file.endswith(".bin")]
        if not binary_files:
            print("binary files folder does not contain any binary files!")
            return
        return binary_files
    else:
        print("binary files folder does not exist!")
        return


def get_guid_pairs():
    """Read guids.txt and return zipped tuples containing matched guid pairs converted to bytes.
    First item is the original guid, second item is the alpha guid.
    Print warning if guids.txt does not exist, is empty, or contains an odd number of entries."""
    guids_path = "./guids.txt"

    if os.path.exists(guids_path):
        # remove spaces and skip blank lines
        with open(guids_path, "r", encoding="UTF-8") as infile:
            guids = [line.strip() for line in infile if line.strip()]

        # fail safes
        if not guids:
            print("guids.txt is empty!")
            return

        if len(guids) % 2 != 0:
            print("guids.txt does not contain an even number of entries!")
            return

        # convert to bytes
        guids = [bytes.fromhex(guid) for guid in guids]

        # match guids
        original_guids = guids[::2]
        replacement_guids = guids[1::2]

        guid_pairs = list(zip(original_guids, replacement_guids))

        return guid_pairs

    else:
        print("guids.txt does not exist!")
        return


def replace_guids():
    """Open and read each file in the binary files directory, replace original guids with alpha guids
    and write the modified contents to a new binary file at root using the following naming scheme:
    [original file name]_modified.bin."""
    # get binaries that need editing
    binary_files = list_files()
    if not binary_files:
        return

    # get guid pairs
    guid_pairs = get_guid_pairs()
    if not guid_pairs:
        return

    # loop through each binary file
    for binary_file in binary_files:
        print(f"Processing {binary_file}...")

        path = f"./binary files/{binary_file}"
        file_name = binary_file.split(".")[0]
        modified_file_name = file_name + "_modified.bin"

        with open(path, "rb") as infile:
            content = infile.read()

        # first item is the original value, second item is the alpha value
        for guid_pair in guid_pairs:
            content = content.replace(guid_pair[0], guid_pair[1])

        # write modified file
        with open(modified_file_name, "wb") as outfile:
            outfile.write(content)

    print(f"Replacements finished! Modified {len(binary_files)} file(s).")


if __name__ == "__main__":
    replace_guids()
