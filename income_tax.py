import sys
import numpy as np
import matplotlib as plt
import pandas as pd

ca_marry_sep_2023 = [
    [10099, 0.01],
    [23942, 0.02],
    [37788, 0.04],
    [52455, 0.06],
    [66295, 0.08],
    [338639, 0.093],
    [406364, 0.103],
    [677275, 0.113],
    [100000000, 0.123]
]

ca_marry_joint_2023 = [
    [20198, 0.01],
    [47884, 0.02],
    [75576, 0.04],
    [104910, 0.06],
    [132590, 0.08],
    [677278, 0.093],
    [812729, 0.103],
    [1354550, 0.113],
    [100000000, 0.123]
]

marry_joint_2023 = [
    [22000, 0.1],
    [89450, 0.12],
    [190750, 0.22],
    [364200, 0.24],
    [462500, 0.32],
    [693750, 0.35],
    [100000000, 0.37]
]
marry_sep_2023 = [
    [11000, 0.1],
    [44725, 0.12],
    [95375, 0.22],
    [182100, 0.24],
    [231250, 0.32],
    [578125, 0.35],
    [100000000, 0.37]
]
ca_marry_sep_2022 = [
    [10099, 0.01],
    [23942, 0.02],
    [37788, 0.04],
    [52455, 0.06],
    [66295, 0.08],
    [338639, 0.093],
    [406364, 0.103],
    [677275, 0.113],
    [100000000, 0.123]
]

ca_marry_joint_2022 = [
    [20198, 0.01],
    [47884, 0.02],
    [75576, 0.04],
    [104910, 0.06],
    [132590, 0.08],
    [677278, 0.093],
    [812729, 0.103],
    [1354550, 0.113],
    [100000000, 0.123]
]

marry_sep_2022 = [
    [10275, 0.1],
    [41775, 0.12],
    [89075, 0.22],
    [170050, 0.24],
    [215950, 0.32],
    [539900, 0.35],
    [100000000, 0.37]
]

marry_joint_2022 = [
    [20550, 0.1],
    [83550, 0.12],
    [178150, 0.22],
    [340100, 0.24],
    [431900, 0.32],
    [647850, 0.35],
    [100000000, 0.37]
    ]

rates_type = {
    'marry_sep_2022': marry_sep_2022,
    'marry_joint_2022': marry_joint_2022,
    'ca_marry_sep_2022': ca_marry_sep_2022,
    'ca_marry_joint_2022': ca_marry_joint_2022,
    'marry_sep_2023': marry_sep_2023,
    'marry_joint_2023': marry_joint_2023,
    'ca_marry_sep_2023': ca_marry_sep_2023,
    'ca_marry_joint_2023': ca_marry_joint_2023,
}

the_rate_type = sys.argv[1]
the_income = int(sys.argv[2])

def get_tax(rtype, income):
    rates = rates_type[rtype]
    tax = 0
    last_step = 0
    for i in range(len(rtype)):
        cur_range = [last_step, rates[i][0]]
        last_step = rates[i][0]
        tax_rate = rates[i][1]
        if income < cur_range[1]:
            tax += (income - cur_range[0]) * tax_rate
            break
        else:
            tax += (cur_range[1] - cur_range[0]) * tax_rate
    return tax

icm = np.arange(50000, 1600000, 10000)
tax_tot = []
col = ['marry_sep_2022', 'marry_joint_2022', 'ca_marry_sep_2022', 'ca_marry_joint_2022',
       'marry_sep_2023', 'marry_joint_2023', 'ca_marry_sep_2023', 'ca_marry_joint_2023']
data = {}
data['income'] = []
for c in col:
    data[c] = []
for i in icm:
    data['income'].append(i)
    for j in col:
        data[j].append(get_tax(j, i))
df = pd.DataFrame(data)
print(df.to_string())

with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='tax')

#for i, t1, t2 in tax_tot:
#    print('%8d %8.1f %.1f%% %8.1f %.1f%%' % (i, t1, t1*1.0/i*100, t2, t2*1.0/i*100))

print(get_tax(the_rate_type, the_income))

#print('income=%.1f tax=%.1f actual=%.1f rate=%.3f' % (income, tax, income - tax, tax * 1.0 / income))
      

