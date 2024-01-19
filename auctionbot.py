import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set your Telegram Bot Token here
TOKEN = "6850951701:AAGbif2CxryFRlKFgJTPeOXHAJROFaOA0Ds"

# Set pokemons,teams,tms name here
LEGENDARY_POKEMON_NAMES = "Articuno","Zapdos","Moltres","Raikou","Entei","Suicune","Regirock","Regice","Registeel","Latias","Latios","Uxie","Mesprit","Azelf","Heatran","Regigigas","Cresselia","Cobalion","Terrakion","Virizion","Buzzwole","Thundurus","Tornadus","Landorus","Type: Null","Silvally","Tapu Koko","Tapu Bulu","Tapu Fini","Tapu Lele","Nihilego","Pheromosa","Xurkitree","Celesteela","Kartana","Guzzlord","Poipole","Naganadel","Stakataka","Blacephalon","Kubfu","Urshifu","Regieleki","Regidrago","Glastrier","Spectrier","Enamorus","Wo-chien","Chien-pao","Ting-lu","Chi-yu","Okidogi","Munkidori","Fezandipiti","Ogerpon","Mewtwo","Lugia","Ho-oh","Kyogre","Groudon","Rayquaza","Dialga","Palkia","Giratina","Reshiram","Zekrom","Kyurem","Xerneas","Yveltal","Zygarde","Cosmog","Cosmoem","Solgaleo","Lunala","Necrozma","Zacian","Zamazenta","Eternatus","Calyrex","Koraidon","Miraidon","Terapagos","Mew","Celebi","Jirachi","Deoxys","Phione","Manaphy","Darkrai","Arceus","shaymin","Victini","Keldeo","Meloetta","Genesect","Diancie","Hoopa","Volcanion","Megearna","Marshadow","Zeraora","Meltan","Melmetal","Zarude"

NON_LEGENDARY_POKEMON_NAMES = "Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran-F","Nidorina","Nidoqueen","Nidoran-M","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetchd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr-Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Dratini","Dragonair","Dragonite","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Larvitar","Pupitar","Tyranitar","Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Wormadam-Plant","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime-Jr","Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon-Z","Gallade","Probopass","Dusknoir","Froslass","Rotom,Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin-Red-Striped","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan-Standard","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Chespin","Thwackey","Rillaboom","Scorbunny","Raboot","Cinderace","Sobble","Drizzile","Inteleon","Skwovet","Greedent","Rookidee","Corvisquire","Corviknight","Blipbug","Dottler","Orbeetle","Nickit","Thievul","Gossifleur","Eldegoss","Wooloo","Dubwool","Chewtle","Drednaw","Yamper","Boltund","Rolycoly","Carkol","Coalossal","Applin","Flapple","Appletun","Silicobra","Sandaconda","Cramorant","Arrokuda","Barraskewda","Toxel","Toxtricity-Amped","Sizzlipede","Centiskorch","Clobbopus","Grapploct","Sinistea","Polteageist","Hatenna","Hattrem","Hatterene","Impidimp","Morgrem","Grimmsnarl","Obstagoon","Perrserker","Cursola","Sirfetchd","Mr-Rime","Runerigus","Milcery","Alcremie","Falinks","Pincurchin","Snom","Frosmoth","Stonjourner","Eiscue-Ice","Indeedee-Male","Morpeko-Full-Belly","Cufant","Copperajah","Dracozolt","Arctozolt","Dracovish","Dartrix","Decidueye","Litten","Torracat","Incineroar","Popplio","Brionne","Primarina","Pikipek","Trumbeak","Toucannon","Yungoos","Gumshoos","Grubbin","Charjabug","Vikavolt","Crabrawler","Crabominable","Oricorio-Baile","Cutiefly","Ribombee","Rockruff","Lycanroc-Midday","Wishiwashi-Solo","Mareanie","Toxapex","Mudbray","Mudsdale","Dewpider","Araquanid","Fomantis","Lurantis","Morelull","Shiinotic","Salandit","Salazzle","Stufful","Bewear","Bounsweet","Steenee","Tsareena","Comfey","Oranguru","Passimian","Wimpod","Golisopod","Sandygast","Palossand","Pyukumuku","Type-Null","Silvally","Minior-Red-Meteor","Komala","Turtonator","Togedemaru","Mimikyu-Disguised","Bruxish","Drampa","Dhelmise","Jangmo-O","Hakamo-O","Kommo-O","Poipole","Naganadel"

SHINY_POKEMON_NAMES = LEGENDARY_POKEMON_NAMES + NON_LEGENDARY_POKEMON_NAMES

POKEMON_TEAM = "Hp","Attack","Defense","Sp. Attack","Sp. Defense","Speed"

TM = "Dragon claw","Psyshock","Venoshock","Hiddenpower","Ice Beam","Blizzard","Hyper Beam","Solar Beam","Smack Down","Thunderbolt","Thunder","Earthquake","Leech Life","Psychic","Shadow Ball","Brick Break","Sludge Wave","Flamethrowr","Sludge Bomb","Fire Blast","Rock Tomb","Aerial Ace","Facade","FlameCharge","Thief","Low Sweep","Round","EchoedVoice","Ovearheat","Steel Wings","Focus Blast","Energy Ball","False swipe","Scald","Charge Beam","Sky Drop","BrutalSwing","Acrobatics","Shadow Claw","Payback","SmartStrike","Giga Impact","Stone Edge","Volt Switch","Fly","Bulldoze","FrostBreath","Rock Slide","X-Scissor","Dragon Tail","Infestation","Poison Jab","Dream Eater","U-Turn","Flash Canon","Wild Charge","Surf","Snarl","Dark Pulse","Waterfall","DazlingGlem"


# Set approved user, banned user, admin and owner id and username here
APPROVED_USER = []

BANNED_USER = []

ADMIN_ID = ['6277479627']

OWNER_ID = '5752004942'

USER_LIST = []

# Online photo url
ONLINE_PHOTO_URL = "https://images.app.goo.gl/MMsr6EQwEaSF32hd6"

# Groups username and id with without @
MAIN_GROUP_USERNAME = 'Pokemongohexafriends'
MAIN_GROUP_ID = '-1001822603599'
AUCTION_GROUP_USERNAME = 'pghfgauctiongroup'
AUCTION_GROUP_ID = '-1002086945467'
SUBMISSION_GROUP_USERNAME = 'guys_no_abuse_allowed'
SUBMISSION_GROUP_ID = '-1002058607013'
REPORT_GROUP_USERNAME = 'pghfbotreportgroup'
REPORT_GROUP_ID = '-1002077064776'

# check if user is member of groups
def check_membership(user_id):
    roles_to_consider = ['creator', 'administrator', 'member', 'restricted']
    is_member_main_group = updater.bot.get_chat_member(MAIN_GROUP_ID, user_id).status in roles_to_consider
    is_member_auction_group = updater.bot.get_chat_member(AUCTION_GROUP_ID, user_id).status in roles_to_consider
    return is_member_main_group, is_member_auction_group

def start(update, context):
    user = update.effective_user
    user_id = str(update.message.from_user.id)

    if user_id not in USER_LIST:
        USER_LIST.append(user_id)

    is_member_main_group, is_member_auction_group = check_membership(user_id)

    inline_buttons = []
    if is_member_main_group and is_member_auction_group:
        inline_buttons.append([InlineKeyboardButton("JOINED", callback_data='joined')])
        reply_text = f"HEY {user.full_name}! YOU ARE ALREADY JOINED OUR MAIN GROUP(POKEMON GO/HEXA FRIENDS GROUP) AND AUCTION GROUP(PGHFG AUCTION GROUP). JUST CLICK ON 'JOINED' AND CONTINUE YOUR PROCESS."
    elif is_member_main_group:
        inline_buttons.extend([
            [InlineKeyboardButton("AUCTION GROUP", url='https://t.me/pghfgauctiongroup')],
            [InlineKeyboardButton("JOINED", callback_data='joined')]
        ])
        reply_text = f"HEY {user.full_name}! YOU ARE ALREADY JOINED OUR MAIN GROUP(POKEMON GO/HEXA FRIENDS GROUP). PLEASE JOIN OUR AUCTION GROUP JUST TAP ON BELOW BUTTON. AFTER JOIN CLICK ON 'JOINED'"
    elif is_member_auction_group:
        inline_buttons.extend([
            [InlineKeyboardButton("MAIN GROUP", url='https://t.me/Pokemongohexafriends')],
            [InlineKeyboardButton("JOINED", callback_data='joined')]
        ])
        reply_text = f"HEY {user.full_name}! YOU ALREADY JOINED OUR AUCTION GROUP(PGHFG AUCTION GROUP). PLEASE JOIN OUR MAIN GROUP(POKEMON GO/HEXA FRIENDS GROUP) TAP ON BELOW BUTTON. AFTER JOIN CLLICK ON 'JOINED'"
    else:
        inline_buttons.extend([
            [InlineKeyboardButton("MAIN GROUP", url='https://t.me/Pokemongohexafriends')],
            [InlineKeyboardButton("AUCTION GROUP", url='https://t.me/pghfgauctiongroup')],
            [InlineKeyboardButton("JOINED", callback_data='joined')]
        ])
        reply_text = f"HEY {user.full_name}! WELCOME TO PGHFG AUCTION BOT. PLEASE JOIN OUR MAIN GROUP  AND AUCTION GROUP FOR START YOUR AUCTION WITH US."

    reply_markup = InlineKeyboardMarkup(inline_buttons)	
    update.message.reply_photo(ONLINE_PHOTO_URL, caption=reply_text, reply_markup=reply_markup)

# Define a function to handle button callback
def button_start(update, context):
    user = update.effective_user
    user_id = user.id
    query = update.callback_query
    query.answer()

    if query.data == 'joined':
        user_id = str(update.callback_query.from_user.id)
        is_member_main_group, is_member_auction_group = check_membership(user_id)

        if is_member_main_group and is_member_auction_group:
            query.message.reply_text(f"Hey {user.first_name} you have join our main and auction group. Use /commands to view all available commands.")
        elif is_member_main_group:
            query.message.reply_text(f"Hey {user.first_name} Please join AUCTION GROUP at first.")
        elif is_member_auction_group:
            query.message.reply_text(f"Hey {user.first_name}Please join MAIN GROUP at first.")
        else:
            query.message.reply_text(f"Hey {user.first_name} Please join both groups.")

# ADD COMMAND HANDLER
def add(update, context):
    keyboard = [
        [
            InlineKeyboardButton("LEGENDARY", callback_data='legendary'),
            InlineKeyboardButton("NON-LEGENDARY", callback_data='non-legendary'),
        ],
        [
            InlineKeyboardButton("SHINY", callback_data='shiny'),
            InlineKeyboardButton("TEAM", callback_data='team'),
        ],
        [
            InlineKeyboardButton("TM", callback_data='tm')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = update.message.reply_text('WHAT YOU WANT TO SELL?', reply_markup=reply_markup)
    context.user_data['message_id'] = message.message_id  # Save the message_id for updating later

# define button
def button_add(update, context):
    query = update.callback_query
    query.answer()
    user = update.effective_user
    user_id = user.id

    # Handle different callback data
    callback_data = query.data

    if query.data == 'legendary':
       reply_text = f"HEY {user.full_name.upper()}! WHICH LEGENDARY POKEMON YOU WANT TO SELL?"
    elif query.data == 'non-legendary':
       reply_text = f"HEY {user.full_name.upper()}! WHICH NON-LEGENDARY POKEMON YOU WANT TO SELL?"
    elif query.data == 'shiny':
       reply_text = f"HEY {user.full_name.upper()}! WHICH SHINY POKEMON YOU WANT TO SELL?"
    elif query.data == 'team':
       reply_text = f"HEY {user.full_name.upper()}! WHICH TEAM YOU WANT TO SELL?"
    elif query.data == 'tm':
       reply_text = f"HEY {user.full_name.upper()}! WHICH TM YOU WANT TO SELL?(PLEASE TELL THE TM NAME NOT TM NUMBER)"

    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=context.user_data['message_id'],
                                  text=reply_text)
# broadcast to all users
def broadcast(update, context):
    user = update.effective_user
    user_id = user.id

    if not is_admin(update, context):
         update.message.reply_text('You are not authorized to use this command.')
         return

    args = context.args
    if not args:
        update.message.reply_text('Please provide a message in the format /broad (message)')
        return

    message_text = ' '.join(args)
    for user_id in USER_LIST:
        context.bot.send_message(chat_id=user_id, text=message_text)

    update.message.reply_text('Broadcast sent to all users.')


# when anyone want to report
def report(update, context):
    user = update.message.from_user

    report_text = ' '.join(context.args)

    if not report_text:
        update.message.reply_text("Please provide a report in the specified format. format is '/report (report_text)'")
        return

    report_message = f'USER NAME - {user.full_name}\nUSER USERNAME - {user.name}\nUSER ID - {user.id}\nREPORT - {report_text}'

    # Forward the report to the bot owner
    context.bot.forward_message(chat_id=REPORT_GROUP_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    context.bot.send_message(chat_id=REPORT_GROUP_ID, text=report_message)

    update.message.reply_text('Your report has been forwarded to the bot admins.')

# Checking if he is admin
def is_admin(update, context):
    user = update.effective_user
    user_id = str(user.id)

    # checking
    if user_id in ADMIN_ID:
       return True
    if user_id in OWNER_ID.split(','):
       return True
    else:
        return False

# message an user who report
def message_user(update, context):
    user = update.effective_user
    user_id = user.id
    # Check if the user who sent the command is an admin
    if is_admin(update, context):
        try:
            # Extract user ID and message from the command
            user_id = int(context.args[0])
            message = ' '.join(context.args[1:])
        except (ValueError, IndexError):
            update.message.reply_text("Invalid command format. Use /message (user_id) (message)")
            return

        # Send the message to the specified user
        context.bot.send_message(chat_id=user_id, text=message)
        update.message.reply_text("Message sent.")
    else:
        update.message.reply_text("You are not authorized to use this command.")

# check if he is owner
def is_owner(update, context):
    user = update.effective_user
    user_id = str(user.id)

    # checking
    if user_id in OWNER_ID.split(','):
       return True

#prmote to bot admin
def promote_admin(update, context):
    admin_id = update.message.from_user.id

    if not is_owner(update, context):
        update.message.reply_text('You are not authorized to use this command.')
        return

    args = context.args
    if not args:
        update.message.reply_text('please type in format /promote (user id)')
        return

    new_admin_id = str(args[0])
    if new_admin_id not in ADMIN_ID:
        ADMIN_ID.append(new_admin_id)
        update.message.reply_text(f'User {new_admin_id} has been promoted to bot admin.')

#prmote to bot admin
def demote_admin(update, context):
    admin_id = update.message.from_user.id

    if not is_owner(update, context):
        update.message.reply_text('You are not authorized to use this command.')
        return

    args = context.args
    if not args:
        update.message.reply_text('please type in format /demote (user id)')
        return

    new_admin_id = str(args[0])
    if new_admin_id in ADMIN_ID:
        ADMIN_ID.remove(new_admin_id)
        update.message.reply_text(f'User {new_admin_id} has been demoted to bot admin.')

# Initialize the Updater and dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('add', add))
dispatcher.add_handler(CommandHandler('report', report))
dispatcher.add_handler(CommandHandler('message', message_user))
dispatcher.add_handler(CommandHandler('promote', promote_admin))
dispatcher.add_handler(CommandHandler('demote', demote_admin))
dispatcher.add_handler(CommandHandler('broad', broadcast))
dispatcher.add_handler(CallbackQueryHandler(button_start))
dispatcher.add_handler(CallbackQueryHandler(button_add))

# Start the bot
updater.start_polling()
updater.idle()
