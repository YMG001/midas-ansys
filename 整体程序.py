# *_*coding:utf-8 *_*
#提取midas节点信息转换成ansys节点信息
fo=open('合并.txt','r',encoding='utf-8')
ls=[]
wflag=False
for line in fo:
    if line[0]=='*':
        wflag=False
    if '*NODE' in line:
        wflag=True
        continue
    if wflag==True:
        if line[0]==';' or line[0]=='\n':
            pass
        else:
            ls.append('n,'+line)
print(ls[0])
fi=open('bridge_node.txt','w')

i=0
for ip in ls:
    if i==0:
        fi.write('finish\n/clear\n/prep7\n')
        i=i+1
        fi.write(str(ip))
    else:
        fi.write(str(ip))
fi.close()


# *_*coding:utf-8 *_*
'''
这个文档是提取mct中的截面种类，和截面数据
'''
def sec():
    fo=open('合并.txt','r',encoding='utf-8')
    ls=[]
    l={}
    wflag=False
    for line in fo:
        if line[0]=='*':
            wflag=False
        if '*SECTION' in line:
            wflag=True
            continue
        if wflag==True:
            if line[0]==';' or line[0]=='\n':
                pass
            else:
                if 'DBUSER' in line and 'B  ' in line:
                    k=line.split(',')
                    # print(k)
                    enum=k[0]+','           #截面的编号
                    type1='BEAM, HREC'
                    w1=k[15]+','
                    w2=k[14]+','
                    t1=k[16]+','
                    t2=k[16]+','
                    t3=k[17]+','
                    t4=k[17]+','
                    # sectype, 1, beam, I
                    # secdata, 400 / 1000, 400 / 1000, 420 / 1000, 12 / 1000, 12 / 1000, 12 / 1000,
                    ls.append('SECTYPE,' + enum + type1 + '\nSECDATA,' + w1 + w2 + t1 + t2 + t3 + t4 + '\n')
                    l[k[0].strip()]='SECTYPE,' + enum + type1 + '\nSECDATA,' + w1 + w2 + t1 + t2 + t3 + t4 + '\n'+'secnum,'+enum+'\n'
                elif 'TAPERED' in line and 'B  ' in line:
                    k3_T = line.split(',')
                    enum3 = k3_T[0] + ','#截面的编号
                    line=next(fo)
                    # print(line)
                    k3=line.split(',')
                    type2='BEAM, HREC'
                    w1=k3[9]+','
                    w2=k3[8]+','
                    t1=k3[10]+','
                    t2=k3[11]+','
                    t3=k3[10]+','
                    t4 = k3[11] + ','
                    # esec=k[3]
                    # n1=k[4]
                    # n2=k[5]
                    # sectype, 1, beam, I
                    # secdata, 400 / 1000, 400 / 1000, 420 / 1000, 12 / 1000, 12 / 1000, 12 / 1000,
                    ls.append('SECTYPE,' + enum3 + type2 + '\nSECDATA,' + w1 + w2 + t1 + t2 + t3 +t4+ '\n')
                    l[k3_T[0].strip()] = 'SECTYPE,' + enum3 + type2 + '\nSECDATA,' + w1 + w2  + t1 + t2 + t3+t4 + '\n'+'secnum,'+enum3+'\n'
                elif 'DBUSER' in line and 'H  ' in line:
                    # print(line)
                    k1=line.split(',')
                    # print(k1)
                    enum1=k1[0]+','           #截面的编号
                    type1='BEAM, I'
                    w1=k1[18]+','
                    w2=k1[15]+','
                    w3=k1[14]+','
                    t1=k1[19]+','
                    t2=k1[17]+','
                    t3=k1[16]+','
                    # esec=k[3]
                    # n1=k[4]
                    # n2=k[5]
                    # sectype, 1, beam, I
                    # secdata, 400 / 1000, 400 / 1000, 420 / 1000, 12 / 1000, 12 / 1000, 12 / 1000,
                    ls.append('SECTYPE,' + enum1 + type1 + '\nSECDATA,' + w1 + w2 + w3 + t1 + t2 + t3 + '\n')
                    l[k1[0].strip()] = 'SECTYPE,' + enum1 + type1 + '\nSECDATA,' + w1 + w2 + w3 + t1 + t2 + t3 + '\n'+'secnum,'+enum1+'\n'
                elif 'TAPERED' in line and 'H  ' in line:
                    k2_T = line.split(',')
                    enum2 = k2_T[0] + ','#截面的编号
                    line=next(fo)
                    # print(line)
                    k2=line.split(',')
                    type2='BEAM, I'
                    w1=k2[12]+','
                    w2=k2[9]+','
                    w3=k2[8]+','
                    t1=k2[13]+','
                    t2=k2[11]+','
                    t3=k2[10]+','
                    # esec=k[3]
                    # n1=k[4]
                    # n2=k[5]
                    # sectype, 1, beam, I
                    # secdata, 400 / 1000, 400 / 1000, 420 / 1000, 12 / 1000, 12 / 1000, 12 / 1000,
                    ls.append('SECTYPE,' + enum2 + type2 + '\nSECDATA,' + w1 + w2 + w3 + t1 + t2 + t3 + '\n')
                    l[k2_T[0].strip()] = 'SECTYPE,' + enum2 + type2 + '\nSECDATA,' + w1 + w2 + w3 + t1 + t2 + t3 + '\n'+'secnum,'+enum2+'\n'
    # print(ls)
    # print(len(ls))
    # print(l)
    fi=open('bridge_elementsec1.txt','w')
    i = 0
    for ip in ls:
        fi.write(str(ip))
    fi.close()
    return l

sec_dist=sec()


fo=open('合并.txt','r',encoding='utf-8')
ls_f=[]
dict1={}
wflag=False
for line in fo:
    if line[0]=='*':
        wflag=False
    if '*ELEMENT' in line:
        wflag=True
        continue
    if wflag==True:
        if line[0]==';' or line[0]=='\n':
            pass
        else:
            if 'BEAM' in line:
                k=line.split(',')
                # print(k)
                enum=k[0]
                etype=k[1]
                emat=k[2]
                esec=k[3]
                n1=k[4]
                n2=k[5]
                str1='E'+','+n1+','+n2
                if k[3].strip() in dict1.keys():
                    dict1[k[3].strip()].append(str1)
                else:
                    dict1[k[3].strip()]=(str1).split('。')#这里的需要将值转换成字典的形式

print(dict1.keys())

fi = open('bridge_elementsec_finsh1.txt', 'w')
i = 0
for ip in dict1.keys():
    if i==0:
        fi.write('et,5,beam188\n\
Mp,ex,5,3.55e4!混凝土\n\
Mp,dens,5,2.549e-9\n\
Mp,prxy,5,0.2\n')
        i=i+1
    fi.write(sec_dist[ip])
    fi.write('type,5\nmat,5\n')
    for x in dict1[ip]:
        fi.write(x+'\n')
fi.close()