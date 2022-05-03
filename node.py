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


