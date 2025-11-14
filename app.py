from flask import Flask
import os
import platform
import psutil

APP = Flask(__name__)

# Função de métricas (com x no nome, como pedido)
def xcoletar_metricas():
    xpid = os.getpid()
    xprocesso = psutil.Process(xpid)
    xmemoria = xprocesso.memory_info().rss / (1024 * 1024)
    xcpu_porcent = xprocesso.cpu_percent(interval=0.3)
    xsistema = platform.system() + " (" + platform.release() + ")"

    return {
        "PID": xpid,
        "memoria_MB": round(xmemoria, 2),
        "CPU_percent": xcpu_porcent,
        "sistema_operacional": xsistema
    }

# Rota INFO
@APP.route("/info")
def xrota_info():
    html = """
    <div style="font-family: Arial; padding: 30px; background: white;">
        <h2>Integrante:</h2>
        

    Henry Mendes Rodrigues

        </pre>
    </div>
    """
    return html

# Rota MÉTRICAS
@APP.route("/metricas")
def xrota_metricas():
    dados = xcoletar_metricas()

    html = f"""
    <div style="font-family: Arial; padding: 30px; background: white;">
        <h2>Métricas:</h2>
        
{{
    Process_ID: {dados["PID"]},<br>
    memoria_MB: {dados["memoria_MB"]},<br>
    CPU_percentagem: {dados["CPU_percent"]},<br>
    sistema_operacional: "{dados["sistema_operacional"]}"<br>
}}
        </pre>
    </div>
    """
    return html

# Execução
if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
