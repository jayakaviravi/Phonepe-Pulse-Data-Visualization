import os
import json
import pandas as pd
import mysql.connector as sql

#aggregated transaction

path1="C:/Users/JAYAKAVI/New folder/pulse/data/aggregated/transaction/country/india/state/"
agg_trans_state_list=os.listdir(path1)

col = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [],'Transaction_count': [], 'Transaction_amount': []}

for i in agg_trans_state_list:
    cur_s=path1+i+"/"
    agg_year_list = os.listdir(cur_s)
    
    for j in agg_year_list:
        cur_y=cur_s+j+"/"
        agg_year_json=os.listdir(cur_y)
        
        for k in agg_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)
            
            for n in m['data']['transactionData']:
                name=n["name"]
                count=n["paymentInstruments"][0]["count"]
                amount=n["paymentInstruments"][0]["amount"]
            
                col["State"].append(i)
                col["Year"].append(j)
                col["Quarter"].append("Q"+str(k[0]))
                col["Transaction_type"].append(name)
                col['Transaction_count'].append(count)
                col['Transaction_amount'].append(amount)

agg_trans=pd.DataFrame(col)
agg_trans['State']=agg_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
agg_trans['State']=agg_trans['State'].str.replace('-',' ')
agg_trans['State']=agg_trans['State'].str.title()
agg_trans['State']=agg_trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
agg_trans


# aggregated user
path2="C:/Users/JAYAKAVI/New folder/pulse/data/aggregated/user/country/india/state/"
agg_user_state_list=os.listdir(path2)

col1 = {'State': [], 'Year': [], 'Quarter': [], 'User_brand': [],'User_count': [], 'User_percentage': []}

for i in agg_user_state_list:
    cur_s=path2+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)
            
            try:
                for n in m["data"]["usersByDevice"]:
                    brand=n['brand']
                    count=n['count']
                    percentage=n['percentage']*100

                    col1['State'].append(i)
                    col1['Year'].append(j)
                    col1['Quarter'].append("Q"+str(k[0]))
                    col1['User_brand'].append(brand)
                    col1['User_count'].append(count)
                    col1['User_percentage'].append(percentage) 

            except:
                pass     

agg_user=pd.DataFrame(col1)
agg_user['State']=agg_user['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
agg_user['State']=agg_user['State'].str.replace('-',' ')
agg_user['State']=agg_user['State'].str.title()
agg_user['State']=agg_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
agg_user


#map transaction
path3="C:/Users/JAYAKAVI/New folder/pulse/data/map/transaction/hover/country/india/state/"
map_trans_state_list=os.listdir(path3)

col2 = {'State': [], 'Year': [], 'Quarter': [], 'District': [],'trans_count': [], 'trans_amount': []}

for i in map_trans_state_list:
    cur_s=path3+i+"/"
    trans_year_list=os.listdir(cur_s)

    for j in trans_year_list:
        cur_y=cur_s+j+'/'
        trans_year_json=os.listdir(cur_y)

        for k in trans_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)
            for n in m["data"]["hoverDataList"]:
                district=n['name'].split(' district')[0]
                count=n['metric'][0]['count']
                amount=n['metric'][0]['amount']
                
                col2['State'].append(i)
                col2['Year'].append(j)
                col2['Quarter'].append("Q"+str(k[0]))
                col2['District'].append(district)
                col2['trans_count'].append(count)
                col2['trans_amount'].append(amount)

map_trans=pd.DataFrame(col2)
map_trans['State']=map_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
map_trans['State']=map_trans['State'].str.replace('-',' ')
map_trans['State']=map_trans['State'].str.title()
map_trans['State']=map_trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
map_trans


#map user
path4="C:/Users/JAYAKAVI/New folder/pulse/data/map/user/hover/country/india/state/"
map_user_state_list=os.listdir(path4)

col3 = {'State': [], 'Year': [], 'Quarter': [], 'District':[],'registered_user': [],'app_opens': []}

for i in map_user_state_list:
    cur_s=path4+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)
 
           
            for d,n in m['data']['hoverData'].items():
                district=d.split('district')[0]
                registered_user=n['registeredUsers']
                appopens=n['appOpens']

                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quarter'].append('Q'+str(k[0]))
                col3['District'].append(district)
                col3['registered_user'].append(registered_user)
                col3['app_opens'].append( appopens)

map_user=pd.DataFrame(col3)
map_user['State']=map_user['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
map_user['State']=map_user['State'].str.replace('-',' ')
map_user['State']=map_user['State'].str.title()
map_user['State']=map_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
map_user


#top trans (pincodes)
path5="C:/Users/JAYAKAVI/New folder/pulse/data/top/transaction/country/india/state/"
top_trans_state_list=os.listdir(path5)

col4 = {'State': [], 'Year': [], 'Quarter': [], 'pincodes':[],'trans_count': [],'trans_amount': []}

for i in top_trans_state_list:
    cur_s=path5+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)

            for n in m['data']['pincodes']:
                entityname=n['entityName']
                count=n['metric']['count']
                amount=n['metric']['amount']

                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quarter'].append('Q'+str(k[0]))
                col4['pincodes'].append(entityname)
                col4['trans_count'].append(count)
                col4['trans_amount'].append(amount)

top_trans=pd.DataFrame(col4)
top_trans['State']=top_trans['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
top_trans['State']=top_trans['State'].str.replace('-',' ')
top_trans['State']=top_trans['State'].str.title()
top_trans['State']=top_trans['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
top_trans


#top trans (district)
path6="C:/Users/JAYAKAVI/Desktop/phonepe/pulse/data/top/transaction/country/india/state/"
top_trans_state_list = os.listdir(path6)

col6 = {'State': [], 'Year': [], 'Quarter': [], 'District': [],'trans_count': [], 'trans_amount': []}

for i in top_trans_state_list :
    cur_s=path6+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)

        
            for n in m['data']['districts']:
                district=n['entityName']
                count=n['metric']['count']
                amount=n['metric']['amount']

                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quarter'].append("Q"+str(k[0]))
                col6['District'].append(district)
                col6['trans_count'].append(count)
                col6['trans_amount'].append(amount)

top_trans_dis=pd.DataFrame(col6)
top_trans_dis['State']=top_trans_dis['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
top_trans_dis['State']=top_trans_dis['State'].str.replace('-',' ')
top_trans_dis['State']=top_trans_dis['State'].str.title()
top_trans_dis['State']=top_trans_dis['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
top_trans_dis


#top user (district)
path7="C:/Users/JAYAKAVI/Desktop/phonepe/pulse/data/top/user/country/india/state/"
top_user_state_list=os.listdir(path7)
col7={'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Registered_user': []}

for i in top_user_state_list:
    cur_s=path7+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)

            for n in m['data']['districts']:
                district=n['name']
                registereduser=n['registeredUsers']

                col7['State'].append(i)
                col7['Year'].append(j)
                col7['Quarter'].append('Q'+str(k[0]))
                col7['District'].append(district)
                col7['Registered_user'].append(registereduser)

top_user_dis=pd.DataFrame(col7)
top_user_dis['State']=top_user_dis['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
top_user_dis['State']=top_user_dis['State'].str.replace('-',' ')
top_user_dis['State']=top_user_dis['State'].str.title()
top_user_dis['State']=top_user_dis['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
top_user_dis


#top user (pincodes)
path8="C:/Users/JAYAKAVI/Desktop/phonepe/pulse/data/top/user/country/india/state/"
top_user_state_list=os.listdir(path8)
col9={'State': [], 'Year': [], 'Quarter': [], 'pincodes': [], 'Registered_user': []}

for i in top_user_state_list:
    cur_s=path8+i+"/"
    user_year_list=os.listdir(cur_s)

    for j in user_year_list:
        cur_y=cur_s+j+'/'
        user_year_json=os.listdir(cur_y)

        for k in user_year_json:
            cur_k=cur_y+k
            l=open(cur_k,"r")

            m=json.load(l)

            for n in m['data']['pincodes']:
                pincode=n['name']
                registereduser=n['registeredUsers']

                col9['State'].append(i)
                col9['Year'].append(j)
                col9['Quarter'].append('Q'+str(k[0]))
                col9['pincodes'].append(pincode)
                col9['Registered_user'].append(registereduser)

top_user_pin=pd.DataFrame(col9)
top_user_pin['State']=top_user_pin['State'].str.replace('andaman-&-nicobar-islands','Andaman & Nicobar')
top_user_pin['State']=top_user_pin['State'].str.replace('-',' ')
top_user_pin['State']=top_user_pin['State'].str.title()
top_user_pin['State']=top_user_pin['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Dama')
top_user_pin


#converting all dataframe to CSV file
agg_trans.to_csv("aggr_transc_file.csv",index=False)
agg_user.to_csv("aggr_users_file.csv",index=False)
map_trans.to_csv("map_transc_file.csv",index=False)
map_user.to_csv("map_user_file.csv",index=False)
top_trans.to_csv("top_trans_pin_file.csv",index=False)
top_trans_dis.to_csv("top_trans_dis_file.csv",index=False)
top_user_dis.to_csv("top_user_dis_file.csv",index=False)
top_user_pin.to_csv("top_user_pin_file.csv",index=False)


#connecting to My SQL to upload datas
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306'
                )
cur=mydb.cursor(buffered=True)
cur.execute('create database if not exists phonepe')


# create table aggregated transactions
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

agg_trans_table='''create table if not exists phonepe.aggreated_transaction(State varchar(100),
                                                                            Year int,
                                                                            Quarter varchar(50),
                                                                            Transaction_type varchar(100),
                                                                            Transaction_count bigint,
                                                                            Transaction_amount bigint
                                                                            )'''
cur.execute(agg_trans_table)
mydb.commit()


for index,row in agg_trans.iterrows():
    query1='''insert into phonepe.aggreated_transaction values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query1,tuple(row))
    mydb.commit()


# create table aggregated user
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

agg_user_table='''create table if not exists phonepe.aggreated_user(State varchar(100),
                                                                    Year int,
                                                                    Quarter varchar(50),
                                                                    User_brand varchar(100),
                                                                    User_count bigint,
                                                                    User_percentage float
                                                                    )'''
cur.execute(agg_user_table)
mydb.commit()


for index,row in agg_user.iterrows():
    query2='''insert into phonepe.aggreated_user values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query2,tuple(row))
    mydb.commit()

# create table map transactions
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

map_trans_table='''create table if not exists phonepe.map_transaction(State varchar(100),
                                                                            Year int,
                                                                            Quarter varchar(50),
                                                                            District varchar(100),
                                                                            trans_count bigint,
                                                                            trans_amount bigint
                                                                            )'''
cur.execute(map_trans_table)
mydb.commit()


for index,row in map_trans.iterrows():
    query3='''insert into phonepe.map_transaction values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query3,tuple(row))
    mydb.commit()

# create table map user
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

map_user_table='''create table if not exists phonepe.map_user(State varchar(100),
                                                                    Year int,
                                                                    Quarter varchar(50),
                                                                    District varchar(100),
                                                                    registered_user bigint,
                                                                    app_opens bigint
                                                                    )'''
cur.execute(map_user_table)
mydb.commit()


for index,row in map_user.iterrows():
    query4='''insert into phonepe.map_user values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query4,tuple(row))
    mydb.commit()

# create table top transactions district
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

top_trans_dis_table='''create table if not exists phonepe.top_transaction_district(State varchar(100),
                                                                                    Year int,
                                                                                    Quarter varchar(50),
                                                                                    District varchar(100),
                                                                                    trans_count bigint,
                                                                                    trans_amount bigint
                                                                                    )'''
cur.execute(top_trans_dis_table)
mydb.commit()


for index,row in top_trans_dis.iterrows():
    query5='''insert into phonepe.top_transaction_district values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query5,tuple(row))
    mydb.commit()

# create table top transactions pincodes
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

top_trans_pin_table='''create table if not exists phonepe.top_transaction_pincodes(State varchar(100),
                                                                                    Year int,
                                                                                    Quarter varchar(50),
                                                                                    pincodes bigint,
                                                                                    trans_count bigint,
                                                                                    trans_amount bigint
                                                                                    )'''
cur.execute(top_trans_pin_table)
mydb.commit()


for index,row in top_trans.iterrows():
    query6='''insert into phonepe.top_transaction_pincodes values(%s,%s,%s,%s,%s,%s) '''

    cur.execute(query6,tuple(row))
    mydb.commit()

# create table top user district
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

top_user_dis_table='''create table if not exists phonepe.top_user_district(State varchar(100),
                                                                            Year int,
                                                                            Quarter varchar(50),
                                                                            District varchar(100),
                                                                            Registered_user bigint
                                                                            )'''
cur.execute(top_user_dis_table)
mydb.commit()


for index,row in top_user_dis.iterrows():
    query7='''insert into phonepe.top_user_district values(%s,%s,%s,%s,%s) '''

    cur.execute(query7,tuple(row))
    mydb.commit()

# create table top user pincodes
mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306',
                database='phonepe'
                )
cur=mydb.cursor(buffered=True)

top_user_pin_table='''create table if not exists phonepe.top_user_pincodes(State varchar(100),
                                                                                    Year int,
                                                                                    Quarter varchar(50),
                                                                                    pincodes bigint,
                                                                                    Registered_user bigint
                                                                                    )'''
cur.execute(top_user_pin_table)
mydb.commit()


for index,row in top_user_pin.iterrows():
    query8='''insert into phonepe.top_user_pincodes values(%s,%s,%s,%s,%s) '''

    cur.execute(query8,tuple(row))
    mydb.commit()


