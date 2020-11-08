txt=open(r'mydata_v2.log')
lines=[]
flag=False
for line in txt:
    if line.strip()=="center_freq":        
        flag=True                                # 起始行开始不再添加
    if not flag:
        lines.append(line)                    # 需求之外的行添加到列表
    if line.strip()=="Spectral resolution":
        flag=False                               # 结束行开始恢复添加
txt.close()
open(r'mydata_v2.log','w').writelines(lines)
