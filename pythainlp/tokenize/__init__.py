# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
import nltk
import re
import codecs
from six.moves import zip
from pythainlp.corpus.thaisyllable import get_data
from pythainlp.corpus.thaiword import get_data as get_dict
from marisa_trie import Trie

DEFAULT_DICT_TRIE = Trie(get_dict())

def dict_word_tokenize(text, custom_dict_trie, engine='newmm'):
	'''
	:meth:`dict_word_tokenize` tokenizes word based on the dictionary you provide. The format has to be in trie data structure.

	:param str text: the text to be tokenized
	:param dict custom_dict_trie: คือ trie ที่สร้างจาก create_custom_dict_trie
	:param str engine: choose between different options of engine to token (newmm, wordcutpy, mm, longest-matching)

	:return: A list of words, tokenized from a text.
	'''
	if engine=="newmm":
		from .newmm import mmcut as segment
	elif engine=="mm":
		from .mm import segment
	elif engine=='longest-matching':
		from .longest import segment
	elif engine=='wordcutpy':
		from .wordcutpy import segment
		return segment(text, custom_dict_trie.keys())
	return segment(text, custom_dict_trie)

def word_tokenize(text, engine='newmm',whitespaces=False):
	"""
    :param str text:  the text to be tokenized
    :param str engine: the engine to tokenize text
    :param bool whitespaces: True to output no whitespace, a common mark of sentence or end of phrase in Thai.
    :Parameters for engine:
        * newmm - ใช้ Maximum Matching algorithm ในการตัดคำภาษาไทย โค้ดชุดใหม่ (ค่าเริ่มต้น)
        * icu -  engine ตัวดั้งเดิมของ PyThaiNLP (ความแม่นยำต่ำ)
        * dict - ใช้ dict ในการตัดคำไทย จะคืนค่า False หากไม่สามารถตัดคำไทย
        * longest-matching ใช้ Longest matching ในการตัดคำ
        * mm ใช้ Maximum Matching algorithm - โค้ดชุดเก่า
        * pylexto - ใช้ LexTo ในการตัดคำ
        * deepcut - ใช้ Deep Neural Network ในการตัดคำภาษาไทย
        * wordcutpy - ใช้ wordcutpy (https://github.com/veer66/wordcutpy) ในการตัดคำ
        * cutkum - ใช้ Deep Neural Network ในการตัดคำภาษาไทย (https://github.com/pucktada/cutkum)
    :return: A list of words, tokenized from a text
	"""

	if engine=='icu':
		from .pyicu import segment
	elif engine=='dicts':
		from .dictsegment import segment
	elif engine=='mm':
		from .mm import segment
	elif engine=='newmm':
		from .newmm import mmcut as segment
	elif engine=='longest-matching':
		from .longest import segment
	elif engine=='pylexto':
		from .pylexto import segment
	elif engine=='deepcut':
		from .deepcut import segment
	elif engine=='cutkum':
		from .cutkum import segment
	elif engine=='wordcutpy':
		from .wordcutpy import segment
	else:
		raise Exception("error no have engine.")
	if whitespaces==False:
		return [i.strip(' ') for i in segment(text) if i.strip(' ')!='']
	return segment(text)

def sent_tokenize(text,engine='whitespace+newline'):
	'''
	sent_tokenize(text,engine='whitespace+newline')
	ตัดประโยคเบื้องต้น โดยการแบ่งด้วยช่องว่าง
	'''
	if engine=='whitespace':
		data=nltk.tokenize.WhitespaceTokenizer().tokenize(text)
	elif engine=='whitespace+newline':
		data=re.sub(r'\n+|\s+','|',text,re.U).split('|')
	return data
def wordpunct_tokenize(text):
	'''
	wordpunct_tokenize(text)
	It is nltk.tokenize.wordpunct_tokenize(text).
	'''
	return nltk.tokenize.wordpunct_tokenize(text)
def WhitespaceTokenizer(text):
	return nltk.tokenize.WhitespaceTokenizer().tokenize(text)
def isthai(text,check_all=False):
	"""
	สำหรับเช็คว่าเป็นตัวอักษรภาษาไทยหรือไม่
	isthai(text,check_all=False)
	text คือ ข้อความหรือ list ตัวอักษร
	check_all สำหรับส่งคืนค่า True หรือ False เช็คทุกตัวอักษร

	การส่งคืนค่า
	{'thai':% อักษรภาษาไทย,'check_all':tuple โดยจะเป็น (ตัวอักษร,True หรือ False)}
	"""
	listext=list(text)
	i=0
	num_isthai=0
	if check_all==True:
		listthai=[]
	while i<len(listext):
		cVal = ord(listext[i])
		if(cVal >= 3584 and cVal <= 3711):
			num_isthai+=1
			if check_all==True:
				listthai.append(True)
		else:
			if check_all==True:
				listthai.append(False)
		i+=1
	thai=(num_isthai/len(listext))*100
	if check_all==True:
		dictthai=tuple(zip(listext,listthai))
		data= {'thai':thai,'check_all':dictthai}
	else:
		data= {'thai':thai}
	return data
def syllable_tokenize(text1):
	"""
	syllable_tokenize(text)
	เป็นคำสั่งสำหรับใช้ตัดพยางค์ในภาษาไทย
	รับ str
	ส่งออก list
	"""
	text1=word_tokenize(text1)
	data=[]
	trie = create_custom_dict_trie(custom_dict_source=get_data())
	if(len(text1)>0):
		i=0
		while(i<len(text1)):
			data.extend(dict_word_tokenize(text=text1[i], custom_dict_trie=trie))
			i+=1
	else:
		data=dict_word_tokenize(text=text1, custom_dict_trie=trie)
	return data

def create_custom_dict_trie(custom_dict_source):
	"""The function is used to create a custom dict trie which will be
	used for word_tokenize() function

	Arguments:
		custom_dict_source {string or list} -- a list of vocaburaries or a path to source file

	Raises:
		ValueError -- Invalid custom_dict_source's object type

	Returns:
		Trie -- A trie created from custom dict input
	"""

	if type(custom_dict_source) is str:
		# Receive a file path of the custom dict to read
		with codecs.open(custom_dict_source, 'r',encoding='utf8') as f:
			_vocabs = f.read().splitlines()
			return Trie(_vocabs)
	elif isinstance(custom_dict_source, (list, tuple, set)):
		# Received a sequence type object of vocabs
		return Trie(custom_dict_source)
	else:
		raise TypeError(
			'Type of custom_dict_source must be either str (path to source file) or collections'
		)

class Tokenizer:
	def __init__(self, custom_dict=None):
		"""
		Initialize tokenizer object

		Keyword arguments:
		custom_dict -- a file path or a list of vocaburaies to be used to create a trie (default - original lexitron)

		Object variables:
		trie_dict -- a trie to use in tokenizing engines
		"""
		if custom_dict:
			if type(custom_dict) is list:
				self.trie_dict = Trie(custom_dict)
			elif type(custom_dict) is str:
				with codecs.open(custom_dict, 'r',encoding='utf8') as f:
					vocabs = f.read().splitlines()
				self.trie_dict = Trie(vocabs)
		else:
			self.trie_dict = Trie(get_dict())

	def word_tokenize(self, text, engine='newmm'):
		from .newmm import mmcut as segment
		return segment(text, self.trie_dict)
