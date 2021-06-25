from kt403A import KT403A
import common


class Sentence:
    def __init__(self, f, duration):
        self.file = f
        self.duration = duration


temperature_sentence = {
    0: Sentence(1, 932),  # ./1000.mp3
    1: Sentence(2, 954),  # ./1001.mp3
    2: Sentence(3, 954),  # ./1002.mp3
    3: Sentence(4, 954),  # ./1003.mp3
    4: Sentence(5, 954),  # ./1004.mp3
    5: Sentence(6, 954),  # ./1005.mp3
    6: Sentence(7, 936),  # ./1006.mp3
    7: Sentence(8, 954),  # ./1007.mp3
    8: Sentence(9, 947),  # ./1008.mp3
    9: Sentence(10, 954),  # ./1009.mp3
    10: Sentence(11, 954),  # ./1010.mp3
    11: Sentence(12, 892),  # ./1011.mp3
    12: Sentence(13, 959),  # ./1012.mp3
    13: Sentence(14, 1157),  # ./1013.mp3
    14: Sentence(15, 1155),  # ./1014.mp3
    15: Sentence(16, 1227),  # ./1015.mp3
    16: Sentence(17, 1184),  # ./1016.mp3
    17: Sentence(18, 1090),  # ./1017.mp3
    18: Sentence(19, 1155),  # ./1018.mp3
    19: Sentence(20, 1175),  # ./1019.mp3
    20: Sentence(21, 1128),  # ./1020.mp3
    21: Sentence(22, 1462),  # ./1021.mp3
    22: Sentence(23, 1584),  # ./1022.mp3
    23: Sentence(24, 1582),  # ./1023.mp3
    24: Sentence(25, 1607),  # ./1024.mp3
    25: Sentence(26, 1666),  # ./1025.mp3
    26: Sentence(27, 1640),  # ./1026.mp3
    27: Sentence(28, 1719),  # ./1027.mp3
    28: Sentence(29, 1534),  # ./1028.mp3
    29: Sentence(30, 1561),  # ./1029.mp3
    30: Sentence(31, 1095),  # ./1030.mp3
    31: Sentence(32, 1446),  # ./1031.mp3
    32: Sentence(33, 1561),  # ./1032.mp3
    33: Sentence(34, 1561),  # ./1033.mp3
    34: Sentence(35, 1583),  # ./1034.mp3
    35: Sentence(36, 1596),  # ./1035.mp3
    36: Sentence(37, 1613),  # ./1036.mp3
    37: Sentence(38, 1649),  # ./1037.mp3
    38: Sentence(39, 1517),  # ./1038.mp3
    39: Sentence(40, 1526),  # ./1039.mp3
    40: Sentence(41, 1139),  # ./1040.mp3
    41: Sentence(42, 1500),  # ./1041.mp3
    42: Sentence(43, 1570),  # ./1042.mp3
    43: Sentence(44, 1570),  # ./1043.mp3
    44: Sentence(45, 1587),  # ./1044.mp3
    45: Sentence(46, 1605),  # ./1045.mp3
    46: Sentence(47, 1605),  # ./1046.mp3
    47: Sentence(48, 1649),  # ./1047.mp3
    48: Sentence(49, 1508),  # ./1048.mp3
    49: Sentence(50, 1561),  # ./1049.mp3
    50: Sentence(51, 1209),  # ./1050.mp3
    51: Sentence(52, 1499),  # ./1051.mp3
    52: Sentence(53, 1631),  # ./1052.mp3
    53: Sentence(54, 1640),  # ./1053.mp3
    54: Sentence(55, 1649),  # ./1054.mp3
    55: Sentence(56, 1657),  # ./1055.mp3
    56: Sentence(57, 1675),  # ./1056.mp3
    57: Sentence(58, 1693),  # ./1057.mp3
    58: Sentence(59, 1570),  # ./1058.mp3
    59: Sentence(60, 1596),  # ./1059.mp3
    60: Sentence(61, 1139),  # ./1060.mp3
    61: Sentence(62, 1402),  # ./1061.mp3
    62: Sentence(63, 1534),  # ./1062.mp3
    63: Sentence(64, 1534),  # ./1063.mp3
    64: Sentence(65, 1543),  # ./1064.mp3
    65: Sentence(66, 1587),  # ./1065.mp3
    66: Sentence(67, 1578),  # ./1066.mp3
    67: Sentence(68, 1613),  # ./1067.mp3
    68: Sentence(69, 1508),  # ./1068.mp3
    69: Sentence(70, 1517),  # ./1069.mp3
    70: Sentence(71, 1139),  # ./1070.mp3
    71: Sentence(72, 1438),  # ./1071.mp3
    72: Sentence(73, 1543),  # ./1072.mp3
    73: Sentence(74, 1534),  # ./1073.mp3
    74: Sentence(75, 1543),  # ./1074.mp3
    75: Sentence(76, 1587),  # ./1075.mp3
    76: Sentence(77, 1596),  # ./1076.mp3
    77: Sentence(78, 1631),  # ./1077.mp3
    78: Sentence(79, 1499),  # ./1078.mp3
    79: Sentence(80, 1508),  # ./1079.mp3
    80: Sentence(81, 1103),  # ./1080.mp3
    81: Sentence(82, 1429),  # ./1081.mp3
    82: Sentence(83, 1561),  # ./1082.mp3
    83: Sentence(84, 1534),  # ./1083.mp3
    84: Sentence(85, 1552),  # ./1084.mp3
    85: Sentence(86, 1596),  # ./1085.mp3
    86: Sentence(87, 1587),  # ./1086.mp3
    87: Sentence(88, 1613),  # ./1087.mp3
    88: Sentence(89, 1508),  # ./1088.mp3
    89: Sentence(90, 1526),  # ./1089.mp3
    90: Sentence(91, 1121),  # ./1090.mp3
    91: Sentence(92, 1411),  # ./1091.mp3
    92: Sentence(93, 1552),  # ./1092.mp3
    93: Sentence(94, 1534),  # ./1093.mp3
    94: Sentence(95, 1570),  # ./1094.mp3
    95: Sentence(96, 1578),  # ./1095.mp3
    96: Sentence(97, 1596),  # ./1096.mp3
    97: Sentence(98, 1622),  # ./1097.mp3
    98: Sentence(99, 1499),  # ./1098.mp3
    99: Sentence(100, 1517),  # ./1099.mp3
    100: Sentence(101, 1191),  # ./1100.mp3
    101: Sentence(102, 1851),  # ./1101.mp3
    102: Sentence(103, 1851),  # ./1102.mp3
    103: Sentence(104, 1851),  # ./1103.mp3
    104: Sentence(105, 1851),  # ./1104.mp3
    105: Sentence(106, 1851),  # ./1105.mp3
    106: Sentence(107, 1825),  # ./1106.mp3
    107: Sentence(108, 1851),  # ./1107.mp3
    108: Sentence(109, 1851),  # ./1108.mp3
    109: Sentence(110, 1851),  # ./1109.mp3
    110: Sentence(111, 1851),  # ./1110.mp3
    111: Sentence(112, 1799),  # ./1111.mp3
    112: Sentence(113, 1851),  # ./1112.mp3
    113: Sentence(114, 2495),  # ./1113.mp3
    114: Sentence(115, 2495),  # ./1114.mp3
    115: Sentence(116, 1949),  # ./1115.mp3
    116: Sentence(117, 2495),  # ./1116.mp3
    117: Sentence(118, 2495),  # ./1117.mp3
    118: Sentence(119, 2495),  # ./1118.mp3
    119: Sentence(120, 2495),  # ./1119.mp3
    120: Sentence(121, 2495),  # ./1120.mp3
    121: Sentence(122, 3040),  # ./1121.mp3
    122: Sentence(123, 3040),  # ./1122.mp3
    123: Sentence(124, 3040),  # ./1123.mp3
    124: Sentence(125, 3040),  # ./1124.mp3
    125: Sentence(126, 3040),  # ./1125.mp3
    -1: Sentence(127, 1363),  # ./2001.mp3
    -2: Sentence(128, 1376),  # ./2002.mp3
    -3: Sentence(129, 1363),  # ./2003.mp3
    -4: Sentence(130, 1363),  # ./2004.mp3
    -5: Sentence(131, 1363),  # ./2005.mp3
    -6: Sentence(132, 1363),  # ./2006.mp3
    -7: Sentence(133, 1409),  # ./2007.mp3
    -8: Sentence(134, 1363),  # ./2008.mp3
    -9: Sentence(135, 1363),  # ./2009.mp3
    -10: Sentence(136, 1392),  # ./2010.mp3
    -11: Sentence(137, 1363),  # ./2011.mp3
    -12: Sentence(138, 1500),  # ./2012.mp3
    -13: Sentence(139, 1597),  # ./2013.mp3
    -14: Sentence(140, 1500),  # ./2014.mp3
    -15: Sentence(141, 1636),  # ./2015.mp3
}


speaker = None
sentence_queue = []
wait_for_duration_timestamp = common.get_millis()


def is_playing():
    return speaker.IsPlaying()


@common.dump_func(showarg=True)
def play(index):
    speaker.PlaySpecific(index)


@common.dump_func(showarg=True)
def play_temperature(temperature):
    sentence_queue.append(temperature_sentence[temperature])

def init():
    global speaker
    speaker = KT403A(volume=70)
    

def loop():
    global wait_for_duration_timestamp
    if len(sentence_queue) > 0 and common.millis_passed(wait_for_duration_timestamp) > sentence_queue[0].duration and not is_playing():
        wait_for_duration_timestamp = common.get_millis()
        word = sentence_queue.pop(0)
        play(word.file)


def loop_test():
    while(True):
        loop()
