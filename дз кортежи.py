user = {'Камин комплект Старый Замок':{'count': 1, 'price': 28490}, 
'Полусапоги Betsy':{'count': 2, 'price': 2399}, 
'Семь навыков высокоэффективных людей':{'count': 1, 'price': 437}}
s = user['Камин комплект Старый Замок']['count'] * user['Камин комплект Старый Замок']['price']+ user['Полусапоги Betsy']['count'] * user['Полусапоги Betsy']['price']+ user['Семь навыков высокоэффективных людей']['count'] * user['Семь навыков высокоэффективных людей']['price'] 
print(f'Общая сумма равна :{s}')
