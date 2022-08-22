# mahjong
Playing the game of Mahjong

# Start
`play.py` to start playing the game
For the fastest input time, input of hand is by convention below.  
For example, '1w2t3t3f' is '一万，二条，三条，西风'.

# Conventions
w - 万  
t - 条  
b - 饼  
f - 风（按'东南西北中发白'的顺序）  
h - 花牌 (按'春夏秋冬梅兰竹菊'的顺序)  
For example, 1w is 一万. 2f is 南风. 4h is 冬.

# Tasks
* Basic objects for tiles and suit
* Group tiles so the we know what tiles can complete a set
* Recognize complicated sets. e.g. group of more than 2. 1) aab, 2) abcd, 3) abcde, 4) ace, 5) abde, 6) aabbc
* Suggest the best tile to discard

# resources
dataclass basics  
https://betterprogramming.pub/python-data-classes-196496c32d75

unittest basics  
https://www.pythontutorial.net/python-unit-testing/python-run-unittest/

other python packages for mahjong  
https://github.com/Kenny2github/mahjong/wiki

Unicode mahjong characters  
https://zh.wikipedia.org/wiki/%E9%BA%BB%E5%B0%87%E7%89%8C_(Unicode%E5%8D%80%E6%AE%B5)  
https://unicode-table.com/en/1F000/  