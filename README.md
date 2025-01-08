# AI Schema Converter para DBT

Un agente de inteligencia artificial que convierte schemas de BigQuery y diccionarios de datos en archivos modelo de DBT (`.yml`).

## 🚀 Características

- Procesa schemas de BigQuery en formato TXT
- Analiza diccionarios de datos en formato TXT
- Genera archivos modelo DBT (`.yml`) automáticamente
- Utiliza Google Gemini API para procesamiento inteligente
- Implementado con PydanticAI para validación de datos
- Containerizado con Docker para fácil despliegue
- Logging detallado para debugging y monitoreo
- Manejo robusto de errores y fallbacks

## 📋 Requisitos Previos

- Python 3.9+
- Docker y Docker Compose
- API Key de Google Gemini
- Archivos de entrada:
  - Schema de BigQuery (`.txt`)
  - Diccionario de datos (`.txt`)

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone [url-del-repositorio]
cd ai_schema_converter
```

2. Crea un archivo `.env` con tus credenciales:
```
GEMINI_API_KEY=tu_api_key_aqui
```

3. Ejecuta el proyecto con Docker Compose:
```bash
docker compose up --build
```

## 📝 Estado Actual del Desarrollo

### ✅ Completado

1. **Configuración del Proyecto**
   - Estructura básica del proyecto implementada
   - Docker y Docker Compose configurados
   - Sistema de logging detallado implementado
   - Gestión de variables de entorno configurada

2. **Integración con Gemini AI**
   - Cliente de Gemini AI configurado
   - Sistema de prompts básico implementado
   - Manejo de respuestas JSON implementado
   - Sistema de fallback para errores

3. **Validación de Datos**
   - Modelos Pydantic para validación implementados
   - Manejo de errores robusto
   - Limpieza y parsing de respuestas JSON

### 🚧 En Progreso

4. **Desarrollo del Parser de Entrada**
   - [ ] Parser para schemas de BigQuery
   - [ ] Parser para diccionarios de datos
   - [ ] Validación de formatos de entrada

5. **Generación de Modelos DBT**
   - [ ] Templates para modelos DBT
   - [ ] Lógica de transformación
   - [ ] Validación de output

6. **Testing y Validación**
   - [ ] Tests unitarios
   - [ ] Tests de integración
   - [ ] Validación de formatos de salida

## 📁 Estructura del Proyecto

```
.
├── Dockerfile              # Configuración de Docker
├── docker-compose.yml      # Orquestación de contenedores
├── requirements.txt        # Dependencias de Python
├── src/
│   ├── main.py            # Punto de entrada principal
│   ├── parsers/           # Parsers para entrada de datos
│   ├── models/            # Modelos Pydantic
│   └── utils/             # Utilidades y helpers
├── tests/                 # Tests unitarios y de integración
├── input/                 # Directorio para archivos de entrada
└── output/                # Directorio para archivos generados
```

## 🔧 Uso Actual

1. Asegúrate de tener una API key válida de Google Gemini en tu archivo `.env`

2. Ejecuta el contenedor:
```bash
docker compose up --build
```

3. El sistema mostrará logs detallados de su ejecución y el estado del proceso.

## 📚 Dependencias Principales

```
python-dotenv==1.0.0
pydantic==2.5.2
google-generativeai==0.3.1
asyncio==3.4.3
```

## 📄 Licencia

[Tipo de Licencia]

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

## 🔜 Próximos Pasos

1. Implementar el parser de schemas de BigQuery
2. Desarrollar el parser de diccionarios de datos
3. Crear los templates base para modelos DBT
4. Implementar la lógica de transformación
5. Agregar tests unitarios y de integración