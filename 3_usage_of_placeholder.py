#-*-coding:utf-8-*-
from __future__ import print_function, division
import tensorflow as tf
# 省内存，placeholder才是王道
def use_placeholder():
	graph = tf.Graph()
	with graph.as_default():
		value1 = tf.placeholder(dtype=tf.float64)
		value2 = tf.Variable([3,4],dtype=tf.float64)
		mul = value1 * value2
	
	with tf.Session(graph=graph) as mySess:
		tf.initialize_all_variables().run()
		#print('一一对应的乘法(value1,value2)',mySess.run(mul))
		value = load_from_remote()
		for partialValue in load_partial(value,2):
				'''
				holderValue = {value1:partialValue}
				evalResult = mul.eval(feed_dict=holderValue)
				print('乘法(value1,value2) = ',evalResult)
				'''
				runResult = mySess.run(mul, feed_dict={value1:partialValue})
				print('乘法(value1, value2) = ', runResult)

def load_from_remote():
	return [-x for x in range(1000)]

# yield 写一个生成器 generator function
def load_partial(value,step):
		index = 0
		while index <= len(value):
				yield value[index:index+step]
				index += step
		return

use_placeholder()
