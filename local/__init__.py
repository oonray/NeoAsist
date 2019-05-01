"""
:author: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
:file: local/__init__.py
:date: 01.05.2019

"""

def save_config(config):
    """Updates the config with the current config dictionary
    
    :param config: The confgig to save
    :type config: dict
    """
    create_dir(CONFIG_PATH)

def load_config():
    """Loads the config form file
       
    :returns: The loaded config or empty dict.
    :rtype: dict 
    """

    if(not create_dir(CONFIG_PATH)):
        if(os.path.isfile(CONFIG_PATH+CONFIG_FILE)):
            with open(CONFIG_PATH+CONFIG_FILE,"r") as f:
                return json.loads(f.read())        
    return dict()


def create_dir(dir):
    """Creates A Directtory
    
    :param dir: The directory path 
    :type dir: str
    :returns: False if folder exists or True when trying to create folder.
    :rtype: bool
    """
    if(os.path.isdir(dir)):
        return False;
    os.mkdir(dir)
    return True;
