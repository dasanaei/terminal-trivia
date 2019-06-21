import urllib, json
import urllib.request
from msvcrt import getch
from statistics import statistics

for i in range(30):
    stat = statistics("category", "difficulty")
    for n in range(10):
        stat.record("correct", "speed")
    stat.endGameRecord("final score", "total time")

