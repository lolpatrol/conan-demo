from conans import ConanFile, CMake


class GiveStringConan(ConanFile):
    name = "stringprovider"
    # version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False] }

    exports_sources = "*" # Copy local sources instead of declaring source() method

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["stringprovider"]

