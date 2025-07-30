import requests
import json
import os
import platform

COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_BLUE_LIGHT = '\033[94m'
COLOR_RESET = '\033[0m'

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display():
    ascii = r"""
 __     __     ______     ______     __  __     ______     ______     __  __    
/\ \  _ \ \   /\  ___\   /\  == \   /\ \_\ \   /\  __ \   /\  __ \   /\ \/ /    
\ \ \/ ".\ \  \ \  __\   \ \  __<   \ \  __ \  \ \ \/\ \  \ \ \/\ \  \ \  _"-.  
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/   \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                                        [V1.0]
                                 Dev: Pingu
                                       
    """
    print(f"{COLOR_BLUE_LIGHT}{ascii}{COLOR_RESET}")

def webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_info = response.json()
            print(f"\nName: {webhook_info.get('name', 'N/A')}")
            print(f"Guild ID: {webhook_info.get('guild_id', 'N/A')}")
            print(f"Channel Chat ID: {webhook_info.get('channel_id', 'N/A')}")
            if 'avatar' in webhook_info and webhook_info['avatar'] is not None:
                avatar_url = f"https://cdn.discordapp.com/avatars/{webhook_info['id']}/{webhook_info['avatar']}.png"
                print(f"Avatar: {avatar_url}")
            else:
                print("Avatar: N/A\n")
        else:
            print(f"{COLOR_RED}Impossibile recuperare le informazioni sul webhook - Codice: {response.status_code}{COLOR_RESET}")
    except json.JSONDecodeError:
        print(f"{COLOR_RED}Errore durante l'analisi della risposta JSON dall'API Discord.{COLOR_RESET}")
    except requests.RequestException as e:
        print(f"{COLOR_RED}Errore durante il recupero delle informazioni sul webhook: {e}{COLOR_RESET}")

def spam_webhook(webhook_url, message):
    try:
        while True:
            response = requests.post(webhook_url, json={"content": message, "username": "Webhook Spam"})
            if response.status_code == 204:
                print(f"{COLOR_GREEN}[+] Messaggio inviato con successo!{COLOR_RESET}")
            else:
                print(f"{COLOR_RED}[-] Errore nell'invio del messaggio! Stato: {response.status_code}{COLOR_RESET}")
    except KeyboardInterrupt:
        print(f"\n{COLOR_RED}Spamming interrotto manualmente.{COLOR_RESET}")
    except requests.RequestException as e:
        print(f"{COLOR_RED}Errore di rete: {e}{COLOR_RESET}")

def delete_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(f"{COLOR_GREEN}[+] Webhook eliminato con successo!{COLOR_RESET}")
        else:
            print(f"{COLOR_RED}[-] Errore nell'eliminazione del webhook! Stato: {response.status_code}{COLOR_RESET}")
    except requests.RequestException as e:
        print(f"{COLOR_RED}Errore di rete: {e}{COLOR_RESET}")

def validate_webhook(webhook_url):
    return webhook_url.startswith("https://discord.com/api/webhooks/")

def menu():
    while True:
        clear()
        display()
        print(" ")
        print("    [1] Webhook Spam")
        print("    [2] Webhook Delete")
        print("    [3] Webhook Information")
        print(" ")
        print("    [x] Exit ")
        print(" ")
        webhook_choice = input(f"┌───<{COLOR_BLUE_LIGHT}Webhook{COLOR_RESET}>\n└──> ")

        if webhook_choice == '1':
            webhook_url = input("Inserisci Webhook: ")
            if validate_webhook(webhook_url):
                message = input("Inserisci messaggio: ")
                try:
                    spam_webhook(webhook_url, message)
                except KeyboardInterrupt:
                    print(f"{COLOR_RED}Spamming interrotto manualmente.{COLOR_RESET}")
            else:
                print(f"{COLOR_RED}URL webhook non valido.{COLOR_RESET}")

        elif webhook_choice == '2':
            webhook_url = input("Inserisci Webhook: ")
            if validate_webhook(webhook_url):
                delete_webhook(webhook_url)
            else:
                print(f"{COLOR_RED}URL webhook non valido.{COLOR_RESET}")

        elif webhook_choice == '3':
            webhook_url = input("Inserisci Webhook: ")
            if validate_webhook(webhook_url):
                fetch_webhook_info(webhook_url)
            else:
                print(f"{COLOR_RED}URL webhook non valido.{COLOR_RESET}")

        elif webhook_choice == 'x':
            break

        else:
            print(f"{COLOR_RED}Scelta non valida!{COLOR_RESET}")

        input("\nPremi Invio per tornare al menu principale.")

clear()
display()
menu()
