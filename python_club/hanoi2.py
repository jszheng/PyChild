def movedisk(disk, frompole, topole):
    print(f'MOVE DISK[{disk}] FROM {frompole} TO {topole}')
    print('MOVE DISK[%d]')


def movetower(height, frompole, withpole, topole):

    if height >= 1:
        movetower(height-1, frompole, withpole, topole)
        movedisk(height, frompole, topole)
        movetower(height-1, withpole, frompole, topole)


movetower(3, '#1', '#2', '#3')


