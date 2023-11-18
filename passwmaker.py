import datetime

yeiar = input("Year:")
if yeiar == "":
    yeiar = 1960

start_date = datetime.date(int(yeiar), 1, 1)
end_date = datetime.date(2023, 12, 24)
current_date = start_date

key_word = input("Key word or name:")
chars = input("Characters:")

if chars == '':
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-"

try:
    print("Have a break, it'll take ~8 minutes.")
    with open(f'{key_word}_wordlist.txt', 'w') as file:
        while current_date <= end_date:
            formatted_date = current_date.strftime('%d%m%Y')
            # day/month/year ++ chars+chars ++ chars ++ key ++ key + %d%m%y
            file.write(formatted_date + '\n')
            for i in chars:
                for j in chars:
                    file.write(formatted_date + i + j + '\n')
                file.write(formatted_date + i + '\n')
            file.write(formatted_date + key_word + '\n')
            file.write(key_word + formatted_date + '\n')
            #month/day/year ++ chars+chars ++ chars ++ key ++ key + %d%m%y
            file.write(current_date.strftime('%m%d%Y') + '\n')
            for i in chars:
                for j in chars:
                    file.write(current_date.strftime('%m%d%Y')+i+j + '\n')
                file.write(current_date.strftime('%m%d%Y')+i + '\n')
            file.write(current_date.strftime('%m%d%Y')+key_word + '\n')
            file.write(key_word+current_date.strftime('%m%d%Y') + '\n')
            #year/month/day ++ chars+chars ++ chars ++ key ++ key + %d%m%y
            file.write(current_date.strftime('%Y%m%d') + '\n')
            for i in chars:
                for j in chars:
                    file.write(current_date.strftime('%Y%m%d')+i+j + '\n')
                file.write(current_date.strftime('%Y%m%d')+i + '\n')
            file.write(current_date.strftime('%Y%m%d')+key_word + '\n')
            file.write(key_word+current_date.strftime('%Y%m%d') + '\n')
            #year/day/month ++ chars+chars ++ chars ++ key ++ key + %d%m%y
            file.write(current_date.strftime('%Y%d%m') + '\n')
            for i in chars:
                for j in chars:
                    file.write(current_date.strftime('%Y%d%m')+i+j + '\n')
                file.write(current_date.strftime('%Y%d%m')+i + '\n')
            file.write(current_date.strftime('%Y%d%m')+key_word + '\n')
            file.write(key_word+current_date.strftime('%Y%d%m') + '\n')
            current_date += datetime.timedelta(days=1)
            if current_date.strftime('%d%m%Y')=="01012000":
                print("It has reached 2000. You have 23 years left.")
            elif current_date.strftime('%d%m%Y')=="01011970":
                print("It has reached 1970. You have 53 years left.")

    print(f'Wordlist generated and saved as {key_word}_wordlist.txt')
except Exception as e:
    print(f"An error occurred: {e}")
