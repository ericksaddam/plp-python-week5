class Smartphone:
    def __init__(self, brand, model, storage, camera_resolution):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_resolution = camera_resolution
        self.installed_apps = []

    def take_photo(self):
        print("Taking a photo with", self.camera_resolution, "camera")

    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(app_name, "installed successfully")

    def play_music(self, song_name):
        print("Playing", song_name)

class Android(Smartphone):
    def __init__(self, brand, model, storage, camera_resolution, android_version):
        super().__init__(brand, model, storage, camera_resolution)
        self.android_version = android_version

    def update_android_version(self, new_version):
        self.android_version = new_version
        print("Android version updated to", new_version)