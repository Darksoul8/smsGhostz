import requests
import time
import os
#ĐαɾƙSσυʅ ‘ ∂¡૯

os.system('clear')
while True:
    print("""\033[1;36m
                      ___ _               _       
 ___ _ __ ___  ___   / _ \ |__   ___  ___| |_ ____
/ __| '_ ` _ \/ __| / /_\/ '_ \ / _ \/ __| __|_  /
\__ \ | | | | \__ \/ /_\\| | | | (_) \__ \ |_ / / 
|___/_| |_| |_|___/\____/|_| |_|\___/|___/\__/___|

                                                  
_______\033[1;31m smsGhostz by ĐαɾƙSσυʅ ‘ ∂¡૯ \033[1;36m _______
    \033[m
      \033[1;97m - https://github.com/Darksoul8 \033[m
      \033[1;97m - https://github.com/Darksoul8/smsGhostz \033m

    """)


    print("\033[1;31m[01]\033[m \033[1;33m- Send SMS\033[m")
    print("\033[1;31m[02]\033[m \033[1;33m- Update\033[m")
    print("\033[1;31m[00]\033[m \033[1;33m- Exit\033[m")
    print("\033[1;97m_________________________\n\033[m")
    opt = input("\033[1;97mOption\033[m \033[1;31m➤ \033[m")

    time.sleep(1)

    if (opt == '01' or opt == '1'):
        print("\n\033[1;33m Tips: \033[m")
        print("\033[1;97m [*]- If the message is not sent, use a vpn and try resend it.\033[m")
        print("\033[1;97m [*]- Se a mensagem não for enviada use uma vpn e tente reenviar.\033[m")

        num = str(input("\n\033[1;33m [+]- Number (+ Country),(Exemple +XXXxxxxxxxx): \033[m"))
        text = str(input("\033[1;33m [+]- Message to be sent: \033[m"))
        print("\n\033[1;97m Sending... \033[m")
        resp = requests.post('https://freebulksmsonline.com/api/v1/index.php',{
        	'number' : num,
        	'message' : text,
        	'token' : '534002faaa0355598444b71bcf8dc234'
        })

        time.sleep(2)

        if '"success":"true"' in resp.text:
            print("\n\033[1;32m Message sent successfully\033[m")
        elif '"success":"false"' in resp.text:
            print("\n\033[1;31m Sending a message failed\033[m")
        else:
            print("\n\033[1;31m Unidentifield error\033[m")

        new = str(input("\n\033[1;33m Run again (Y/n): \033[m").upper())

        if(new == "N"):
            break 
        else:
            pass
    elif(opt == '2' or opt == '02'):
        os.system("bash update.sh")
        print('\n\033[1;97m System Update...\033[m')
        time.sleep(2)
        quit()
    elif(opt == '0' or opt == '00'):
        print("\033[1;33m\n    Exiting... \033[m")
        time.sleep(1)
        exit() 
    else:
        print("\033[1;31m\n     -Invalid Option- \033[m")
        time.sleep(2)
        os.system('clear')

#                                                                                                     ĐαɾƙSσυʅ ‘ ∂¡૯
#ĐαɾƙSσυʅ ‘ ∂¡૯
