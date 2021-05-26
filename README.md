# **COMPOUND INTEREST FACTORS**
This is a module of compound interest factors which includes single payment, uniform payment series, and arithmetic gradient calculations
### **By Zaafirrahman**

## **Installation**

This library can be installed by the pip command, open your terminal and type in the following command...

```python
pip install compoundinterest
```

## **Functions of this library**

First import the library using this command 
```python
import compoundinterest as ci
```
 and then proceed to call the functions

## Single Payment

## `ci.fp()`

This function can be used to calculate compound interest factor of future value based on present value

## `ci.pf()`

This function can be used to calculate compound interest factor of present value based on future value


## Uniform Payment Series

## `ci.fa()`

This function can be used to calculate compound interest factor of future value based on annual value

## `ci.af()`

This function can be used to calculate compound interest factor of annual value based on future value

## `ci.pa()`

This function can be used to calculate compound interest factor of present value based on annual value

## `ci.ap()`

This function can be used to calculate compound interest factor of annual value based on present value


## Arithmetic Gradient

## `ci.pg()`

This function can be used to calculate compound interest factor of present value based on gradient value

## `ci.ag()`

This function can be used to calculate compound interest factor of annual value based on gradient value


## **The parameters**

**i (interest rate)** - Interest rate (without percent) used in the calculation

**n (time period)** - Investment time period (in year/s) used in the calculation

### **Example :**

You are saving $ 30,000 USD in the bank at an interest rate of 10% annually. How much will it be worth when you take it in 5 years?

In this case, the variables that you already know are present value ($ 30,000 USD), interest rate (10%), and investment period (5 years). Whereas the variable that you are looking for is the future value. So you will need the `ci.fp()` function with the following calculations:

```python
>>> import compoundinterest as ci
>>> ci.fp(10,5)*30000

48315.30000000002
```

So, your money in the next 5 years is $ 48,315.3 USD
