#___________________________decimals____________________________#
import decimal as dc

dc.getcontext().prec = 4       # setting the decimal precision globally
k = dc.Decimal('1')            # decimal literal
f = dc.Decimal('7')
print(k)
print(f)
with dc.localcontext() as ctx: # creating a local context manager as ctx
    ctx.prec = 2               # setting local context precision of 2 decimal places
    print(k/f)                 # answer with local context pricision

print(k/f)                     # answer with global context pricision

print('='*40)#_____________________Fractions________________________#
import fractions as fr

x = fr.Fraction(1, 7) # Fractional number literal
y = fr.Fraction(0.25) # converting a float to fraction
z = fr.Fraction(k/f)  # converting a decimal to fraction
print(x)
print(y)
print(z)              # numbers are automatically simplified to GCD ie. 4/6 ~ 2/3