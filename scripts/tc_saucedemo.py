from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Inicialização do WebDriver usando webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_login_sucesso():
    print("▶️ Executando TC-001: Login bem-sucedido...")
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        print("✅ TC-001: Login bem-sucedido - OK")
    except Exception:
        salvar_erro("erro_login_sucesso.png")
        raise Exception("❌ TC-001: Falha no login bem-sucedido.")

def test_login_falha():
    print("▶️ Executando TC-002: Login mal-sucedido...")
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    try:
        erro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
        if erro.is_displayed():
            print("✅ TC-002: Mensagem de erro exibida corretamente - OK")
    except Exception:
        salvar_erro("erro_login_falha.png")
        raise Exception("❌ TC-002: Falha na verificação de mensagem de erro.")

def salvar_erro(nome_arquivo):
    erro_path = os.path.join(r"J:\SCHAEDLER\Senac Gabriel 2025\Testes Selenium 27042025\projeto-selenium\drivers", nome_arquivo)
    driver.save_screenshot(erro_path)
    print(f"📸 Screenshot de erro salva em: {erro_path}")

# Execução principal
try:
    inicio = datetime.datetime.now()
    print(f"🕘 Testes iniciados em: {inicio.strftime('%d/%m/%Y %H:%M:%S')}")
    
    test_login_sucesso()
    time.sleep(2)
    test_login_falha()
    
except Exception as e:
    print(f"⚠️ Erro durante execução: {e}")

finally:
    fim = datetime.datetime.now()
    print(f"🕙 Testes finalizados em: {fim.strftime('%d/%m/%Y %H:%M:%S')}")
    driver.quit()
