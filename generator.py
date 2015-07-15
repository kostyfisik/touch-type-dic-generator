#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#    Copyright (C) 2015  Konstantin Ladutenko <kostyfisik@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import string
import random
letters = set(string.ascii_letters)
workman_step0 = set('ashtneoi')
workman_step1 = set('ashtneoidrclup')
workman_step2 = set('ashtgyneoiqdrwbjfup')
workman_step3 = set('ashtgyneoizxmcvkl')
workman_step4 = set(set(string.ascii_lowercase))
step0 = letters - workman_step0
step1 = letters - workman_step1
step2 = letters - workman_step2
step3 = letters - workman_step3
step4 = letters - workman_step4
exclude=set("'- :")
step = [step0.union(exclude),
        step1.union(exclude),
        step2.union(exclude),
        step3.union(exclude),
        step4.union(exclude)]
count = 0
for i in xrange(5):
    with open("workman_step%i.dic"%i,'w') as file_:
        with open("en_US.dic") as f:
            for line in f:
                if not any((c in step[i]) for c in line):
                    count = count + 1
                    if len(line)>1:
                        file_.write(line)
    print(count)
    with open("workman_step%i.dic"%i,'r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open("workman_step%i.dic"%i,'w') as target:
        for _, line in data:
            target.write( line )
