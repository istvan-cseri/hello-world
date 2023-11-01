# Databricks notebook source
a = [1, 2, 10]
import matplotlib.pyplot as plt
print(a)
plt.plot(a)
print(a)

# COMMAND ----------

# MAGIC %%capture cap
# MAGIC print(a)

# COMMAND ----------

print(cap)
%matplotlib inline

plt.plot((2, 3, 4))

print(cap)

#comment
