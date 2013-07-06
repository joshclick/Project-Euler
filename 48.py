def sum_self_pow(num):
    if num == 1:
        return 1
    else:
        return sum_self_pow(num - 1) + num ** num

print str(sum_self_pow(1000))[-10:]
