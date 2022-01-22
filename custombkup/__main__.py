from custombkup.cli import args
from custombkup import Custombkup
from custombkup.utils import in_interaction_mode, custombkup_banner, custombkup_status


def main():
    """Run the main instructions of the Custombkup CLI."""

    FROM_PATH = args.frompath
    TO_PATH = args.topath
    LOG_PATH = args.logpath

    if in_interaction_mode(FROM_PATH, TO_PATH, LOG_PATH):
        custombkup_banner()

        from_path = input('? Enter the folder path: ')
        to_path = input('? Enter the backup folder path: ')
        log_path = input('? Enter the path to save the logs: ')

        assert from_path and to_path and log_path, 'Some path is empty'

        custombkup_status(is_i_mode=True)
        bkup = Custombkup(from_path, to_path, log_path)
        
    else:

        if LOG_PATH == None:
            LOG_PATH = '/home/'
    
        custombkup_status(is_i_mode=False)
        bkup = Custombkup(FROM_PATH, TO_PATH, LOG_PATH)
        
    bkup.generate()
    bkup.execute()
    bkup.cleanup()

    
if __name__ == '__main__':
    main()
