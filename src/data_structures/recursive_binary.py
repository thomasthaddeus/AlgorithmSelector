def find(low, high):
    mid = (high + low) // 2  # Midpoint of low..high
    answer  = input(f'Is it {mid}? (l/h/y): ')

    if (answer != 'l') and (answer != 'h'):  # Base case
        print('Got it!')
    else:
        if answer == 'l':
            find(low, mid)
        else:
            find(mid+1, high)

print('Choose a number from 0 to 100.')
print('Answer with:')
print('   l (your num is lower)')
print('   h (your num is higher)')
print(' any other key (guess is right).')

find(0, 100)
