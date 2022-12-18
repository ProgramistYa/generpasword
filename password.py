#Гениратор кода который трудно взломать для hacers

import random

nijniy_reg = 'qwertyuiopasdfghjklzxcvbnm'
verh_reg = 'QWERTYUIOPASDFGHJKLZXCVBNM'
number = '0987654321'
symbols = '@#$!%*/\?'

input('Нажми enter сгенерируются пароль из 9 символов!')

use_for = nijniy_reg + verh_reg + number + symbols
dlina_pass =  9

password = "".join(random.sample(use_for, dlina_pass))
print('Твой сгенерирующийся пароль:'"\n" , password)
