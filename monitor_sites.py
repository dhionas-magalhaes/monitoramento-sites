import os
import re
import requests
from datetime import datetime
from dotenv import load_dotenv
from datetime import datetime
def main():
    print(f"\n🕒 Execução iniciada em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    # resto do seu código...

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()  # ← Carrega o .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SITES = {
    "Uniodonto": "https://www.uniodontopoa.com.br/",
    "E-Commerce": "https://ecommerce.uniodontopoa.com.br/home",
    "Odontosfera Login": "https://www.odontosfera.com.br/login.aspx?operadora=366439",
    "Prestador Odontosfera": "https://prestador.odontosfera.com.br/login.aspx?operadora=366439",
    "Index - Atendimento Ambulatório": "http://index2.uniodontopoa.com.br:3000/",
    "API Beneficiário": "https://beneficiario-src.uniodontopoa.com.br:2083/apidocs/",
    "API Clientes": "https://cliente-src.uniodontopoa.com.br:2096/docs",
    "API Prestadores": "https://prestador-src.uniodontopoa.com.br:2087/apidocs/"
}

def escape_markdown(text):
    # Escapa os caracteres especiais exigidos pelo MarkdownV2
    return re.sub(r'([_\*\[\]\(\)\~\`\>\#\+\=\|\{\}\.\!\-])', r'\\\1', text)

def send_telegram(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("⚠️ Bot do Telegram não está configurado.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": escape_markdown(message),
        "parse_mode": "MarkdownV2"
    }

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Erro ao enviar mensagem: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao enviar para o Telegram: {e}")
        return False

def main():
    print(f"\n🕒 Execução iniciada em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    offline_sites = []

    for name, url in SITES.items():
        try:
            # Para o E-Commerce, desabilita a verificação do certificado
            verify_ssl = False if name == "E-Commerce" else True
            response = requests.get(url, timeout=10, verify=verify_ssl, headers={"User-Agent": "Mozilla/5.0"})

            if not (200 <= response.status_code < 400):
                offline_sites.append(f"❌ {name} ({url}) - Código: {response.status_code}")
            else:
                print(f"✅ {name} está acessível.")
        except Exception as e:
            offline_sites.append(f"❌ {name} ({url}) - Erro: {str(e)}")

    if offline_sites:
        msg = (
            f"🚨 *SITES INDISPONÍVEIS* 🚨\n"
            f"🕒 {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            + "\n".join(offline_sites)
        )
        send_telegram(msg)
    else:
        print("✅ Todos os sites estão acessíveis.")

if __name__ == "__main__":
    main()
