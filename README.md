Configuração do Ambiente de Desenvolvimento
Para executar este projeto localmente, siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias.

Pré-requisitos
Python 3.10 instalado

pip atualizado

Passo a Passo
Crie um ambiente virtual (recomendado para isolar as dependências do projeto):

Como ativar o ambiente virtual
python -m venv venv
Ative o ambiente virtual:

No Windows:

.\venv\Scripts\activate
No Linux/MacOS:

source venv/bin/activate
Instale as dependências do projeto usando o arquivo requirements.txt:

pip install -r requirements.txt
Verifique se todas as dependências foram instaladas corretamente:

pip list
Desativando o Ambiente Virtual
Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual executando:

deactivate