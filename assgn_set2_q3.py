def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    five_needed = rupees_to_make//5
    one_needed = rupees_to_make-five_needed*5
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    if no_of_one<one_needed:
        print(-1)
    elif no_of_five<five_needed:
        rem = rupees_to_make-no_of_five*5
        if no_of_one<rem:
            print(-1)
        else:
            print("No. of Five needed :", no_of_five)
            print("No. of One needed  :", rem)
    else: #if no_of_five>=five_needed:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)


    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)

make_amount(19,3,3)