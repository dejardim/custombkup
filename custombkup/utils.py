def in_format_file(path: str) -> bool:
    if path[-1] == '/':
        return True
    return False


def fix_file_path(path: str) -> str:
    return path + '/'


def in_interaction_mode(arg1, arg2, arg3) -> bool:
    if arg1 == None and arg2 == None and arg3 == None:
        return True
    return False


def custombkup_banner() -> None:
    print('''
----------------------------------------------------------------------------------------------
   _______  __   __  _______  _______  _______  __   __  _______  ___   _  __   __  _______   
  |       ||  | |  ||       ||       ||       ||  |_|  ||  _    ||   | | ||  | |  ||       |  
  |       ||  | |  ||  _____||_     _||   _   ||       || |_|   ||   |_| ||  | |  ||    _  |  
  |       ||  |_|  || |_____   |   |  |  | |  ||       ||       ||      _||  |_|  ||   |_| |  
  |      _||       ||_____  |  |   |  |  |_|  ||       ||  _   | |     |_ |       ||    ___|  
  |     |_ |       | _____| |  |   |  |       || ||_|| || |_|   ||    _  ||       ||   |      
  |_______||_______||_______|  |___|  |_______||_|   |_||_______||___| |_||_______||___|  
                                                                                      
----------------------------------------------------------------------------------------------
    ''')


def custombkup_status(is_i_mode: bool = False) -> None:
    
    details: str = '| Custombkup'
    
    if is_i_mode:
        details = ''

    print(f'''
  Stages Status {details}                                                          v0.0.1
----------------------------------------------------------------------------------------------    
    ''')
