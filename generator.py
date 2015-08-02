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
exclude=set("'- :")
letters = letters.union(exclude)
workman_step0 = set('ashtneoi')
new_step0 = set('ashtneoi')
workman_step1 = set('ashtneoidrclup')  # basic letters
new_step1 = workman_step1-workman_step0
workman_step2 = set('ashtgyneoiqdrwbjfup')
new_step2 = workman_step2 - workman_step1
workman_step3 = set('ashtgyneoizxmcvkl')
new_step3 = workman_step3 - workman_step1
workman_step4 = set(set(string.ascii_lowercase))
new_step4 = workman_step4
step0 = letters - workman_step0
step1 = letters - workman_step1
step2 = letters - workman_step2
step3 = letters - workman_step3
step4 = letters - workman_step4
step = [step0, step1, step2, step3, step4]
new = [new_step0, new_step1, new_step2, new_step3, new_step4]
count = 0
for i in xrange(5):
    with open("workman_step%i.dic"%i,'w') as file_:
        with open("en_US.dic") as f:
            for line in f:
                if not any((c in step[i]) for c in line):
                    if len(line)>1:
                        for new_letter in new[i]:
                            #if True:
                            if new_letter in line:
                                count = count + 1
                                file_.write(line)
                                break
    print(count)
    with open("workman_step%i.dic"%i,'r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open("workman_step%i.dic"%i,'w') as target:
        for _, line in data:
            target.write( line )
