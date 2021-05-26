def fp(i,n) :
  i /= 100
  return (1+i)**n

def pf(i,n) :
  i /= 100
  return 1/((1+i)**n)

def fa(i,n) :
  i /= 100
  return (((1+i)**n)-1)/i

def af(i,n) :
  i /= 100
  return i/(((1+i)**n)-1)

def pa(i,n) :
  i /= 100
  return (((1+i)**n)-1)/(i*((1+i)**n))

def ap(i,n) :
  i /= 100
  return (i*((1+i)**n))/(((1+i)**n)-1)

def pg(i,n) :
  i /= 100
  return (((1+i)**n)-(1+n*i))/((i**2)*((1+i)**n))

def ag(i,n) :
  i /= 100
  return (1/i)-(n/(((1+i)**n)-1))
