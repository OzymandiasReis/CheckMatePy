import os
from pathlib import Path

root_path = "C:\TestRoot"
required_dirs_level0 = [  # defining the top-level directory structure which should be found in root_path
    "Advance letters",
    "Data protection statement",
    "Interviewer roster",
    "NTS dates",
    "NTS observation protocol",
    "NTS slides",
    "SAFF_after end of fw",
    "Showcards"
]


def setup_test_root(root_location):
    """
    Checks if all the directories listed in 'required_dirs_level0' are present in the root_location directory and
    creates them if not
    :param root_location: The directory in which all directories should be present
    :return: None
    """
    for dir in required_dirs_level0:
        current_path = os.path.join(root_location, dir)
        if not check_dir_exists(current_path):
            print("Creating dir '%s' in root folder '%s'" % (dir, root_location))
            os.mkdir(current_path)


def check_dir_exists(dir, location):
    return check_dir_exists((os.path.join(location, dir)))


def check_dir_exists(path):
    """

    :param path:
    :return:
    """
    if isinstance(path, Path):
        # print("check_dir_exists(path): isinstance Path is True")
        return path.exists()
    elif isinstance(path, str):
        # print("check_dir_exists(path): isinstance str is True")
        return os.path.exists(path)
    else:
        return False


if __name__ == '__main__':
    path = Path(root_path)
    if not check_dir_exists(root_path):
        exit("Root folder does not exist! Exiting...!")
    for x in path.iterdir():  # x is type pathlib.WindowsPath
        print(type(x), ": ", x)
    setup_test_root(root_path)
