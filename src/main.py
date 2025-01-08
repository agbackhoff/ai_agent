import os
from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel, Field
from typing import Optional
import json
import logging
import sys
import re

# Configurar logging con formato detallado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def limpiar_respuesta_json(texto: str) -> str:
    """Limpia la respuesta de Gemini para obtener solo el JSON válido."""
    logger.debug("Limpiando respuesta JSON...")
    
    # Eliminar bloques de código markdown
    texto = re.sub(r'```(?:json|JSON)?\n', '', texto)
    texto = texto.replace('```', '')
    
    # Eliminar espacios en blanco al inicio y final
    texto = texto.strip()
    
    logger.debug(f"Texto limpio: {texto}")
    return texto

logger.info("Iniciando aplicación...")
logger.info(f"Python version: {sys.version}")
logger.info(f"Current working directory: {os.getcwd()}")

# Cargar variables de entorno
logger.info("Cargando variables de entorno...")
load_dotenv()

# Obtener y validar API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logger.error("GEMINI_API_KEY no encontrada en variables de entorno")
    raise ValueError("GEMINI_API_KEY no encontrada en variables de entorno")
else:
    logger.info("API key encontrada (primeros 4 caracteres): " + api_key[:4] + "...")

# Configurar Gemini AI
try:
    logger.info("Configurando cliente de Gemini AI...")
    genai.configure(api_key=api_key)
    logger.info("✅ Gemini AI configurado correctamente")
except Exception as e:
    logger.error(f"❌ Error al configurar Gemini AI: {str(e)}")
    logger.error(f"Tipo de error: {type(e).__name__}")
    raise

class Mensaje(BaseModel):
    """Modelo Pydantic para estructurar el mensaje de salida"""
    saludo: str = Field(..., description="Mensaje principal de saludo")
    estado: str = Field(..., description="Estado actual del sistema")
    version: Optional[str] = Field(default="1.0", description="Versión del sistema")

    def __init__(self, **data):
        logger.debug(f"Creando instancia de Mensaje con datos: {data}")
        super().__init__(**data)
        logger.debug("✅ Instancia de Mensaje creada correctamente")

async def generar_mensaje() -> Mensaje:
    """Genera un mensaje personalizado usando Gemini AI"""
    try:
        # Configurar el modelo
        logger.info("🤖 Iniciando generación de mensaje con Gemini AI")
        logger.debug("Creando instancia del modelo gemini-pro...")
        model = genai.GenerativeModel('gemini-pro')
        logger.info("✅ Modelo gemini-pro instanciado correctamente")
        
        prompt = """
        Genera un mensaje de bienvenida para una aplicación de conversión de schemas.
        Devuelve SOLO un objeto JSON con los siguientes campos, sin ningún texto adicional:
        - saludo: Un mensaje de bienvenida amigable
        - estado: Estado actual del sistema
        - version: La versión del sistema
        """
        
        logger.debug(f"Prompt a enviar: {prompt}")
        
        # Generar respuesta
        logger.info("📤 Enviando prompt a Gemini AI...")
        response = model.generate_content(prompt)
        logger.info("📥 Respuesta recibida de Gemini AI")
        logger.debug(f"Respuesta original: {response.text}")
        
        # Limpiar y parsear la respuesta JSON
        try:
            logger.info("🔍 Limpiando y parseando respuesta JSON...")
            texto_limpio = limpiar_respuesta_json(response.text)
            mensaje_dict = json.loads(texto_limpio)
            logger.debug(f"JSON parseado correctamente: {mensaje_dict}")
            
            logger.info("✨ Creando instancia de Mensaje con datos validados...")
            mensaje = Mensaje(**mensaje_dict)
            logger.info("✅ Mensaje creado y validado correctamente")
            return mensaje
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ Error al parsear JSON: {str(e)}")
            logger.error(f"Texto limpio problemático: {texto_limpio}")
            logger.error(f"Posición del error: {e.pos}")
            logger.error(f"Línea del error: {e.lineno}, Columna: {e.colno}")
            raise
            
    except Exception as e:
        logger.error(f"❌ Error en generar_mensaje: {str(e)}")
        logger.error(f"Tipo de error: {type(e).__name__}")
        logger.info("⚠️ Utilizando mensaje por defecto...")
        # Mensaje por defecto en caso de error
        return Mensaje(
            saludo="¡Hola Mundo! - AI Schema Converter para DBT",
            estado="Sistema iniciado y listo para procesar schemas",
            version="1.0"
        )

async def main():
    try:
        logger.info("🚀 Iniciando proceso principal...")
        
        # Generar mensaje usando Gemini AI y validarlo con Pydantic
        logger.info("Llamando a generar_mensaje()...")
        mensaje = await generar_mensaje()
        
        # Imprimir el mensaje estructurado
        logger.info("📝 Imprimiendo mensaje generado:")
        print("\n" + "="*50)
        print(f"📢 {mensaje.saludo}")
        print(f"🔄 Estado: {mensaje.estado}")
        print(f"📌 Versión: {mensaje.version}")
        print("="*50 + "\n")
        
        logger.info("✅ Proceso completado exitosamente")
        
    except Exception as e:
        logger.error(f"❌ Error fatal en main: {str(e)}")
        logger.error(f"Tipo de error: {type(e).__name__}")
        raise

if __name__ == "__main__":
    logger.info("🎬 Iniciando script principal...")
    try:
        import asyncio
        logger.info("Iniciando loop de asyncio...")
        asyncio.run(main())
        logger.info("🏁 Script finalizado correctamente")
    except Exception as e:
        logger.error(f"❌ Error fatal en script principal: {str(e)}")
        logger.error(f"Tipo de error: {type(e).__name__}")
        sys.exit(1) 