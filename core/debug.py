from colorama import Style, Fore

import inspect
import time


class DebugSettings:
    # If true, print all the available logs,
    # Else, just the types defined in 'forced_types'
    verbose_debugging = True
    
    # The section title, to separate the logs
    section_separators = '-' * 35
    section_color = Fore.LIGHTBLUE_EX
    section_title = 'PYPRINT SECTION'
    
    # List of debug log types and their colors in a dict
    all_types = {
        'INFO': Fore.LIGHTBLUE_EX,
        'DATA': Fore.CYAN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.LIGHTRED_EX,
        'SUCCESS': Fore.LIGHTGREEN_EX
    }
    
    # Debug log types that are always printed (even when verbose debugging is turned off)
    forced_types = ['WARNING', 'ERROR', 'SUCCESS']
    
    # Debug log types that shows the name of the function that calls pyprint()
    function_name_types = ['WARNING', 'ERROR']
    
    # Status codes used for general errors
    # I usually use modified HTTP Status Codes
    # Simply use 'log_or_status' with 'ST_' and the code after it (log_or_status = 'ST_42')
    status_codes = {
        42: 'Pyprint Status Example'
    }


class Logger:
    __is_first_print = True
    
    
    @staticmethod
    def __get_log_color(log_type: str):
        '''Get the color of the log depending on the log type.
        
        Args:
            log_type (str): The type of the log.
            
        Returns:
            str: The colorama color chars.
        '''
        
        color = Fore.WHITE
        
        if log_type in DebugSettings.all_types.keys():
            color = DebugSettings.all_types[log_type]
            
        return color
        
    
    @staticmethod
    def __show_section_title():
        '''Show the section title (printed only once).
        It separates the normal console logs and pyprint() ones.
        '''

        separated_title = f'{DebugSettings.section_separators}{DebugSettings.section_title}{DebugSettings.section_separators}'
        print(f'\n{DebugSettings.section_color}{separated_title}{Style.RESET_ALL}')
        

    @staticmethod
    def pyprint(
        log_type: str,
        log_or_status: str,
        same_line: bool = False
    ):
        '''Debug Mode formatted print statements.
        
        Supported message types:
        - INFO -> Light blue
        - DATA -> Cyan
        - WARNING -> Yellow
        - ERROR -> Light red
        - SUCCESS -> Light green

        Args:
            log_type (str): Type of the log (Unsupported title returns white colored log).
            log_or_status_code (str): Printed log message or a status code if 'ST_000'
                where '000' is the status code integer corresponding to the one in the settings.
            same_line (bool, optional): Print on the same line as before.
        '''

        if (not DebugSettings.verbose_debugging and log_type in DebugSettings.forced_types) or DebugSettings.verbose_debugging:
            # Show the section title
            if Logger.__is_first_print:
                Logger.__show_section_title()
                Logger.__is_first_print = False
        
            # Get the color of the log
            color = Logger.__get_log_color(log_type)
            
            # Check if it's a status code
            if not log_or_status.startswith('ST_'):
                
                # Basic normal output
                if log_type not in DebugSettings.function_name_types:
                    output = f'[{log_type}] {log_or_status}'
                else:
                    # Get the function that calls pyprint
                    cur_frame = inspect.currentframe()
                    out_frame = inspect.getouterframes(cur_frame, 2)
                    output = f'[{log_type}] {out_frame[1][3]}(): {log_or_status}'
            
            # Status code case   
            else:
                if log_or_status in DebugSettings.status_codes:
                    output = f'[{log_or_status}] {DebugSettings.status_codes[int(log_or_status[3:])]}'
                    
                # Non-existing status code catch
                else:
                    color = Fore.LIGHTRED_EX
                    output = f'[PYPRINT_ERROR] Wrong status code, "{log_or_status}" does not exists'

            # Same line handling
            if same_line:
                print_end = '\r'
            else:
                print_end = None
            
            # Final output
            print(f'{color}{output}{Style.RESET_ALL}', end=print_end)
            
            
    @staticmethod
    def extime(
        name: str,
        timer: int,
        multiply_timer: int = 1,
        print_msg: bool = True,
        approximated_value: bool = False,
    ) -> str:
        '''Automatic timer format (ns, µs, ms, s and mins units).
        
        Args:
            name (str): Name of the timer.
            timer (int): Using time.perf_counter_ns() to get the starting point of the timer.
            multiply_timer (int, optional): Multiply the time by a value (To estimate time).
            print_msg (bool, optional): If True, it also prints the formatted timer message.
            approximated_value (bool, optional): If True, adds the "~" character for an approximation.
            
        Returns:
            str: The formatted timer message
        '''

        timer = (time.perf_counter_ns() - timer) * multiply_timer
        
        units = ['ns', 'µs', 'ms', 's', ' mins']
        powers = [10**3, 10**6, 10**9]
        res = 0
        i = 0
        
        if timer < powers[0]:
            res = timer
        elif powers[0] <= timer < powers[1]:
            res = round(timer / powers[0])
            i = 1
        elif powers[1] <= timer < powers[2]:
            res = round(timer / powers[1])
            i = 2
        elif powers[2] <= timer:
            res = timer / powers[2]
            i = 3
            
            # Using minutes instead
            if res > 120:
                res = round(res / 60)
                i = 4
        
        res = round(res, 2)
        
        if approximated_value:
            output = f'{name}: ~{res}{units[i]}'
        else:
            output = f'{name}: {res}{units[i]}'
        
        if print_msg:
            Logger.pyprint('SUCCESS', output)
        
        return output
