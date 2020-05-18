import datetime
import json
import sys, re
import Levenshtein

print('Reading exams.json ...')
exams = []
try:
    with open('exams.json', 'r') as f:
        exams = json.load(f)
except IOError:
    print(f'Failed to read exams.json')
    sys.exit(1)

re_date = re.compile(r'^.+(?P<date>(\d{2}\.){2}20\d{2})\..+(?P<time>\d{2}\.\d{2})$')
re_info = re.compile(r'^\(.+\)$')

def find_exam_abbr(exam):
    lds = min(map(lambda e: (Levenshtein.distance(e[0], exam), e[1]), exams))
    if lds[0] > 6:
        return exam
    return lds[1]

def try_parse_location(info):
    loc = []
    if "Јагић" in info or "ЈАГ" in info:
        loc.append("JAG")
    if "Н" in info:
        loc.append("N")
    if not loc:
        return info
    return f'({",".join(loc)})'

def convert(text):
    lines = text.splitlines()
    
    years = ['', 'ПРВА', 'ДРУГА', 'ТРЕЋА', 'ЧЕТВРТА', 'ПЕТА', '']
    schedule = [ {'exams' : [], 'dates' : []} for y in range(len(years[0:-1])) ]

    curr_year = 0
    reading = False
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.endswith(':') or line.startswith(years[curr_year]) or line.startswith('-'):
            reading = False

        if Levenshtein.distance(f'{years[curr_year + 1]} ГОДИНА - информатика', line) < 3 or line.startswith('ПЕТА ГОДИНА - '):
            reading = True
            curr_year += 1
            continue

        if not reading:
            continue

        m = re_date.match(line)
        if m:
            exam_date = datetime.datetime.strptime(f"{m.group('date')} {m.group('time')}", "%d.%m.%Y %H.%M")
            exam_date = datetime.datetime.strftime(exam_date, "%Y-%m-%d %H:%M")
            if line.startswith('ПРАКТИЧНИ'):
                schedule[curr_year]['dates'][-1] += f' {exam_date}'
            else:
                schedule[curr_year]['dates'].append(exam_date)
        else: 
            if re_info.match(line) or str.islower(line[0]):
                schedule[curr_year]['exams'][-1] += f' {try_parse_location(line)}'
            else:
                schedule[curr_year]['exams'].append(find_exam_abbr(line))
    
    return schedule


def print_schedule(schedule):
    i = 1
    for y in schedule[1:]:
        print('-----------------------------------------------------')
        print(f'YEAR: {i}:')
        print('-----------------------------------------------------')
        for kvp in sorted(zip(y['dates'], y['exams'])):
            print(f'{kvp[1].ljust(30)} | {kvp[0].rjust(20)}')
        i += 1

def schedule_to_json(schedule):
    zipped = list(map(lambda y: list(sorted(zip(y['dates'], y['exams']))), schedule[1:]))
    return json.dumps(zipped, ensure_ascii=False, indent=4)
