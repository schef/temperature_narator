from kt403A import KT403A
import common

class Word:
    def __init__(self, f, duration):
        self.file = f
        self.duration = duration

word_to_file = {
    0: Word(1, 630),
    1: Word(2, 710),
    2: Word(3, 760),
    3: Word(4, 680),
    4: Word(5, 710),
    5: Word(6, 710),
    6: Word(7, 760),
    7: Word(8, 860),
    8: Word(9, 650),
    9: Word(10, 760),
}

sentence_to_word = {
    "0": [0],
    "10": [1, 0],
    "100": [1, 0, 0]
}

speaker = KT403A()
word_queue = []
wait_for_duration_timestamp = common.get_millis()


def is_playing():
    return speaker.IsPlaying()


@common.dump_func(showarg=True)
def play(index):
    speaker.PlaySpecific(index)


@common.dump_func(showarg=True)
def sentence_to_files(sentence):
    files = []
    for word in sentence_to_word[sentence]:
        files.append(word_to_file[word])
    return files


@common.dump_func(showarg=True)
def play_sentence(sentence):
    for f in sentence_to_files(sentence):
        word_queue.append(f)


def loop():
    global wait_for_duration_timestamp
    if len(word_queue) > 0 and common.millis_passed(wait_for_duration_timestamp) > word_queue[0].duration and not is_playing():
            wait_for_duration_timestamp = common.get_millis()
            word = word_queue.pop(0)
            play(word.file)


def loop_test():
    while(True):
        loop()
