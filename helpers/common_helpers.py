import os


def ensure_dir_exists(path: str) -> None:
    """
    Create directory if it doesn't exist
    :param path: checked path
    :return: None
    """
    if not os.path.exists(path):
        os.makedirs(path)
