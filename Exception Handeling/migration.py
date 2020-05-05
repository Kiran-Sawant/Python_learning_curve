import duck as du

flock = du.Flock()

donald = du.Duck()
donald2 = du.Duck()
donald3 = du.Duck()
donald4 = du.Duck()
doland5 = du.Duck()
daisy = du.Duck()
dogers = du.Duck()
percy = du.Penguin()

flock.add_duck(donald)
flock.add_duck(donald2)
flock.add_duck(donald3)
flock.add_duck(donald4)
flock.add_duck(doland5)
flock.add_duck(percy)
flock.add_duck(daisy)
flock.add_duck(dogers)

flock.migrate()