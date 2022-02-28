class GlobalSettings:
    '''The debugging settings for the custom Logger class.
    '''
    
    # Debugging
    dist_mode = False  # If True, remove all the console messages, even forced ones
    verbose_debugging = True  # Print a lot more data about the NFTs
    debug_types = ['INFO', 'DATA', 'WARN', 'ERRO', 'SUCCESS']  # List of debug message types
    
    # Status codes used for general errors
    # I usually use modified HTTP Status Codes
    # Simply use the parameter 'status_code' with the code ID inside pyprint
    status_codes = {
        42: 'Pyprint Status Example',
        
        100: 'Continue',
        102: 'Processing',
        
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        409: 'Conflict',
        429: 'Too Many Requests',
        
        500: 'Internal Server Error',
        501: 'Not Implemented',
        503: 'Service Unavailable',
        511: 'Network Authentication Required',
        599: 'Network Connect Timeout Error'
    }