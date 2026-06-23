# Guía de Configuración - FiberNeuro

## Requisitos Previos

### Backend
- Docker 20.10+
- Docker Compose 2.0+
- Python 3.11+ (para scripts de utilidad)

### Aplicación Móvil
- Flutter SDK 3.0+
- Android SDK / Xcode
- Emulador o dispositivo físico

## Pasos de Configuración

### 1. Configurar Backend

```bash
cd 03_CODIGO_FUENTE/fiberneuro-api

# Copiar archivo de ejemplo
cp .env.example .env

# Editar variables según tu entorno
nano .env
```

### 2. Iniciar Contenedores Docker

```bash
docker-compose up -d

# Verificar estado
docker-compose ps

# Ver logs
docker-compose logs -f api
```

### 3. Verificar API

```bash
curl http://localhost:8000/health
```

### 4. Configurar Aplicación Flutter

```bash
cd ../fiberneuro-campo

# Obtener dependencias
flutter pub get

# Verificar dispositivos disponibles
flutter devices
```

### 5. Inicializar Autenticación

```bash
cd ../..
python app/auth/script_init_auth.py
```

## Solución de Problemas

### Puerto 8000 ya en uso
```bash
# Cambiar puerto en docker-compose.yml o .env
API_PORT=8001
```

### Problemas de conexión a BD
```bash
# Verificar contenedor de BD
docker logs fiberneuro_db

# Reiniciar servicios
docker-compose restart
```

### Flutter no encuentra SDK
```bash
# Verificar instalación de Flutter
flutter doctor

# Instalar dependencias faltantes
flutter pub get
```

## Variables de Entorno Importantes

| Variable | Descripción | Ejemplo |
|----------|-------------|----------|
| `DATABASE_URL` | Conexión a PostgreSQL | `postgresql://user:pass@localhost:5432/fiberneuro` |
| `API_PORT` | Puerto de la API | `8000` |
| `SECRET_KEY` | Clave secreta JWT | `cambiar-en-produccion` |
| `DEBUG` | Modo depuración | `False` |

## Desarrollo vs Producción

### Desarrollo
```
DEBUG=True
CORS_ORIGINS=*
```

### Producción
```
DEBUG=False
CORS_ORIGINS=https://yourdomain.com
SECRET_KEY=[generar clave fuerte]
```
