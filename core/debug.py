from colorama import Style, Fore

import inspect
import time


class Logger:
    # If true, print all the available logs,
    # Else, just the types defined in 'forced_types'
    verbose_debugging = True
    
    # The section title, to separate the logs
    section_separators = '-' * 35
    section_color = Fore.LIGHTBLUE_EX
    section_title = 'PYPRINT SECTION'
    
    # List of debug message types
    all_types = ['INFO', 'DATA', 'WARNING', 'ERROR', 'SUCCESS']
    forced_types = ['WARNING', 'ERROR', 'SUCCESS']
    
    # Status codes used for general errors
    # I usually use modified HTTP Status Codes
    # Simply use 'log_or_status' with 'ST_' and the code after it (log_or_status = 'ST_42')
    status_codes = {
        42: 'Pyprint Status Example'
    }
    
    # Internal vars
    __is_first_print = True
    
    
    def __get_log_color(self, log_type: str):
        '''Get the color of the log depending on the log type.
        
        Args:
            log_type (str): The type of the log.
            
        Returns:
            str: The colorama color chars.
        '''
        
        color = Fore.WHITE
        
        if log_type == self.all_types[0]:
            color = Fore.LIGHTBLUE_EX 
        elif log_type == self.all_types[1]:
            color = Fore.CYAN
        elif log_type == self.all_types[2]:
            color = Fore.YELLOW
        elif log_type == self.all_types[3]:
            color = Fore.LIGHTRED_EX
        elif log_type == self.all_types[4]:
            color = Fore.LIGHTGREEN_EX
            
        return color
        
    
    def __show_section_title(self):
        '''Show the section title (printed only once).
        It separates the normal console logs and pyprint() ones.
        '''

        separated_title = f'{self.section_separators}{self.section_title}{self.section_separators}'
        print(f'\n{self.section_color}{separated_title}{Style.RESET_ALL}')
        

    def pyprint(self,
        log_type: str,
        log_or_status: str,
        show_function_name: bool = True,
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
            show_function_name (bool, optional): Show the name of the calling function.
            same_line (bool, optional): Print on the same line as before.
        '''

        if (not self.verbose_debugging and log_type in self.forced_types) or self.verbose_debugging:
            # Show the section title
            if self.__is_first_print:
                self.__show_section_title()
                self.__is_first_print = False
        
            # Get the color of the log
            color = self.__get_log_color(log_type)
            
            # Check if it's a status code
            if not log_or_status.startswith('ST_'):
                
                # Basic normal output
                if not show_function_name:
                    output = f'[{log_type}] {log_or_status}'
                    
                else:
                    # Get the function that calls pyprint
                    cur_frame = inspect.currentframe()
                    out_frame = inspect.getouterframes(cur_frame, 2)
                    
                    output = f'[{log_type}] {out_frame[1][3]}(): {log_or_status}'
            
            # Status code case   
            else:
                if log_or_status in self.status_codes:
                    output = f'[{log_or_status}] {self.status_codes[log_or_status[3:]]}'
                    
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


    def extime(self,
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
            self.pyprint('SUCCESS', output)
        
        return output
