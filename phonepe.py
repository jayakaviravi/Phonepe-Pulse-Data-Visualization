
import pandas as pd
import mysql.connector as sql
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


#Creating database in SQL:

mydb=sql.connect(host='127.0.0.1',
                user='root',
                password='test',
                port='3306'
                )
cur=mydb.cursor(buffered=True)
cur.execute('create database if not exists phonepe ')

#Function to get overall state transaction amount

def overall_state_transaction(Year,quarter):
    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select State, sum(Transaction_amount) as transactions,sum(Transaction_count) as count from aggreated_transaction where Year = {Year} and Quarter='{quarter}' group by State order by transactions desc ;")
    table1=cur.fetchall()
    df1=pd.DataFrame(table1,columns=['States','Transaction amount','Transaction count'])
    fig1 = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Transaction amount',
                        title='Overall state Transaction amount'
                        )

    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(title_font_color='violet',title_font=dict(size=22),title_x=0.3)
    st.plotly_chart(fig1,use_container_width=True)  
    st.write(df1)
    

#Function to get overall state transaction count

def overall_state_count(Year,quarter):

    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select State, sum(Transaction_amount) as transactions,sum(Transaction_count) as count from aggreated_transaction where Year = {Year} and Quarter='{quarter}' group by State order by count desc ;")
    table2=cur.fetchall()
    df2=pd.DataFrame(table2,columns=['States','Transaction amount','Transaction count'])
    fig2 = px.choropleth(df2,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='States',
                        color='Transaction count',
                        title='Overall State Transaction count')

    fig2.update_geos(fitbounds="locations", visible=False)
    fig2.update_layout(title_font_color='violet',title_font=dict(size=22),title_x=0.3)
    st.plotly_chart(fig2,use_container_width=True)
    st.write(df2)


#Function to get Payment type with transaction amount

def payment_type_transaction(Year,quarter):

    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select Transaction_type as trans_name, sum(Transaction_amount) as trans_amount from aggreated_transaction where Year = {Year} and Quarter='{quarter}' group by trans_name order by trans_amount desc ;")
    table3=cur.fetchall()
    df3=pd.DataFrame(table3,columns=['Transaction type','Transaction amount'])
    fig3 = px.bar(df3, y='Transaction amount', x='Transaction type',color='Transaction type',orientation='v',text_auto='.3s')
    fig3.update_layout(width=900, height=600)
    st.plotly_chart(fig3,use_container_width=True)
    st.write(df3)


#Function to get Payment type with transaction count

def payment_type_count(Year,quarter):

    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select Transaction_type as trans_name, sum(Transaction_count) as count from aggreated_transaction where Year = {Year} and Quarter='{quarter}' group by trans_name order by count desc ;")
    table4=cur.fetchall()
    df4=pd.DataFrame(table4,columns=['Transaction type','Transaction count'])
    fig4 = px.bar(df4, y='Transaction count', x='Transaction type',color='Transaction type',orientation='v')
    fig4.update_layout(width=800, height=500)    
    st.plotly_chart(fig4,use_container_width=True)
    st.write(df4)      

#Function to get overall States and Districts with transaction

def district_wise_trans(Year,quarter,selected_state):

    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select State,Year,Quarter,District,sum(trans_count) as count,sum(trans_amount) as transaction_amount from map_transaction where Year={Year} and Quarter='{quarter}' and State='{selected_state}' group by State,District,Year,Quarter order by State,District")
    table5=cur.fetchall()
    df5=pd.DataFrame(table5,columns=['States','year','Quarter','District','transaction count','transaction amount'])
    fig5 = px.bar(df5,
                    title=selected_state,
                    x="District",
                    y="transaction count",
                    orientation='v',
                    color='transaction amount',
                    color_continuous_scale=px.colors.sequential.Agsunset
                    )
    fig5.update_layout(width=900, height=500,title_font_color='violet',title_font=dict(size=22),title_x=0.3)
    st.plotly_chart(fig5,use_container_width=True)
    st.write(df5)


#Function to get overall States and Pincodes with transaction


def overall_pincodes_transaction(Year,quarter,selected_state1):

    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()
    cur.execute(f"select State,Year,Quarter,pincodes,sum(trans_count) as count,sum(trans_amount) as transaction_amount from top_transaction_pincodes where Year={Year} and Quarter='{quarter}' and State='{selected_state1}' group by State,pincodes,Year,Quarter order by State,pincodes")
    table5=cur.fetchall()
    df6=pd.DataFrame(table5,columns=['States','year','Quarter','Pincodes','transaction count','transaction amount'])
    fig6 = px.pie(df6, names= 'Pincodes', values='transaction amount',title=selected_state1,color='transaction count',
                       color_discrete_sequence=px.colors.sequential.RdBu)
    fig6.update_layout(title_font_color='violet',title_font=dict(size=22),title_x=0.3)
    st.plotly_chart(fig6,use_container_width=True)    
    st.write(df6)

#Function to get Registered Users

def map_state_user(Year,quarter):
    cur.execute(f"select State,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' group by State order by users desc")
    table1=cur.fetchall()
    df1=pd.DataFrame(table1,columns=["State",'Total registered users','Total appopens'])
    fig1 = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='State',title='Registered Users',
                        color='Total registered users',hover_data=['Total appopens']
                        )

    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(width=900, height=500,title_font_color='violet',title_font=dict(size=22),title_x=0.3)
    st.plotly_chart(fig1,use_container_width=True)    
    st.write(df1)

#Function to get District wise Registered Users
    
def district_wise_user(Year,quarter,selected_state): 
    cur.execute(f"select State,Year,Quarter,District,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' and State='{selected_state}' group by State,District,Year,Quarter order by State,District")
    table2=cur.fetchall()
    df2=pd.DataFrame(table2,columns=["State","Year","Quarter","District",'Total registered users','Total appopens'])
    fig2 = px.bar(df2,title=selected_state,
                        x="District",
                        y="Total registered users",
                        orientation='v',
                        color='Total registered users'
                        )
    fig2.update_layout(width=900, height=500,title_font_color='violet',title_font=dict(size=22),title_x=0.3)    
    st.plotly_chart(fig2,use_container_width=True)    
    st.write(df2)



#setting page configuration
img=Image.open("C:\\Users\\JAYAKAVI\\Downloads\\phonepe.png")
st.set_page_config(page_title="Phonepe Pulse Data Visualization", 
                    page_icon=img, 
                    layout="wide",
                    initial_sidebar_state="expanded")

st.title(':violet[Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly]')

with st.sidebar:
    selected = option_menu(None, ["Application Details","Informations","Top insights","Explore data"], 
                           icons=["house-door-fill","map","bar-chart"],
                           default_index=0,
                           orientation="horizontal",
                           styles={"nav-link": {"font-size": "20px", "text-align": "centre", "margin": "0px", 
                                                "--hover-color": "white"},
                                   "icon": {"font-size": "20px"},
                                   "container" : {"max-width": "3000px"},
                                   "nav-link-selected": {"background-color": "violet"}})
    

if selected=="Application Details":
    
    col1,col2=st.columns([2.5,1.5],gap='small')

    with col1:
        st.subheader(':red[India Best Transaction App]')
        st.markdown('#### PhonePe is a digital wallet and online payment app that allows users to make instant money transfers with UPI. It can also be used to recharge mobile, pay utility bills, and more.')
        st.subheader(':red[Technologies]')
        st.markdown('#### Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly.')
        st.markdown('#### :red[Domain:] Fintech')
   
    with col2:
        st.subheader(':red[Download Phonepe app]')
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        st.subheader(':red[Video about Phonepe]')
        st.video("https://www.youtube.com/watch?v=Yy03rjSUIB8&t=90s")

if selected=='Informations':

    col1,col2=st.columns([3.5,4],gap='medium')

    col1.image(Image.open("C:\\Users\\JAYAKAVI\\Downloads\\pulse-2.png"),width = 400)
    with col2:
        st.subheader(':red[State Insights:]')
        st.markdown('#### The dashboard provides rankings of states based on various metrics.This insight is valuable for benchmarking, competitive analysis, market expansion and optimization strategies.')
        
        
        st.subheader(':red[District and Pincode Insights:]')
        st.markdown("#### Identifying the top districts and pincodes with the highest transaction amounts and count can inform localized marketing and partnership strategies.")

        st.subheader(':red[Transaction Types:]')
        st.markdown('#### Payment type provide valuable information about user preferences, trends, and the overall dynamics of digital transactions.some insights are UPI,Credit/Debit Cards,Wallet Usage,QR Code Payments and P2P (Peer-to-Peer) Transactions')


if selected=='Top insights':
   
    Type = st.selectbox(":red[Type]", ("Transactions", "Users"))
    if Type == "Transactions":
        st.info(
                """
                #### :red[From this menu we can get insights like :]
                - Analyzing transaction amounts ,counts and payment type over time and across states,districts and pincodes can reveal trends in user behavior.
                """,icon="🔍"
                )
        
        mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
        cur=mydb.cursor()

        tab1,tab2,tab3,tab4,tab5=st.tabs([':green[***Transaction amount***]',':green[***Transaction count***]',':green[***Payment type***]',':green[***District***]',':green[***Pincode***]'])
        
        with tab1:

            Year=st.selectbox(":orange[Year]",("Select Year to know overall state transactions",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to know overall state transactions",'Q1','Q2','Q3','Q4'))

            if Year!='Select Year to know overall state transactions' and quarter!='Select quarter to know overall state transactions':
           
                overall_state_transaction(Year,quarter)
        
        with tab2:

            Year=st.selectbox(":orange[Year]",("Select Year to know overall state transactions count",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to know overall state transactions count",'Q1','Q2','Q3','Q4'))

            if Year!='Select Year to know overall state transactions count' and quarter!='Select quarter to know overall state transactions count':
                overall_state_count(Year,quarter)
        
        with tab3:

            col1,col2=st.columns([1,1],gap='medium')

            with col1:
                st.markdown('#### :blue[Payment type vs Transaction Amount]')
                Year=st.selectbox(":orange[Year]",("Select Year to know  transactions type vs transaction amount",2018,2019,2020,2021,2022,2023))
                quarter=st.selectbox(':orange[quarter]',("Select quarter to know transactions type vs transaction amount",'Q1','Q2','Q3','Q4'))
                
                if Year!='Select Year to know  transactions type vs transaction amount' and quarter!='Select quarter to know transactions type vs transaction amount':
                    payment_type_transaction(Year,quarter)
            
            with col2:
                st.markdown('#### :blue[Payment type vs Transaction Count]')
                Year=st.selectbox(":orange[Year]",("Select Year to know  transactions type vs transaction count",2018,2019,2020,2021,2022,2023))
                quarter=st.selectbox(':orange[quarter]',("Select quarter to know transactions type vs transaction count",'Q1','Q2','Q3','Q4'))

                if Year!='Select Year to know  transactions type vs transaction count' and quarter!='Select quarter to know transactions type vs transaction count':
                    payment_type_count(Year,quarter)


        with tab4:
            Year=st.selectbox(":orange[Year]",("Select Year to know  district wise transaction",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to know district wise transaction",'Q1','Q2','Q3','Q4'))
            selected_state=st.selectbox(":orange[select the state to know district wise transaction]",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                                                        'Dadra and Nagar Haveli and Dama', 'Delhi', 'Goa', 'Gujarat',
                                                                                        'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                                                                        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                                                                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                                                                        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                                                                        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                                                        'Uttarakhand', 'West Bengal'),index=None,placeholder="Select state")
        
            
            if Year!="Select Year to know  district wise transaction" and quarter!="Select quarter to district wise transaction" and selected_state!="select the state to district wise transaction":
                district_wise_trans(Year,quarter,selected_state)
        
        with tab5:

            Year=st.selectbox(":orange[Year]",("Select Year to know  pincode wise transaction",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to pincode wise transaction",'Q1','Q2','Q3','Q4'))
            selected_state1=st.selectbox(":orange[select the state to pincode wise transaction]",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                                                        'Dadra and Nagar Haveli and Dama', 'Delhi', 'Goa', 'Gujarat',
                                                                                        'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                                                                        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                                                                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                                                                        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                                                                        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                                                        'Uttarakhand', 'West Bengal'),index=None,placeholder="Select state")
        
            
            if Year!="Select Year to know  pincode wise transaction" and quarter!="Select quarter to pincode wise transaction" and selected_state!="select the state to pincode wise transaction":
                 overall_pincodes_transaction(Year,quarter,selected_state1)
                

           
    if Type == "Users":

        st.info(
                """
                #### :red[From this menu we can get insights like :]
                - By visualizing metrics such as the total number of registered users and app opens, it provides insights into user engagement.
                - Understanding which states have the highest user activity can help in targeted marketing and user acquisition efforts.
                """,icon="🔍"
                )
            
        mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
        cur=mydb.cursor()

        tab1,tab2=st.tabs([':green[***State***]',':green[***District***]'])

        with tab1:

            Year=st.selectbox(":orange[Year]",("Select Year to know overall state registered users",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to know overall state registered users",'Q1','Q2','Q3','Q4'))
            
            if Year!="Select Year to know overall state registered users" and quarter!="Select quarter to know overall state registered users": 
                map_state_user(Year,quarter)

        with tab2:
            Year=st.selectbox(":orange[Year]",("Select Year to know district wise registered users",2018,2019,2020,2021,2022,2023))
            quarter=st.selectbox(':orange[quarter]',("Select quarter to know district wise registered users",'Q1','Q2','Q3','Q4'))
            selected_state=st.selectbox(":orange[select the state to know district wise registered users]",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                                                        'Dadra and Nagar Haveli and Dama', 'Delhi', 'Goa', 'Gujarat',
                                                                                        'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand',
                                                                                        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                                                                        'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                                                                        'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim',
                                                                                        'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                                                        'Uttarakhand', 'West Bengal'),index=None,placeholder="Select state")
        
            
            if Year!="Select Year to know district wise registered users" and quarter!="Select quarter to know district wise registered users" and selected_state!="select the state to know district wise registered users": 
                district_wise_user(Year,quarter,selected_state)


if selected=="Explore data":
    
    mydb=sql.connect(host='127.0.0.1',
                        user='root',
                        password='test',
                        port='3306',
                        database='phonepe'
                        )
    cur=mydb.cursor()

    st.info(
                """
                #### :red[From this menu we can get insights like :]
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )

    select=st.selectbox(":red[Select the facts]",('1.Top 10 States and Districts with Highest Transactions',
                                            '2.Top 10 States and Districts with Lowest Transactions',
                                            '3.Top 10 Districts with Highest Transaction count',
                                            '4.Top 10 Districts  with lowest Transactions count',
                                            '5.Top 10 pincodes with highest transactions',
                                            '6.Top 10 pincodes with highest Phonepe users',
                                            '7.Top Brands of mobile used',
                                            '8.Top 10 States with Highest Phonepe Users',
                                            '9.Top 10 States with Lowest Phonepe users',
                                            '10.Top 10 Districts with Highest phonepe users',
                                            '11.Top 10 Districts with Lowest phonepe users'),index=None,placeholder="Select the facts to know about data")
    
    if select=='1.Top 10 States and Districts with Highest Transactions':
        
        Year=st.selectbox(":orange[Year]",("Select Year for Highest transaction in states and districts",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest transaction in states and districts",'Q1','Q2','Q3','Q4'))

        
        if Year!='Select Year for Highest transaction in states and districts' and 'Select quarter for Highest transaction in states and districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select State,District,sum(trans_amount) as transaction,sum(trans_count) as count from map_transaction where Year={Year} and Quarter='{quarter}' group by State,District order by transaction desc limit 10")
                table1=cur.fetchall()
                df1=pd.DataFrame(table1,columns=['State',"District",'Transaction amount','Transaction count'])
                st.write(df1)
            
            with col2:
                fig1 = px.sunburst(df1, path=['State', 'District'], values='Transaction amount',title="States and Districts with Highest Transactions",
                        color_discrete_sequence=px.colors.sequential.Plasma)
                fig1.update_layout(title_font_color='red',title_font=dict(size=22))
                st.plotly_chart(fig1,use_container_width=True)
    
    elif select=='2.Top 10 States and Districts with Lowest Transactions':
        
        Year=st.selectbox(":orange[Year]",("Select Year for Lowest transaction in states and districts",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Lowest transaction in states and districts",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Lowest transaction in states and districts' and 'Select quarter for Lowest transaction in states and districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select State,District,sum(trans_amount) as transaction,sum(trans_count) as count from map_transaction where Year={Year} and Quarter='{quarter}' group by State,District order by transaction asc limit 10")
                table2=cur.fetchall()
                df2=pd.DataFrame(table2,columns=['State',"District",'Transaction amount','Transaction count'])
                st.write(df2)
            
            with col2:
                fig2 = px.sunburst(df2, path=['State', 'District'], values='Transaction amount',title="States and Districts with Lowest Transactions",
                       color_discrete_sequence=px.colors.sequential.YlOrRd_r)
                fig2.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig2,use_container_width=True)
    
    elif select=='3.Top 10 Districts with Highest Transaction count':

        Year=st.selectbox(":orange[Year]",("Select Year for Highest transaction count in districts",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest transaction count in  districts",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Highest transaction count in districts' and 'Select quarter for Highest transaction count in  districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select District,sum(trans_amount) as transaction,sum(trans_count) as count from map_transaction where Year={Year} and Quarter='{quarter}' group by District order by count desc limit 10")
                table3=cur.fetchall()
                df3=pd.DataFrame(table3,columns=["District",'Transaction amount','Transaction count'])
                st.write(df3)
            
            with col2:
                fig3 = px.pie(df3, names='District',values='Transaction count', hole=0.5,color_discrete_sequence=px.colors.sequential.Emrld_r,title="Districts with Highest Transaction count")
                fig3.update_traces(text=df3['District'], textinfo='percent+label',texttemplate='%{percent:.2%}', textposition='outside')
                fig3.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig3,use_container_width=True)


    elif select=='4.Top 10 Districts  with lowest Transactions count':

        Year=st.selectbox(":orange[Year]",("Select Year for Lowest transaction count in districts",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Lowest transaction count in  districts",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Lowest transaction count in districts' and 'Select quarter for Lowest transaction count in  districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select District,sum(trans_amount) as transaction,sum(trans_count) as count from map_transaction where Year={Year} and Quarter='{quarter}' group by District order by count asc limit 10")
                table4=cur.fetchall()
                df4=pd.DataFrame(table4,columns=["District",'Transaction amount','Transaction count'])
                st.write(df4)
            
            with col2:
                fig4 = px.bar(df4, y='Transaction count', x='District',orientation='v',color='District',hover_data=['District','Transaction amount','Transaction count'],title="Districts  with lowest Transactions count")
                fig4.update_layout(width=900, height=500,title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig4,use_container_width=True)
    
    elif select=='5.Top 10 pincodes with highest transactions':

        Year=st.selectbox(":orange[Year]",("Select Year for Highest transaction in pincodes",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest transaction in pincodes",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Highest transaction in pincodes' and 'Select quarter for Highest transaction in pincodes':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select pincodes,sum(trans_amount) as Trans_amount,sum(trans_count) as Trans_count from top_transaction_pincodes where Year={Year} and Quarter='{quarter}'  group by pincodes order by Trans_amount desc limit 10 ")
                table5=cur.fetchall()
                df5=pd.DataFrame(table5,columns=['Pincodes','Transaction amount','Transaction count'])
                st.write(df5)
            
            with col2:
                fig5 = px.pie(df5, names='Pincodes',values='Transaction count', hole=0.4,color_discrete_sequence=px.colors.sequential.Sunsetdark_r,title="pincodes with highest transactions")
                fig5.update_traces(text=df5['Pincodes'], textinfo='percent+label',texttemplate='%{percent:.2%}', textposition='outside')
                fig5.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig5,use_container_width=True)


    elif select=='6.Top 10 pincodes with highest Phonepe users':

        Year=st.selectbox(":orange[Year]",("Select Year for Highest phonepe users in pincodes",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest phonepe users in pincodes",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Highest phonepe users in pincodes' and 'Select quarter for Highest phonepe users in pincodes':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select pincodes,sum(Registered_user) as users  from top_user_pincodes where Year={Year} and Quarter='{quarter}' group by pincodes order by users desc limit 10 ")
                table6=cur.fetchall()
                df6=pd.DataFrame(table6,columns=['Pincodes','Total registered users'])
                st.write(df6)
            
            with col2:
                fig6 = px.pie(df6, names='Pincodes',values='Total registered users', hole=0.4,color_discrete_sequence=px.colors.sequential.Viridis_r,title="pincodes with highest Phonepe users")
                fig6.update_traces(text=df6['Pincodes'], textinfo='percent+label',texttemplate='%{percent:.2%}', textposition='outside')
                fig6.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig6,use_container_width=True)

    elif select=='7.Top Brands of mobile used':

        Year=st.selectbox(":orange[Year]",("Select Year for Top brands of mobile used",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter  for Top brands of mobile used",'Q1','Q2','Q3','Q4'))

        if (Year == 2022 or Year==2023) and (quarter=='Q2'or quarter=='Q3' or quarter=='Q4') :
                st.markdown("#### Sorry No Data to Display ")

        elif Year!='Select Year for Top brands of mobile used' and 'Select quarter  for Top brands of mobile used':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select User_brand,sum(User_count) as count,avg(User_percentage) as average_percentange from phonepe.aggreated_user where Year={Year} and Quarter='{quarter}' group by User_brand order by count desc limit 10")
                table7=cur.fetchall()
                df7=pd.DataFrame(table7,columns=["Brand","count of users","avg User percentage"])
                st.write(df7)
            
            with col2:
                fig7 = px.bar(df7, y='Brand', x='count of users',orientation='h',text_auto='.2s',hover_data=['Brand','count of users','avg User percentage'],title="Top Brands of mobile used")
                fig7.update_traces(textfont_size=12,marker_color=px.colors.diverging.balance_r,textposition="outside")
                fig7.update_layout(width=900, height=500,title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig7,use_container_width=True)

    elif select=='8.Top 10 States with Highest Phonepe Users':

        Year=st.selectbox(":orange[Year]",("Select Year for Highest phonepe users in state",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest phonepe users in state",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Highest phonepe users in state' and 'Select quarter for Highest phonepe users in state':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select State,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' group by State order by users desc limit 10")
                table8=cur.fetchall()
                df8=pd.DataFrame(table8,columns=["State",'Total registered users','Total appopens'])
                st.write(df8)
            
            with col2:
                fig8 = px.bar(df8, y='Total registered users', x='State',orientation='v',text_auto='.2s',hover_data=["State",'Total registered users','Total appopens'],title="States with Highest Phonepe Users ")
                fig8.update_traces(textfont_size=12,marker_color=px.colors.diverging.RdYlBu_r)
                fig8.update_layout(width=900, height=500,title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig8,use_container_width=True)
    
    elif select=='9.Top 10 States with Lowest Phonepe users':

        Year=st.selectbox(":orange[Year]",("Select Year for Lowest phonepe users in state",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Lowest phonepe users in state",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Lowest phonepe users in state' and 'Select quarter for Lowest phonepe users in state':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select State,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' group by State order by users asc limit 10")
                table9=cur.fetchall()
                df9=pd.DataFrame(table9,columns=["State",'Total registered users','Total appopens'])
                st.write(df9)
            
            with col2:
                fig9 = px.pie(df9, names='State',values='Total registered users', hole=0.4,color_discrete_sequence=px.colors.sequential.Pinkyl_r,title="States with Lowest Phonepe users")
                fig9.update_traces(text=df9['Total registered users'], textinfo='percent+label',texttemplate='%{percent:.2%}', textposition='outside')
                fig9.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig9,use_container_width=True)
    
    elif select=='10.Top 10 Districts with Highest phonepe users':

        Year=st.selectbox(":orange[Year]",("Select Year for Highest phonepe users in Districts",2018,2019,2020,2021,2022,2023))
        quarter=st.selectbox(':orange[quarter]',("Select quarter for Highest phonepe users in Districts",'Q1','Q2','Q3','Q4'))

        if Year!='Select Year for Highest phonepe users in Districts' and 'Select quarter for Highest phonepe users in Districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select District,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' group by District order by users desc limit 10")
                table10=cur.fetchall()
                df10=pd.DataFrame(table10,columns=["District",'Total registered users','Total appopens'])
                st.write(df10)
            
            with col2:
                fig10 = px.pie(df10, names= 'District', values='Total registered users',title="Top 10 Districts with Highest phonepe users",
                       color_discrete_sequence=px.colors.sequential.RdBu,hover_data=['Total appopens'])
                fig10.update_layout(title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig10,use_container_width=True)
    
    elif select=='11.Top 10 Districts with Lowest phonepe users':

         Year=st.selectbox(":orange[Year]",("Select Year for Lowest phonepe users in Districts",2018,2019,2020,2021,2022,2023))
         quarter=st.selectbox(':orange[quarter]',("Select quarter for Lowest phonepe users in Districts",'Q1','Q2','Q3','Q4'))

         if Year!='Select Year for Lowest phonepe users in Districts' and 'Select quarter for Lowest phonepe users in Districts':
            
            col1,col2=st.columns(2)

            with col1:
                cur.execute(f"select District,sum(registered_user) as users ,sum(app_opens) as total_opens from map_user where Year={Year} and Quarter='{quarter}' group by District order by users asc limit 10")
                table11=cur.fetchall()
                df11=pd.DataFrame(table11,columns=["District",'Total registered users','Total appopens'])
                st.write(df11)
            
            with col2:
                fig11 = px.bar(df11, y='Total registered users', x='District',orientation='v',text_auto='.3s', title="Districts with Lowest phonepe users")
                fig11.update_traces(textfont_size=12,marker_color=px.colors.diverging.RdYlGn)
                fig11.update_layout(width=900, height=500,title_font_color='red',title_font=dict(size=22),title_x=0.1)
                st.plotly_chart(fig11,use_container_width=True)

