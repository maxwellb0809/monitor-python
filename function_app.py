import json
import time
import urllib.request
import azure.functions as func

app = func.FunctionApp()


def verificar_estado_web(url):
    # Asegurar que tenga protocolo http/https
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        inicio = time.time()
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as respuesta:
            codigo = respuesta.getcode()
            latencia = round((time.time() - inicio) * 1000, 2)
            return {
                "url": url,
                "estado": "ONLINE" if codigo == 200 else "ERROR",
                "codigo_http": codigo,
                "latencia_ms": latencia,
            }
    except Exception as e:
        return {
            "url": url,
            "estado": "OFFLINE",
            "codigo_http": None,
            "error": str(e),
        }


@app.route(route="monitor", auth_level=func.AuthLevel.ANONYMOUS)
def monitor(req: func.HttpRequest) -> func.HttpResponse:
    # Captura la URL que la persona escriba en la dirección web
    url_usuario = req.params.get("url")

    if not url_usuario:
        return func.HttpResponse(
            json.dumps(
                {
                    "mensaje": "Por favor escribe una URL al final de tu enlace. Ejemplo: ?url=instagram.com"
                }
            ),
            mimetype="application/json",
            status_code=400,
        )

    resultado = verificar_estado_web(url_usuario)

    return func.HttpResponse(
        json.dumps(resultado, indent=4),
        mimetype="application/json",
        status_code=200,
    )