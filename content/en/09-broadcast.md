# Broadcast integration

Receive Twitch, CHZZK and SOOP viewer events and reactions from Discord friends, and make the avatar react to them. Broadcast integration is a Pro feature and is currently in beta. If something goes wrong on a real broadcast, let us know with an [error report](12-troubleshooting.md#when-broadcast-integration-does-not-work).

The Broadcast page has two tabs.

| Tab | What it does |
|---|---|
| Interactions | Sets what happens when an event arrives. It has [Simple setup](09-interactions.md), the [Node editor](09-node-editor.md), and [Falling, Donation display and Test](09-reactions.md). |
| Connections | Connects platform accounts and Discord channels, and opens the WebSocket and the [remote collaboration](09-session.md) session. |

![Platform list in the Broadcast › Connections tab](img/guide-broadcast-connect.png)

## Connecting Twitch, CHZZK and SOOP

1. Open Broadcast → Connections.
2. Turn on the switch of the platform you want to connect.
3. On the platform login page that opens in your browser, log in with your streaming account and allow the permissions.
4. When the card shows Connected, it is ready to receive events.

![Receive whispers and Debug log settings on the Twitch card](img/guide-twitch.png)

| Platform | Events you can receive |
|---|---|
| Twitch | Channel points redeemed, chat, follows, subscriptions (including gifts and subscription messages), bits, raids, hype trains, whispers |
| CHZZK | Chat, donations (chat donations and video donations), subscriptions |
| SOOP | Chat, star balloons, ad balloons, video balloons, stickers, subscriptions, gifts |

Turn the switch off to stop receiving events. Your saved login and rules are not deleted. Turn on **Debug log** to record the received events in detail in the diagnostic log.

> 🔒 The token exchange in the Twitch, CHZZK and SOOP login goes through the developer's server (`stream-auth.erp.pictures`). The platforms' secret keys are only on this server, and the login information you receive is saved on this PC.

## Connecting Discord

Friends who are not watching the stream can also move the avatar from a Discord channel with buttons or the `/react` command. It works only while the Avatar Live app is running.

![Reactions list on the Discord card](img/guide-discord.png)

### 1. Add the Discord app

Open [Add the Avatar Live Discord app](https://discord.com/oauth2/authorize?client_id=1563157504995754014) and choose where to add it. The app asks only for the commands (`applications.commands`) permission. It does not read messages or manage servers.

| Where to add | When to use |
|---|---|
| Add to server | Use it in a channel of your Discord server. You need permission to manage the server. Your friends do not install anything. |
| Add to my account | Use it when you have no server, or in a group DM. To type the commands themselves in a group DM, friends must also add the app to their own account. Friends who did not install it press the buttons you posted. |

### 2. Link a channel

1. In the app, turn on the switch in Broadcast → Connections → Discord.
2. Press **Make a connect code**. An 8-character code is shown for 10 minutes.
3. In the Discord channel you want to link, choose the `/link` command, put the code in the code field and send it.
4. When the app shows a window asking whether to connect the channel, check the server and channel names and press **Connect**.
5. The channel appears in **Linked channels**.

A code can be used only once. A channel someone else has already linked cannot be linked.

### 3. Post reaction buttons

1. Send `/panel` in the linked channel. The reactions in the **Reactions** list are posted as buttons.
2. When a friend presses a button or chooses a reaction with `/react`, the rule that handles that reaction runs.
3. The Discord message shows who did what.

In the **Reactions** list, set the name, emoji, value and rule for each button. The value is the number that the rule's minimum and maximum count conditions look at. Press **Rule** to cycle through the rules; the Discord reaction trigger of the chosen rule is turned on.

### Discord commands

| Command | Who | What it does |
|---|---|---|
| `/link code:` | You | Links this channel to your Avatar Live. |
| `/unlink` | You or a server admin | Unlinks this channel. |
| `/panel` | You or a server admin | Posts the reaction buttons. Works in group DMs too. |
| `/react` | Friends | Picks one reaction. If none is chosen, it is the first reaction. |
| `/points` `/daily` `/gift` `/rank` | Friends | Check, collect and share points for the point games. |
| `/roulette` `/slots` `/highlow` `/blackjack` `/duel` `/predict` `/lottery` `/race` `/quiz` `/boss` | Friends | Mini-games of the point games. |

When the Discord client language is Korean, Japanese or Chinese, Discord shows the commands under localized names such as `/연결`, `/接続` or `/连接`.

Set the point games' rules and point values in **Point games** on the Discord card. Points are saved on this PC for each channel.

> 🔒 The developer's server (`discord-check.erp.pictures`) relays between Discord and the app. Your friends' Discord names and profile pictures are passed to your app and used for display and stickers. The app never posts to Discord on its own; it only answers your friends' commands.

## WebSocket

![Port setting on the WebSocket card](img/guide-websocket.png)

Lets other programs on this PC exchange events with Avatar Live. It is off by default, and the port is 19190. Only programs on the same PC can connect, at `ws://127.0.0.1:port`. Handle what is exchanged with the WebSocket nodes in the [Node editor](09-node-editor.md).

## Basic and Pro

| Feature | Basic | Pro |
|---|---|---|
| View the Broadcast page | Yes | Yes |
| Platform, Discord and WebSocket connections | Locked | Yes |
| Simple setup, Donation display, Test | Locked | Yes |
| Node editor | View, pan and zoom only | Edit and run |

Even on Basic, your saved logins, rules and graphs are not deleted; they stay, locked.
