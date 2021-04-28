class HardDisk:
    def __init__(self):
        self.capacity = 100
        self.us_space = 0
        self.num_file = 0

    def print_(self):
        print(f'Capacity on your disk - {self.capacity}\nUsed space is - {self.us_space}\nYou have {self.num_file} files on your disk')

    def free_space(self):
        free=self.capacity-self.us_space
        return free

    def add_file(self,GB_size):
        if GB_size<self.freeSpace():
            self.us_space+=GB_size
            self.num_file += 1
            return print("Done")
        else:
            print("You don't have enough space on you disk")
    def del_file(self,GB_size):
        if self.freeSpace()+GB_size >= self.capacity:
            self.us_space=0
            self.freeSpace()
            self.num_file-=1
        else:
            self.us_space-=GB_size
            self.num_file-=1