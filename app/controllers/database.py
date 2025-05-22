import mysql.connector

class Database:
    def __init__(self, host='db', user='root', password='password', database='formulario'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def get_estudiantes(self):
        conn = self.connect()
        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM estudiantes'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def insert_estudiante(self, nombre, edad, sexo, carrera, semestre, matricula, fecha, fecha_nacimiento, lugar_nacimiento):
        conn = self.connect()
        cursor = conn.cursor()
        query = '''
            INSERT INTO estudiantes
            (nombre, edad, sexo, carrera, semestre, matricula, fecha, fecha_nacimiento, lugar_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (nombre, edad, sexo, carrera, semestre, matricula, fecha, fecha_nacimiento, lugar_nacimiento))
        conn.commit()
        cursor.close()
        conn.close()