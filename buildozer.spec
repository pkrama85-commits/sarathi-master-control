[app]
title = Sarathi Master Control
package.name = sarathi
package.domain = com.sarathi

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1.0

requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1

[app:permissions]
android.permissions = INTERNET

[app:features]
android.features = android.hardware.screen.portrait
