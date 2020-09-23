movieEntered = input("Enter a movie")
thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","MoneyHeist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","TheOffice","Space Force"]
movieEntered = movieEntered.lower()
thriller = map(str.lower,thriller)
comedy = map(str.lower,comedy)
if movieEntered in thriller:
      print("It is a thriller")
elif movieEntered in comedy:
      print("It is a comedy")
else:
     print("It's neither thriller nor comedy")