from __future__ import absolute_import

import user_agent.base
from user_agent import (
    InvalidOption,
    generate_navigator,
    generate_navigator_js,
    generate_user_agent,
)

import csv

header = ['agent']
data = []

for i in range(10): 
    agent = generate_user_agent()
    data.append([agent])

with open('agents.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)