class Instrument():
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')


class Guitar(Instrument):
    def make_sound(self):
        print('吉他在演奏')


def play(instrument):
    instrument.make_sound()



play(Violin())
play(Guitar())
play(Erhu())