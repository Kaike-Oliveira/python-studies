# Main file

# Imports
from log import LogFileMixin, LogPrintMixin

print('Main')

log_print = LogPrintMixin()
log_print.log_error('Any thing')
log_print.log_success('Any thing')

log_file = LogFileMixin()
log_file.log_error('Any thing')
log_file.log_success('Any thing')
