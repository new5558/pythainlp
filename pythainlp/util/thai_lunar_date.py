# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
This file is port from
> https://gist.github.com/touchiep/99f4f5bb349d6b983ef78697630ab78e
"""
from datetime import date, timedelta
from typing import Tuple, Union


def XLMod(a: float, b: float) -> int:
    return a - b * int(a / b)


StartY = [[0 for _ in range(2)] for _ in range(113)]
years = [
    0, 1901, 1906, 1911, 1916, 1921, 1926, 1931, 1936, 1941, 1946,
    1951, 1956, 1961, 1966, 1971, 1976, 1981, 1986, 1991, 1996,
    2001, 2006, 2011, 2016, 2021, 2026, 2031, 2036, 2041, 2046,
    2051, 2056, 2061, 2066, 2071, 2076, 2081, 2086, 2091, 2096,
    2101, 2106, 2111, 2116, 2121, 2126, 2131, 2136, 2141, 2146,
    2151, 2156, 2161, 2166, 2171, 2176, 2181, 2186, 2191, 2196,
    2201, 2206, 2211, 2216, 2221, 2226, 2231, 2236, 2241, 2246,
    2251, 2256, 2261, 2266, 2271, 2276, 2281, 2286, 2291, 2296,
    2301, 2306, 2311, 2316, 2321, 2326, 2331, 2336, 2341, 2346,
    2351, 2356, 2361, 2366, 2371, 2376, 2381, 2386, 2391, 2396,
    2401, 2406, 2411, 2416, 2421, 2426, 2431, 2436, 2441, 2446,
    2451, 2456
]
for i, year in enumerate(years):
    StartY[i][0] = year

v = [
    0,
    0.122733000004352,
    1.91890000045229E-02,
    -8.43549999953059E-02,
    -0.187898999995135,
    -0.291442999994964,
    7.44250000052413E-02,
    -2.91189999945876E-02,
    -0.132662999994416,
    -0.236206999994245,
    -0.339750999994074,
    -0.443294999993903,
    -7.74269999936981E-02,
    -0.180970999993527,
    -0.284514999993356,
    -0.388058999993185,
    -0.491602999993014,
    -0.595146999992842,
    -0.698690999992671,
    -0.332822999992466,
    -0.436366999992295,
    -0.539910999992124,
    -0.643454999991953,
    0.253001000008218,
    0.149457000008389,
    -0.484674999991406,
    -0.588218999991235,
    0.308237000008937,
    0.204693000009108,
    0.101149000009279,
    -2.39499999055015E-03,
    -0.105938999990379,
    0.259929000009826,
    0.156385000009997,
    5.28410000101682E-02,
    -5.07029999896607E-02,
    -0.15424699998949,
    -0.257790999989318,
    0.108077000010887,
    4.53300001105772E-03,
    -9.90109999887712E-02,
    -0.2025549999886,
    -0.306098999988429,
    -0.409642999988258,
    -4.37749999880528E-02,
    -0.147318999987882,
    -0.250862999987711,
    -0.354406999987539,
    -0.457950999987368,
    -0.561494999987197,
    -0.665038999987026,
    -0.299170999986821,
    -0.40271499998665,
    -0.506258999986479,
    -0.609802999986308,
    -0.713346999986137,
    0.183109000014035,
    -0.45102299998576,
    -0.554566999985589,
    0.341889000014582,
    0.238345000014753,
    0.134801000014924,
    3.12570000150951E-02,
    -7.22869999847338E-02,
    0.293581000015471,
    0.190037000015642,
    8.64930000158135E-02,
    -1.70509999840154E-02,
    -0.120594999983844,
    -0.224138999983673,
    0.141729000016532,
    0.038185000016703,
    -6.53589999831259E-02,
    -0.168902999982955,
    -0.272446999982784,
    -0.375990999982613,
    -1.01229999824075E-02,
    -0.113666999982236,
    -0.217210999982065,
    -0.320754999981894,
    -0.424298999981723,
    -0.527842999981552,
    -0.631386999981381,
    -0.265518999981176,
    -0.369062999981005,
    -0.472606999980834,
    -0.576150999980662,
    -0.679694999980491,
    0.21676100001968,
    -0.417370999980115,
    -0.520914999979944,
    -0.624458999979773,
    0.271997000020398,
    0.168453000020569,
    6.49090000207404E-02,
    -3.86349999790885E-02,
    0.327233000021117,
    0.223689000021288,
    0.120145000021459,
    1.66010000216299E-02,
    -0.086942999978199,
    -0.190486999978028,
    0.175381000022177,
    7.18370000223483E-02,
    -3.17069999774806E-02,
    -0.135250999977309,
    -0.238794999977138,
    -0.342338999976967,
    2.35290000232378E-02,
    -8.00149999765911E-02,
    -0.18355899997642,
    -0.287102999976249,
    -0.390646999976078]
for i, year in enumerate(v):
    StartY[i][1] = year


def calculate_Fyear_FDev(iYear: int) -> Tuple[int, float]:
    if iYear >= 2456:
        Fyear, FDev = StartY[112]
    elif iYear >= 2451:
        Fyear, FDev = StartY[111]
    elif iYear >= 2446:
        Fyear, FDev = StartY[110]
    elif iYear >= 2441:
        Fyear, FDev = StartY[109]
    elif iYear >= 2436:
        Fyear, FDev = StartY[108]
    elif iYear >= 2431:
        Fyear, FDev = StartY[107][0], StartY[107][1]
    elif iYear >= 2426:
        Fyear, FDev = StartY[106][0], StartY[106][1]
    elif iYear >= 2421:
        Fyear, FDev = StartY[105][0], StartY[105][1]
    elif iYear >= 2416:
        Fyear, FDev = StartY[104][0], StartY[104][1]
    elif iYear >= 2411:
        Fyear, FDev = StartY[103][0], StartY[103][1]
    elif iYear >= 2406:
        Fyear, FDev = StartY[102][0], StartY[102][1]
    elif iYear >= 2401:
        Fyear, FDev = StartY[101][0], StartY[101][1]
    elif iYear >= 2396:
        Fyear, FDev = StartY[100][0], StartY[100][1]
    elif iYear >= 2391:
        Fyear, FDev = StartY[99][0], StartY[99][1]
    elif iYear >= 2386:
        Fyear, FDev = StartY[98][0], StartY[98][1]
    elif iYear >= 2381:
        Fyear, FDev = StartY[97][0], StartY[97][1]
    elif iYear >= 2376:
        Fyear, FDev = StartY[96][0], StartY[96][1]
    elif iYear >= 2371:
        Fyear, FDev = StartY[95][0], StartY[95][1]
    elif iYear >= 2366:
        Fyear, FDev = StartY[94][0], StartY[94][1]
    elif iYear >= 2361:
        Fyear, FDev = StartY[93][0], StartY[93][1]
    elif iYear >= 2356:
        Fyear, FDev = StartY[92][0], StartY[92][1]
    elif iYear >= 2351:
        Fyear, FDev = StartY[91][0], StartY[91][1]
    elif iYear >= 2346:
        Fyear, FDev = StartY[90][0], StartY[90][1]
    elif iYear >= 2341:
        Fyear, FDev = StartY[89][0], StartY[89][1]
    elif iYear >= 2336:
        Fyear, FDev = StartY[88][0], StartY[88][1]
    elif iYear >= 2331:
        Fyear, FDev = StartY[87][0], StartY[87][1]
    elif iYear >= 2326:
        Fyear, FDev = StartY[86][0], StartY[86][1]
    elif iYear >= 2321:
        Fyear, FDev = StartY[85][0], StartY[85][1]
    elif iYear >= 2316:
        Fyear, FDev = StartY[84][0], StartY[84][1]
    elif iYear >= 2311:
        Fyear, FDev = StartY[83][0], StartY[83][1]
    elif iYear >= 2306:
        Fyear, FDev = StartY[82][0], StartY[82][1]
    elif iYear >= 2301:
        Fyear, FDev = StartY[81][0], StartY[81][1]
    elif iYear >= 2296:
        Fyear, FDev = StartY[80][0], StartY[80][1]
    elif iYear >= 2291:
        Fyear, FDev = StartY[79][0], StartY[79][1]
    elif iYear >= 2286:
        Fyear, FDev = StartY[78][0], StartY[78][1]
    elif iYear >= 2281:
        Fyear, FDev = StartY[77][0], StartY[77][1]
    elif iYear >= 2276:
        Fyear, FDev = StartY[76][0], StartY[76][1]
    elif iYear >= 2271:
        Fyear, FDev = StartY[75][0], StartY[75][1]
    elif iYear >= 2266:
        Fyear, FDev = StartY[74][0], StartY[74][1]
    elif iYear >= 2261:
        Fyear, FDev = StartY[73][0], StartY[73][1]
    elif iYear >= 2256:
        Fyear, FDev = StartY[72][0], StartY[72][1]
    elif iYear >= 2251:
        Fyear, FDev = StartY[71][0], StartY[71][1]
    elif iYear >= 2246:
        Fyear, FDev = StartY[70][0], StartY[70][1]
    elif iYear >= 2241:
        Fyear, FDev = StartY[69][0], StartY[69][1]
    elif iYear >= 2236:
        Fyear, FDev = StartY[68][0], StartY[68][1]
    elif iYear >= 2231:
        Fyear, FDev = StartY[67][0], StartY[67][1]
    elif iYear >= 2226:
        Fyear, FDev = StartY[66][0], StartY[66][1]
    elif iYear >= 2221:
        Fyear, FDev = StartY[65][0], StartY[65][1]
    elif iYear >= 2216:
        Fyear, FDev = StartY[64][0], StartY[64][1]
    elif iYear >= 2211:
        Fyear, FDev = StartY[63][0], StartY[63][1]
    elif iYear >= 2206:
        Fyear, FDev = StartY[62][0], StartY[62][1]
    elif iYear >= 2201:
        Fyear, FDev = StartY[61][0], StartY[61][1]
    elif iYear >= 2196:
        Fyear, FDev = StartY[60][0], StartY[60][1]
    elif iYear >= 2191:
        Fyear, FDev = StartY[59][0], StartY[59][1]
    elif iYear >= 2186:
        Fyear, FDev = StartY[58][0], StartY[58][1]
    elif iYear >= 2181:
        Fyear, FDev = StartY[57][0], StartY[57][1]
    elif iYear >= 2176:
        Fyear, FDev = StartY[56][0], StartY[56][1]
    elif iYear >= 2171:
        Fyear, FDev = StartY[55][0], StartY[55][1]
    elif iYear >= 2166:
        Fyear, FDev = StartY[54][0], StartY[54][1]
    elif iYear >= 2161:
        Fyear, FDev = StartY[53][0], StartY[53][1]
    elif iYear >= 2156:
        Fyear, FDev = StartY[52][0], StartY[52][1]
    elif iYear >= 2151:
        Fyear, FDev = StartY[51][0], StartY[51][1]
    elif iYear >= 2146:
        Fyear, FDev = StartY[50][0], StartY[50][1]
    elif iYear >= 2141:
        Fyear, FDev = StartY[49][0], StartY[49][1]
    elif iYear >= 2136:
        Fyear, FDev = StartY[48][0], StartY[48][1]
    elif iYear >= 2131:
        Fyear, FDev = StartY[47][0], StartY[47][1]
    elif iYear >= 2126:
        Fyear, FDev = StartY[46][0], StartY[46][1]
    elif iYear >= 2121:
        Fyear, FDev = StartY[45][0], StartY[45][1]
    elif iYear >= 2116:
        Fyear, FDev = StartY[44][0], StartY[44][1]
    elif iYear >= 2111:
        Fyear, FDev = StartY[43][0], StartY[43][1]
    elif iYear >= 2106:
        Fyear, FDev = StartY[42][0], StartY[42][1]
    elif iYear >= 2101:
        Fyear, FDev = StartY[41][0], StartY[41][1]
    elif iYear >= 2096:
        Fyear, FDev = StartY[40][0], StartY[40][1]
    elif iYear >= 2091:
        Fyear, FDev = StartY[39][0], StartY[39][1]
    elif iYear >= 2086:
        Fyear, FDev = StartY[38][0], StartY[38][1]
    elif iYear >= 2081:
        Fyear, FDev = StartY[37][0], StartY[37][1]
    elif iYear >= 2076:
        Fyear, FDev = StartY[36][0], StartY[36][1]
    elif iYear >= 2071:
        Fyear, FDev = StartY[35][0], StartY[35][1]
    elif iYear >= 2066:
        Fyear, FDev = StartY[34][0], StartY[34][1]
    elif iYear >= 2061:
        Fyear, FDev = StartY[33][0], StartY[33][1]
    elif iYear >= 2056:
        Fyear, FDev = StartY[32][0], StartY[32][1]
    elif iYear >= 2051:
        Fyear, FDev = StartY[31][0], StartY[31][1]
    elif iYear >= 2046:
        Fyear, FDev = StartY[30][0], StartY[30][1]
    elif iYear >= 2041:
        Fyear, FDev = StartY[29][0], StartY[29][1]
    elif iYear >= 2036:
        Fyear, FDev = StartY[28][0], StartY[28][1]
    elif iYear >= 2031:
        Fyear, FDev = StartY[27][0], StartY[27][1]
    elif iYear >= 2026:
        Fyear, FDev = StartY[26][0], StartY[26][1]
    elif iYear >= 2021:
        Fyear, FDev = StartY[25][0], StartY[25][1]
    elif iYear >= 2016:
        Fyear, FDev = StartY[24][0], StartY[24][1]
    elif iYear >= 2011:
        Fyear, FDev = StartY[23][0], StartY[23][1]
    elif iYear >= 2006:
        Fyear, FDev = StartY[22][0], StartY[22][1]
    elif iYear >= 2001:
        Fyear, FDev = StartY[21][0], StartY[21][1]
    elif iYear >= 1996:
        Fyear, FDev = StartY[20][0], StartY[20][1]
    elif iYear >= 1991:
        Fyear, FDev = StartY[19][0], StartY[19][1]
    elif iYear >= 1986:
        Fyear, FDev = StartY[18][0], StartY[18][1]
    elif iYear >= 1981:
        Fyear, FDev = StartY[17][0], StartY[17][1]
    elif iYear >= 1976:
        Fyear, FDev = StartY[16][0], StartY[16][1]
    elif iYear >= 1971:
        Fyear, FDev = StartY[15][0], StartY[15][1]
    elif iYear >= 1966:
        Fyear, FDev = StartY[14][0], StartY[14][1]
    elif iYear >= 1961:
        Fyear, FDev = StartY[13][0], StartY[13][1]
    elif iYear >= 1956:
        Fyear, FDev = StartY[12][0], StartY[12][1]
    elif iYear >= 1951:
        Fyear, FDev = StartY[11][0], StartY[11][1]
    elif iYear >= 1946:
        Fyear, FDev = StartY[10][0], StartY[10][1]
    elif iYear >= 1941:
        Fyear, FDev = StartY[9][0], StartY[9][1]
    elif iYear >= 1936:
        Fyear, FDev = StartY[8][0], StartY[8][1]
    elif iYear >= 1931:
        Fyear, FDev = StartY[7][0], StartY[7][1]
    elif iYear >= 1926:
        Fyear, FDev = StartY[6][0], StartY[6][1]
    elif iYear >= 1921:
        Fyear, FDev = StartY[5][0], StartY[5][1]
    elif iYear >= 1916:
        Fyear, FDev = StartY[4][0], StartY[4][1]
    elif iYear >= 1911:
        Fyear, FDev = StartY[3][0], StartY[3][1]
    elif iYear >= 1906:
        Fyear, FDev = StartY[2][0], StartY[2][1]
    elif iYear >= 1901:
        Fyear, FDev = StartY[1][0], StartY[1][1]
    else:
        Fyear, FDev = StartY[0][0], StartY[0][1]

    return Fyear, FDev


def AthikaMas(iYear: int) -> bool:
    Athi = XLMod((iYear - 78) - 0.45222, 2.7118886)
    return Athi < 1


def AthikaVar(iYear: int) -> bool:
    if AthikaMas(iYear):
        return False
    if AthikaMas(iYear + 1):
        CutOff = 1.69501433191599E-02
    else:
        CutOff = -1.42223099315486E-02
    return Deviation(iYear) > CutOff


def Deviation(iYear: int) -> float:
    FDev = None
    Fyear = None
    CurrDev = 0
    lastDev = None
    Fyear, FDev = calculate_Fyear_FDev(iYear)
    if iYear == Fyear:
        CurrDev = FDev
    else:
        Fyear = Fyear + 1
        for i in range(Fyear, iYear + 1):
            if i == Fyear:
                lastDev = FDev
            else:
                lastDev = CurrDev
            if AthikaMas(i - 1):
                CurrDev = -0.102356
            elif AthikaVar(i - 1):
                CurrDev = -0.632944
            else:
                CurrDev = 0.367056
            CurrDev = lastDev + CurrDev
    return CurrDev


def LDayInYear(iYear: int) -> int:
    if AthikaMas(iYear):
        return 384
    elif AthikaVar(iYear):
        return 355
    else:
        return 354


def AthikaSurathin(iYear: int) -> bool:
    # Check divisibility by 400 (divisible by 400 is always a leap year)
    if iYear % 400 == 0:
        return True

    # Check divisibility by 100 (divisible by 100 but not 400 is not a leap
    # year)
    elif iYear % 100 == 0:
        return False

    # Check divisibility by 4 (divisible by 4 but not by 100 is a leap year)
    elif iYear % 4 == 0:
        return True

    # All other cases are not leap years
    else:
        return False


def NODIYear(iYear: int) -> int:
    if AthikaSurathin(iYear):
        return 366
    else:
        return 365


def th_zodiac(i_year: int, o_type: int = 1) -> Union[str, int]:
    """
    Thai Zodiac Year Name
    Converts a Gregorian year to its corresponding Thai Zodiac name.

    :param int i_year: The Gregorian year. AD (Anno Domini)
    :param int o_type: Output Type (1 = Thai, 2 = English, 3 = Number).

    :return: The Thai Zodiac name or number corresponding to the input year.
    :rtype: Union[str, int]
    """

    # Zodiac names in Thai, English, and Numeric representations
    zodiac = {1: ["ชวด",
                  "ฉลู",
                  "ขาล",
                  "เถาะ",
                  "มะโรง",
                  "มะเส็ง",
                  "มะเมีย",
                  "มะแม",
                  "วอก",
                  "ระกา",
                  "จอ",
                  "กุน"],
              2: ["RAT",
                  "OX",
                  "TIGER",
                  "RABBIT",
                  "DRAGON",
                  "SNAKE",
                  "HORSE",
                  "GOAT",
                  "MONKEY",
                  "ROOSTER",
                  "DOG",
                  "PIG"],
              3: list(range(1,
                      13))}

    # Calculate zodiac index
    result = i_year % 12
    if result - 3 < 1:
        result = result - 3 + 12
    else:
        result = result - 3

    # Return the zodiac based on the output type
    return zodiac[o_type][result - 1]


def to_lunar_date(i_date: date) -> str:
    """
    Solar Date convert to Thai Lunar Date

    :param date i_date: date of the day.
    :return: Thai text lunar date
    :rtype: str
    """
    s_dates = [
        date(1902, 11, 30), date(1912, 12, 8), date(1922, 11, 19), date(1932, 11, 27),
        date(1942, 12, 7), date(1952, 11, 16), date(1962, 11, 26), date(1972, 12, 5),
        date(1982, 11, 15), date(1992, 11, 24), date(2002, 12, 4), date(2012, 11, 13),
        date(2022, 11, 23), date(2032, 12, 2), date(2042, 12, 12), date(2052, 11, 21),
        date(2062, 12, 1), date(2072, 12, 9), date(2082, 11, 20), date(2092, 11, 28),
        date(2102, 12, 9), date(2112, 11, 18), date(2122, 11, 28), date(2132, 12, 7),
        date(2142, 11, 17), date(2152, 11, 26), date(2162, 12, 6), date(2172, 11, 15),
        date(2182, 11, 25), date(2192, 12, 4), date(2202, 12, 15), date(2212, 11, 24),
        date(2222, 12, 4), date(2232, 12, 12), date(2242, 11, 23), date(2252, 12, 1),
        date(2262, 12, 11), date(2272, 11, 20), date(2282, 11, 30), date(2292, 12, 9),
        date(2302, 11, 20), date(2312, 11, 29), date(2322, 12, 9), date(2332, 11, 18),
        date(2342, 11, 28), date(2352, 12, 7), date(2362, 12, 17), date(2372, 11, 26),
        date(2382, 12, 6), date(2392, 12, 14), date(2402, 11, 25), date(2412, 12, 3),
        date(2422, 12, 13), date(2432, 11, 23), date(2442, 12, 2), date(2452, 12, 11)
    ]

    # Check if date is within supported range
    if i_date.year < 1903 or i_date.year > 2460:
        return "ไม่รองรับ"  # Unsupported date

    # Choose the nearest start date
    c_year = i_date.year - 1
    begin_date = None
    for year in reversed(s_dates):
        if c_year > year.year:
            begin_date = year
            break

    current_date = begin_date
    for year in range(begin_date.year + 1, i_date.year):
        day_in_year = LDayInYear(year)  # Custom function needed
        current_date += timedelta(days=day_in_year)

    r_day_prev = (date(current_date.year, 12, 31) - current_date).days
    day_of_year = (i_date - date(i_date.year, 1, 1)).days
    day_from_one = r_day_prev + day_of_year + 1
    nb_lday_year = LDayInYear(i_date.year)  # Custom function needed
    if nb_lday_year == 354:  # Normal year
        RDayLY = r_day_prev + NODIYear(i_date.year)
        DofY = day_from_one
        for j in range(1, 14 + 1):
            ThM = j
            if j == 1:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 2:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 3:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 4:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 5:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 6:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 7:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 8:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 9:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 10:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 11:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 12:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 13:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 14:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
        if ThM > 12:
            ThM = ThM - 12
            ThZ = 1
        else:
            ThZ = 0
        if DofY > 15:
            ThS = "แรม "
            DofY = DofY - 15
        else:
            ThS = "ขึ้น "
        THLDate = ThS + str(DofY) + " ค่ำ เดือน " + str(ThM)
    elif nb_lday_year == 355:  # Normal year
        RDayLY = r_day_prev + NODIYear(i_date.year)
        DofY = day_from_one
        for j in range(1, 14 + 1):
            ThM = j
            if j == 1:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 2:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 3:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 4:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 5:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 6:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 7:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 8:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 9:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 10:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 11:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 12:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 13:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 14:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
        if ThM > 12:
            ThM = ThM - 12
            ThZ = 1
        else:
            ThZ = 0
        if DofY > 15:
            ThS = "แรม "
            DofY = DofY - 15
        else:
            ThS = "ขึ้น "
        THLDate = ThS + str(DofY) + " ค่ำ เดือน " + str(ThM)
    elif nb_lday_year == 384:  # Normal year
        RDayLY = r_day_prev + NODIYear(i_date.year)
        DofY = day_from_one
        for j in range(1, 15 + 1):
            ThM = j
            if j == 1:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 2:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 3:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 4:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 5:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 6:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 7:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 8:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 9:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 10:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 11:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 12:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 13:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
            elif j == 14:
                if DofY <= 29 and DofY > 0:
                    break
                else:
                    DofY -= 29
            elif j == 15:
                if DofY <= 30 and DofY > 0:
                    break
                else:
                    DofY -= 30
        if ThM > 13:
            ThM = ThM - 13
            ThZ = 1
        else:
            ThZ = 0
        if ThM == 9:
            ThM = 8
        elif ThM == 10:
            ThM = 9
        elif ThM == 11:
            ThM = 10
        elif ThM == 12:
            ThM = 11
        elif ThM == 13:
            ThM = 12
        if DofY > 15:
            ThS = "แรม "
            DofY = DofY - 15
        else:
            ThS = "ขึ้น "
        THLDate = ThS + str(DofY) + " ค่ำ เดือน " + str(ThM)
    return THLDate
