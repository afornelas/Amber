import linearwinvolume
import sys

def change_volume(amount):
    print('change by '+str(amount))
    linearwinvolume.change_volume(amount)

def set_volume(amount):
    print('set to '+str(amount))
    linearwinvolume.set_volume(amount)

if __name__ == "__main__":
    command = str(sys.argv[1])
    value = int(float(sys.argv[2]))
    if command == 'set':
        set_volume(value)
    elif command == 'change':
        change_volume(value)
    else:
        print('Inncorrect arguments')
    sys.exit()