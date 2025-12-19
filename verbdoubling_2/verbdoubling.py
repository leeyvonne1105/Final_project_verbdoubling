#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from verbdoubling.main import askLoki


def main():
    """"""
    return None


if __name__ == "__main__":
    inputSTR = "馬小莉看電影三小時"
    refDICT = {"FT":[]}
    resultDICT = askLoki(inputSTR, refDICT=refDICT)
    print(resultDICT)