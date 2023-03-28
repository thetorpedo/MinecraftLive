import sys
import yaml
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent, GiftEvent, LikeEvent, FollowEvent, CommentEvent, ShareEvent
from mctools import RCONClient

# Importa as configs do config.yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Define o Cliente do TikTok e o Usuário
client: TikTokLiveClient = TikTokLiveClient(unique_id=config['tiktok_user'])

HOST = config['host'] # IP do Servidor
PORT = config['port'] # Porta do RCON - Fica no server.properties

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Conectado na LIVE - ID: ", client.room_id)

    # Cria o RCON
    rcon = RCONClient(HOST, port=PORT)

    # Logar no RCON
    if not rcon.login(config['senha']):
        print("RCON não foi conectado, confira a senha!")
        sys.exit()

    tabelaPresentes = {}
    for presente in config['presentes']:
        tabelaPresentes[presente['id']] = presente['cmd']

    # Likes
    if config['likes']:
        tabelaLikes = dict()
        @client.on("like")
        async def on_like(event: LikeEvent):
            likes = event.likes
            if event.user.unique_id not in tabelaLikes:
                tabelaLikes[event.user.unique_id] = 0
            while likes > 0:
                tabelaLikes[event.user.unique_id] += 1
                likes -= 1
            if tabelaLikes[event.user.unique_id] >= config['quantidade_likes']:
                tabelaLikes[event.user.unique_id] -= config['quantidade_likes']
                print(event.user.unique_id+": Executando CMDs - Likes")
                for cmd_like in config['cmd_like']:
                    rcon.command(f"{cmd_like.format(name=event.user.nickname)}")

    # Comentários
    if config['comment']:
        @client.on("comment")
        async def on_comment(event: CommentEvent):
            for cmd_comment in config['cmd_comment']:
                rcon.command(f"{cmd_comment.format(name=event.user.nickname,comment=event.comment)}")

    # Compartilhar
    if config['share']:
        compartilhou = {}
        @client.on("share")
        async def on_share(event: ShareEvent):
            if event.user.unique_id not in compartilhou:
                compartilhou[event.user.unique_id] = True
                print(event.user.unique_id + ": Executando CMDs - Compartilhou")
                for cmd_share in config['cmd_share']:
                    rcon.command(f"{cmd_share.format(name=event.user.nickname)}")

    # Follow
    if config['follow']:
        seguiu = {}
        @client.on("follow")
        async def on_follow(event: FollowEvent):
            if event.user.unique_id not in seguiu:
                seguiu[event.user.unique_id] = True
                print(event.user.unique_id + ": Executando CMDs - Follow")
                for cmd_follow in config['cmd_follow']:
                    rcon.command(f"{cmd_follow.format(name=event.user.nickname)}")


    # Presentes
    if config['gift']:
        @client.on("gift")
        async def on_gift(event: GiftEvent):

            if event.gift.id in tabelaPresentes:
                print(event.user.unique_id+": Executando CMDs - Presentes - ID:"+str(event.gift.id))
                for cmd in tabelaPresentes[event.gift.id]:
                    rcon.command(f"{cmd.format(name=event.user.nickname)}")


    # Verifica se chegou presente, like, etc.
    if config['gift']:
        client.add_listener("gift", on_gift)
    if config['likes']:
        client.add_listener("like", on_like)
    if config['follow']:
        client.add_listener("follow", on_follow)
    if config['comment']:
        client.add_listener("comment", on_comment)
    if config['share']:
        client.add_listener("share", on_share)


# Roda o Cliente do TikTok Live
if __name__ == '__main__':
    client.run()
