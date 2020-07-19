def Hanoi(N, source, dest, spare):
    # This function moves N disks from peg source to peg destination
    # source: where to move from
    # dest: where to move to
    # spare: spare peg
    if N == 1:
        # move disk from source to dest
        print('move disk '+str(N)+' from '+source+' to '+dest)
    else:
        # move all top stack, but larger one, from source to spare
        Hanoi (N-1, source, spare, dest)
        # since the top stack has gone, we can move the larger disc directly from source to dest
        print('move disk '+str(N)+' from '+source+' to '+dest)
        # move all top stack from spare to dest, on top of the larger disc which has just been moved on to dest
        Hanoi (N-1, spare, dest, source)

# move 4 disks from A to C
Hanoi(5,'A','C','B')

        

