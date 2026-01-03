# Proyecto Airbnb València – Análisis de Datos End-to-End

## Objetivo del proyecto
El objetivo de este proyecto es analizar datos reales de Airbnb en València para entender cómo varían los precios, las reviews y el rating de los alojamientos según el barrio y el tipo de propiedad.
Además, busca demostrar un **flujo completo de datos end-to-end**, desde la ingestión hasta el análisis final, usando Python, dbt y Postgres.

---


---

## Flujo de datos

1. Los CSVs originales se cargan en la base de datos mediante `ingest.py`.  
2. dbt crea la capa **staging**, donde los datos se limpian y se renombrar columnas para que sean más claros.  
3. dbt crea la capa **mart**, donde se combinan listings y reviews, se calculan métricas agregadas y se filtran datos faltantes.  
4. Las notebooks usan estos marts para generar gráficos, análisis y conclusiones finales.

---

## Tecnologías usadas

- **Python** (pandas, matplotlib, seaborn, SQLAlchemy)  
- **dbt** para modelado de datos y tests de calidad  
- **Postgres** como base de datos  
- **Jupyter Notebooks** para análisis y visualizaciones

---

## Insights principales

- Los barrios **costeros** tienen precios más estables porque casi todos los alojamientos están cerca de la playa.  
- Los barrios **del centro histórico** muestran una **amplitud de precios mucho mayor**, debido a la mezcla de pisos pequeños económicos y apartamentos de lujo.  
- Los listings con **precios moderados** suelen recibir más reviews y engagement que los extremadamente baratos o caros.  
- La **ubicación y el tipo de alojamiento** influyen mucho en el rendimiento y la valoración de los listings.

---

## Cómo ejecutar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/airbnb_project.git
cd airbnb_project
pip install -r requirements.txt
python ingestion/ingest.py
dbt run
dbt test
dbt docs generate
dbt docs serve

```

## Notas finales

Todos los tests de calidad de datos están incluidos en dbt (not_null, unique).

Las decisiones de limpieza y filtrado (como eliminar filas sin listing_id o sin price) están documentadas en las notebooks.