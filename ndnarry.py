#%%
import numpy as np
#%% [markdown]
## arrary 的创建和操作
# 可以使用np.arrary 将list转换为ndarry
#%% 
alist = [1, 2, 3]
arr = np.array(alist)
#%% [markdown]
# 也可以使用zeros和arange （0到100）初始化
#%%
arr1 = np.zeros(5)
arr2 = np.arange(100)
arr3 = np.arange(10,100)
arr4 = np.linspace(0, 1, 100)
print(arr1, arr2, arr3, arr4)

#%%[markdown]
# 一样可以使用创建二维，或者使用上述方法
#%%
image = np.zeros((5,5))
cube = np.zeros((5,5,5)).astype(int) + 1
arr2d = arr2.reshape(10,10)
arr3d = np.reshape(arr2, (1, 10, 10))
print(image.shape, cube.shape, arr2d.shape, arr3d.shape)
#%% [markdown]
## 数据类型
# 在arrary 的data type 也可以通过相应的参数进行设置

#%%
arr = np.zeros(2, dtype=int)

#%% [markdown]
## array 索引
### 分片索引
#  array 的操作和分片操作和python的List操作一样，但表达上更为方便。
#%%
alist=[[1,5],[3,4]]
alist[0][1]

arr = np.array(alist)
arr[0,1]
arr[1,:]
#%%[markdown]
### 用多维array去索引数组 相关知识总结在OneNote上。
#%%
a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
#%%[markdown]
### 布尔式索引
# 可以使用 ```
#  x[y>2]```这样来引用数组，y>2 返回的是一个布尔变量数组
# x[y>2] 只会引用布尔变量为true的数组元素。
#%%
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2) 
print(a[bool_idx])
print(a[a > 2])   

#%%[markdown]
## 数组的增改删查
### 增
# 在创建一项已经说明了。append(),
### 改
#### 数学运算 
# 数学运算中(+-*/)，照理array是应该统一维度的。但是numpy中有broadcasting的机制，可以减少赋值的循环，使循环在C语言中实现而不是在python中实现，减少了运行时间。
#%%
x = np.array([1, 2])
y = np.array([[3], [4]])
b = 2
print(x+y)
print(b*x)
#%%[markdown]

#1. 如果两个数组在维度中大小相同，
#2. 或者其中一个数组在该维度中大小为1，那么这两个数组在维度中是兼容的。
#3. 如果数组在所有维度上都兼容，则可以将它们一起广播。进入翻译页面
### 查
#  np.where函数可以使用返回满足对应条件的索引，def where(condition, x, y)符合条件输出x，不符合输出y。在一维的情况下，xy缺省，即返回条件式为true的索引。 二维情况，返回的是坐标，竖着看即是坐标。

#%%
arr = np.arange(4,10)
arr2 = arr.reshape(2,3)
index = np.where(arr > 5)
print(index)
index = np.where(arr2 > 5)
print(index)

#%%[markdown]
# 对于麻烦的a[np.where(a>5)] 提取大于5 的元素来说，直接使用arr[arr>5] 这形式就容易多了.无论维数，都是等价的。
### 删
# 删除操作可以使用np.delete 来进行操作

#%%
np.delete