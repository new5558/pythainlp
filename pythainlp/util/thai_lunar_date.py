# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0
"""
This file is port from
> https://gist.github.com/touchiep/99f4f5bb349d6b983ef78697630ab78e
"""
from datetime import date, timedelta
from typing import Tuple, Union


start_y = [[0 for _ in range(2)] for _ in range(113)]
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
    start_y[i][0] = year

value_years = [
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
for i, value in enumerate(value_years):
    start_y[i][1] = value


def calculate_f_year_f_dev(i_year: int) -> Tuple[int, float]:
    if i_year >= 2456:
        f_year, f_dev = start_y[112]
    elif i_year >= 2451:
        f_year, f_dev = start_y[111]
    elif i_year >= 2446:
        f_year, f_dev = start_y[110]
    elif i_year >= 2441:
        f_year, f_dev = start_y[109]
    elif i_year >= 2436:
        f_year, f_dev = start_y[108]
    elif i_year >= 2431:
        f_year, f_dev = start_y[107][0], start_y[107][1]
    elif i_year >= 2426:
        f_year, f_dev = start_y[106][0], start_y[106][1]
    elif i_year >= 2421:
        f_year, f_dev = start_y[105][0], start_y[105][1]
    elif i_year >= 2416:
        f_year, f_dev = start_y[104][0], start_y[104][1]
    elif i_year >= 2411:
        f_year, f_dev = start_y[103][0], start_y[103][1]
    elif i_year >= 2406:
        f_year, f_dev = start_y[102][0], start_y[102][1]
    elif i_year >= 2401:
        f_year, f_dev = start_y[101][0], start_y[101][1]
    elif i_year >= 2396:
        f_year, f_dev = start_y[100][0], start_y[100][1]
    elif i_year >= 2391:
        f_year, f_dev = start_y[99][0], start_y[99][1]
    elif i_year >= 2386:
        f_year, f_dev = start_y[98][0], start_y[98][1]
    elif i_year >= 2381:
        f_year, f_dev = start_y[97][0], start_y[97][1]
    elif i_year >= 2376:
        f_year, f_dev = start_y[96][0], start_y[96][1]
    elif i_year >= 2371:
        f_year, f_dev = start_y[95][0], start_y[95][1]
    elif i_year >= 2366:
        f_year, f_dev = start_y[94][0], start_y[94][1]
    elif i_year >= 2361:
        f_year, f_dev = start_y[93][0], start_y[93][1]
    elif i_year >= 2356:
        f_year, f_dev = start_y[92][0], start_y[92][1]
    elif i_year >= 2351:
        f_year, f_dev = start_y[91][0], start_y[91][1]
    elif i_year >= 2346:
        f_year, f_dev = start_y[90][0], start_y[90][1]
    elif i_year >= 2341:
        f_year, f_dev = start_y[89][0], start_y[89][1]
    elif i_year >= 2336:
        f_year, f_dev = start_y[88][0], start_y[88][1]
    elif i_year >= 2331:
        f_year, f_dev = start_y[87][0], start_y[87][1]
    elif i_year >= 2326:
        f_year, f_dev = start_y[86][0], start_y[86][1]
    elif i_year >= 2321:
        f_year, f_dev = start_y[85][0], start_y[85][1]
    elif i_year >= 2316:
        f_year, f_dev = start_y[84][0], start_y[84][1]
    elif i_year >= 2311:
        f_year, f_dev = start_y[83][0], start_y[83][1]
    elif i_year >= 2306:
        f_year, f_dev = start_y[82][0], start_y[82][1]
    elif i_year >= 2301:
        f_year, f_dev = start_y[81][0], start_y[81][1]
    elif i_year >= 2296:
        f_year, f_dev = start_y[80][0], start_y[80][1]
    elif i_year >= 2291:
        f_year, f_dev = start_y[79][0], start_y[79][1]
    elif i_year >= 2286:
        f_year, f_dev = start_y[78][0], start_y[78][1]
    elif i_year >= 2281:
        f_year, f_dev = start_y[77][0], start_y[77][1]
    elif i_year >= 2276:
        f_year, f_dev = start_y[76][0], start_y[76][1]
    elif i_year >= 2271:
        f_year, f_dev = start_y[75][0], start_y[75][1]
    elif i_year >= 2266:
        f_year, f_dev = start_y[74][0], start_y[74][1]
    elif i_year >= 2261:
        f_year, f_dev = start_y[73][0], start_y[73][1]
    elif i_year >= 2256:
        f_year, f_dev = start_y[72][0], start_y[72][1]
    elif i_year >= 2251:
        f_year, f_dev = start_y[71][0], start_y[71][1]
    elif i_year >= 2246:
        f_year, f_dev = start_y[70][0], start_y[70][1]
    elif i_year >= 2241:
        f_year, f_dev = start_y[69][0], start_y[69][1]
    elif i_year >= 2236:
        f_year, f_dev = start_y[68][0], start_y[68][1]
    elif i_year >= 2231:
        f_year, f_dev = start_y[67][0], start_y[67][1]
    elif i_year >= 2226:
        f_year, f_dev = start_y[66][0], start_y[66][1]
    elif i_year >= 2221:
        f_year, f_dev = start_y[65][0], start_y[65][1]
    elif i_year >= 2216:
        f_year, f_dev = start_y[64][0], start_y[64][1]
    elif i_year >= 2211:
        f_year, f_dev = start_y[63][0], start_y[63][1]
    elif i_year >= 2206:
        f_year, f_dev = start_y[62][0], start_y[62][1]
    elif i_year >= 2201:
        f_year, f_dev = start_y[61][0], start_y[61][1]
    elif i_year >= 2196:
        f_year, f_dev = start_y[60][0], start_y[60][1]
    elif i_year >= 2191:
        f_year, f_dev = start_y[59][0], start_y[59][1]
    elif i_year >= 2186:
        f_year, f_dev = start_y[58][0], start_y[58][1]
    elif i_year >= 2181:
        f_year, f_dev = start_y[57][0], start_y[57][1]
    elif i_year >= 2176:
        f_year, f_dev = start_y[56][0], start_y[56][1]
    elif i_year >= 2171:
        f_year, f_dev = start_y[55][0], start_y[55][1]
    elif i_year >= 2166:
        f_year, f_dev = start_y[54][0], start_y[54][1]
    elif i_year >= 2161:
        f_year, f_dev = start_y[53][0], start_y[53][1]
    elif i_year >= 2156:
        f_year, f_dev = start_y[52][0], start_y[52][1]
    elif i_year >= 2151:
        f_year, f_dev = start_y[51][0], start_y[51][1]
    elif i_year >= 2146:
        f_year, f_dev = start_y[50][0], start_y[50][1]
    elif i_year >= 2141:
        f_year, f_dev = start_y[49][0], start_y[49][1]
    elif i_year >= 2136:
        f_year, f_dev = start_y[48][0], start_y[48][1]
    elif i_year >= 2131:
        f_year, f_dev = start_y[47][0], start_y[47][1]
    elif i_year >= 2126:
        f_year, f_dev = start_y[46][0], start_y[46][1]
    elif i_year >= 2121:
        f_year, f_dev = start_y[45][0], start_y[45][1]
    elif i_year >= 2116:
        f_year, f_dev = start_y[44][0], start_y[44][1]
    elif i_year >= 2111:
        f_year, f_dev = start_y[43][0], start_y[43][1]
    elif i_year >= 2106:
        f_year, f_dev = start_y[42][0], start_y[42][1]
    elif i_year >= 2101:
        f_year, f_dev = start_y[41][0], start_y[41][1]
    elif i_year >= 2096:
        f_year, f_dev = start_y[40][0], start_y[40][1]
    elif i_year >= 2091:
        f_year, f_dev = start_y[39][0], start_y[39][1]
    elif i_year >= 2086:
        f_year, f_dev = start_y[38][0], start_y[38][1]
    elif i_year >= 2081:
        f_year, f_dev = start_y[37][0], start_y[37][1]
    elif i_year >= 2076:
        f_year, f_dev = start_y[36][0], start_y[36][1]
    elif i_year >= 2071:
        f_year, f_dev = start_y[35][0], start_y[35][1]
    elif i_year >= 2066:
        f_year, f_dev = start_y[34][0], start_y[34][1]
    elif i_year >= 2061:
        f_year, f_dev = start_y[33][0], start_y[33][1]
    elif i_year >= 2056:
        f_year, f_dev = start_y[32][0], start_y[32][1]
    elif i_year >= 2051:
        f_year, f_dev = start_y[31][0], start_y[31][1]
    elif i_year >= 2046:
        f_year, f_dev = start_y[30][0], start_y[30][1]
    elif i_year >= 2041:
        f_year, f_dev = start_y[29][0], start_y[29][1]
    elif i_year >= 2036:
        f_year, f_dev = start_y[28][0], start_y[28][1]
    elif i_year >= 2031:
        f_year, f_dev = start_y[27][0], start_y[27][1]
    elif i_year >= 2026:
        f_year, f_dev = start_y[26][0], start_y[26][1]
    elif i_year >= 2021:
        f_year, f_dev = start_y[25][0], start_y[25][1]
    elif i_year >= 2016:
        f_year, f_dev = start_y[24][0], start_y[24][1]
    elif i_year >= 2011:
        f_year, f_dev = start_y[23][0], start_y[23][1]
    elif i_year >= 2006:
        f_year, f_dev = start_y[22][0], start_y[22][1]
    elif i_year >= 2001:
        f_year, f_dev = start_y[21][0], start_y[21][1]
    elif i_year >= 1996:
        f_year, f_dev = start_y[20][0], start_y[20][1]
    elif i_year >= 1991:
        f_year, f_dev = start_y[19][0], start_y[19][1]
    elif i_year >= 1986:
        f_year, f_dev = start_y[18][0], start_y[18][1]
    elif i_year >= 1981:
        f_year, f_dev = start_y[17][0], start_y[17][1]
    elif i_year >= 1976:
        f_year, f_dev = start_y[16][0], start_y[16][1]
    elif i_year >= 1971:
        f_year, f_dev = start_y[15][0], start_y[15][1]
    elif i_year >= 1966:
        f_year, f_dev = start_y[14][0], start_y[14][1]
    elif i_year >= 1961:
        f_year, f_dev = start_y[13][0], start_y[13][1]
    elif i_year >= 1956:
        f_year, f_dev = start_y[12][0], start_y[12][1]
    elif i_year >= 1951:
        f_year, f_dev = start_y[11][0], start_y[11][1]
    elif i_year >= 1946:
        f_year, f_dev = start_y[10][0], start_y[10][1]
    elif i_year >= 1941:
        f_year, f_dev = start_y[9][0], start_y[9][1]
    elif i_year >= 1936:
        f_year, f_dev = start_y[8][0], start_y[8][1]
    elif i_year >= 1931:
        f_year, f_dev = start_y[7][0], start_y[7][1]
    elif i_year >= 1926:
        f_year, f_dev = start_y[6][0], start_y[6][1]
    elif i_year >= 1921:
        f_year, f_dev = start_y[5][0], start_y[5][1]
    elif i_year >= 1916:
        f_year, f_dev = start_y[4][0], start_y[4][1]
    elif i_year >= 1911:
        f_year, f_dev = start_y[3][0], start_y[3][1]
    elif i_year >= 1906:
        f_year, f_dev = start_y[2][0], start_y[2][1]
    elif i_year >= 1901:
        f_year, f_dev = start_y[1][0], start_y[1][1]
    else:
        f_year, f_dev = start_y[0][0], start_y[0][1]

    return f_year, f_dev


def AthikaMas(i_year: int) -> bool:
    Athi = ((i_year - 78) - 0.45222) % 2.7118886
    return Athi < 1


def AthikaVar(i_year: int) -> bool:
    if AthikaMas(i_year):
        return False
    if AthikaMas(i_year + 1):
        CutOff = 1.69501433191599E-02
    else:
        CutOff = -1.42223099315486E-02
    return deviation(i_year) > CutOff


def deviation(i_year: int) -> float:
    f_dev = None
    f_year = None
    curr_dev = 0
    last_dev = None
    f_year, f_dev = calculate_f_year_f_dev(i_year)
    if i_year == f_year:
        curr_dev = f_dev
    else:
        f_year = f_year + 1
        for i in range(f_year, i_year + 1):
            if i == f_year:
                last_dev = f_dev
            else:
                last_dev = curr_dev
            if AthikaMas(i - 1):
                curr_dev = -0.102356
            elif AthikaVar(i - 1):
                curr_dev = -0.632944
            else:
                curr_dev = 0.367056
            curr_dev = last_dev + curr_dev
    return curr_dev


def last_day_in_year(i_year: int) -> int:
    if AthikaMas(i_year):
        return 384
    elif AthikaVar(i_year):
        return 355
    else:
        return 354


def athikasurathin(i_year: int) -> bool:
    """
    AthikaSurathin
    """
    # Check divisibility by 400 (divisible by 400 is always a leap year)
    if i_year % 400 == 0:
        return True

    # Check divisibility by 100 (divisible by 100 but not 400 is not a leap
    # year)
    elif i_year % 100 == 0:
        return False

    # Check divisibility by 4 (divisible by 4 but not by 100 is a leap year)
    elif i_year % 4 == 0:
        return True

    # All other cases are not leap years
    else:
        return False


def number_day_in_year(i_year: int) -> int:
    if athikasurathin(i_year):
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
    Convert the solar date to Thai Lunar Date

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
        raise NotImplementedError("Unsupported date")  # Unsupported date

    # Choose the nearest start date
    c_year = i_date.year - 1
    begin_date = None
    for year in reversed(s_dates):
        if c_year > year.year:
            begin_date = year
            break

    current_date = begin_date
    for year in range(begin_date.year + 1, i_date.year):
        day_in_year = last_day_in_year(year)  # Custom function needed
        current_date += timedelta(days=day_in_year)

    r_day_prev = (date(current_date.year, 12, 31) - current_date).days
    day_of_year = (i_date - date(i_date.year, 1, 1)).days
    day_from_one = r_day_prev + day_of_year + 1
    nb_lday_year = last_day_in_year(i_date.year)  # Custom function needed
    if nb_lday_year == 354:  # Normal year
        days_of_year = day_from_one
        for j in range(1, 14 + 1):
            th_m = j
            if j == 1:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 2:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 3:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 4:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 5:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 6:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 7:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 8:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 9:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 10:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 11:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 12:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 13:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 14:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
        if th_m > 12:
            th_m = th_m - 12
            th_z = 1
        else:
            th_z = 0
        if days_of_year > 15:
            th_s = "แรม "
            days_of_year = days_of_year - 15
        else:
            th_s = "ขึ้น "
        thai_lunar_date = th_s + str(days_of_year) + " ค่ำ เดือน " + str(th_m)
    elif nb_lday_year == 355:  # Normal year
        days_of_year = day_from_one
        for j in range(1, 14 + 1):
            th_m = j
            if j == 1:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 2:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 3:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 4:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 5:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 6:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 7:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 8:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 9:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 10:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 11:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 12:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 13:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 14:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
        if th_m > 12:
            th_m = th_m - 12
            th_z = 1
        else:
            th_z = 0
        if days_of_year > 15:
            th_s = "แรม "
            days_of_year = days_of_year - 15
        else:
            th_s = "ขึ้น "
        thai_lunar_date = th_s + str(days_of_year) + " ค่ำ เดือน " + str(th_m)
    elif nb_lday_year == 384:  # Normal year
        days_of_year = day_from_one
        for j in range(1, 15 + 1):
            th_m = j
            if j == 1:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 2:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 3:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 4:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 5:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 6:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 7:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 8:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 9:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 10:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 11:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 12:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 13:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
            elif j == 14:
                if days_of_year <= 29 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 29
            elif j == 15:
                if days_of_year <= 30 and days_of_year > 0:
                    break
                else:
                    days_of_year -= 30
        if th_m > 13:
            th_m = th_m - 13
            th_z = 1
        else:
            th_z = 0
        if th_m == 9:
            th_m = 8
        elif th_m == 10:
            th_m = 9
        elif th_m == 11:
            th_m = 10
        elif th_m == 12:
            th_m = 11
        elif th_m == 13:
            th_m = 12
        if days_of_year > 15:
            th_s = "แรม "
            days_of_year = days_of_year - 15
        else:
            th_s = "ขึ้น "
        thai_lunar_date = th_s + str(days_of_year) + " ค่ำ เดือน " + str(th_m)
    return thai_lunar_date
