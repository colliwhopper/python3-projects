#!/usr/bin/env python3

row1 = [ "⬜","⬜️","⬜️" ]
row2 = [ "⬜️","⬜️","⬜️" ]
row3 = [ "⬜️","⬜️","⬜️" ]

map = [ row1, row2, row3 ]

position = input( "Where do you want to put the treasure? " )

column = int( position[0] )
row = int( position[1] )

selected_row = map[ row -1 ]
selected_row[ column -1 ] = "X"
