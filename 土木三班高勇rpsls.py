#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2021.12.1
"""
import random

def name_to_number(name):#����Ϸ���������ֱ��
    if name=='ʯͷ':
        number=0
    elif name=='ʷ����':
        number=1
    elif name=='��':
        number=2
    elif name=='����':
        number=3
    elif name=='����':
        number=4
    return number

def number_to_name(number):#ʹ��0-4������Ϸ����
    if number==0:
       name='ʯͷ'
    elif number==1:
         name='ʷ����'
    elif number==2:
         name='��'
    elif number==3:
         name='����'
    elif number==4:
         name='����'
    return name
    return

def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    comp_number=random.randrange(0,4)
    if player_choice=='ʯͷ' or player_choice=='��' or player_choice=='����' or player_choice=='ʷ����' or player_choice=='����':
       print('����ѡ��Ϊ:'+player_choice)
       print('�������ѡ��Ϊ:'+number_to_name(comp_number))
    else:
        print('��Error: No Correct Name��')#����涨��������ʾError: No Correct Name
        return
    player_choice_number=name_to_number(player_choice)
    if comp_number==0 and (player_choice_number==3 or player_choice_number==4):
        result=print('����Ӯ��')
    elif comp_number==1 and (player_choice_number==0 or player_choice_number==4):
        result=print('����Ӯ��')
    elif comp_number==2 and (player_choice_number==0 or player_choice_number==1):
        result=print('����Ӯ��')
    elif comp_number==3 and (player_choice_number==2 or player_choice_number==1):
        result=print('����Ӯ��')
    elif comp_number==4 and (player_choice_number==2 or player_choice_number==3):
        result=print('����Ӯ��')
    elif comp_number==player_choice_number:
        result=print('���ͼ��������һ����')
    else:
        result=print('��Ӯ��!')
    return result
    return
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")#��������
choice_name=input()
rpsls(choice_name)