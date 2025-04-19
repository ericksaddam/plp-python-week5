from vehicles import Vehicle, Car, Plane
from smartphone import Smartphone, Android

vehicles = [
    Car("Toyota", 180),
    Plane("Boeing", 800),
    Vehicle("Generic Vehicle", 50)
]

for vehicle in vehicles:
    vehicle.move()

smartphone = Smartphone("Samsung", "S21", "128GB", "108MP")
smartphone.take_photo()
smartphone.install_app("Facebook")
smartphone.play_music("Bohemian Rhapsody")

android = Android("Google", "Pixel 5", "128GB", "12MP", "11")
android.take_photo()
android.install_app("Twitter")
android.play_music("Stairway to Heaven")
android.update_android_version("12")