#IMPORT LIBRAIRIES
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import streamlit as st
import plotly.graph_objs as go
import pydeck as pdk



#IMPORT DATA AND CLEAN
data = '/Users/perrine/Desktop/1potentiels-enr-2050.csv'
df = pd.read_csv(data, delimiter = ';')
df.head()
df.describe()
df2=df.drop(['code_insee_region', 'geo_shape_departement', 'lat', 'lon'], axis = 1)
df.info()
df1 = df.drop(columns=['code_departement', 'code_insee_region', 'geo_shape_departement', 'lat', 'lon'])
df3 = df1.sum(axis = 0)
df4 =df1.append({'departement' : 'FRANCE', 'cimse' : 51355, 'residus_cultures' : 31452, 'dejections_elevage' : 26974, 'herbe' : 12910, 'residus_iaa' : 5122, 'bio_dechets' : 10329, 'algues' : 13999, 'potentiel_total_production_methane' : 152135, 'potentiel_bois_energie' : 232653, 'potentiel_electricite_power_to_gas' : 206616, 'energie_recuperation_csr' : 19800, 'energie_recuperation_h2_fatal' : 4356}, ignore_index=True)



#SIDE BAR :
with st.sidebar: 
    st.image('/Users/perrine/Documents/image.png')
    st.caption(" ")
    
choice = st.sidebar.selectbox(
        'Green gas potential in France',
        ('Introduction', 'Analysis of France', 'French Department Analysis', 'About')
)
with st.sidebar: 
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    st.caption("Keys words : green gas, France, forecast, 2050, raw material")
    

#PAGE INTRODUCTION
if choice == 'Introduction' :
    st.title('What gas resources do we have in France ?')
    st.caption("The purpose of these analyzes is to identify the resources available for the production of green gas in France by department. Several primary resources are analyzed :") 
    st.caption("- the potential for methane production with CIMSE (intermediate multi-environmental service crops), crop residues, livestock manure, grasses, residues from agro-food industries (IAA), bio-waste and algae, in GWh HCV;")
    st.caption("- the wood energy potential - in GWh PCI;")
    st.caption("- the potential for recovered energy: Solid fuels from Recovery (CSR) and Fatal Hydrogen (H2) - in GWh PCI;")
    st.caption("- the potential for electricity production by Power-to-Gas, in GWh elec.")
    st.caption(" ")
    st.caption(" ")
    st.caption(" ")
    #INDICATORS
    st.subheader("Informations data sources")
    col1, col2, col3 = st.columns(3)
    col1.metric("Origin of the data set", "data.gouv", "ODRE : Open Data Réseaux Energies")
    col2.metric("Prediction date of forecast", "2050")
    col3.metric("Localisation", "France")
    if st.button('See database'):
     df
    else:
     st.write(' ')


#PAGE FRANCE ANALYSIS
if choice == 'Analysis of France' :
    st.title("Analysis of France")
    status1 = st.radio("Choose one: ", ('There is not my country 🌍', 'DROM-COM', 'France'))
    if (status1 == 'France'): 
        st.success("You selected France") 
        if st.button('See analysis'):
            st.caption(" ")
            st.caption(" ")
            st.caption(" ")
            st.caption(" ")
            #GRAPH BARRE
            st.subheader('Energy production potential in France')
            st.write('In this analysis, we will focus on the total production of green gas in France. First, the graph below shows the part of potential electricity power to gas, energy wood potential, and the methan production potential.')
            potentiels = ['Potential electricity power to gas', 'Energy wood potential', 'Methan production potential']
            energy = [206616, 232653, 152135]
            fig = go.Figure(data=[go.Bar(x=potentiels, y=energy)])
            fig.update_layout(
                xaxis = dict(
                    tickangle = 0,
                    title_text = "Type of potential",
                    title_standoff = 25),
                yaxis = dict(
                    title_text = "Energy potential",
                    title_standoff = 25),
                title ='Energy production potential in France')
            st.plotly_chart(fig, use_container_width=True)
            

            col1, col2= st.columns(2)
            st.caption(" ")
            st.caption(" ")
            st.subheader('Detailed view of methane production potential')
            st.caption('We can now look in more detail at the production of methane in France. The graph below allows us to observe the origin of the material allowing the production of gas.')
            col1, col2= st.columns(2)
            #PIE CHART
            with col1 :
                st.caption(" ")
                st.caption(" ")
                st.caption(" ")
                st.caption(" ")
                labels = 'Cisme', 'residus_cultures', 'déjections élevage', 'herbe', 'résidus iaa', 'biodéchets', 'algues'
                sizes = [51355, 31452, 26974, 12910, 5122, 10329, 13999]
                explode = (0, 0, 0, 0, 0, 0, 0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')
                st.pyplot(fig1)  
            with col2:
                st.caption(" ")
                st.caption(" ") 
                st.caption('- cisme : crops used for methane production (=cive : wheat, barley, beet)')
                st.caption('- algues [algae]')
                st.caption('- biodéchets [bio-waste] : food waste and other biodegradable natural waste')
                st.caption('- résidus iaa : food mud (meat, fish, fruits, vegetables…)')
                st.caption('- herbe [grass]')
                st.caption('- déjections élevage [livestock manure] : comes from cattle')
                st.caption('- résidus cultures [crop residues] : part of the crop not harvested')
            st.caption(" ")
            st.caption(" ")
            st.subheader('Origin of the material allowing the production of gas')
            st.caption(" ")
            st.caption(" ") 
            # CARTE
            c= []
            for L,l in zip(df.lon,df.lat):
                c.append([L,l])
            df["coordinates"] = c
            
            layer = pdk.Layer(
                "ScatterplotLayer",
                df,
                pickable=True,
                opacity=0.5,
                stroked=True,
                filled=True,
                radius_scale=12,
                radius_min_pixels=5,
                radius_max_pixels=200,
                line_width_min_pixels=0.3,
                get_position="coordinates",
                get_radius="potentiel_total_production_methane",
                get_fill_color=[255, 500, 0],
                get_line_color=[0, 0, 0],
            )
            
            view_state = pdk.ViewState(latitude=46, longitude=2, zoom=4, bearing=0, pitch=0)
            r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "Département: {departement}\n Potentiel: {potentiel_total_production_methane}"})
            st.pydeck_chart(r)
            st.caption(" ")
            st.caption("We can see that department of Pas-de-Calais, Cotes-d'Armor and Ile-et-Vilaine are the most important localisation of material allowing the production of gas. The potential production of gas is arount 4000 GWh HCV. Localisation near Paris have the less ressources for methane production.")
            
    if (status1== 'There is not my country 🌍') :
        st.error("Not yet available")
    if (status1== 'DROM-COM') :
        st.warning("It's coming soon") 


#PAGE DEPARTMENT
if choice == 'French Department Analysis' :
    st.title("French Department Analysis")
    data = list()
    for i in df1['departement']:
        data.append(i)
    st.caption(" ")
    
    selectbox = st.selectbox(
        "Choose a department :",
        [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27], data[28], data[29], data[30], data[31], data[32], data[33], data[34], data[35], data[36], data[37], data[38], data[39], data[40], data[41], data[42], data[43], data[44], data[45], data[46], data[47], data[48], data[49], data[50], data[51], data[52], data[53], data[54], data[55], data[56], data[57], data[58], data[59], data[60], data[61], data[62], data[63], data[64], data[65], data[66], data[67], data[68], data[69], data[70], data[71], data[72], data[73], data[74], data[75], data[76], data[77], data[78], data[79], data[80], data[81], data[82], data[83], data[84], data[85], data[86], data[87], data[88], data[89], data[90], data[91], data[92], data[93]]
)
     
    if selectbox:
        df2=df1[df1['departement']==selectbox]
        df2
        st.caption(" ")
        st.caption(" ")
        st.caption(" ")
        st.caption(" ")
        st.subheader('Detailed view of methane production potential')
        st.caption('Here is the detail of the raw material used for the production of methane for the chosen region : ')
        df2=df2.drop(columns=['departement', 'potentiel_bois_energie', 'potentiel_electricite_power_to_gas', 'energie_recuperation_csr', 'energie_recuperation_h2_fatal', 'potentiel_total_production_methane'])
        df2=df2.melt(var_name='raw material', value_name='potential')
        st.table(df2)

        title ='Part of raw material for this department'
        fig = px.pie(df2, values='potential', names='raw material', title='Detailed view of methane production potential')
        fig
        st.caption('*** cisme : crops used for methane production (=cive : wheat, barley, beet) / algues [algae] / biodéchets [bio-waste] : food waste and other biodegradable natural waste / résidus iaa : food mud (meat, fish, fruits, vegetables…) / herbe [grass] / déjections élevage [livestock manure] : comes from cattle / résidus cultures [crop residues] : part of the crop not harvested')
        
        
#PAGE ABOUT
if choice == 'About' :
    st.title('About')
    st.caption(" ")
    st.subheader('Thank you for your attention !')
    col1, col2= st.columns(2)
    with col1 :
        st.caption('Im Perrine Delabie and you can follow me on : ')
        if st.button('Github'):
            st.caption('https://github.com/pdelabie')
        if st.button('Linkedin'):
            st.caption('www.linkedin.com/in/perrine-delabie')
    with col2 :
        st.caption('Please share me your feelings about this topic ! You can send me a message with this form : ')
        contact_form_2 = """
                  <div class="container contact-form">
                      <form action="https://formsubmit.co/exemple@hotmail.com" method="POST">
                          <div class="row">
                              <div class="col-md-6">
                                  <div class="form-group">
                                      <input type="text" name="name" class="form-control" placeholder="Your Name *" required>
                                  </div>
                                  <div class="form-group">
                                      <input type="email" name="email" class="form-control" placeholder="Your Email *" required>
                                  </div>
                              <div class="form-group">
                                <input type="text" name="Phone number" class="form-control" placeholder="Your Phone Number *" required>
                            </div>
                              </div>
                              <div class="col-md-6">
                                  <div class="form-group">
                                      <textarea name="Message" class="form-control-message" placeholder="Your Message *" style="width: 330px; height: 220px;"></textarea>
                                  </div>
                                  <div class="form-group">
                                      <button type="submit" class="btnContact">Send Message</button>
                                  </div>
                              </div>
                          </div>
                      </form>
            </div> """
        st.markdown(contact_form_2, unsafe_allow_html=True)

