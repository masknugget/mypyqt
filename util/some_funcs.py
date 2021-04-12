import inspect
import os

from PySide2.QtCore import QAbstractAnimation

f_path = r'D:\pull_data\mypyqt\docs\pyside2'

flist = os.listdir(f_path)


ff = os.path.join(f_path, flist[0])

with open(ff, encoding='utf-8') as f:
    ll = f.readlines()



file = open('test.txt', 'w', encoding='utf-8')
# file.write('a')
# file.write('b')
# file.close()

base = r'from PySide2.'
for i in flist:
    ff = os.path.join(f_path, i)

    with open(ff, encoding='utf-8') as f:
        ll = f.readlines()

    for j in ll:
        if str(j).startswith('    '):
            j = str(j).replace('\n', '').replace('    ', '')

            base_1 = base + str(i) + ' import ' + str(j)

            try:
                exec (base_1)

                a = None
                exec('a = dir({})'.format(j))
                # print(a)
                if a:
                    print(base_1)
                    file.write(str(base_1) + '\n\n')
                    print('\n\n')
                    for v in a:
                        if not str(v).startswith('__'):

                            print('    '+ v)
                            file.write('    '+ v + '\n')

                            # f.write(v)
                            res = '    ' + str(v) + '\n'
                            vv = 'vv = inspect.signature({}).parameters'.format(j+'.'+v)
                            try:
                                exec (vv)
                                print('        ', vv)
                                file.write('        '+ vv + '\n')
                                # f.write(res)
                            except:
                                print('    '+j+'.'+v)
                                print('        not a callable object' + '\n')
                                file.write('    '+j+'.'+v)
                                file.write('        not a callable object' + '\n')
                                continue
                    f.write('\n\n\n')
            except Exception as e:
                # print('!!!!!', base_1, e)
                continue



f.close()