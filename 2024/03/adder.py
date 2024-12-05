#!/usr/bin/python
# receives a sequces of expressions, just use eval and add them together

print(
    sum(
        (eval(exp) for exp in 
         (lambda: iter(input,''))())
        ))
