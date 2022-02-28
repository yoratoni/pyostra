class GlobalSettings:
    '''The debugging settings for the custom Logger class.
    '''
    
    # Debugging
    dist_mode = False  # If True, remove all the console messages, even forced ones
    verbose_debugging = True  # Print a lot more data about the NFTs
    debug_types = ['INFO', 'DATA', 'WARN', 'ERRO', 'SUCCESS']  # List of debug message types
    
    # Status codes used for general errors
    # Simply use the parameter 'status_code' with the code ID inside pyprint
    status_codes = {
        101: 'Pyprint Status Example'
    }