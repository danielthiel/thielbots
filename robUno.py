

class Robot:
    def act(self, game):
        do_this = ['move', (self.location[0]+1, self.location[1])]
        print do_this
        return do_this