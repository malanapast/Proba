#for i while

'''
#######
 ######
  #####
   ####
    ###
     ##
      #

'''

for x in range(10):
    for y in range(10):
        if y > x:
        #if y<x: obrnuto bude
            print("#", end="")
        else:
            print(" ", end="")
    print()



automobil = 0
cilj = 100

brzina = 10
gorivo = 10
while automobil < cilj:
    print("voznja je u toku")
    automobil += brzina
    gorivo -= 5
    # if gorivo == 0:
    #     break
    #if automobil == cilj:
else:
    print("automobil je stigao na cilj")


    