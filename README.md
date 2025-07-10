Configuração do Ambiente de Desenvolvimento
Para executar este projeto localmente, siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias.

Pré-requisitos
Python 3.10 instalado

pip atualizado

Passo a Passo
Crie um ambiente virtual (recomendado para isolar as dependências do projeto):

bash
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
.\venv\Scripts\activate
No Linux/MacOS:

bash
source venv/bin/activate
Instale as dependências do projeto usando o arquivo requirements.txt:

bash
pip install -r requirements.txt
Verifique se todas as dependências foram instaladas corretamente:

bash
pip list
Desativando o Ambiente Virtual
Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual executando:

bash
deactivate