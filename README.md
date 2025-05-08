```
# 🎟️ Plataforma de Venta de Boletos con Docker, Flask, MySQL y NGINX + HTTPS

Este proyecto es una plataforma web que permite:
- Registrar conciertos
- Crear cuentas de usuario
- Comprar boletos
- Visualizar historial de compras
- Servir la interfaz web de forma segura mediante HTTPS

Está contenida completamente en Docker con arquitectura modular.

---

## 🚀 Tecnologías utilizadas

- 🐍 Flask (Backend API)
- 🐬 MySQL (Base de datos)
- 🐳 Docker + Docker Compose
- 🔐 NGINX con certificados SSL autofirmados
- 🌐 HTML5 + CSS (Frontend básico)

---

## 📁 Estructura del proyecto

```

plataforma-docker/
│
├── backend/               # API Flask
│   ├── app.py
│   ├── requirements.txt
│
├── db/                    # Script para base de datos
│   └── init.sql
│
├── frontend-secure/       # HTML servido con HTTPS por NGINX
│   ├── index.html
│   ├── nginx.conf
│   ├── certs/
│   │   ├── server.crt
│   │   └── server.key
│   └── Dockerfile
│
├── docker-compose.yml     # Orquestación completa
├── .env                   # Variables sensibles (NO subir a Git)
└── .gitignore

````

---

## 🐳 Instrucciones de ejecución

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/plataforma-docker.git
   cd plataforma-docker
   ```

2. **Crea el archivo `.env`** en la raíz con tu configuración de base de datos.

3. **Genera los certificados HTTPS si no los tienes**

   ```bash
   openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout frontend-secure/certs/server.key \
     -out frontend-secure/certs/server.crt \
     -subj "/CN=localhost"
   ```

4. **Levanta todo el sistema**

   ```bash
   docker-compose up --build
   ```

5. **Abre en el navegador:**
   [https://localhost:8443](https://localhost:8443)

> Acepta el certificado autofirmado si tu navegador muestra advertencia.

---

## 🧪 Endpoints del backend (Flask)

| Ruta          | Método | Descripción                       |
| ------------- | ------ | --------------------------------- |
| `/usuarios`   | GET    | Listar usuarios                   |
| `/usuarios`   | POST   | Crear nuevo usuario               |
| `/conciertos` | GET    | Listar conciertos disponibles     |
| `/conciertos` | POST   | Registrar un nuevo concierto      |
| `/boletos`    | POST   | Comprar boleto (usuario + evento) |

---

## 🛡️ Seguridad aplicada

* 🔐 HTTPS con certificados autofirmados
* ✅ Variables sensibles aisladas en `.env`
* ✅ SQL parametrizado (evita inyección SQL)
* 🔒 Red interna para la base de datos (`networks: internals`)

---

## 📌 Notas finales

* Esta práctica está lista para ser entregada o desplegada localmente.
* Puedes extenderla fácilmente agregando login real, exportación PDF de recibos, o diseño responsivo.

---

🚀 Proyecto académico


