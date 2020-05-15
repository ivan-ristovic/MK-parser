import argparse
import datetime
import json
import os
import pdfminer.high_level  
import sys
import wget
import sys

def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


parser = argparse.ArgumentParser(description='Convert MK PDF to a human readable format.')
parser.add_argument("-y", "--year", type=int, default=datetime.datetime.now().year,
                    help="Change year in URL because sometimes it is wrong")
parser.add_argument('--urls', nargs='*',
                    help='PDF URLs in case you wish to add them manually for some reason')
parser.add_argument('-j', '--json', 
                    help='Generate JSON output', dest='json', action='store_true')
parser.set_defaults(json=False)
args = vars(parser.parse_args())

files = []

if not args['urls']:
    def get_pdf_url(year, period):
        y = year % 100
        return f'http://poincare.matf.bg.ac.rs/~kmiljan/raspored/RASPORED_ISPITA_{period}_{y}{y+1}.pdf'

    for period in ['JAN', 'FEB', 'JUN', 'JUL', 'SEP', 'OKT']:
        files.append(get_pdf_url(args['year'], period))
        
pdfs = []
print('Downloading PDFs...')
print(files)
for f in files:
    overwrite = True
    filename = f.split('/')[-1]
    if os.path.exists(filename):
        print(f'File exists: {f}')
        overwrite = query_yes_no('Overwrite?', default='no')
    if overwrite:
        wget.download(f)
    pdfs.append(filename)
print('Downloaded PDFs.')

import conv

print('Parsing PDFs ...')
for pdf in pdfs:
    print(f'======== {pdf} ========')
    text = pdfminer.high_level.extract_text(pdf)
    schedule = conv.convert(text)
    if args['json']:
        print(conv.schedule_to_json(schedule))
    else:
        conv.print_schedule(schedule)
    print(f'=======================')

print('Done! Have a nice day.')
