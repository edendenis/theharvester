#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `theharvester` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `theharvester` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `theharvester` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `theharvester`
# 
# O "theHarvester" é uma ferramenta de código aberto amplamente usada para coletar informações de reconhecimento em um alvo específico, como endereços de e-mail, nomes de domínio, subdomínios, hosts e outras informações relacionadas à presença online. Desenvolvido em Python, o theHarvester permite que os profissionais de segurança, pesquisadores de segurança e hackers éticos coletem informações valiosas que podem ser usadas para avaliar a superfície de ataque de um alvo e identificar possíveis vulnerabilidades ou pontos fracos em sua infraestrutura de TI. A ferramenta é especialmente útil durante as fases de coleta de informações e reconhecimento em testes de penetração e auditorias de segurança, auxiliando na análise de ameaças e na tomada de decisões informadas para melhorar a postura de segurança de uma organização. O theHarvester suporta várias fontes de dados públicas e privadas e é uma escolha popular para tarefas de coleta de informações em cenários de segurança cibernética. É importante observar que o uso dessa ferramenta deve ser sempre legal e ético, em conformidade com as leis e regulamentos aplicáveis.

# ## 1. Como configurar/instalar/usar o `theharvester` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `theharvester` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Root Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Suft + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.2 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.3 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.4 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.5 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.6 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.7 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para instalar o theHarvester no Linux Ubuntu, você pode seguir os passos abaixo. Essa ferramenta é amplamente utilizada em testes de penetração para coletar informações públicas que podem ajudar a identificar os alvos e possíveis vulnerabilidades.
# 
# 3. **Instale as Dependências Necessárias:** O theHarvester pode precisar de algumas dependências específicas, dependendo de como você decide instalá-lo. Normalmente, `Python 3` e `pip` (gerenciador de pacotes do Python) são necessários. `sudo apt install python3 python3-pip -y
# `
# 4. **Instalação do theHarvester:** Existem várias maneiras de instalar o theHarvester, incluindo a clonagem do repositório GitHub e a instalação via `pip`. A seguir, estão os passos para ambas as abordagens:
# 
# 5. **Via GitHub:**
# 
#     5.1 **Clone o repositório do GitHub:** `git clone https://github.com/laramies/theHarvester.git`
# 
#     5.2 **Navegue até o diretório do theHarvester:** `cd theHarvester`
# 
#     5.3 **Instale as dependências utilizando pip:** `pip3 install -r requirements.txt`
# 
# 6. **Via `pip` (opcional, se você instalou via GitHub NÃO instale via `pip`, pois pode haver conflitos e vice-versa):** Você também pode instalar o theHarvester diretamente via `pip`. Esta é a maneira mais fácil e rápida de instalar a ferramenta: `pip3 install theHarvester`
# 
# 7. **Verifique a Instalação:** Para garantir que o theHarvester foi instalado corretamente, execute o comando abaixo. Ele deve exibir a versão da ferramenta e como usá-la: `python3 theHarvester.py -h`
# `
# Escolha o método de instalação que melhor se adapte às suas necessidades. A instalação via pip é geralmente mais simples e direta, mas a clonagem do repositório GitHub pode oferecer mais flexibilidade, como acesso às últimas alterações antes de serem oficialmente lançadas.

# ## 3. Usar o `theharvester`
# 
# 1. Abrir o `Root Terminal Emultator` no `Linux Ubuntu` ou o `Terminal Emulator` no `Linux`, porém, no ambiente `root`, para este último, com o comando `Crtl + Alt + T` seguido do comando: `sudo su` 
# 
# 2. **Verificar se o Harvester está Instalado:** Antes de começar, verifique se o Harvester já está instalado no seu sistema com o comando: `theHarvester -h`
# 
#     Se o programa retornar a ajuda do comando, ele está instalado. Caso contrário, prossiga para a instalação.
# 
# 3. **Instalar o Harvester (Se Necessário):** Se o Harvester não estiver instalado, você pode instalá-lo utilizando o gerenciador de pacotes do sistema. Execute: `sudo apt-get install theharvester`
# 
# 4. **Usando o Harvester:** Após a instalação, você pode executar o Harvester diretamente do terminal. Para começar a coletar informações, você deve especificar os parâmetros desejados. A sintaxe básica do comando é: `theHarvester -d [domínio] -[limit] -b [fonte]`
# 
#     - `[domínio]` é o domínio que você deseja pesquisar.
# 
#     - `[limit]` é o limite do número de resultados de pesquisa, padrão=500.
#     
#     - `[fonte]` é a fonte de dados que você deseja usar (ex.: google, bing etc.).
# 
#     4.1 **Exemplo de Comando:** Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d google.com -l 300 -b duckduckgo`
# 
#     4.2 **Outro Exemplo de Comando:** Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d sixthstarttech.com -l 300 -b bing`
# 
#     4.3 **Outro Exemplo de Comando:** Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d meklogistics.com -l 300 -b duckduckgo`
# 
#     4.4 **Outro Exemplo de Comando:** Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d meklogistics.com.br -l 300 -b bing`
# 
#     4.5 **Outro Exemplo de Comando:** Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d arknvie.com -l 300 -b duckduckgo`
# 
#     
# 5. **Explorar Opções Adicionais:** O Harvester possui várias opções e parâmetros que podem ser ajustados para refinar sua busca. Utilize `theHarvester -h` para ver todas as opções disponíveis, incluindo limites para o número de resultados, atrasos entre as requisições e exportação dos resultados.
# 
# 6. **Analisar os Resultados:** Após a execução, o Harvester apresentará os resultados no terminal. Isso pode incluir e-mails, nomes de host, subdomínios e outros dados coletados das fontes especificadas. Analise esses dados para identificar informações relevantes.
# 
# 7. **Práticas de Segurança:** Lembre-se de utilizar essas informações respeitando as leis e diretrizes éticas de testes de penetração. A coleta de dados deve ser realizada apenas com permissão explícita dos proprietários dos domínios.
# 
# Este passo a passo foca na execução prática do Harvester no terminal do Linux Ubuntu, desde a instalação até a coleta e análise de informações. Lembre-se de sempre usar essas ferramentas de maneira responsável e ética, dentro do escopo de um teste de penetração autorizado.

# ## 2. Demais comandos
# 
# ### 2.1 Exemplo de Comando com todas as fontes de dados
# 
# 1. Por exemplo, para coletar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d meklogistics.com.br -l 300 -b all`
# 
# ### 2.2 Salvar os resultados
# 
# 1. Por exemplo, para coletar e salvar informações do domínio example.com usando o Google como fonte, você usaria: `theHarvester -d meklogistics.com.br -l 300 -b all -f /home/edendenis/pentest_meklogistics`

# ### 3. Código completo para configurar/instalar
# 
# Para instalar o `theharvester` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     **NÃO** há.
#     ```
# 

# ## Referências
# 
# [1] USER: FREE EDUCATION FOR ALL. ***Lesson 26: the harvester overview:*** https://www.youtube.com/watch?v=HX0RCNI4LJY&list=PLnjNR4-S-EVqfJWovxEJyb7I0IOkKkoYM&index=26. Acessado em: 08/02/2024 23:40.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 08/02/2024 23:40.
# 
# [3] USER: FREE EDUCATION FOR ALL. ***Lesson 27: the harvester process and function:*** https://www.youtube.com/watch?v=ZTr3rBnwp-Y&list=PLnjNR4-S-EVqfJWovxEJyb7I0IOkKkoYM&index=27. Acessado em: 03/02/2024 08/02/2024 23:40.
# 
# [4] OPENAI. ***Instale theHarvester no Ubuntu:*** https://chat.openai.com/c/f9ed573c-41d6-48bb-8277-906606f907b1 (texto adaptado). Acessado em: 08/02/2024 23:40.
# 
