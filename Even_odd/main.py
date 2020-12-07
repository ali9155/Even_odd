class EvenOdd():
    def even_odd():
        while True:
            data = input('please insert real number.its chek even or odd numbers:')
            try:
                int(data)
                if int(data) % 2 == 0:
                    print("%s is even number" % data)
                else:
                    print("%s is odd number" % data)
            except:
                print('please insert number!!!')

    even_odd()


