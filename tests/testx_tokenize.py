# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0

import unittest

from pythainlp.tokenize import (
    DEFAULT_WORD_DICT_TRIE,
    attacut,
    deepcut,
    nercut,
    oskut,
    paragraph_tokenize,
    pyicu,
    sefr_cut,
    sent_tokenize,
    ssg,
    subword_tokenize,
    tltk,
    word_tokenize,
)
from pythainlp.tokenize import clause_tokenize as sent_clause_tokenize

from .test_tokenize import (
    SENT_1,
    SENT_1_TOKS,
    SENT_2,
    SENT_2_TOKS,
    SENT_3,
    SENT_3_TOKS,
    SENT_4,
    TEXT_1,
)


# Tests for functions that need external imports
class TokenizeTestCaseX(unittest.TestCase):
    def testx_subword_tokenize(self):
        self.assertEqual(subword_tokenize(None, engine="ssg"), [])
        self.assertEqual(subword_tokenize(None, engine="han_solo"), [])
        self.assertEqual(
            subword_tokenize("แมวกินปลา", engine="ssg"), ["แมว", "กิน", "ปลา"]
        )
        self.assertTrue(
            "ดาว" in subword_tokenize("สวัสดีดาวอังคาร", engine="ssg")
        )
        self.assertFalse("า" in subword_tokenize("สวัสดีดาวอังคาร", engine="ssg"))
        self.assertEqual(
            subword_tokenize("แมวกินปลา", engine="han_solo"),
            ["แมว", "กิน", "ปลา"],
        )
        self.assertTrue(
            "ดาว" in subword_tokenize("สวัสดีดาวอังคาร", engine="han_solo")
        )
        self.assertFalse(
            "า" in subword_tokenize("สวัสดีดาวอังคาร", engine="han_solo")
        )
        self.assertEqual(subword_tokenize(None, engine="tltk"), [])
        self.assertEqual(subword_tokenize("", engine="tltk"), [])
        self.assertIsInstance(
            subword_tokenize("สวัสดิีดาวอังคาร", engine="tltk"), list
        )
        self.assertFalse(
            "า" in subword_tokenize("สวัสดีดาวอังคาร", engine="tltk")
        )
        self.assertIsInstance(subword_tokenize("โควิด19", engine="tltk"), list)

        self.assertEqual(subword_tokenize(None, engine="phayathai"), [])
        self.assertEqual(subword_tokenize("", engine="phayathai"), [])
        self.assertIsInstance(
            subword_tokenize("สวัสดิีดาวอังคาร", engine="phayathai"), list
        )
        self.assertFalse(
            "า" in subword_tokenize("สวัสดีดาวอังคาร", engine="phayathai")
        )
        self.assertIsInstance(
            subword_tokenize("โควิด19", engine="phayathai"), list
        )
        self.assertEqual(subword_tokenize(None, engine="wangchanberta"), [])
        self.assertEqual(subword_tokenize("", engine="wangchanberta"), [])
        self.assertIsInstance(
            subword_tokenize("สวัสดิีดาวอังคาร", engine="wangchanberta"), list
        )
        self.assertFalse(
            "า" in subword_tokenize("สวัสดีดาวอังคาร", engine="wangchanberta")
        )
        self.assertIsInstance(
            subword_tokenize("โควิด19", engine="wangchanberta"), list
        )

    def testx_sent_tokenize(self):
        # Use default engine (crfcut)
        self.assertEqual(sent_tokenize(None), [])
        self.assertEqual(sent_tokenize(""), [])

        self.assertEqual(
            sent_tokenize(SENT_1, engine="crfcut"),
            SENT_1_TOKS,
        )
        self.assertEqual(
            sent_tokenize(SENT_2, engine="crfcut"),
            SENT_2_TOKS,
        )
        self.assertEqual(
            sent_tokenize(SENT_3, engine="crfcut"),
            SENT_3_TOKS,
        )
        self.assertEqual(
            sent_tokenize(SENT_1),
            SENT_1_TOKS,
        )
        self.assertEqual(
            sent_tokenize(SENT_2),
            SENT_2_TOKS,
        )
        self.assertEqual(
            sent_tokenize(SENT_3),
            SENT_3_TOKS,
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_1,
                engine="tltk",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_2,
                engine="tltk",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_3,
                engine="tltk",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_1,
                engine="thaisum",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_2,
                engine="thaisum",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_3,
                engine="thaisum",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_3,
                engine="wtp",
            ),
        )
        self.assertIsNotNone(
            sent_tokenize(
                SENT_3,
                engine="wtp-tiny",
            ),
        )
        # self.assertIsNotNone(
        #     sent_tokenize(
        #         SENT_3,
        #         engine="wtp-base",
        #     ),
        # )
        # self.assertIsNotNone(
        #     sent_tokenize(
        #         SENT_3,
        #         engine="wtp-large",
        #     ),
        # )
        self.assertEqual(
            sent_tokenize(SENT_4, engine="crfcut"),
            [["ผม", "กิน", "ข้าว", " ", "\n", "เธอ", "เล่น", "เกม"]],
        )
        self.assertEqual(
            sent_tokenize(SENT_4, engine="thaisum"),
            [["ผม", "กิน", "ข้าว", " ", "เธอ", "เล่น", "เกม"]],
        )

    def testx_word_tokenize(self):
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="nlpo3"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="attacut"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="deepcut"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="icu"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="nercut"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="sefr_cut"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="tltk"))
        self.assertIsNotNone(word_tokenize(TEXT_1, engine="oskut"))

    def test_numeric_data_format(self):
        engines = ["attacut", "deepcut", "newmm", "sefr_cut"]

        for engine in engines:
            self.assertIn(
                "127.0.0.1",
                word_tokenize("ไอพีของคุณคือ 127.0.0.1 ครับ", engine=engine),
            )

            tokens = word_tokenize(
                "เวลา 12:12pm มีโปรโมชั่น 11.11", engine=engine
            )
            self.assertTrue(
                any(value in tokens for value in ["12:12pm", "12:12"]),
                msg=f"{engine}: {tokens}",
            )
            self.assertIn("11.11", tokens)

            self.assertIn(
                "1,234,567.89",
                word_tokenize("รางวัลมูลค่า 1,234,567.89 บาท", engine=engine),
            )

            tokens = word_tokenize("อัตราส่วน 2.5:1 คือ 5:2", engine=engine)
            self.assertIn("2.5:1", tokens)
            self.assertIn("5:2", tokens)

        # try turning off `join_broken_num`
        engine = "attacut"
        self.assertNotIn(
            "127.0.0.1",
            word_tokenize(
                "ไอพีของคุณคือ 127.0.0.1 ครับ",
                engine=engine,
                join_broken_num=False,
            ),
        )
        self.assertNotIn(
            "1,234,567.89",
            word_tokenize(
                "รางวัลมูลค่า 1,234,567.89 บาท",
                engine=engine,
                join_broken_num=False,
            ),
        )

    def test_attacut(self):
        self.assertEqual(attacut.segment(None), [])
        self.assertEqual(attacut.segment(""), [])
        self.assertEqual(
            word_tokenize("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", engine="attacut"),
            ["ฉัน", "รัก", "ภาษา", "ไทย", "เพราะ", "ฉัน", "เป็น", "คน", "ไทย"],
        )
        self.assertEqual(
            attacut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", model="attacut-sc"),
            ["ฉัน", "รัก", "ภาษา", "ไทย", "เพราะ", "ฉัน", "เป็น", "คน", "ไทย"],
        )
        self.assertIsNotNone(
            attacut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", model="attacut-c")
        )

    def test_deepcut(self):
        self.assertEqual(deepcut.segment(None), [])
        self.assertEqual(deepcut.segment(""), [])
        self.assertIsNotNone(deepcut.segment("ทดสอบ", DEFAULT_WORD_DICT_TRIE))
        self.assertIsNotNone(deepcut.segment("ทดสอบ", ["ทด", "สอบ"]))
        self.assertIsNotNone(word_tokenize("ทดสอบ", engine="deepcut"))
        self.assertIsNotNone(
            word_tokenize(
                "ทดสอบ", engine="deepcut", custom_dict=DEFAULT_WORD_DICT_TRIE
            )
        )

    def test_icu(self):
        self.assertEqual(pyicu.segment(None), [])
        self.assertEqual(pyicu.segment(""), [])
        self.assertEqual(
            word_tokenize("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", engine="icu"),
            ["ฉัน", "รัก", "ภาษา", "ไทย", "เพราะ", "ฉัน", "เป็น", "คน", "ไทย"],
        )

    def test_oskut(self):
        self.assertEqual(oskut.segment(None), [])
        self.assertEqual(oskut.segment(""), [])
        self.assertIsNotNone(
            oskut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย"),
        )
        self.assertIsNotNone(
            oskut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", engine="scads"),
        )

    def test_nercut(self):
        self.assertEqual(nercut.segment(None), [])
        self.assertEqual(nercut.segment(""), [])
        self.assertIsNotNone(nercut.segment("ทดสอบ"))
        self.assertEqual(nercut.segment("ทันแน่ๆ"), ["ทัน", "แน่ๆ"])
        self.assertEqual(nercut.segment("%1ครั้ง"), ["%", "1", "ครั้ง"])
        self.assertEqual(nercut.segment("ทุ๊กกโคนน"), ["ทุ๊กกโคนน"])
        self.assertIsNotNone(nercut.segment("อย่าลืมอัพการ์ดนะจ๊ะ"))
        self.assertIsNotNone(word_tokenize("ทดสอบ", engine="nercut"))

    def test_sefr_cut(self):
        self.assertEqual(sefr_cut.segment(None), [])
        self.assertEqual(sefr_cut.segment(""), [])
        self.assertIsNotNone(
            sefr_cut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย"),
        )
        self.assertIsNotNone(
            sefr_cut.segment("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย", engine="tnhc"),
        )

    def test_ssg(self):
        self.assertEqual(ssg.segment(None), [])
        self.assertEqual(ssg.segment(""), [])
        self.assertTrue(
            "ดาว" in subword_tokenize("สวัสดีดาวอังคาร", engine="ssg")
        )

    def test_tltk(self):
        self.assertEqual(tltk.segment(None), [])
        self.assertEqual(tltk.segment(""), [])
        self.assertEqual(
            tltk.syllable_tokenize("ฉันรักภาษาไทยเพราะฉันเป็นคนไทย"),
            [
                "ฉัน",
                "รัก",
                "ภา",
                "ษา",
                "ไทย",
                "เพราะ",
                "ฉัน",
                "เป็น",
                "คน",
                "ไทย",
            ],
        )
        self.assertEqual(tltk.syllable_tokenize(None), [])
        self.assertEqual(tltk.syllable_tokenize(""), [])

    def test_paragraph_tokenize(self):
        sent = (
            "(1) บทความนี้ผู้เขียนสังเคราะห์ขึ้นมา"
            + "จากผลงานวิจัยที่เคยทำมาในอดีต"
            + " มิได้ทำการศึกษาค้นคว้าใหม่อย่างกว้างขวางแต่อย่างใด"
            + " จึงใคร่ขออภัยในความบกพร่องทั้งปวงมา ณ ที่นี้"
        )
        self.assertIsNotNone(paragraph_tokenize(sent))
        with self.assertRaises(ValueError):
            paragraph_tokenize(
                sent, engine="ai2+2thai"
            )  # engine does not exist

    def test_clause_tokenize(self):
        self.assertIsNotNone(sent_clause_tokenize(["ฉัน", "ทดสอบ"]))
        self.assertIsInstance(sent_clause_tokenize(["ฉัน", "ทดสอบ"]), list)
