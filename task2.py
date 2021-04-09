# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

a = 1                   # creating starting values to list
b = 2                   # creating starting values to list
c = 0                   # define c
cnt = 0                 # define counter
while c < 4000000:
    c = a + b           # c получаю из суммы двух предыдущих чисел
    if c % 2 == 0:      # если c чётное
        cnt += c        # то прибавляю к счётчику
    a = b               # значение a теперь равняется значению b
    b = c               # значение b теперь равняется значению c
cnt += 2                # после завершения условия while добавляю 2 к значению счётчика
print(cnt)