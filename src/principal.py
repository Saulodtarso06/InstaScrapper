import instaloader

dir = 'C:/Users/Saulo de Tarso/Desktop/{target}'
bot = instaloader.Instaloader(
    dirname_pattern=dir
    )
bot.download_profile('lilliluxe', profile_pic_only=True)
