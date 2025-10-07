import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import constants
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Tableau Périodique par Date de Découverte",
    page_icon="🕰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        background: linear-gradient(45deg, #8B4513, #D2691E, #CD853F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .section-header {
        color: #8B4513;
        border-bottom: 2px solid #D2691E;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        font-weight: bold;
    }
    .epoch-antique { 
        background-color: #F5DEB3; 
        border-left: 5px solid #8B4513; 
        color: #333;
    }
    .epoch-moyenage { 
        background-color: #DEB887; 
        border-left: 5px solid #A0522D; 
        color: #333;
    }
    .epoch-renaissance { 
        background-color: #F4A460; 
        border-left: 5px solid #D2691E; 
        color: #333;
    }
    .epoch-revolution { 
        background-color: #CD853F; 
        border-left: 5px solid #8B4513; 
        color: white;
    }
    .epoch-spectro { 
        background-color: #D2691E; 
        border-left: 5px solid #A52A2A; 
        color: white;
    }
    .epoch-moderne { 
        background-color: #A0522D; 
        border-left: 5px solid #8B0000; 
        color: white;
    }
    .discovery-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border: 1px solid #ddd;
        color: #333333;
    }
    .rgb-spectrum {
        height: 20px;
        border-radius: 10px;
        margin: 5px 0;
        border: 1px solid #ccc;
    }
    .timeline-period {
        padding: 0.5rem;
        border-radius: 5px;
        text-align: center;
        margin: 0.2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class HistoricalPeriodicTableDashboard:
    def __init__(self):
        self.elements_data = self.define_elements_with_discovery_dates()
        self.epochs_data = self.define_historical_epochs()
        self.spectral_data = self.define_spectral_rgb_data()
        
    def define_historical_epochs(self):
        """Définit les périodes historiques de découverte"""
        return [
            {
                'nom': 'Antiquité', 'periode': 'Avant 500', 'couleur': '#F5DEB3',
                'description': 'Éléments connus depuis l\'antiquité',
                'elements': ['C', 'S', 'Fe', 'Cu', 'Ag', 'Sn', 'Au', 'Hg', 'Pb']
            },
            {
                'nom': 'Moyen-Âge', 'periode': '500-1500', 'couleur': '#DEB887',
                'description': 'Éléments découverts au Moyen-Âge',
                'elements': ['As', 'Sb', 'Bi', 'Zn']
            },
            {
                'nom': 'Renaissance', 'periode': '1500-1700', 'couleur': '#F4A460',
                'description': 'Découvertes de la Renaissance',
                'elements': ['P', 'Co', 'Ni', 'Pt']
            },
            {
                'nom': 'Révolution Chimique', 'periode': '1700-1800', 'couleur': '#CD853F',
                'description': 'Période de la révolution chimique',
                'elements': ['H', 'N', 'O', 'Cl', 'Mn', 'Mo', 'Te', 'Cr', 'W', 'U', 'Ti', 'Be']
            },
            {
                'nom': 'Ère Spectroscopique', 'periode': '1800-1900', 'couleur': '#D2691E',
                'description': 'Découvertes par spectroscopie',
                'elements': ['Li', 'Na', 'K', 'Rb', 'Cs', 'Ca', 'Sr', 'Ba', 'B', 'Al', 'Si', 'Se', 'Br', 'I', 'He', 'Ne', 'Ar', 'Kr', 'Xe']
            },
            {
                'nom': 'Période Moderne', 'periode': '1900-Aujourd\'hui', 'couleur': '#A0522D',
                'description': 'Éléments découverts au 20ème siècle',
                'elements': ['Ra', 'Rn', 'Fr', 'Tc', 'Pm', 'Tous les actinides']
            }
        ]
    
    def define_elements_with_discovery_dates(self):
        """Définit les éléments avec leurs dates de découverte"""
        return [
            # Éléments antiques
            {'symbole': 'C', 'nom': 'Carbone', 'date_decouverte': -25000, 'decouvreur': 'Préhistoire', 'periode_epoch': 'Antiquité'},
            {'symbole': 'S', 'nom': 'Soufre', 'date_decouverte': -2000, 'decouvreur': 'Chinois anciens', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Fe', 'nom': 'Fer', 'date_decouverte': -1500, 'decouvreur': 'Hittites', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Cu', 'nom': 'Cuivre', 'date_decouverte': -9000, 'decouvreur': 'Moyen-Orient', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Ag', 'nom': 'Argent', 'date_decouverte': -3000, 'decouvreur': 'Mésopotamiens', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Sn', 'nom': 'Étain', 'date_decouverte': -2000, 'decouvreur': 'Civilisations anciennes', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Au', 'nom': 'Or', 'date_decouverte': -6000, 'decouvreur': 'Égyptiens', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Hg', 'nom': 'Mercure', 'date_decouverte': -1500, 'decouvreur': 'Chinois/Égyptiens', 'periode_epoch': 'Antiquité'},
            {'symbole': 'Pb', 'nom': 'Plomb', 'date_decouverte': -3000, 'decouvreur': 'Mésopotamiens', 'periode_epoch': 'Antiquité'},
            
            # Moyen-Âge
            {'symbole': 'As', 'nom': 'Arsenic', 'date_decouverte': 1250, 'decouvreur': 'Albert le Grand', 'periode_epoch': 'Moyen-Âge'},
            {'symbole': 'Sb', 'nom': 'Antimoine', 'date_decouverte': 800, 'decouvreur': 'Jâbir ibn Hayyân', 'periode_epoch': 'Moyen-Âge'},
            {'symbole': 'Bi', 'nom': 'Bismuth', 'date_decouverte': 1400, 'decouvreur': 'Inconnu', 'periode_epoch': 'Moyen-Âge'},
            {'symbole': 'Zn', 'nom': 'Zinc', 'date_decouverte': 1000, 'decouvreur': 'Indiens', 'periode_epoch': 'Moyen-Âge'},
            
            # Renaissance
            {'symbole': 'P', 'nom': 'Phosphore', 'date_decouverte': 1669, 'decouvreur': 'H. Brand', 'periode_epoch': 'Renaissance'},
            {'symbole': 'Co', 'nom': 'Cobalt', 'date_decouverte': 1735, 'decouvreur': 'G. Brandt', 'periode_epoch': 'Renaissance'},
            {'symbole': 'Ni', 'nom': 'Nickel', 'date_decouverte': 1751, 'decouvreur': 'A. F. Cronstedt', 'periode_epoch': 'Renaissance'},
            {'symbole': 'Pt', 'nom': 'Platine', 'date_decouverte': 1557, 'decouvreur': 'J. C. Scaliger', 'periode_epoch': 'Renaissance'},
            
            # Révolution Chimique
            {'symbole': 'H', 'nom': 'Hydrogène', 'date_decouverte': 1766, 'decouvreur': 'H. Cavendish', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'N', 'nom': 'Azote', 'date_decouverte': 1772, 'decouvreur': 'D. Rutherford', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'O', 'nom': 'Oxygène', 'date_decouverte': 1774, 'decouvreur': 'J. Priestley', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'Cl', 'nom': 'Chlore', 'date_decouverte': 1774, 'decouvreur': 'C. W. Scheele', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'Mn', 'nom': 'Manganèse', 'date_decouverte': 1774, 'decouvreur': 'J. G. Gahn', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'Cr', 'nom': 'Chrome', 'date_decouverte': 1797, 'decouvreur': 'L. N. Vauquelin', 'periode_epoch': 'Révolution Chimique'},
            {'symbole': 'U', 'nom': 'Uranium', 'date_decouverte': 1789, 'decouvreur': 'M. H. Klaproth', 'periode_epoch': 'Révolution Chimique'},
            
            # Ère Spectroscopique
            {'symbole': 'Li', 'nom': 'Lithium', 'date_decouverte': 1817, 'decouvreur': 'J. A. Arfwedson', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Na', 'nom': 'Sodium', 'date_decouverte': 1807, 'decouvreur': 'H. Davy', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'K', 'nom': 'Potassium', 'date_decouverte': 1807, 'decouvreur': 'H. Davy', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Rb', 'nom': 'Rubidium', 'date_decouverte': 1861, 'decouvreur': 'R. Bunsen, G. Kirchhoff', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Cs', 'nom': 'Césium', 'date_decouverte': 1860, 'decouvreur': 'R. Bunsen, G. Kirchhoff', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Ca', 'nom': 'Calcium', 'date_decouverte': 1808, 'decouvreur': 'H. Davy', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Sr', 'nom': 'Strontium', 'date_decouverte': 1790, 'decouvreur': 'A. Crawford', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Ba', 'nom': 'Baryum', 'date_decouverte': 1808, 'decouvreur': 'H. Davy', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'He', 'nom': 'Hélium', 'date_decouverte': 1868, 'decouvreur': 'P. Janssen, J. N. Lockyer', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Ne', 'nom': 'Néon', 'date_decouverte': 1898, 'decouvreur': 'W. Ramsay, M. Travers', 'periode_epoch': 'Ère Spectroscopique'},
            {'symbole': 'Ar', 'nom': 'Argon', 'date_decouverte': 1894, 'decouvreur': 'Lord Rayleigh, W. Ramsay', 'periode_epoch': 'Ère Spectroscopique'},
            
            # Période Moderne
            {'symbole': 'Ra', 'nom': 'Radium', 'date_decouverte': 1898, 'decouvreur': 'P. et M. Curie', 'periode_epoch': 'Période Moderne'},
            {'symbole': 'Rn', 'nom': 'Radon', 'date_decouverte': 1900, 'decouvreur': 'F. E. Dorn', 'periode_epoch': 'Période Moderne'},
            {'symbole': 'Fr', 'nom': 'Francium', 'date_decouverte': 1939, 'decouvreur': 'M. Perey', 'periode_epoch': 'Période Moderne'},
            {'symbole': 'Tc', 'nom': 'Technétium', 'date_decouverte': 1937, 'decouvreur': 'C. Perrier, E. Segrè', 'periode_epoch': 'Période Moderne'}
        ]
    
    def define_spectral_rgb_data(self):
        """Définit les données spectrales RGB pour chaque élément"""
        return {
            # Spectres rouges caractéristiques
            'Li': {'rgb': (255, 0, 0), 'longueur_onde_principale': 670.8, 'raies': ['670.8 nm']},
            'Rb': {'rgb': (200, 50, 50), 'longueur_onde_principale': 780.0, 'raies': ['780.0 nm', '794.8 nm']},
            'Sr': {'rgb': (255, 100, 100), 'longueur_onde_principale': 460.7, 'raies': ['460.7 nm']},
            
            # Spectres verts caractéristiques
            'Tl': {'rgb': (0, 255, 0), 'longueur_onde_principale': 535.0, 'raies': ['535.0 nm']},
            'Ba': {'rgb': (100, 255, 100), 'longueur_onde_principale': 553.5, 'raies': ['553.5 nm']},
            'Cu': {'rgb': (0, 200, 0), 'longueur_onde_principale': 521.8, 'raies': ['521.8 nm']},
            
            # Spectres bleus caractéristiques
            'Cs': {'rgb': (0, 0, 255), 'longueur_onde_principale': 455.5, 'raies': ['455.5 nm']},
            'Hg': {'rgb': (100, 100, 255), 'longueur_onde_principale': 435.8, 'raies': ['435.8 nm']},
            'As': {'rgb': (50, 50, 200), 'longueur_onde_principale': 450.0, 'raies': ['450.0 nm']},
            
            # Spectres mixtes
            'Na': {'rgb': (255, 255, 0), 'longueur_onde_principale': 589.0, 'raies': ['589.0 nm', '589.6 nm']},
            'K': {'rgb': (255, 200, 0), 'longueur_onde_principale': 766.5, 'raies': ['766.5 nm', '769.9 nm']},
            'H': {'rgb': (255, 100, 255), 'longueur_onde_principale': 656.3, 'raies': ['656.3 nm (Hα)', '486.1 nm (Hβ)']},
            'He': {'rgb': (200, 150, 255), 'longueur_onde_principale': 587.6, 'raies': ['587.6 nm']},
            'Ne': {'rgb': (255, 100, 100), 'longueur_onde_principale': 640.2, 'raies': ['640.2 nm']}
        }
    
    def get_element_rgb(self, element_symb):
        """Retourne la couleur RGB d'un élément"""
        if element_symb in self.spectral_data:
            return self.spectral_data[element_symb]['rgb']
        else:
            # Couleur par défaut basée sur la période de découverte
            epoch_colors = {
                'Antiquité': (245, 222, 179),
                'Moyen-Âge': (222, 184, 135),
                'Renaissance': (244, 164, 96),
                'Révolution Chimique': (205, 133, 63),
                'Ère Spectroscopique': (210, 105, 30),
                'Période Moderne': (160, 82, 45)
            }
            element = next((e for e in self.elements_data if e['symbole'] == element_symb), None)
            if element and element['periode_epoch'] in epoch_colors:
                return epoch_colors[element['periode_epoch']]
            return (200, 200, 200)  # Gris par défaut
    
    def display_header(self):
        """Affiche l'en-tête du dashboard"""
        st.markdown('<h1 class="main-header">🕰️ Tableau Périodique par Date de Découverte</h1>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; color: #666; margin-bottom: 2rem;'>
        <strong>Classification historique des éléments avec leurs spectres RGB caractéristiques</strong><br>
        Explorez l'histoire de la découverte des éléments et leurs signatures spectrales
        </div>
        """, unsafe_allow_html=True)
    
    def create_timeline_view(self):
        """Crée une vue chronologique des découvertes"""
        st.markdown('<h3 class="section-header">📅 FRISE CHRONOLOGIQUE DES DÉCOUVERTES</h3>', 
                   unsafe_allow_html=True)
        
        # Préparer les données pour la timeline
        timeline_data = []
        for element in self.elements_data:
            if element['date_decouverte'] > -10000:  # Filtrer les dates trop anciennes
                rgb = self.get_element_rgb(element['symbole'])
                timeline_data.append({
                    'Element': element['symbole'],
                    'Nom': element['nom'],
                    'Année': max(0, element['date_decouverte']),
                    'Découvreur': element['decouvreur'],
                    'Période': element['periode_epoch'],
                    'Couleur': f'rgb({rgb[0]}, {rgb[1]}, {rgb[2]})'
                })
        
        df_timeline = pd.DataFrame(timeline_data)
        
        # Timeline interactive
        fig = px.scatter(df_timeline, 
                        x='Année', 
                        y=[1]*len(df_timeline),
                        color='Période',
                        hover_data=['Nom', 'Découvreur'],
                        title="Chronologie des Découvertes des Éléments",
                        color_discrete_sequence=['#F5DEB3', '#DEB887', '#F4A460', '#CD853F', '#D2691E', '#A0522D'])
        
        fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
                         selector=dict(mode='markers'))
        fig.update_layout(yaxis=dict(showticklabels=False, title=''),
                         height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_epoch_overview(self):
        """Affiche une vue par époque historique"""
        st.markdown('<h3 class="section-header">🏺 CLASSIFICATION PAR ÉPOQUE HISTORIQUE</h3>', 
                   unsafe_allow_html=True)
        
        for epoch in self.epochs_data:
            elements_epoch = [e for e in self.elements_data if e['periode_epoch'] == epoch['nom']]
            
            st.markdown(f"""
            <div class="epoch-{epoch['nom'].lower().replace(' ', '').replace('é', 'e')}">
                <h3>{epoch['nom']} ({epoch['periode']})</h3>
                <p>{epoch['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Afficher les éléments de cette époque
            cols = st.columns(6)
            for i, element in enumerate(elements_epoch[:6]):  # Maximum 6 éléments par ligne
                with cols[i % 6]:
                    rgb = self.get_element_rgb(element['symbole'])
                    rgb_hex = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
                    
                    st.markdown(f"""
                    <div class="discovery-card">
                        <div style="text-align: center;">
                            <h4>{element['symbole']}</h4>
                            <div class="rgb-spectrum" style="background: linear-gradient(90deg, {rgb_hex}80, {rgb_hex});"></div>
                            <strong>{element['nom']}</strong><br>
                            <small>Découvert en {element['date_decouverte'] if element['date_decouverte'] > 0 else 'Antiquité'}</small><br>
                            <small><em>{element['decouvreur'][:20]}{'...' if len(element['decouvreur']) > 20 else ''}</em></small>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            if len(elements_epoch) > 6:
                cols = st.columns(6)
                for i, element in enumerate(elements_epoch[6:12]):
                    with cols[i % 6]:
                        rgb = self.get_element_rgb(element['symbole'])
                        rgb_hex = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
                        
                        st.markdown(f"""
                        <div class="discovery-card">
                            <div style="text-align: center;">
                                <h4>{element['symbole']}</h4>
                                <div class="rgb-spectrum" style="background: linear-gradient(90deg, {rgb_hex}80, {rgb_hex});"></div>
                                <strong>{element['nom']}</strong><br>
                                <small>Découvert en {element['date_decouverte'] if element['date_decouverte'] > 0 else 'Antiquité'}</small><br>
                                <small><em>{element['decouvreur'][:20]}{'...' if len(element['decouvreur']) > 20 else ''}</em></small>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("---")
    
    def create_spectral_rgb_analysis(self):
        """Analyse des spectres RGB par période"""
        st.markdown('<h3 class="section-header">🌈 ANALYSE DES SPECTRES RGB PAR PÉRIODE</h3>', 
                   unsafe_allow_html=True)
        
        # Statistiques par époque
        epoch_stats = []
        for epoch in self.epochs_data:
            elements_epoch = [e for e in self.elements_data if e['periode_epoch'] == epoch['nom']]
            elements_with_spectra = [e for e in elements_epoch if e['symbole'] in self.spectral_data]
            
            if elements_with_spectra:
                # Calculer la couleur moyenne
                rgb_values = [self.get_element_rgb(e['symbole']) for e in elements_with_spectra]
                avg_rgb = tuple(int(np.mean([rgb[i] for rgb in rgb_values])) for i in range(3))
                
                epoch_stats.append({
                    'Époque': epoch['nom'],
                    'Période': epoch['periode'],
                    'Nombre éléments': len(elements_epoch),
                    'Éléments avec spectre': len(elements_with_spectra),
                    'Couleur moyenne': f'rgb{avg_rgb}',
                    'RGB': avg_rgb
                })
        
        # Afficher les statistiques
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Palette des Époques")
            
            for stat in epoch_stats:
                rgb = stat['RGB']
                rgb_hex = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
                
                st.markdown(f"""
                <div style="display: flex; align-items: center; margin: 10px 0; padding: 10px; background-color: #f8f9fa; border-radius: 5px;">
                    <div style="width: 50px; height: 50px; background-color: {rgb_hex}; border-radius: 5px; margin-right: 15px; border: 1px solid #ccc;"></div>
                    <div>
                        <strong>{stat['Époque']}</strong> ({stat['Période']})<br>
                        <small>{stat['Éléments avec spectre']}/{stat['Nombre éléments']} éléments avec spectre RGB</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.subheader("Évolution des Couleurs")
            
            # Graphique d'évolution
            fig = go.Figure()
            
            for i, stat in enumerate(epoch_stats):
                fig.add_trace(go.Scatter(
                    x=[i], y=[1],
                    mode='markers',
                    marker=dict(size=30, color=stat['Couleur moyenne'], line=dict(width=2, color='black')),
                    name=stat['Époque'],
                    text=f"{stat['Époque']}<br>RGB: {stat['RGB']}",
                    hoverinfo='text'
                ))
            
            fig.update_layout(
                title="Évolution des Palettes Spectrales",
                xaxis=dict(showticklabels=False, title=""),
                yaxis=dict(showticklabels=False, title=""),
                height=300,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def create_spectral_explorer(self):
        """Explorateur détaillé des spectres"""
        st.markdown('<h3 class="section-header">🔍 EXPLORATEUR DES SPECTRES RGB</h3>', 
                   unsafe_allow_html=True)
        
        # Sélection d'élément
        col1, col2 = st.columns([1, 3])
        
        with col1:
            element_choice = st.selectbox("Choisir un élément:", 
                                        [f"{e['symbole']} - {e['nom']}" for e in self.elements_data])
            element_symb = element_choice.split(' - ')[0]
            element_data = next(e for e in self.elements_data if e['symbole'] == element_symb)
        
        with col2:
            rgb = self.get_element_rgb(element_symb)
            rgb_hex = f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
            
            st.markdown(f"""
            <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, {rgb_hex}20, {rgb_hex}50); border-radius: 10px;">
                <h2>{element_data['symbole']} - {element_data['nom']}</h2>
                <div style="display: flex; justify-content: center; align-items: center; margin: 20px 0;">
                    <div style="width: 100px; height: 100px; background-color: {rgb_hex}; border-radius: 50%; border: 3px solid white; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"></div>
                </div>
                <p><strong>Spectre RGB caractéristique</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Détails de l'élément
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="discovery-card">
                <h4>📜 Historique</h4>
                <strong>Date de découverte:</strong> {element_data['date_decouverte'] if element_data['date_decouverte'] > 0 else 'Antiquité'}<br>
                <strong>Découvreur:</strong> {element_data['decouvreur']}<br>
                <strong>Période historique:</strong> {element_data['periode_epoch']}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if element_symb in self.spectral_data:
                spectral_info = self.spectral_data[element_symb]
                st.markdown(f"""
                <div class="discovery-card">
                    <h4>🌈 Spectre</h4>
                    <strong>Couleur RGB:</strong> {rgb}<br>
                    <strong>Longueur d'onde principale:</strong> {spectral_info['longueur_onde_principale']} nm<br>
                    <strong>Raies caractéristiques:</strong><br>
                    {', '.join(spectral_info['raies'])}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="discovery-card">
                    <h4>🌈 Spectre</h4>
                    <strong>Couleur d'époque:</strong> {rgb}<br>
                    <em>Spectre RGB spécifique non défini</em>
                </div>
                """, unsafe_allow_html=True)
        
        with col3:
            # Simulation du spectre
            st.markdown(f"""
            <div class="discovery-card">
                <h4>📊 Spectre Simulé</h4>
            </div>
            """, unsafe_allow_html=True)
            
            # Spectre simulé simple
            lambda_range = np.linspace(380, 780, 400)
            spectre = np.zeros_like(lambda_range)
            
            if element_symb in self.spectral_data:
                # Ajouter des raies spectrales simulées
                raie_principale = self.spectral_data[element_symb]['longueur_onde_principale']
                spectre += 0.8 * np.exp(-0.5 * ((lambda_range - raie_principale) / 10)**2)
                
                # Ajouter d'autres raies
                for i in range(3):
                    raie_pos = raie_principale + (i+1)*30
                    if 380 <= raie_pos <= 780:
                        spectre += 0.3 * np.exp(-0.5 * ((lambda_range - raie_pos) / 8)**2)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=lambda_range, y=spectre,
                mode='lines',
                line=dict(color=rgb_hex, width=3),
                name=f"Spectre {element_symb}"
            ))
            
            fig.update_layout(
                title=f"Spectre simulé de {element_symb}",
                xaxis=dict(title="Longueur d'onde (nm)"),
                yaxis=dict(title="Intensité relative"),
                height=200,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    def create_sidebar(self):
        """Crée la sidebar avec les contrôles"""
        st.sidebar.markdown("## 🎛️ NAVIGATION HISTORIQUE")
        
        # Navigation principale
        st.sidebar.markdown("### 🧭 Vues Historiques")
        section = st.sidebar.radio("Choisir la vue:", 
                                 ["Frise Chronologique", "Vue par Époque", "Analyse Spectrale", "Explorateur"])
        
        # Filtres temporels
        st.sidebar.markdown("### ⏳ Filtres Temporels")
        siecles = st.sidebar.multiselect(
            "Siècles:",
            ["Avant JC", "1-1000", "11ème", "12ème", "13ème", "14ème", "15ème", "16ème", "17ème", "18ème", "19ème", "20ème"],
            default=["18ème", "19ème"]
        )
        
        # Options d'affichage
        st.sidebar.markdown("### 🎨 Options d'Affichage")
        show_rgb = st.sidebar.checkbox("Afficher les spectres RGB", value=True)
        group_by_epoch = st.sidebar.checkbox("Grouper par époque", value=True)
        
        return {
            'section': section,
            'siecles': siecles,
            'show_rgb': show_rgb,
            'group_by_epoch': group_by_epoch
        }
    
    def run_dashboard(self):
        """Exécute le dashboard complet"""
        # Sidebar
        controls = self.create_sidebar()
        
        # Header
        self.display_header()
        
        # Navigation principale
        if controls['section'] == "Frise Chronologique":
            self.create_timeline_view()
            self.create_epoch_overview()
        elif controls['section'] == "Vue par Époque":
            self.create_epoch_overview()
        elif controls['section'] == "Analyse Spectrale":
            self.create_spectral_rgb_analysis()
            self.create_epoch_overview()
        elif controls['section'] == "Explorateur":
            self.create_spectral_explorer()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #666;'>
        <strong>Tableau Périodique Historique avec Spectres RGB</strong><br>
        Classification des éléments par date de découverte et analyse de leurs signatures spectrales caractéristiques<br>
        Données historiques et spectrales compilées pour l'étude de l'évolution de la chimie
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard
if __name__ == "__main__":
    dashboard = HistoricalPeriodicTableDashboard()
    dashboard.run_dashboard()