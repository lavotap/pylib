#-*-coding:utf-8-*-

from pylib.vector import Vector
# 二维向量
v1=Vector(0,2)
v2=Vector(2,0)
print('v1='+str(v1))
print('v2='+str(v2))
print('v1+v2='+str(v1+v2))
print('v1-v2='+str(v1-v2))
print('v1*2='+str(v1*2))
print('v1/2='+str(v1/2))
print('点乘v1*v2='+str(v1*v2))
print('叉乘v1^v2='+str(v1^v2))
print('v1取模='+str(v1.get_length()))
print('v1单位向量化='+str(v1.get_unit()))
print('v1与v2夹角='+str(v1.get_theta(v2)))
print('v1与v2带符号夹角='+str(v1.get_theta_with_sign(v2)))
print('v1取左垂直向量='+str(v1.get_left()))
print('v1取右垂直向量='+str(v1.get_right()))

# 三维向量
v3=Vector(0,1,1)
v4=Vector(1,0,1)
print('v3='+str(v3))
print('v4='+str(v4))
print('v3+v4='+str(v3+v4))
print('v3-v4='+str(v3-v4))
print('v3*2='+str(v3*2))
print('v3/2='+str(v3/2))
print('点乘v3*v4='+str(v3*v4))
print('叉乘v3^v4='+str(v3^v4))
print('v3取模='+str(v3.get_length()))
print('v3单位向量化='+str(v3.get_unit()))
print('v3与v4夹角='+str(v3.get_theta(v4)))
print('v3与v4带符号夹角='+str(v3.get_theta_with_sign(v4)))
print('v3取左垂直向量='+str(v3.get_left()))
print('v3取右垂直向量='+str(v3.get_right()))
