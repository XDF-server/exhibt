# *-* coding:utf-8 *-*

from mysql import Mysql
from gl import LOG
from exception import DBException,CKException
import json
import re

class Business(object):

	@staticmethod
	def get_group_list(okid):
	
		mysql = Mysql()

		mysql.connect_master()
		
		query_sql = "select B.id,B.name,A.question_group,count(A.id) from entity_question A  left outer join entity_group B on (A.question_group=B.id) where upload_id=12837 and question_group <> 0 group by question_group;" 
		
		try:
			if mysql.query(query_sql,group_name = group_name):

				res = mysql.fetchall()

				group_list = []

				for line in res:
					group_id = line[0]
					group_name = line[1]
					question_num = [2]
					group_dict = {'id':group_id,'name':group_name,'num':question_num}
					group_list.append(group_dict)
			
				return group_list
			else:
				return False

		except DBException as e:
			LOG.error('check topic error [%s]' % e)
			raise CKException('check topic error')


	@staticmethod
	def group_exist(group_name):
		
		mysql = Mysql()

		mysql.connect_master()
		
		query_sql = "select 1 from entity_group where name = '%(group_name)s';" 
		
		try:
			if mysql.query(query_sql,group_name = group_name):
				return True
			else:
				return False

		except DBException as e:
			LOG.error('check topic error [%s]' % e)
			raise CKException('check topic error')

	@staticmethod
	def is_topic(topic_id):
		
		mysql = Mysql()

		mysql.connect_master()
		
		query_sql = "select 1 from entity_topic where id = %(topic_id)d;" 
		
		try:
			if mysql.query(query_sql,topic_id = int(topic_id)):
				return True
			else:
				return False

		except DBException as e:
			LOG.error('check topic error [%s]' % e)
			raise CKException('check topic error')

	@staticmethod
	def is_seriess(seriess_id):
		
		mysql = Mysql()
		
		mysql.connect_master()

		query_sql = "select 1 from entity_seriess where id = %(seriess_id)d;"
		
		try:
			if mysql.query(query_sql,seriess_id = int(seriess_id)):
				return True
			else:
				return False

		except DBException as e:
			LOG.error('check seriess error [%s]' % e)
			raise CkException('check seriess error')

	@staticmethod 
	def is_level(level_id):
		
		level_dict = {"1" : "简单","2" : "中等","3" : "困难","4" : "极难"}	

		if str(level_id) in level_dict.keys():
			return True

		return False

	@staticmethod 
	def is_type(type_id):
		
		mysql = Mysql()
		
		mysql.connect_master()

		query_sql = "select name from entity_question_type where type_id = %(type_id)d and enable = 1;"
		
		try:
			if mysql.query(query_sql,type_id = int(type_id)):
				return mysql.fetch()[0][0]
			else:
				return False

		except DBException as e:
			LOG.error('check type error [%s]' % e)
			raise CkException('check type error')

		
	@staticmethod
	def q_type_filter_num(type):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "select count(*) from entity_question_new where type = '%(type)s';"	

		try:
			if mysql.query(query_sql,type = type):
				return mysql.fetchall()[0][0]

			else:
				return None

		except DBException as e:
			LOG.error('filtet type error [%s]' % e)
			raise CkException('filter type error')

	@staticmethod
	def q_type_filter(type,start,num):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "select oldid,subject from entity_question_new where type = '%(type)s' limit %(start)d,%(num)d;"	

		try:
			if mysql.query(query_sql,type = type,start = start,num = num):
				return mysql.fetchall()

			else:
				return None

		except DBException as e:
			LOG.error('filtet type error [%s]' % e)
			raise CkException('filter type error')

	@staticmethod
	def q_subject_filter_num(type):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "select count(*) from entity_question_new where subject = '%(type)s';"	

		try:
			if mysql.query(query_sql,type = type):
				return mysql.fetchall()[0][0]

			else:
				return None

		except DBException as e:
			LOG.error('filtet type error [%s]' % e)
			raise CkException('filter type error')

	@staticmethod
	def q_subject_filter(type,start,num):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "select oldid,subject from entity_question_new where subject = '%(type)s' limit %(start)d,%(num)d;"	

		try:
			if mysql.query(query_sql,type = type,start = start,num = num):
				return mysql.fetchall()

			else:
				return None

		except DBException as e:
			LOG.error('filtet type error [%s]' % e)
			raise CkException('filter type error')

	@staticmethod
	def q_mark_list():

		mysql = Mysql()
		
		mysql.connect_master()

		query_sql = "select id,name from link_question_mark;"	

		mark_list = []

		try:
			if mysql.query(query_sql):
				mark_tuple =  mysql.fetchall()
				
				for mark in mark_tuple:
					tmp_tuple = (mark[0],mark[1])
					mark_list.append(tmp_tuple)
					print mark_list
				return mark_list

			else:
				return None

		except DBException as e:
			LOG.error('get mark error [%s]' % e)
			raise CkException('get mark error')

	@staticmethod
	def q_mark(oldid,newid,mark):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "insert into entity_question_mark (oldid,newid,mark,mark_time) values (%(oldid)d,%(newid)d,%(mark)d,now());"	

		try:
			if mysql.query(query_sql,oldid = oldid,newid = newid,mark = mark):
				return 'success'

			else:
				return None

		except DBException as e:
			LOG.error('mark error [%s]' % e)
			raise CkException('mark error')

	@staticmethod
	def add_mark(name):

		mysql = Mysql()

		mysql.connect_master()

		query_sql = "insert into link_question_mark (name,mark_time) values ('%(name)s',now());"	

		try:
			if mysql.query(query_sql,name = name):
				return mysql.get_last_id()

			else:
				return None

		except DBException as e:
			LOG.error('add mark error [%s]' % e)
			raise CkException('add mark error')

	@staticmethod
	def q_type_list():

		mysql = Mysql()
		
		mysql.connect_master()

		query_sql = "select distinct type from entity_question_new where type is not null;"	

		type_list = []

		try:
			if mysql.query(query_sql):
				type_tuple =  mysql.fetchall()
				
				for type in type_tuple:
					tmp_tuple = (type[0])
					type_list.append(tmp_tuple)
					print type_list
				return type_list

			else:
				return None

		except DBException as e:
			LOG.error('get type error [%s]' % e)
			raise CkException('get type error')

	@staticmethod
	def q_subject_list():

		mysql = Mysql()
		
		mysql.connect_master()

		query_sql = "select distinct subject from entity_question_new where type is not null;"	

		subject_list = []

		try:
			if mysql.query(query_sql):
				subject_tuple =  mysql.fetchall()
				
				for type in subject_tuple:
					tmp_tuple = (type[0])
					subject_list.append(tmp_tuple)
					print subject_list
				return subject_list

			else:
				return None

		except DBException as e:
			LOG.error('get subject error [%s]' % e)
			raise CkException('get subject error')


	@staticmethod
	def q_json_parse(question_json):

		try:
			encode_json = json.loads(question_json)

		except (ValueError,KeyError,TypeError):

			return None

		body_list = []
		options_list = []
		answer_list = []
		analysis_list = []
		question_dict = {}

		if 'body' in encode_json.keys():
			question_body = encode_json['body']
			
			body_list = Business.q_item_parse(question_body)
			question_dict['body'] = body_list
				
		#	print "题干"
		#	print body_list
		
		if 'options' in encode_json.keys():
			question_options = encode_json['options']

			for i,option in enumerate(question_options):
				options_list.append(Business.q_item_parse(option))
			
			question_dict['options'] = options_list

		#	print "题选项"
		#	print options_list

		if 'answer' in encode_json.keys():
			question_answer = encode_json['answer']

			answer_list = Business.q_item_parse(question_answer)

			question_dict['answer'] = answer_list

		#	print "题解答"
		#	print answer_list

		if 'analysis' in encode_json.keys():
			question_analysis = encode_json['analysis']			

			analysis_list = Business.q_item_parse(question_analysis)
	
			question_dict['analysis'] = analysis_list

		#	print "题分析"
		#	print analysis_list
		return question_dict

	@staticmethod
	def q_item_parse(item_list):

		tmp_list = []
		
		for item_dict in item_list:
			if 'text' == item_dict['type']:
				value = item_dict['value']
				value = value.replace(r'<','^<$')			
				value = value.replace(r'>','^>$')
				value = value.replace(r'^','<cdata>')
				value = value.replace(r'$','</cdata>')

				if 4 == item_dict['style']:
					item_html = "<u>%s</u>" % (value.encode('utf8'))
				elif 16 == item_dict['style']:
					item_html =  '<span style="border-bottom:dotted 2px">%s</span>' % (value.encode('utf8'))
				else:
					item_html = "<span>%s</span>" % (value.encode('utf8'))
				
				tmp_list.append(item_html)

			if 'newline' == item_dict['type']:
				item_html = "<br />" 
				tmp_list.append(item_html)

			if 'image' == item_dict['type']:
				item_html = '<img src = "%s" />'  % (item_dict['value'].encode('utf8'))

				tmp_list.append(item_html)

			if 'option' == item_dict['type']:
				item_html = "<span>%s.</span>" % (item_dict['value'].encode('utf8'))

				tmp_list.append(item_html)

		return tmp_list
	
