import pandas as pd
from sodapy import Socrata
#11:34pm

def clean_value(value):
    # Remove '<' and '>' characters and any other non-numeric characters
    cleaned_value = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', value))
    return cleaned_value

def get_data(registers_limit, departament_name ,municipality_name , cultivation_name):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", limit=registers_limit, departamento=departament_name, municipio= municipality_name , cultivo=cultivation_name )
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
        # Clean and convert columns to float, then calculate medians
    results_df['ph_agua_suelo_2_5_1_0'] = results_df['ph_agua_suelo_2_5_1_0'].apply(clean_value).astype(float)
    results_df['f_sforo_p_bray_ii_mg_kg'] = results_df['f_sforo_p_bray_ii_mg_kg'].apply(clean_value).astype(float)
    results_df['potasio_k_intercambiable_cmol_kg'] = results_df['potasio_k_intercambiable_cmol_kg'].apply(clean_value).astype(float)

    mediana_pH = results_df['ph_agua_suelo_2_5_1_0'].median()
    mediana_fosforo = results_df['f_sforo_p_bray_ii_mg_kg'].median()
    mediana_potasio = results_df['potasio_k_intercambiable_cmol_kg'].median()
    print("══════════════════════════════════════════════════════════════════════════════════════")
    print(" Mediana del pH:", mediana_pH)
    print("\n Mediana del FOSFORO(P):", mediana_fosforo)
    print("\n Mediana del POTASIO(K): ", mediana_potasio)
    print("══════════════════════════════════════════════════════════════════════════════════════")
    return results_df