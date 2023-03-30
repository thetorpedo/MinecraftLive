# MinecraftLive

<details>

<summary>Português</summary>

Integração RCON do **TikTokLive** e **mctools**.
[TikTokLive](https://github.com/isaackogan/TikTokLive) por [isaackogan](https://github.com/isaackogan) / [mctools](https://github.com/Owen-Cochell/mctools) por [Owen Cochell](https://github.com/Owen-Cochell)


Este é um dos meus primeiros projetos (se é que posso chamá-lo assim), e é basicamente apenas uma conexão entre essas duas ferramentas incríveis para que você possa executar comandos minecraft quando eventos do TikTok Live ocorrem.

</details>


**TikTokLive** and **mctools**' RCON integration.
[TikTokLive](https://github.com/isaackogan/TikTokLive) by [isaackogan](https://github.com/isaackogan) / [mctools](https://github.com/Owen-Cochell/mctools) by [Owen Cochell](https://github.com/Owen-Cochell)


This is one of my first projects (if you can call it that), and it's basically just a connection between these two amazing tools so you can run minecraft commands when TikTok Live events happen.

## Installation

<details>

<summary>Português</summary>

 1. Baixe o **MinecraftLivePT-BR.zip** da [última versão](github.com/thetorpedo/MinecraftLive/releases/latest).
 2. Extraia o arquivo.
 3. Edite o **config.yaml** com um editor de texto. *(por exemplo, Notepad)*
 4. Execute o **MinecraftLive.exe** no mesmo diretório que o **config.yaml**.
 5. *Tanto a Live quanto o servidor precisam estar ativos para que ele seja executado.*

</details>


 1. Download the **MinecraftLive.zip** from the [latest release](github.com/thetorpedo/MinecraftLive/releases/latest).
 2. Extract the archive.
 3. Edit the **config.yaml** with a text editor. *(e.g. Notepad)*
 4. Run the **MinecraftLive.exe** on the same directory as the **config.yaml**.
 5. *Both the TikTok Live and the server need to be up for it to run.*
 
 ## Configuration

<details>

<summary>Português</summary>

Seu @usuário do TikTok. O script vai procurar a Live desse usuário. 
```
tiktok_user: "@..."
```

IP do servidor, porta RCON e senha. Todos esses podem ser encontrados em seu server.properties.
Se eles não estiverem configurados corretamente, o script provavelmente não vai rodar.
```
host: '0.0.0.0' # IP
port: 00000 # PORTA
senha: 'password' # SENHA
```
O resto é explicado no próprio arquivo. Basta adicionar os comandos que desejar aos eventos que desejar.

</details>

 *Ignore some of the portuguese words left in the file, this is just a simple python script I made for me and my friends, so I coded most of it in portuguese. I translated the commentaries in the config.yaml to English, but not the code itself. I'll translate the rest in a near future.*

Your Tiktok @user. The script will look for this user's livestream. 
```
tiktok_user: "@..."
```

Server IP, RCON port and password. All of these can be found on your server.properties. If these aren't properly set up, the script will most likely not run.
```
host: '0.0.0.0' # IP
port: 00000 # PORT
senha: 'password' # PASSWORD
```
The rest is explained on the file itself. Simply add the commands you like, to the events you like.
	
