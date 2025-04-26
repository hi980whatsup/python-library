class workers:

    def __init__(self):
        print('workers are created.')

    def __del__(self):
            print('Destructor called, workers deleted.')
object=workers()
del object


      