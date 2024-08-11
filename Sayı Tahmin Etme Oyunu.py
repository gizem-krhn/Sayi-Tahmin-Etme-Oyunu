import random

def guess_number():
    while True:
        target_number = random.randint(1, 100)
        attempts = 0

        while True:
            user_guess = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
            attempts += 1

            if user_guess < target_number:
                print("Daha yüksek bir sayı girin.")
            elif user_guess > target_number:
                print("Daha düşük bir sayı girin.")
            else:
                print(f"Tebrikler! {target_number} sayısını {attempts} denemede buldunuz.")
                break

        play_again = input("Yeniden oynamak istiyor musunuz? (evet/hayır): ")
        if play_again.lower() != "evet":
            break

if __name__ == "__main__":
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    guess_number()
