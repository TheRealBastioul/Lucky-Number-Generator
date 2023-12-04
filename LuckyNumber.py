import timeit


# Created by Vincent aka Bast
def tester():
    start = timeit.default_timer()
    bday = str(input('Enter your birthday example(month/day/year = 1/1/2020)'))
    # This is to calculate runtime it is pasted below input, so it does not count how long it takes for you to input
    splitter = bday.split('/')
    #lucky variable is a number derived from the birth month it is used to calculate the lucky number.
    lucky = int(splitter[1])
    tuple_dict = {'ones': (), 'tens': (), 'hundreds': (), 'thousands': ()}
    ranger = int(splitter[0]) + int(splitter[2])
    basttuple = tuple(range(1, ranger))
    #This function seperates the numbers in the range to be organized tuple_dict. Then it checks to see if each number is divisible by the lucky number.
    def solve(number):
        def arrange(number):
            for i in basttuple:
                if i % number == 0:
                    if len(str(i)) == 1:
                        tuple_dict['ones'] += i,
                    elif len(str(i)) == 2:
                        tuple_dict['tens'] += i,
                    elif len(str(i)) == 3:
                        tuple_dict['hundreds'] += i,
                    elif len(str(i)) == 4:
                        tuple_dict['thousands'] += i,
            return tuple_dict

        #This is to iterate through each item in the dictionary using items() method
        for key, value in arrange(number).items():
            #This enumerates the values, and starts index at 1 so we are able to get a count of how many numbers exist
            x = enumerate(value, 1)
            b = tuple(x)
            print(f'There is {len(b)} number/s in the {key} that are divisible by {number} in the range of {ranger}')
            print('These numbers are..')
            print(value)
        #This zips together the hundreds and thousands to solve your lucky number
        return tuple(zip(tuple_dict['hundreds'], tuple_dict['thousands']))

    #This grabs the last index of the zipped tuple to give you your lucky number
    luck = tuple(enumerate(solve(lucky)))[-1][0]
    print(f'Your lucky number is {luck}.')
    #This is how long it took for the code to process
    print('time taken')
    stop = timeit.default_timer()
    print(start - stop)


tester()
