
## Setup

```
1. Install Appium 
2. Install Appium Doctor 
    (to check that you have everything set up): "npm install -g appium-doctor --android"
3. Run "appium-doctor" in terminal
4. Install everything that is needed according to what appium doctor says.

Should have something like this available: 
info AppiumDoctor  ✔ Node version is 12.19.0
info AppiumDoctor  ✔ ANDROID_HOME is set to: C:\Users\Lenovo\AppData\Local\Android\Sdk
info AppiumDoctor  ✔ JAVA_HOME is set to: C:\Program Files\Java\jre1.8.0_251
info AppiumDoctor    Checking adb, android, emulator
info AppiumDoctor      'adb' is in C:\Users\Lenovo\AppData\Local\Android\Sdk\platform-tools\adb.exe
info AppiumDoctor      'android' is in C:\Users\Lenovo\AppData\Local\Android\Sdk\tools\android.bat
info AppiumDoctor      'emulator' is in C:\Users\Lenovo\AppData\Local\Android\Sdk\emulator\emulator.exe
info AppiumDoctor  ✔ adb, android, emulator exist: C:\Users\Lenovo\AppData\Local\Android\Sdk
info AppiumDoctor  ✔ 'bin' subfolder exists under 'C:\Program Files\Java\jre1.8.0_251'

5. Start your emulator session or real android device. Find out the name of the started device.
6. In helpers.py update with the name of the device (ex: 'deviceName':"emulator-5554")
7. Run "pip install -r requirements.txt"

```

## Run tests

```
1. Run a test with "py.test .\test\test_android_login.py".
2. Run all tests with "py.test".

```