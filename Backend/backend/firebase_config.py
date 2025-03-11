import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON con las credenciales de servicio
cred = credentials.Certificate("ruta/al/archivo/credenciales.json")

# Inicializa la app de Firebase
firebase_admin.initialize_app(cred)

# Obtén la referencia a la base de datos de Firestore (o la base de datos en tiempo real)
db = firestore.client()
