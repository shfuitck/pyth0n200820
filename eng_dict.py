d={}
print('wellcome to eng high heand')
while True:
        print('1.build the dictionary')
        print('2.列出所有單字 ')
        print('3.英翻中')
        print('4.中翻英')
        print('5.測驗') 
        print('6.離開')
        option=input('please tipe the number:')
        if option=='6':
            break
        elif option=='1':
            while True:
                voc=input('please tipe the new voc(push 0 to leave)')
                if voc=='0':
                    break
                if voc not in d:
                    voc_ch=input('tipe the 中文: ')
                    d[voc]=voc_ch
                else:
                  print('已存在')  
        elif option =='2':
            s=sorted(d)
            for i in s:
                print(i,':',d[i])
        elif option =='3':
            while True:
                  voc=input('please tipe the eng  voc(push 0 to leave)')
                  if voc=='0':
                     break
                  if voc in d:
                     print(voc,'中文是',d[voc])
                  else:   
                      print('do not have this voc')
        elif option =='4':
            while True:     
                got = False
                ch = input('please tipe the 中文: ')
                if ch =='0':
                     break     
                for k,v in d.items():
                    if ch==v:
                        print(ch,'的英文是',k)
                        got = True
                if got == False:
                    print('do not have this voc')                        
        elif option =='5':
             score=0
             for k,v in d.items():
                 print(v,':')    
                 ans=input()
                 if ans ==k:
                     score+=1
                     print('答對')
                 else:
                      print('答錯')
             print('you get',score,'分')         
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     
                     