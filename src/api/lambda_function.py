import json
import math
import boto3
import uuid  
from datetime import datetime, date

def write_data_s3_log(event):
    bucket = 'denue-logs-consulta'
    s3 = boto3.client('s3')
    giro = event['giro']
    size = event['size']
    lugar = event['lugar']
    correo = event['mail']
    telefono = event['telefono']
    
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    now = datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    data_to_s3 = {}
    data_to_s3['giro'] = giro
    data_to_s3['size'] = size
    data_to_s3['lugar'] = lugar
    data_to_s3['correo'] = correo
    data_to_s3['telefono'] = telefono
    data_to_s3['timestamp'] = now_string
    
    # Printing random id using uuid1()  
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")
    id = str(uuid.uuid1()) + '-' + today + '.json'
    
    upload_data = bytes(json.dumps(data_to_s3).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=id, Body=upload_data)
    
    

def lambda_handler(event, context):
    # TODO implement
    write_data_s3_log(event)
    
    
    json_data = [{'CLEE': '01001722219007771000000000S9',
          'Id': '1704',
          'Nombre': 'TORTAS AHOGADAS ERNI',
          'Razon_social': '',
          'Clase_actividad': 'Restaurantes con servicio de preparación de tacos y tortas',
          'Estrato': '0 a 5 personas',
          'Tipo_vialidad': 'AVENIDA',
          'Calle': 'AGUASCALIENTES SUR',
          'Num_Exterior': '',
          'Num_Interior': '',
          'Colonia': 'JARDINES DE LAS BUGAMBILIAS',
          'CP': '20280',
          'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
          'Telefono': '4491796170',
          'Correo_e': 'ALEXTORTAS2@HOTMAIL.COM',
          'Sitio_internet': '',
          'Tipo': 'Fijo',
          'Longitud': '-102.28579495',
          'Latitud': '21.85933583',
          'CentroComercial': '',
          'TipoCentroComercial': '',
          'NumLocal': ''},
         {'CLEE': '01001722212006451000000000U4',
          'Id': '6280',
          'Nombre': 'CARNITAS OSCAR',
          'Razon_social': '',
          'Clase_actividad': 'Restaurantes con servicio de preparación de antojitos',
          'Estrato': '0 a 5 personas',
          'Tipo_vialidad': 'AVENIDA',
          'Calle': 'AVENIDA DEL LAGO',
          'Num_Exterior': '102',
          'Num_Interior': '',
          'Colonia': 'JARDINES DEL PARQUE',
          'CP': '20276',
          'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
          'Telefono': '4499135368',
          'Correo_e': '',
          'Sitio_internet': '',
          'Tipo': 'Fijo',
          'Longitud': '-102.28293106',
          'Latitud': '21.85564060',
          'CentroComercial': '',
          'TipoCentroComercial': '',
          'NumLocal': ''},
         {'CLEE': '01001722513002441000000000U0',
          'Id': '34181',
          'Nombre': 'LAS GORDAS DE HUGO',
          'Razon_social': '',
          'Clase_actividad': 'Restaurantes con servicio de preparación de antojitos',
          'Estrato': '0 a 5 personas',
          'Tipo_vialidad': 'AVENIDA',
          'Calle': 'AVENIDA DEL LAGO',
          'Num_Exterior': '102',
          'Num_Interior': '',
          'Colonia': 'JARDINES DEL PARQUE',
          'CP': '20276',
          'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
          'Telefono': '4499130912',
          'Correo_e': '',
          'Sitio_internet': '',
          'Tipo': 'Fijo',
          'Longitud': '-102.28280004',
          'Latitud': '21.85567762',
          'CentroComercial': '',
          'TipoCentroComercial': '',
          'NumLocal': ''},
         {'CLEE': '01001722110001876001000000U3',
          'Id': '6281500',
          'Nombre': 'SIRLOIN STOCKADE',
          'Razon_social': 'VIRREY BUFFETS SA DE CV',
          'Clase_actividad': 'Restaurantes con servicio de preparación de alimentos a la carta o de comida corrida',
          'Estrato': '51 a 100 personas',
          'Tipo_vialidad': 'AVENIDA',
          'Calle': 'Héroe de Nacozari Sur',
          'Num_Exterior': '3016',
          'Num_Interior': '0',
          'Colonia': 'JARDIN DE LAS BUGAMBILIAS',
          'CP': '20280',
          'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
          'Telefono': '',
          'Correo_e': '',
          'Sitio_internet': '',
          'Tipo': 'Fijo',
          'Longitud': '-102.28296030',
          'Latitud': '21.85887008',
          'CentroComercial': '',
          'TipoCentroComercial': '',
          'NumLocal': ''},
         {'CLEE': '01001722219024032000000000U5',
          'Id': '6292',
          'Nombre': 'TORTAS DE CALIDAD',
          'Razon_social': '',
          'Clase_actividad': 'Restaurantes con servicio de preparación de tacos y tortas',
          'Estrato': '0 a 5 personas',
          'Tipo_vialidad': 'AVENIDA',
          'Calle': 'HEROE DE NACOZARI SUR',
          'Num_Exterior': '2405',
          'Num_Interior': '0',
          'Colonia': 'JARDINES DEL PARQUE',
          'CP': '20276',
          'Ubicacion': 'AGUASCALIENTES, Aguascalientes, AGUASCALIENTES',
          'Telefono': '4499788409',
          'Correo_e': '',
          'Sitio_internet': '',
          'Tipo': 'Fijo',
          'Longitud': '-102.28256252',
          'Latitud': '21.85568589',
          'CentroComercial': '',
          'TipoCentroComercial': '',
          'NumLocal': ''}]
    

    return {
        'statusCode': 200,
        'body': json_data
    }
