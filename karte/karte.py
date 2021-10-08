import sys

def karte(lines):
    suites = ['P', 'K', 'H', 'T']
    found = {}

    for suite in suites:
        for i in range(1,14):
            if i < 10:
                found[f'{suite}0{i}'] = False
            else:
                found[f'{suite}{i}'] = False
    line = lines[0]
    for card in [line[i:i+3] for i in range(0, len(line), 3)]:
        if found.get(card, False):
            print('GRESKA')
            return ''
        found[card] = True

    suite_counter = {
        'P':0,
        'K':0,
        'H':0,
        'T':0,
    }
    for suite in suites:
        for i in range(1,14):
            if i < 10:
                if not found.get(f'{suite}0{i}', False):
                    suite_counter[suite] = suite_counter.get(suite, 0) + 1
            else:
                if not found.get(f'{suite}{i}', False):
                    suite_counter[suite] = suite_counter.get(suite, 0) + 1

    return suite_counter['P'], suite_counter['K'],suite_counter['H'],suite_counter['T']



def main():
    lines = [line.strip() for line in sys.stdin]
    print(' '.join([str(x) for x in karte(lines)]))
main()
