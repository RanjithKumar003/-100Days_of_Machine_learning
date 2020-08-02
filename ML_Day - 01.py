#!/usr/bin/env python
# coding: utf-8

# # print function and string

# In[28]:


print('This is an example of print function')


# In[29]:


print('We're going to the store')


# In[30]:


print("We're going to the store")   #In above case i got error, so here iam useing double qoutes to print we're


# In[31]:


print('He said "Hi."')


# In[32]:


print('We\'re going to the store')


# In[33]:


print('Hi'+'there') #it concaternate(add) 2 string


# In[34]:


print('Hi '+'there')


# In[35]:


print('Hi '+5) #it  give error because 5 is integer


# In[36]:


print('Hi '+ str(5))  #here we using string function for 5 - string conversion


# In[37]:


print(int('8') + 5) #integer conversion


# In[38]:


print(int('8.5')+5) #conversion error it is float


# In[39]:


print(float('8.5')+5)


# # Basic math for python

# In[40]:


#     +      -    *     /

#single line comment
#print('Hi')
print('hi')


# In[41]:


'''multiple line comments
dose not sho or run any thing
'''


# In[42]:


5+3


# In[43]:


7-4


# In[44]:


3*6


# In[45]:


4/2   #qoutiont


# In[46]:


4%3   #reminder


# In[47]:


4**4    #power


# In[ ]:





# In[ ]:





# # variable

# In[ ]:


var = 5
print(var)


# In[8]:


x,y = 5,7
print(x, y)
print(x)
print(y)


# In[10]:


x, y = 10, 5, 6
print(x, y)


# # while loop

# In[11]:


condition = 1
while condition < 10:    #YOUR CONDITION LESS UNTILKL less then 10, it print up to 9
    print(condition)
    condition += 1     #INCREMENT


# # for loop

# In[12]:


ex_list = [1, 4, 6, 55, 78, 96, 33, 5, 8, 2, 11]
for eachNumber in ex_list:
    print(eachNumber)


# In[13]:


ex_list = [1, 4, 6, 55, 78, 96, 33, 5, 8, 2, 11]
for eachNumber in ex_list:
    print(eachNumber)
    print('continue program')


# In[14]:


for x in range(1, 11):
    print(x)


# # if statement

# In[15]:


x = 5
y = 8
if x < y:
    print('x is less then y')


# In[16]:


x = 5
y = 8
z = 5
if x < y > z:
    print('y is greater then z and x')


# In[18]:


x = 5
y = 8
z = 5
if x >= z :
    print('z is equal to x')


# In[19]:


x = 5
y = 8
z = 5
if x == z :
    print('z is equal to x')


# In[20]:


x = 5
y = 8
z = 5
if y != z :
    print('y is not equal to z')


# # if - else

# In[21]:


x = 5
y = 8
if x > y :
    print('x is greater than y')
else:
    print('x is lesser then y')


# In[22]:


x = 5
y = 8
if x > y :
    print('x is greater than y')
if x> 55:
    print('x is greter than 55')
else:
    print('x is lesser then y')


# # if, elif, else

# In[25]:


x = 5
y = 10
z = 22
if x > y :
    print('x is greater than y')
elif x<z:
    print('x is less than z')
else:
    print('if and elif never run')


# In[26]:


x = 5
y = 10
z = 22
if x > y :
    print('x is greater than y')
elif x<z:
    print('x is less than z')
elif 5 > 2:
    print('5 is greater the 2')
else:
    print('if and elif never run')


# In[27]:


x = 5
y = 10
z = 22
if x > y :
    print('x is greater than y')
elif x == z:
    print('x is less than z')
elif 5== 2:
    print('5 is greater the 2')
else:
    print('if and elif never run')


# In[ ]:




