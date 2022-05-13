from random import randint, choice
from time import sleep

# printing functions
SLOW_PRINT_SPEED = 0.05 # seconds / character
FAST_PRINT_SPEED = 0.03 # seconds / character
REALLY_FAST_PRINT_SPEED = 0.01 # seconds / character
CREDITS_PRINT_SPEED = 0.0004 # seconds / character
ASCII_PUZZLE_PRINT_SPEED = 0.001 # seconds / character

def slow_print(string):
    for char in string:
        print(char, end='', flush=True)
        sleep(SLOW_PRINT_SPEED)
    print()

def fast_print(string):
    for char in string:
        print(char, end='', flush=True)
        sleep(FAST_PRINT_SPEED)
    print()

def really_fast_print(string):
    for char in string:
        print(char, end='', flush=True)
        sleep(REALLY_FAST_PRINT_SPEED)
    print()

def credits_print(string):
    for char in string:
        print(char, end='', flush=True)
        sleep(CREDITS_PRINT_SPEED)
    print()

def ascii_puzzle_print(string):
    for char in string:
        print(char, end='', flush=True)
        sleep(ASCII_PUZZLE_PRINT_SPEED)
    print()

# create ascii puzzle

def ascii_puzzle():
    print()
    for row in image:
        ascii_puzzle_print(row)
    print()
    for row in image_2:
        print(' ' * 19, end='')
        ascii_puzzle_print(row)
    print()

image = ["MMMMMMMMMMMMMMMMNk    kNMMMMMMMMMMMMMMM  MMMMMMMMMMMWxoXMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMW0:.''.'oXMMM",
"MMMMMMMMMMMMMMNk,      ,kNMMMMMMMMMMMMM  MMMMMMMMMMWx..kWMMMMMMMMMMMMMMMMMMMMMMMMM  XXXXXXXXXXXXNNNNWMMMMMMMMMMX:      .dWMM",
"MMMMMMMMMMMMNk,          ,kNMMMMMMMMMMM  MMMMMMMWXOc.  ,0MMMMMMMMMMMMMMMMMMMMMMMMM  ...............o0WMMMMMMMMWXl      .kMMM",
"MMMMMMMMMMNk,              ,kNMMMMMMMMM  MMWXOdc,.      cNMMMMMMMMMMMMMMMMMMMMMMMM  XXXXXXXXXXXXXXXNWMMMMMN0dc,,,,,'',l0WMMM",
"MMMMMMMMNk,                  ,kNMMMMMMM  Mo;.           .xWMMMMMMMMMMMMMMMMMMMMMMK  dddddddddddONMMMMN0doc'.      'dXWMMMMMM",
"MMMMMMNx,                      ,xNMMMMM  M,              '0MMMMMMMMMMMMMMMMMMMMWk;  .............N0xc'.            .kMMMMMMM",
"MMMMNk,                          ,kNMMM  M0,     .    .,:o0WMMMMMMMMMMMMMMMMMW0c.,  XXXXXXXXNMMNd,.   .;coo.        :XMMMMMM",
"MMNk,                              ,kNM  MWO;,cdOOocooooc;,lkOkkkkkkkkkkkkkxl;. 'O  DDDDMMMMMMMMK:..,lkKWMX:         .dWMMMM",
"Nk,                                  ,k  NMMWWMMMWOc,.                         :0M  NNNNNNNNWMMMNKKNMMWKx:      :x,  .cdk0XW",
"kNMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMNl                           lXM  ..........MMMMMMMXo.       '0WO,      .;",
"kNMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMNc                          .kMM  MMMMMMMMMMMMMMMNx'         .lXWXOxoc;MMM",
"kNMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMMNc                          .kM  MMMMMMMMMMWX0ko;     'ox;    ,OWMMMMWNNW",
"kNMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMMNc                          .OM  MMMMMMWOl:,..     .lkKWMNd.   .xWMMMMMMM",
"kNMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMMNc      ...............     .OM  MMMMMM0'     .':lxKWMMMMMWk.   :XMMMMMMM",
"MMMMMMMMMMMMMMWl        lWMMNkMMMMMMMMM  MMMMMMMMMMX:    .kMMMMMMMMMMMMMMX:    '0M  MMMMMMNkcclxOKNWMMMMMMMMMWx.  .dWMMMMMMM",
"kNMMMMMMMMMMMMWl        lWMMMMMMMMMMMMN  kMMMMMMMMMX;    :XMMMMMMMMMMMMMMWx.   '0M  MMMMMMMMMMMMMMMMMMMMMMMMX:   :XMMMMMMMMM",
"MMMMMMMMMMMMMMWlMMMMMMMMlWMMMMMMMMMMMMM  MMMMMMMMMMX;   .dWMMMMMMMMMMMMMMM0'   ,KM  MMMMMMMMMMMMMMMMMMMMMMMMNo. 'kMMMMMMMMMM"]

image_2 = ["MMMMMMMMMMMMMMMMMMMMMMMWkMMMMMMMMMMMMMM  MMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMWOl            M  MMWKMMM    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMMWNNNNNN0o    kN  MMMW0M       MMMMMMMMMMMMMMMMMMMMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc    KWM  MMMMN         MMMMMMMMMMMMWM  MMMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMWKd;    NMMM  MMMW          MMMMMMMMMMMMWO   MMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMMMMNOc     KWMMM  MMW          MMMMMMMMMMMMMK        MMMMMM",
"MMMMMMMMMXMMM         XOccc     ddddoMM  MMX         MMMMMMMMMMMW0               M",
"MMMMMMMMMNkoooooc    xXdMM            M  MMNd                                  MMM",
"MMMMMMMMMMWWWWN0   cOWWXOOOOOOOOOOOOO0M  MMW0d                              MMMMMM",
"MMMMMMMMMMMMMNx   XWMMMMMMMMMMMMMMMMMMM  MMMWXds                        MMMMMMMMMM",
"MMMMMMMMMMMMMM          MMMMMMMMMMMMMMM  MMMMMMMMM                      MMMMMMMMMM",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMWK                     MMMMMMMMMMM",
"MMMM        MMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMW0ddM        xXWWO        MMMMMMMMMM",
"MMMMMMMM   MMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMWxMMMM  d   WMMM0l   d   MMMMMMMMMMM",
"MWXxMMM   WWWWWWWWWWWWMMMMMMMMMMMMMMMMM  MMMMMWMMMM  Kdd  MMMMWk  kOd  XMMMMMMMMMM",
"NWWWMM       MMMMMMMMMMMMMMMMMMMMMMMMWM  MMMMMMNXXM  WNX  MMMMMW  NWN  WMMMMMMMMMM",
"NWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWW  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"]

# bonus game functions

def get_random_image():
    images = [bat, spider, dolphin, alien, owl, lion, scorpion, monkey]
    random_image = choice(images)
    return random_image

def scramble_image(image, percent_scrambled):
    scrambled_image = []
    index = 0
    for row in image:
        scrambled_image.append('')
        for symbol in row:
            if randint(1,100) < percent_scrambled:
                scrambled_image[index] += 'X'
            else:
                scrambled_image[index] += symbol
        index += 1
    for row in scrambled_image:
        really_fast_print(row)

# bonus game images

dolphin = {"animal" : [
    "                    ",
    "       ,-._         ",
    "     _.-'  '--.     ",
    "   .'      _  -`\_  ",
    "  / .----.`_.'----' ",
    "  ;/     `          ",
    " /_;                ",
    "                    "
    ], "name" : "dolphin"}

bat = {"animal" : [
    "                       ",
    " /\                 /\ ",
    "/ \\'._   (\_/)   _.'/ \ ",
    "|.''._'--(o.o)--'_.''.|",
    ' \_ / `;=/ " \=;` \ _/ ',
    "   `\__| \___/ |__/`   ",
    "        \(_|_)/        ",
    '         " ` "         ',
    "                       "
    ], "name" : "bat"}

spider = {"animal" : [
    "                       ",
    "          (            ",
    "           )           ",
    "          (            ",
    '     /\ .-"""-.  /\    ',
    '   //\\\\/  ,,,  \//\\\\   ',
    "   |/\| ,;;;;;, |/\|   ",
    '   //\\\\\;-"""-;///\\\\   ',
    '  //  \/   .   \/  \\\\  ',
    " (| ,-_| \ | / |_-, |) ",
    "   //`__\.-.-./__`\\\\   ",
    "  // /.-(() ())-.\ \\\\  ",
    " (\ |)   '---'   (| /) ",
    "  ` (|           |) `  ",
    "    \)           (/    "
    ], "name" : "spider"}

alien = {"animal" : [
    "       ______       ",
    "      /_.  ._\\    ",
    "     (( \\\\// ))     ",
    "      \\\\ \/ //      ",
    "       \\\\/\//       ",
    "  \\\\\  ( '' )  ///  ",
    "   )))  \__/  (((   ",
    "  (((.'__||__'.)))  ",
    "   \\\\  )    (  //   ",
    "    \\\\/.'  '.\//    ",
    "     \/ |,,| \/     ",
    "        |  |        ",
    "        |  |        ",
    "        //\\\\        ",
    "       //  \\\\       ",
    "      ||    ||      ",
    "      ||    ||      ",
    "      ||    ||      ",
    "   ___))    ((___   ",
    "  (____)    (____)  ",
    ], "name" : "alien"}

owl = {"animal" :[
"                          ",
"       __________         ",
"      / ___  ___ \        ",
"     / / @ \/ @ \ \       ",
"     \ \___/\___/ /\      ",
"      \____/ ____/||      ",
"      /     /\\\\\\\\\//      ",
"      |     |\\\\\\\\\\\\       ",
"       \      \\\\\\\\\\\\      ",
"        \______/\\\\\\\\      ",
"         _||_||_          ",
"                          ",
], "name" : "owl"}

lion = {"animal" : [
"        \|\||                                    ",  
"       -- ||||/                                  ",
"      /@   |||||/                                ",     
"     /    |||||||/`-.____________                ",
"     \-' |||||||||               `-._            ",
"      -/||||||||\                `` -`.          ",
"        /||||||\             \_  |   \\\\          ",
"        //|||\|________...---'\  \    \\\\         ",
"           |  |  \           | \  |    ``-.__--. ",
"           |  |\  \         / / | |       ``---' ",
"         _/  / _|  )     __/ / _| |              ",
"       /,__/ /,__/     /,__/ /,__/               "
], "name" : "lion"}

scorpion = {"animal" : [
"          /  \              /  \          ",
"         /|  |\            /|  |\         ",
"        / |  | \          / |  | \        ",
"       | |  | |          | |  | |         ",
"       \  \/  /  __  __  \  \/  /         ",
"        \    /  / /  \ \  \    /          ",
"         \  /   \ \__/ /   \  /           ",
"         \  /   /      \   \  /           ",
"        _ \ \__/ O    O \__/ / _          ",
"        \\\\ \___          ___/ //          ",
"      _  \\\\___/  ______  \___//  _        ",
"      \\\\  ----(          )----  //        ",
"       \\\\_____( ________ )_____//         ",
"        ~-----(          )-----~ _        ",
"         _____( ________ )_____  \\\\       ",
"        /,----(          )----  _//       ",
"       //     (  ______  )     /  \       ",
"       ~       \        /      \  /       ",
"                \  __  /       / /        ",
"                 \    /       / /         ",
"                  \   \      / /          ",
"                   \   ~----~ /           ",
"                    \________/            "
], "name" : "scorpion"}

monkey = {"animal" :[
"     _...._                    ",
"   .-.     /                   ",
"  /o.o\ ):.\                   ", 
"  \   / `- .`--._              ",
"  // /            `-.          ",
" '...\     .         `.        ",
"  `--''.    '          `.      ",
"      .'   .'            `-.   ",
"   .-'    /`-.._            \  ",
" .'    _.'      :      .-'\"'/  ",
"| _,--`       .'     .'    /   ",
"\ \          /     .'     /    ",
" \///        |    ' |    /     ",
"             \   (  `.   ``-.  ",
"              \   \   `._    \ ",
"            _.-`   )    .'    )",
"            `.__.-'  .-' _-.-' ",
"                     `.__,'    ",
], "name" : "monkey"}