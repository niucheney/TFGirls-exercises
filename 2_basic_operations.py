#-*-coding:utf-8-*-
from __future__ import print_function, division
import tensorflow as tf

def basic_operator():
	v1 = tf.Variable(10)
	v2 = tf.Variable(5)
	addv = v1 + v2
	print(addv)
	print(type(addv))
	print(type(v1))
	
	# constant与Variable不一样，Variable是一个类型，而constant直接是一个Tensor
	c1 = tf.constant(10)
	c2 = tf.constant(5)
	addc = c1 + c2
	# Session是用来计算图谱的对象/实例？
	# session is a runtime
	sess = tf.Session()
	
	# Variable -> 初始化 -> 有值的Tensor
	tf.initialize_all_variables().run(session=sess)
	print('变量是需要初始化的')
	print('加法(v1,v2)=',addv.eval(session=sess))
	#其等价写法：
	print('加法(v1,v2)=',sess.run(addv))
	print('加法(c1,c2)=',sess.run(addc))
	print('\n\n')

	#这种定义操作，再执行操作的模式被称为"符号式编程 Symbolic Programming

	# tf 更好的模组的方式是如下， 
	# tf.Graph__init__()
	# Crates a new, empty Graph
	graph = tf.Graph()
	with graph.as_default():
		value1 = tf.constant([1,2])
		value2 = tf.Variable([3,4])
		mul = value1 * value2
	#这里mul和线性代数里面的矩阵乘法不一样，这里是对应位置相乘。
	with tf.Session(graph=graph) as mySess:
		tf.initialize_all_variables().run()
		print('乘法(value1, value2) = ', mySess.run(mul))
		print('乘法(value1, value2) = ', mul.eval())


def test():
	d1 = tf.Variable(4)
	d2 = tf.Variable(5)
	addd = d1 + d2
	
	sess = tf.Session()
	tf.initialize_all_variables().run(session=sess)
	print('d1 + d2 = ',sess.run(addd))

	graph = tf.Graph()
	with graph.as_default():
		v1 = tf.constant([1,2])
		v2 = tf.constant([3,4])
		mul = v1 * v2
	with tf.Session(graph=graph) as mySess:
		tf.initialize_all_variables().run()
		print('乘法(value1, value2) = ',mySess.run(mul))
		print('乘法(value1, value2) = ',mul.eval())

	
#basic_operator()
test()
