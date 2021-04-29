print('Pick a number between 1-100 and I\'ll try and guess it in 7 guesses')

def r_search(start, end, guesses):
    if guesses == 0:
        return 'MISSION FAILURE'
    mid = (start+end)//2
    check = input(f'Is {mid} your number? ').lower()
    if check == 'yes':
        return 'Yeet'
    if check == 'lower':
        return r_search(start, mid, guesses -1)
    if check == 'higher':
        return r_search(mid, end, guesses -1)


r_search(0, 100, 7)